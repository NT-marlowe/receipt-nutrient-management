import React, { useState, useEffect } from "react";
import axios from "axios";
import ReceiptHistoryList from "../components/receipts/ReceiptHistoryList";

const dateSort = (a, b) => {
  if (a.date < b.date) return 1;
  else if (a.date > b.date) return -1;
  return 0;
};

const ReceiptHistoryPage = () => {
  const [histories, setHistories] = useState([]);
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/history/")
      .then((response) => {
        setHistories(() => response.data.sort(dateSort));
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>Receipt History</h1>
      {histories.length > 0 ? (
        <ReceiptHistoryList histories={histories} />
      ) : (
        <div>
          <p>No receipt is uploaded.</p>
          <p>Let's upload now!</p>
        </div>
      )}
    </div>
  );
};

export default ReceiptHistoryPage;
