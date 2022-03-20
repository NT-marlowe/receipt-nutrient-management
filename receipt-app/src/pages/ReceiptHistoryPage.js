import React from "react";
import axios from "axios";
import { useState, useEffect } from "react";
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
  const [histories, setHistories] = useState([]);

  useEffect(() => {
    setHistories(getReceiptHistory());
  }, []);

  return (
    <section>
      <h1>Receipt History</h1>
      {histories.length > 0 ? (
        <ReceiptHistoryList histories={histories} />
      ) : (
        <div>
          <p>No receipt is uploaded.</p>
          <p>Let's upload now!</p>
        </div>
      )}
    </section>
  );
}

export default ReceiptHistoryPage;
