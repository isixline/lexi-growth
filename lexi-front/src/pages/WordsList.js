import React, { useEffect, useState } from 'react';
import './WordsList.css';
import { Button, List, Card, Select } from 'antd';
import lexiServerApi from '../services/lexiServer';

const WordsList = ({ words }) => {
    const [showedWords, setShowedWords] = useState([]);
    const [sortType, setSortType] = useState('order');

    useEffect(() => {
        const indexedWords = words.map((word, index) => {
            return { ...word, index };
          });
        sortWords(indexedWords, sortType);
        setShowedWords(indexedWords);
    }, [words, sortType]);

    const handleSortChange = (value) => {
        setSortType(value);
    };

    const sortWords = (words, sortType) => {
        words.sort((a, b) => {
            if (sortType === 'order') {
                return a.index - b.index;
            } else if (sortType === 'count') {
                return b.count - a.count;
            }
            return 0;
        });
    }

    const handleMergeClick = async (item) => {
        await lexiServerApi.merge(item.word);
        console.log('merge', item.word);
        const mergedWords = showedWords.map((d) => {
            if (d.word === item.word) {
                return { ...d, known: true };
            }
            return d;
        });
        setShowedWords(mergedWords);
    }

    const formatContent = (content) => {
        return content.split('\\n').map((line, index) => (
            <span key={index}>
                {line}
                <br />
            </span>
        ));
    }

    const renderItem = (item) => (
        <List.Item>
            <Card size="small"
                title={item.word}
                extra={<div><span>{item.count}</span><Button type="link" onClick={() => handleMergeClick(item)}> known! </Button></div>}
                style={{ width: "100%", display: item.known ? 'none' : 'block' }}
            >
                <p>
                    {item.difficulty && `🌟 ${item.difficulty}`}
                    <br />
                    {formatContent(item.definition)}
                </p>
                { }
            </Card>
        </List.Item>
    );

    return (
        <div className='words-list-container'>
            <h3>total:{showedWords.length}</h3>

            <Select
                value={sortType}
                onChange={handleSortChange}
                style={{ width: 120 }}
            >
                 <Select.Option value="order">Order ⬆️</Select.Option>
                <Select.Option value="count">Count ⬇️</Select.Option>
            </Select>

            <List
                itemLayout="horizontal"
                dataSource={showedWords}
                renderItem={renderItem}
            />

        </div>
    );
};

export default WordsList;