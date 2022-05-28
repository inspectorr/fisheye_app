import React, { useEffect, useState } from 'react';

export function ImagePreview({
    file,
    url,
}) {
    const [localUrl, setLocalUrl] = useState();
    useEffect(() => {
        if (file instanceof Blob) {
            previewImage(file);
            return;
        }

        setLocalUrl(null);
    }, [file]);

    function previewImage(file) {
        const reader  = new FileReader();
        reader.onload = () => setLocalUrl(reader.result);
        reader.readAsDataURL(file);
    }

    if (!url && !localUrl) {
        return null;
    }

    return (
        <img
            src={ localUrl || url }
            alt="Превью"
        />
    );
}
