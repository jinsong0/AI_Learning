# Anaconda常用指令

## 1. 环境管理

### 创建新环境
```bash
conda create -n 环境名 python=版本号
# 例：conda create -n myenv python=3.8
```

### 查看所有环境
```bash
conda env list
# 或
conda info --envs
```

### 激活环境
```bash
conda activate 环境名
# 例：conda activate myenv
```

### 退出当前环境
```bash
conda deactivate
```

### 删除环境
```bash
conda remove -n 环境名 --all
# 例：conda remove -n myenv --all
```

### 克隆环境
```bash
conda create -n 新环境名 --clone 原环境名
```

### 导出环境
```bash
conda env export > environment.yml
```

### 从yml文件创建环境
```bash
conda env create -f environment.yml
```

## 2. 包管理

### 安装包
```bash
conda install 包名
# 例：conda install numpy
```

### 指定版本安装包
```bash
conda install 包名=版本号
# 例：conda install numpy=1.19.2
```

### 安装多个包
```bash
conda install 包名1 包名2
```

### 更新包
```bash
conda update 包名
```

### 升级conda自身
```bash
conda update conda
```

### 查看已安装包
```bash
conda list
```

### 移除包
```bash
conda remove 包名
```

### 搜索包
```bash
conda search 包名
```

## 3. 通道管理

### 添加新的channel
```bash
conda config --add channels channel名称
# 例：conda config --add channels conda-forge
```

### 查看所有channel
```bash
conda config --get channels
```

### 设置channel优先级
```bash
conda config --set channel_priority strict
```

## 4. 其他常用命令

### 查看conda信息
```bash
conda info
```

### 清理缓存
```bash
conda clean -a
```

### 检查更新
```bash
conda update --all
```

### 生成requirements.txt（pip环境）
```bash
pip freeze > requirements.txt
```

---

## 附加说明

- 建议优先使用`conda`管理包和环境，如果某些包找不到可以尝试`pip install 包名`。
- 使用Anaconda Navigator可视化界面也可进行环境和包管理。
