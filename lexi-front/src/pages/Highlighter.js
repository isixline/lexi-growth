// Highlighter.js
import React, { useEffect, useState } from 'react';
import './Highlighter.css'

const Highlighter = ({ text, words }) => {
  const [highlightedText, setHighlightedText] = useState('');

  useEffect(() => {
    // 定义一个处理文本的函数
    const highlightWords = (inputText, wordsToHighlight) => {
      // 使用正则表达式匹配整个单词，忽略大小写
      const regex = new RegExp(`\\b(${wordsToHighlight.map(w => w.replace(/\s+/g, '\\ ')).join('|')})\\b`, 'gi');
      return inputText.replace(regex, '<span class="highlight">$1</span>');
    };

    // 调用函数并设置状态
    setHighlightedText(highlightWords(text, words));
  }, [text, words]);

  return (
    <div
      dangerouslySetInnerHTML={{ __html: highlightedText }}
    />
  );
};

export default Highlighter;