import React, { useState, useEffect } from 'react';

function UploadImages() {
    // 現在のstateの値と，それを更新するための関数をペアで返す
    const [images, setImages] = useState([]);
    const [imageURLs, setImageURLs] = useState([]);

    // ReactがDOMを更新するとuseEffect関数が実行される
    useEffect(() => {
        if (images.length < 1) return;
        const newImageUrls = [];
        images.forEach( (image) => newImageUrls.push(URL.createObjectURL(image)));
        setImageURLs(newImageUrls);
        }, 
        [images]
    );

    // ... はspread構文、配列リテラル中に既存の配列を展開する
    function onImageChange(event) {
        setImages([...event.target.files]);
    }

    return (
        // inputタグでユーザが入力可能 
        // 入力タイプはファイル
        // 、複数画像アップ可能(multiple), ファイルタイプはimage
        // 画像アップロード時にonImageChangeが実行される
        <div className="App">
            <p>
                <
                    input type="file" 
                    multiple accept="image/*"
                    onChange={onImageChange}
                /> 
                { imageURLs.map(imageSrc => 
                    <img 
                        src={imageSrc}
                        alt="description"  
                    />)
                }
            </p>
        </div>
    );
}

export default UploadImages;