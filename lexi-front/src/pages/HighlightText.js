import React from 'react';
import Highlighter from "react-highlight-words";

const HighlightText = ({ text, words }) => {
  const lines = text.split('\n');

  const highlightedLines = lines.map((line, index) => (
    <p>
      <Highlighter
        key={index}
        searchWords={words.map(wordObj => wordObj.word)}
        autoEscape={true}
        textToHighlight={line}
        caseSensitive={false}
      />
    </p>

  ));

  return <div>{highlightedLines}</div>;
};

export default HighlightText;