import axios from 'axios';

const lexiServerApi = {
  async filter(text) {
    const response = await axios.post(
      '/api/filter',
      { text },
    );
    return response.data;
  },
};

export default lexiServerApi;