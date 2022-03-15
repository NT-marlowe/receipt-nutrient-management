import React from "react";
import axios from "axios";
import ReceiptHistoryList from "../components/receipts/ReceiptHistoryList";

const getReceiptHistory = () => {
  let histories;
  axios
    .get("dummy_API_URL")
    .then((response) => {
      histories = response.data;
    })
    .catch((error) => {
      console.error(error);
    });
  return histories;
};

function ReceiptHistoryPage() {
  return (
    <section>
      <h1>Receipt History</h1>
      <ReceiptHistoryList histories={getReceiptHistory} />
    </section>
  );
}

export default ReceiptHistoryPage;
