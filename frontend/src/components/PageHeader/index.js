import React from 'react';
import classnames from './style.module.scss';
import { APP_TITLE } from '../../constants';
import { appUrls } from '../../urls';

export function PageHeader({ navigationString }) {
    return (
        <div className={ classnames.pageHeader }>
            <a
                href={ appUrls.index }
            >
                { APP_TITLE }
            </a>
            { navigationString && ` / ${navigationString}` }
        </div>
    );
}
