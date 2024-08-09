import nltk
from nltk.corpus import brown, words
from nltk.stem import PorterStemmer

# 下载必要的语料库
nltk.download('brown')
nltk.download('words')

def evaluate_word_difficulty(word):
    # 1. 词频分析
    word_frequency = brown.words().count(word.lower())  # 将单词转换为小写以避免大小写差异
    
    # 2. 是否为常用词
    is_common = word.lower() in words.words()
    
    # 3. 拼写复杂度
    word_length = len(word)
    has_complex_letters = any(letter in word.lower() for letter in 'qzjx')
    
    # 4. 词根分析
    ps = PorterStemmer()
    root_word = ps.stem(word.lower())
    root_similarity = 1 if root_word == word.lower() else 0.5  # 如果词根与原词一致，降低难度

    # 综合评分 (可以根据需要调整权重)
    # 词频越高，难度越低
    # 常用词难度降低
    # 拼写复杂度、词根差异增加难度
    difficulty_score = (word_length * (1 + has_complex_letters) - word_frequency) / root_similarity
    if is_common:
        difficulty_score -= 5

    # 确保评分为正值，负分代表简单
    return max(difficulty_score, 0)

if __name__ == '__main__':
    word_list = ['calories', 'apple', 'quixotic', 'jazz', 'python']
    for word in word_list:
        difficulty = evaluate_word_difficulty(word)
        print(f'{word}: {difficulty}')