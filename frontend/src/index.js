import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { FilterDetails } from './pages/FilterDetails';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/filter/:filterId" element={ <FilterDetails /> } />
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
