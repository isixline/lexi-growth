import pytest
import requests_mock

@pytest.fixture
def mock_dictionaryapi_get_entries_en_success(word="cat"):
  print(f"mock_dictionaryapi_get_entries_en_success: {word}")
  with requests_mock.Mocker() as m:
    m.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}', status_code=200, json=[
    {
      "word": word,
      "meanings": [
        {
          "partOfSpeech": "noun",
          "definitions": [
            {
              "definition": "a domesticated carnivorous mammal that originated from wolves"
            }
          ]
        }
      ]
    }
    ])
    yield m

@pytest.fixture
def mock_dictionaryapi_get_entries_en_success_multiple_definitions(word="cat"):
  with requests_mock.Mocker() as m:
    m.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}', status_code=200, json=[
    {
      "word": word,
      "meanings": [
        {
          "partOfSpeech": "noun",
          "definitions": [
            {
              "definition": "a domesticated carnivorous mammal that originated from wolves"
            },
            {
              "definition": "a small domesticated carnivorous mammal with soft fur"
            }
          ]
        }
      ]
    }
    ])
    yield m

@pytest.fixture
def mock_dictionaryapi_get_entries_en_success_no_definitions(word="cat"):
  with requests_mock.Mocker() as m:
    m.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}', status_code=200, json=[
    {
      "word": word,
      "meanings": []
    }
    ])
    yield m

@pytest.fixture
def mock_dictionaryapi_get_entries_en_not_found(word="cat"):
  with requests_mock.Mocker() as m:
    m.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}', status_code=404)
    yield m

@pytest.fixture
def mock_dictionaryapi_get_entries_en_error(word="cat"):
  with requests_mock.Mocker() as m:
    m.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}', exc=Exception)
    yield m
