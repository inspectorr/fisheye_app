const apiUrls = {
    getFilter: (filterId) => `/api/nodes/filter/${filterId}/`,
    executeFilter: (filterId) => `/api/nodes/filter/${filterId}/execute/`,
    getFilters: `/api/nodes/filter/available/`,
};

const appUrls = {
    index: '/',
    filterDetails: (filterId) => `/filter/${filterId}`,
};

export { apiUrls, appUrls };
