import React, { useState } from 'react';
import { useParams } from 'react-router-dom';

import { toBase64 } from '../../helpers/utils';
import { useApi, useRequest } from '../../helpers/hooks';
import { apiUrls } from '../../urls';
import { DropZone } from '../../components/DropZone';
import { ImagePreview } from '../../components/ImagePreview';
import classnames from './style.module.scss';

export function FilterDetails() {
    const { filterId } = useParams();
    const [filter, reloadFilter] = useApi(apiUrls.getFilter(filterId));
    const [result, isExecuting, executeFilter, setResultManually] = useRequest({ url: apiUrls.executeFilter(filterId), method: 'post' })
    const [uploadingImage, setUploadingImage] = useState(null);

    if (!filter) {
        return null;
    }

    function onUploadClick() {
        toBase64(uploadingImage).then(image_base64 => {
            executeFilter({
                data: { image_base64 }
            });
        });
    }

    function onResetClick() {
        setUploadingImage(null);
        setResultManually(null);
        reloadFilter({
            ...filter,
            last_benchmark: result?.benchmark,
        });
    }


    const uploadDisabled =  !filter || !uploadingImage || result;
    const resetRendered =  !filter || uploadingImage || result;

    const resultImageBase64 = result?.data?.image_base64;
    const currentBenchmark = result?.benchmark ?? filter?.last_benchmark;
    const lastBenchmarkSeconds = currentBenchmark ? `${currentBenchmark.seconds}s` : 'never';

    return (
        <div className={ classnames.page }>
            <div>🐟👁FISHEYE👁🐟 "{ filter.name }"</div>
            <div>
                <div>Last benchmark: { lastBenchmarkSeconds }</div>
            </div>
            <div>
                <DropZone onDrop={ ([file] = []) => setUploadingImage(file) }/>
            </div>
            <div className={ classnames.buttonsPad }>
                <button
                    disabled={ uploadDisabled }
                    onClick={ onUploadClick }
                >
                    Go!
                </button>
                { resetRendered && (
                    <button
                        onClick={ onResetClick }
                    >
                        Reset
                    </button>
                )}
                { isExecuting && 'Executing, please wait...' }
            </div>
            <div className={ classnames.imagePreviewPad }>
                <div className={ classnames.imagePreviewContainer }>
                    <ImagePreview file={ uploadingImage } />
                </div>
                <div className={ classnames.imagePreviewContainer }>
                    <ImagePreview url={ resultImageBase64 } />
                </div>
            </div>
        </div>
    );
}
