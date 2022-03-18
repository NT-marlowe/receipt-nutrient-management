import React from "react";
import classes from "./ReceiptHistoryItem.modlue.css";
import Card from "../ui/Card";

const ReceiptHistoryItem = (props) => {
  const handleToggleSummary = () => {};

  return (
    <Card>
      {/* <div>Hello, your id is {props.id}.</div> */}
      <li className={classes.item}>
        <div className={classes.content}>
          <h3>{props.date}</h3>
          <p>{props.description}</p>
        </div>
        <div className={classes.actions}>
          <button onClick={handleToggleSummary}>
            open summary / close summary
          </button>
        </div>
      </li>
    </Card>
  );
};

export default ReceiptHistoryItem;
