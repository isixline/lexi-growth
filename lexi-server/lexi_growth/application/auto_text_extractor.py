import re
from lexi_growth.utils.txtractor.youtube_subtitles_extractor import extract_youtube_subtitles
 
def extract_text(text):
    # 正则表达式来匹配YouTube视频URL
    youtube_pattern = r'(https?://)?(www\.)?(youtube\.com)'

    extractd_text = text
    if re.match(youtube_pattern, text):
        extractd_text = extract_youtube_subtitles(text)
    
    return extractd_text