import subprocess
import os
import glob

def extract_youtube_subtitles_by_language_code(video_url, language_code='en'):
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
            print(f"未找到{language_code}字幕文件。")
            return None
        
        subtitle_file = subtitle_files[0]
    
        with open(subtitle_file, 'r') as f:
            subtitles = f.read()
        
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

def extract_youtube_subtitles(video_url):
    language_codes=['en', 'en-US']
    for language_code in language_codes:
        subtitles = extract_youtube_subtitles_by_language_code(video_url, language_code)
        if subtitles is not None:
            return subtitles

# 示例调用
if __name__ == "__main__":
    video_url = input("YouTube vidoe URL: ")
    subtitles = extract_youtube_subtitles(video_url)
    print(subtitles)
