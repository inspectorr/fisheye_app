import React from 'react';
import { Button as BButton } from 'react-bootstrap';
import cn from 'classnames';
import classnames from './style.module.scss';

export function Button(props) {
    return (
        <BButton { ...props } className={ cn(classnames.button, props.className) } />
    );
}
