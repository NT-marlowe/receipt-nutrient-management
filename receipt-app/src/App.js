// import logo from './logo.svg';
// import './App.css';
import React, { useState, useEffect } from 'react';

export default function UploadImages() {
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
        />) }
    </p>
  );
}

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
