import axios from 'axios';

function getCsrfToken() {
    const match = document.cookie.match(/csrftoken=([^ ;]+)/);
    if (!match) {
        return null;
    }
    return match[1];
}

function getHeaders() {
    const headers = {'content-type': 'application/json'};
    const csrfToken = getCsrfToken();
    if (csrfToken) {
        headers['X-CSRFToken'] = csrfToken;
    }
    return headers;
}

const request = axios.create({
  baseURL: '/',
  headers: getHeaders(),
});

export default request;
