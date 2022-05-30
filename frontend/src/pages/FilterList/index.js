import React from 'react';
import { useApi } from '../../helpers/hooks';
import { apiUrls, appUrls } from '../../urls';
import { Page } from '../../components/Page';
import classnames from './style.module.scss';

export function FilterListPage() {
    const [filters = [], isLoading] = useApi(apiUrls.getFilters);
    if (isLoading || !filters) {
        return null;
    }
    if (filters.length === 0) {
        return 'No filters available.';
    }
    return (
        <Page>
            { filters.map(filter => (
                <FilterItem
                    key={ filter.id }
                    { ...filter }
                />
            )) }
        </Page>
    );
}

function FilterItem({ id, name }) {
    return (
        <div className={ classnames.filterItem }>
            <a href={ appUrls.filterDetails(id) }>{ name }</a>
        </div>
    );
}
