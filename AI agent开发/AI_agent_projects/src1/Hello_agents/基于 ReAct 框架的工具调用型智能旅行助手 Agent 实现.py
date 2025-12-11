AGENT_SYSTEM_PROMPT = """
你是一个智能旅行助手。你的任务是分析用户的请求，并使用可用工具一步步地解决问题。

# 可用工具:
- `get_weather(city: str)`: 查询指定城市的实时天气。
- `get_attraction(city: str, weather: str)`: 根据城市和天气搜索推荐的旅游景点。

# 行动格式:
你的回答必须严格遵循以下格式。首先是你的思考过程，然后是你要执行的具体行动，每次回复只输出一对Thought-Action：
Thought: [这里是你的思考过程和下一步计划]
Action: [这里是你要调用的工具，格式为 function_name(arg_name="arg_value")]

# 任务完成:
当你收集到足够的信息，能够回答用户的最终问题时，你必须在`Action:`字段后使用 `finish(answer="...")` 来输出最终答案。

请开始吧！
"""

##工具 1：查询真实天气
import requests
import json

def get_weather(city: str) -> str:
    """
    通过调用 wttr.in API 查询真实的天气信息。
    """
    # API端点，我们请求JSON格式的数据
    url = f"https://wttr.in/{city}?format=j1"

    try:
        # 发起网络请求
        response = requests.get(url)
        # 检查响应状态码是否为200 (成功)
        response.raise_for_status()
        # 解析返回的JSON数据
        data = response.json()

        # 提取当前天气状况
        current_condition = data['current_condition'][0]
        weather_desc = current_condition['weatherDesc'][0]['value']
        temp_c = current_condition['temp_C']

        # 格式化成自然语言返回
        return f"{city}当前天气:{weather_desc}，气温{temp_c}摄氏度"

    except requests.exceptions.RequestException as e:
        # 处理网络错误
        return f"错误:查询天气时遇到网络问题 - {e}"
    except (KeyError, IndexError) as e:
        # 处理数据解析错误
        return f"错误:解析天气数据失败，可能是城市名称无效 - {e}"


##工具 2：搜索并推荐旅游景点
import os
from tavily import TavilyClient


def get_attraction(city: str, weather: str) -> str:
    """
    根据城市和天气，使用Tavily Search API搜索并返回优化后的景点推荐。
    """
    # 1. 从环境变量中读取API密钥
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        return "错误:未配置TAVILY_API_KEY环境变量。"

    # 2. 初始化Tavily客户端
    tavily = TavilyClient(api_key=api_key)

    # 3. 构造一个精确的查询
    query = f"'{city}' 在'{weather}'天气下最值得去的旅游景点推荐及理由"

    try:
        # 4. 调用API，include_answer=True会返回一个综合性的回答
        response = tavily.search(query=query, search_depth="basic", include_answer=True)

        # 5. Tavily返回的结果已经非常干净，可以直接使用
        # response['answer'] 是一个基于所有搜索结果的总结性回答
        if response.get("answer"):
            return response["answer"]

        # 如果没有综合性回答，则格式化原始结果
        formatted_results = []
        for result in response.get("results", []):
            formatted_results.append(f"- {result['title']}: {result['content']}")

        if not formatted_results:
            return "抱歉，没有找到相关的旅游景点推荐。"

        return "根据搜索，为您找到以下信息:\n" + "\n".join(formatted_results)

    except Exception as e:
        return f"错误:执行Tavily搜索时出现问题 - {e}"


# 将所有工具函数放入一个字典，方便后续调用
available_tools = {
    "get_weather": get_weather,
    "get_attraction": get_attraction,
}

# 接入大语言模型
# 封装一个通用的客户端类，用于调用任何兼容 OpenAI API 协议的大语言模型（LLM）服务(如 OpenAI 官方、通义千问 Qwen、Moonshot、DeepSeek 等)
# 导入操作系统模块，用于读取环境变量（比如 API 密钥）
import os
# 导入 OpenAI 官方提供的 Python SDK，用来调用大模型 API
from openai import OpenAI


class OpenAICompatibleClient:
    """
    这是一个通用的大语言模型（LLM）客户端类。
    它可以用来调用任何“兼容 OpenAI 接口”的 AI 服务，
    比如：通义千问（Qwen）、OpenAI 官方 GPT、Kimi、DeepSeek 等。
    """

    def __init__(self, model: str, api_key: str, base_url: str):
        """
        初始化客户端。
        :param model: 要使用的模型名称，例如 "qwen3-max" 或 "gpt-5"
        :param api_key: 访问 AI 服务所需的密钥（请不要直接写在代码里！建议用环境变量）
        :param base_url: AI 服务的 API 地址（不同服务商地址不同）
        """
        # 保存用户指定的模型名称
        self.model = model
        # 创建一个 OpenAI 客户端对象，指向指定的服务地址和密钥
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def generate(self, prompt: str, system_prompt: str) -> str:
        """
        向大模型发送请求，并返回它的回答。
        :param prompt: 用户输入的问题或指令（比如“你好！”）
        :param system_prompt: 系统提示，用来设定 AI 的角色或行为（比如“你是一个 helpful 的助手”）
        :return: 模型生成的文本回复
        """
        print("正在调用大语言模型...")

        try:
            # 构造对话消息列表（OpenAI API 要求的格式）
            messages = [
                # 第一条是系统消息：告诉 AI 它应该扮演什么角色
                {'role': 'system', 'content': system_prompt},
                # 第二条是用户消息：用户实际说的话
                {'role': 'user', 'content': prompt}
            ]

            # 调用大模型 API，发送请求
            response = self.client.chat.completions.create(
                model=self.model,      # 使用哪个模型
                messages=messages,     # 发送上面构造的对话历史
                stream=False           # 不使用流式输出（一次性返回完整结果）
            )

            # 从响应中提取 AI 回答的文本内容
            answer = response.choices[0].message.content

            print("大语言模型响应成功。")
            return answer

        except Exception as e:
            # 如果发生任何错误（比如网络问题、API 密钥无效等），打印错误信息
            print(f"调用LLM API时发生错误: {e}")
            # 返回一个友好的错误提示
            return "错误:调用语言模型服务时出错。"
# 使用通义千问（Qwen）——通过 DashScope 的 OpenAI 兼容接口
if __name__ == "__main__":
    # 从环境变量安全读取 API Key
    api_key = os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        raise ValueError("请设置环境变量 DASHSCOPE_API_KEY")

    client = OpenAICompatibleClient(
        model="qwen3-max",
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    reply = client.generate(
        # “请用‘乐于助人的AI助手’的身份，回答用户说的‘你好！’这句话。”
        prompt="你好！",
        system_prompt="你是一个乐于助人的AI助手。"
    )
    print(reply)


import os
from dotenv import load_dotenv  # 必须先安装：pip install python-dotenv
import re

# --- 1. 加载环境变量 ---
load_dotenv()  # 自动读取 .env 文件中的配置

# 从环境变量中获取参数（如果没设置会报错或提示）
API_KEY = os.getenv("DASHSCOPE_API_KEY")
if not API_KEY:
    raise ValueError("请设置环境变量 API_KEY")

BASE_URL = os.getenv("BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
if not BASE_URL:
    raise ValueError("请设置环境变量 BASE_URL")

MODEL_ID = os.getenv("MODEL_ID", "qwen-plus")  # 默认使用 qwen-plus

# 设置 Tavily API Key 到环境变量（供其他库使用）
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
if TAVILY_API_KEY:
    os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY

# --- 2. 初始化 LLM 客户端 ---
try:
    llm = OpenAICompatibleClient(
        model=MODEL_ID,
        api_key=API_KEY,
        base_url=BASE_URL
    )
    print("✅ LLM 客户端初始化成功！")
except Exception as e:
    print(f"❌ LLM 客户端初始化失败: {e}")
    exit(1)

# --- 3. 初始化 ---
user_prompt = "你好，请帮我查询一下今天杭州的天气，然后根据天气推荐一个合适的旅游景点。"
prompt_history = [f"用户请求: {user_prompt}"]

print(f"用户输入: {user_prompt}\n" + "=" * 40)

# --- 3. 运行主循环 ---
for i in range(5):  # 设置最大循环次数
    print(f"--- 循环 {i + 1} ---\n")

    # 3.1. 构建Prompt
    full_prompt = "\n".join(prompt_history)

    # 3.2. 调用LLM进行思考
    llm_output = llm.generate(full_prompt, system_prompt=AGENT_SYSTEM_PROMPT)
    # 模型可能会输出多余的Thought-Action，需要截断
    match = re.search(r'(Thought:.*?Action:.*?)(?=\n\s*(?:Thought:|Action:|Observation:)|\Z)', llm_output, re.DOTALL)
    if match:
        truncated = match.group(1).strip()
        if truncated != llm_output.strip():
            llm_output = truncated
            print("已截断多余的 Thought-Action 对")
    print(f"模型输出:\n{llm_output}\n")
    prompt_history.append(llm_output)

    # 3.3. 解析并执行行动
    action_match = re.search(r"Action: (.*)", llm_output, re.DOTALL)
    if not action_match:
        print("解析错误:模型输出中未找到 Action。")
        break
    action_str = action_match.group(1).strip()

    if action_str.startswith("finish"):
        final_answer = re.search(r'finish\(answer="(.*)"\)', action_str).group(1)
        print(f"任务完成，最终答案: {final_answer}")
        break

    tool_name = re.search(r"(\w+)\(", action_str).group(1)
    args_str = re.search(r"\((.*)\)", action_str).group(1)
    kwargs = dict(re.findall(r'(\w+)="([^"]*)"', args_str))

    if tool_name in available_tools:
        observation = available_tools[tool_name](**kwargs)
    else:
        observation = f"错误:未定义的工具 '{tool_name}'"

    # 3.4. 记录观察结果
    observation_str = f"Observation: {observation}"
    print(f"{observation_str}\n" + "=" * 40)
    prompt_history.append(observation_str)
















