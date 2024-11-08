# Video subtitle generation using AI
# 使用AI生成视频字幕

## 简介
video subtitle generation using AI（Speech Recognition and Language Translation）. 
使用AI生成视频字幕（语音识别+语言翻译） 

字幕翻译 基于whisper、translate、ffmpeg，自动为视频生成翻译过后的srt字幕文件，支持自定义各种语言。


## 功能
1.基于视频中的语音直接生成字幕文件  
支持指定whisper model，支持使用huggingface下载的自定义model
2.翻译字幕文件

## 使用方法
1. 安装 `ffmpeg`

2. 安装依赖 `pip install -r requirements.txt`  （默认你已经安装了torch和cuda环境）

3. 填写配置文件 `config.yaml`
主要配置视频列表，音频列表和字幕列表可以不需要配置，默认采用视频列表里的路径和文件名，将".mp4"后缀名修改为".audio"和".srt"

4. 运行 `python main.py`

## TODO
提高翻译结果准确度
