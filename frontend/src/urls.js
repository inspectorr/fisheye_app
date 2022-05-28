const apiUrls = {
    getFilter: (filterId) => `/api/nodes/filter/${filterId}/`,
    executeFilter: (filterId) => `/api/nodes/filter/${filterId}/execute/`,
};

export { apiUrls };
