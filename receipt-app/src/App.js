import "./App.css";
import React from "react";
import { Route, Switch } from "react-router-dom";
// import ApiFetch from "./components/receipts/ApiFetch";
// import UploadImages from "./components/receipts/UploadImages";
import HowToUsePage from "./pages/HowToUsePage";
import ImageUploadPage from "./pages/ImageUploadPage";
import ReceiptHistoryPage from "./pages/ReceiptHistoryPage";
import Layout from "./components/layout/Layout";

function App() {
  return (
    <Layout>
      {/* <div className="App"> */}
      {/* <header className="App-header">
          <h1>Receipt Nutriton Management</h1>
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
          <HowToUsePage />
          <UploadImages /> */}
      {/* <ApiFetch /> */}
      {/* </header>
      </div> */}
      <Switch>
        <Route path="/" exact>
          <HowToUsePage />
        </Route>
        <Route path="/new-image">
          <ImageUploadPage />
        </Route>
        <Route path='/history'>
          <ReceiptHistoryPage />
        </Route>
      </Switch>
    </Layout>
  );
}

export default App;
