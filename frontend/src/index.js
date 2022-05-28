import React from 'react';
import ReactDOM from 'react-dom';
import { FilterDetails } from './pages/filter_details';

function App() {
    return <FilterDetails />;
}

document.addEventListener('DOMContentLoaded', () => {
    let root = document.getElementById('root');
    if (!root) {
        root = document.createElement('div');
        root.id = 'root';
        document.body.appendChild(root);
    }
    ReactDOM.render(<App />, root)
});
