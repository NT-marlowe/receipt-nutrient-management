import React from "react";
import classes from "./FoodRecommendation.module.css";
import Card from "../ui/Card";
import { foods, translation } from "./Constants";

const FoodRecommendation = (props) => {
  const threshold = 30;
  const names = Object.keys(props.nutritions);
  return (
    <div className={classes.list_center}>
      <ul className={classes.no_dots}>
        {names.map((name) => {
          if (props.nutritions[name] < threshold) {
            return (
              <Card>
                <li className={classes.item}>
                  <p>
                    <b>{translation[name]}</b>が不足しています．
                    <b>{foods[name].name}</b>を食べましょう！
                  </p>
                  <img
                    alt="torimuneniku"
                    src={foods[name].imageLink}
                    className={classes.image}
                  />
                </li>
              </Card>
            );
          } else {
            return null;
          }
        })}
      </ul>
    </div>
  );
};

export default FoodRecommendation;
