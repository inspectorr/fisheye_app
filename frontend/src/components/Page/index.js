import React from 'react';
import cn from 'classnames';
import { PageHeader } from '../PageHeader';
import classnames from './style.module.scss';

export function Page({
    children,
    navigationString,
    ...props
}) {
    return (
        <div
            { ...props }
            className={ cn(classnames.page, props.className) }
        >
            <PageHeader navigationString={ navigationString } />
            { children }
        </div>
    );
}
