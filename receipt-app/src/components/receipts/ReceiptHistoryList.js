import React from "react";
import ReceiptHistoryItem from "./ReceiptHistoryItem";
import classes from "./ReceiptHistoryList.module.css";

const ReceiptHistoryList = (props) => {
  if (props.histories === null) {
    return (
      <div>
        <p>loading</p>
      </div>
    );
  }
  return (
    <ul className={classes.list}>
      {props.histories.map((history) => (
        <ReceiptHistoryItem
          key={history.ID}
          id={history.ID}
          date={history.date}
          description={history.description}
        />
      ))}
      {/* hjoge */}
    </ul>
  );
};

export default ReceiptHistoryList;
