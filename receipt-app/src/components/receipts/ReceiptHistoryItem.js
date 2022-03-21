import React, { useState } from "react";
import classes from "./ReceiptHistoryItem.module.css";
import Card from "../ui/Card";
import NutritionTable from "../nutrition/NutritionTable";

const ReceiptHistoryItem = (props) => {
  const [tableIsOpen, setTableIsOpen] = useState(false);
  const handleToggleSummary = () => {
    setTableIsOpen(() => !tableIsOpen);
  };

  return (
    <Card>
      <li className={classes.item}>
        <div className={classes.content}>
          <h3>{props.date}</h3>
          <p>{props.description}</p>
        </div>
        {tableIsOpen ? (
          <div className={classes.table}>
            <NutritionTable nutritions={props.nutritions} />
          </div>
        ) : null}
        <div className={classes.actions}>
          <button onClick={handleToggleSummary}>
            {tableIsOpen ? "close summary" : "open summary"}
          </button>
        </div>
      </li>
    </Card>
  );
};

export default ReceiptHistoryItem;
