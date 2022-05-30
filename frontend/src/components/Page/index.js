import React from 'react';
import cn from 'classnames';
import classnames from './style.module.scss';

export function Page(props) {
    return (
        <div
            { ...props }
            className={ cn(classnames.page, props.className) }
        />
    );
}
