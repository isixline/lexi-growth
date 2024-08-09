import axios from 'axios';

const lexiServerApi = {
  async filter(text) {
    const response = await axios.post(
      '/api/filter',
      { text },
    );
    return response.data;
  },

  async merge(word) {
    const response = await axios.post(
      '/api/merge-to-known',
      { word },
    );
    return response.data;
  },

  async revert(word) {
    const response = await axios.post(
      '/api/revert-word',
      { word },
    );
    return response.data;
  },

  async extractText(resourceLocator) {
    const response = await axios.post(
      '/api/extract-text',
      { resourceLocator },
    );
    return response.data['text'];
  },
};

export default lexiServerApi;