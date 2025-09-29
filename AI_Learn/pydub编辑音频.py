#裁剪音频时长
from pydub import AudioSegment
# 定义输入文件的完整路径
input_file = r"C:\Users\ASUS\Desktop\歌曲\miku_虫儿飞.wav"
# 加载音频文件
audio = AudioSegment.from_wav(input_file)
# 定义裁剪的起始和结束时间（单位：毫秒）
start_time_ms = 9000
end_time_ms = 103000
# 裁剪音频
cropped_audio = audio[start_time_ms:end_time_ms]
# 定义输出文件名
output_file = r"C:\Users\ASUS\Desktop\歌曲\miku_虫儿飞.wav"
# 导出裁剪后的音频文件
cropped_audio.export(output_file, format="wav")
# 打印完成信息

print("裁剪完成，保存为：", output_file)
