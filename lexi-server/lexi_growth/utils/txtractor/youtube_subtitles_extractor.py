import subprocess
import os
import glob

def extract_youtube_subtitles(video_url, language_code='en'):
    try:
        # 临时文件名
        base_file_name = "temp_subtitle"
        
        # yt-dlp 命令，下载字幕并保存为临时文件
        command = [
            "yt-dlp",
            "--write-subs",
            "--sub-lang", language_code,
            "--skip-download",
            "--output", base_file_name,
            video_url
        ]
        
        # 执行命令
        subprocess.run(command, check=True)

        subtitle_file_pattern = f"{base_file_name}*.{language_code}.*"
        subtitle_files = glob.glob(subtitle_file_pattern)
        
        if not subtitle_files:
            print("未找到字幕文件。")
            return None
        
        subtitle_file = subtitle_files[0]  # 获取第一个匹配的文件
        
        
        # 读取字幕文件
        with open(subtitle_file, 'r', encoding='utf-8') as file:
            subtitles = file.read()
        
        # 删除临时文件
        os.remove(subtitle_file)
        
        return subtitles
    
    except subprocess.CalledProcessError as e:
        print(f"字幕下载失败: {e}")
        return None
    except FileNotFoundError:
        print("没有找到字幕文件，可能字幕未被下载。")
        return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None

# 示例调用
if __name__ == "__main__":
    video_url = input("YouTube vidoe URL: ")
    subtitles = extract_youtube_subtitles(video_url)
    print(subtitles)
