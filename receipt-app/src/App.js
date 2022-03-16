import "./App.css";
import React from "react";
import { Route, Switch } from "react-router-dom";
import SummaryPage from "./pages/SummaryPage";
import ImageUploadPage from "./pages/ImageUploadPage";
import ReceiptHistoryPage from "./pages/ReceiptHistoryPage";
import Layout from "./components/layout/Layout";

function App() {
  return (
    <Layout>
      <Switch>
        <Route path="/" exact>
          <SummaryPage />
        </Route>
        <Route path="/new-image">
          <ImageUploadPage />
        </Route>
        <Route path="/history">
          <ReceiptHistoryPage />
        </Route>
      </Switch>
    </Layout>
  );
}

export default App;
