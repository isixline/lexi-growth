import React, { useState } from 'react';
import './Workbench.css';
import { Input, Button } from 'antd';
import lexiServerApi from '../services/lexiServer';
import WordsList from './WordsList';

const Workbench = () => {
  const [data, setData] = useState([]);
  const [inputValue, setInputValue] = useState('hello lexi-growth!');
  const [revertedWord, setRevertedWord] = useState('');
  const [loadingData, setLoadingData] = useState(false);
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

  const handleButtonClick = async () => {
    setLoadingData(true);
    const list = await lexiServerApi.filter(inputValue);
    setData(list);
    setLoadingData(false);
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
    setData([]);
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
      
      <Button type="primary" onClick={handleButtonClick}>
        Filter
      </Button>

      {
        loadingData 
          ? (<h3>Loading...</h3>)
          : (
            // <div/>
            <WordsList words={data} />
          ) 
      }

    </div>
  );
};

export default Workbench;