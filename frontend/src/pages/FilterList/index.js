import React from 'react';

import { useApi } from '../../helpers/hooks';
import { apiUrls, appUrls } from '../../urls';
import { Page } from '../../components/Page';
import { Table } from '../../components/Table';
import classnames from './style.module.scss';

const columns = [
    {
        Header: 'Available filters',
        accessor: 'name',
        Cell: ({ row: { original: filter } }) => {
            return <FilterItem {...filter} />;
        },
    },
    {
        Header: 'Using nodes',
        accessor: 'nodes',
        Cell: ({ row: { original: filter } }) => {
            return filter?.nodes.map(node => node.name).join(', ');
        },
    },
    {
        Header: 'Last benchmark (s)',
        accessor: 'last_benchmark.seconds',
    },
];

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
            <div className={ classnames.filterList }>
                <Table columns={ columns } data={ filters } />
            </div>
        </Page>
    );
}

function FilterItem({ id, name }) {
    return (
        <div className={ classnames.filterListItem }>
            <a href={ appUrls.filterDetails(id) }>{ name }</a>
        </div>
    );
}
