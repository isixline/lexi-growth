import React, { useState } from 'react';
import './Workbench.css';
import { Input, Button } from 'antd';
import lexiServerApi from '../services/lexiServer';
import WordsList from './WordsList';
import HighlightText from './HighlightText';

const Workbench = () => {
  const [words, setWords] = useState([]);
  const [inputValue, setInputValue] = useState('hello lexi-growth!');
  const [revertedWord, setRevertedWord] = useState('');
  const [loadingWords, setLoadingWords] = useState(false);
  const [resourceLocator, setResourceLocator] = useState('');

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleRevertChange = (e) => {
    setRevertedWord(e.target.value);
  }

  const handleResourceLocatorChange = (e) => {
    setResourceLocator(e.target.value);
  }

  const handleFilterClick = async () => {
    setLoadingWords(true);
    const list = await lexiServerApi.filter(inputValue);
    setWords(list);
    setLoadingWords(false);
  };

  const handleRevertClick = async () => {
    if (!revertedWord) {
      return;
    }

    await lexiServerApi.revert(revertedWord);

    setRevertedWord('');
  }

  const handleExtractClick = async () => {
    setInputValue('Extracting...');
    const text = await lexiServerApi.extractText(resourceLocator);
    setInputValue(text);
    setWords([]);
  }

  return (
    <div className='workbench-container'>
      <h1>LexiGrowth</h1>

      <div className='util-container'>
        <Input
          value={revertedWord}
          onChange={handleRevertChange}
        />
        <Button danger onClick={handleRevertClick}>
          Revert
        </Button>


        <Input
          value={resourceLocator}
          onChange={handleResourceLocatorChange}
        />
        <Button onClick={handleExtractClick}>
          Extract
        </Button>
      </div>

      <Input.TextArea
        placeholder="Enter some text..."
        value={inputValue}
        autoSize={{ minRows: 3, maxRows: 5 }}
        onChange={handleInputChange}
      />
      <Button type="primary" onClick={handleFilterClick}>
        Filter
      </Button>

      {
        loadingWords
          ? (<h3>Loading...</h3>)
          : (
            <>
              <h3>total:{words.length}</h3>
              <HighlightText text={inputValue} words={words} />
              <WordsList words={words} />
            </>
          )
      }

    </div>
  );
};

export default Workbench;