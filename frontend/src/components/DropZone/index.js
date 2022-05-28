import React from 'react';
import { useDropzone } from 'react-dropzone';

import classnames from './style.module.scss';

export function DropZone({ onDrop }) {
  const { getRootProps, getInputProps, isDragActive } = useDropzone({onDrop})

  return (
    <div className={ classnames.dropZone } { ...getRootProps() }>
      <input { ...getInputProps() } />
      {
        isDragActive ?
          <p>Drop the files here...</p> :
          <p>Drop some files here, or click to select files</p>
      }
    </div>
  )
}
