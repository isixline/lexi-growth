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
};

export default lexiServerApi;