import "./App.css";
import React from "react";
import { Route, Switch } from "react-router-dom";
import HowToUsePage from "./pages/HowToUsePage";
import ImageUploadPage from "./pages/ImageUploadPage";
import ReceiptHistoryPage from "./pages/ReceiptHistoryPage";
import Layout from "./components/layout/Layout";

function App() {
  return (
    <Layout>
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
