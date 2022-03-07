// import logo from './logo.svg';
import './App.css';
import React from 'react';
import ApiFetch from './components/ApiFetch';
import UploadImages from './components/UploadImages';

function App() {
	return (
		<div className="App">
			<header className="App-header"> 
				{/* <img src={logo} className="App-logo" alt="logo" /> */}
				<h1>
					Receipt Nutriton Management
				</h1>
				<b>
					GitHub Repositry is &nbsp;		  
					<a
						className="App-link"
						href="https://github.com/NT-marlowe/receipt-nutrient-management"
						target="_blank"
						rel="noopener noreferrer"
					>
						Here
					</a>
				</b>

				<UploadImages />
				<h2>How to Use</h2>
				<ol>
					<li>Upload an image of a receipt</li>
					<li>You can find how much and what kind of nutritions you take</li>
				</ol>
				<ApiFetch />

			</header>
		</div>
	);
}

export default App;
