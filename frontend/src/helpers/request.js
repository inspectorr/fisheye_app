import axios from 'axios';

const request = axios.create({
  baseURL: '/',
  headers: {'content-type': 'application/json'}
});

export default request;
