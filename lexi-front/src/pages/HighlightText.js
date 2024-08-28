import React from 'react';
import Highlighter from "react-highlight-words";

const HighlightText = ({ text, words }) => {
  const lines = text.split('\n');
  const searchWords = words.map(wordObj => `\\b${wordObj.word}\\b`);

  const highlightedLines = lines.map((line, index) => (
    <p>
      <Highlighter
        key={index}
        textToHighlight={line}
        searchWords={searchWords}
        caseSensitive={false}
      />
    </p>

  ));

  return <div>{highlightedLines}</div>;
};

export default HighlightText;