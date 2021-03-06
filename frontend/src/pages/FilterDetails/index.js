import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import imageCompression from 'browser-image-compression';

import { toBase64 } from '../../helpers/utils';
import { useApi, useRequest } from '../../helpers/hooks';
import { apiUrls } from '../../urls';
import { DropZone } from '../../components/DropZone';
import { ImagePreview } from '../../components/ImagePreview';
import { Page } from '../../components/Page';
import { Button } from '../../components/Button';
import classnames from './style.module.scss';

export function FilterDetailsPage() {
    const { filterId } = useParams();
    const [filter, isFilterLoading, reloadFilter] = useApi(apiUrls.getFilter(filterId));
    const [result, isExecuting, executeFilter, setResultManually] = useRequest({ url: apiUrls.executeFilter(filterId), method: 'post' })
    const [imageToUpload, setImageToUpload] = useState(null);

    if (!filter) {
        return null;
    }

    function reset() {
        reloadFilter({
            ...filter,
            last_benchmark: getCurrentBenchmark(),
        });
        setResultManually(null);
    }

    function getCurrentBenchmark() {
        return result?.benchmark ?? filter?.last_benchmark;
    }

    function handleGoClick() {
        reset();
        toBase64(imageToUpload).then(image_base64 => {
            executeFilter({
                data: { image_base64 }
            });
        });
    }

    function handleResetClick() {
        setImageToUpload(null);
        reset();
    }

    function handleDrop([file]) {
        imageCompression(file, {
            maxSizeMB: 1,
        }).then((compressedFile) => {
            setImageToUpload(compressedFile);
            reset();
        });
    }

    const goDisabled = !imageToUpload || isExecuting;
    const resetRendered = imageToUpload || result && !isExecuting;
    const resetDisabled = isExecuting;

    const resultImageBase64 = result?.data?.image_base64;
    const currentBenchmark = getCurrentBenchmark();
    const lastBenchmarkSeconds = currentBenchmark ? `${currentBenchmark.seconds}s` : 'never';
    const goButtonText = 'Go!';
    const usingNodes = filter?.nodes.map(node => node.name).join(', ');

    return (
        <Page navigationString={ filter?.name } >
            <div>
                <div>Last benchmark: { lastBenchmarkSeconds }</div>
                <div>Using nodes: { usingNodes }</div>
            </div>
            <div>
                <DropZone
                    onDrop={ handleDrop }
                    accept={ {
                        'image/*': ['.png', '.jpg', '.jpeg'],
                    } }
                />
            </div>
            <div className={ classnames.buttonsPad }>
                <Button
                    disabled={ goDisabled }
                    onClick={ handleGoClick }
                >
                    { goButtonText }
                </Button>
                { resetRendered && (
                    <Button
                        disabled={ resetDisabled }
                        onClick={ handleResetClick }
                    >
                        Reset
                    </Button>
                )}
                { isExecuting && 'Executing, please wait...' }
            </div>
            <div className={ classnames.imagePreviewPad }>
                <div className={ classnames.imagePreviewContainer }>
                    <ImagePreview file={ imageToUpload } />
                </div>
                <div className={ classnames.imagePreviewContainer }>
                    <ImagePreview url={ resultImageBase64 } />
                </div>
            </div>
        </Page>
    );
}
