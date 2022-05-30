import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { FilterListPage } from './pages/FilterList';
import { FilterDetailsPage } from './pages/FilterDetails';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={ <FilterListPage /> } />
                <Route path="/filter/:filterId" element={ <FilterDetailsPage /> } />
            </Routes>
        </BrowserRouter>
    );
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
