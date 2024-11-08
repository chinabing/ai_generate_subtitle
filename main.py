import yaml

from script import translate_tool, audio_tool, whisper_tool

if __name__ == '__main__':
    with open('config.yaml', 'r', encoding='utf-8') as file:
        file_data = file.read()
    config = yaml.load(file_data, Loader=yaml.FullLoader)

    video_file_list = config['input']

    with open(video_file_list, "r", encoding="utf-8") as file:
        for line in file:
            video_file = line.strip()
            audio_file = video_file.replace(".mp4", ".mp3")
            caption_file = video_file.replace(".mp4", ".srt")

            ## 1. 从视频文件中提取音频文件
            print("%s audio extract begin" %audio_file)
            audio_tool.audio_extract(video_file, audio_file)
            print("%s audio extract finish" %audio_file)

            ## 2. 采用whisper模型进行语音识别
            print("%s whisper recognition begin" %audio_file)
            whisper_tool.do_whisper(audio_file, caption_file, config['from'], config['hf_model_path'],
                                    config['device'])
            print("%s whisper recognition finish" %audio_file)

            ## 3. 翻译字幕
            print("translate begin")
            translate_tool.do_translate(caption_file, config['srt_translate_path'], config['from'], config['to'],
                                        config['translate_threads'])
            print("translate success")

            print("success")

