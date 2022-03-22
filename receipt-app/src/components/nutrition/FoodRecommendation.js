import React from "react";

const foods = {
  protein: "豚肉、鶏ささみ肉",
  carbon: "コーンフレーク",
  fat: "牛肉、ベーコン、鯖",
  mineral: "チーズ、昆布",
  vitamin: "ホウレンソウ、ニンジン",
  fiber: "ブロッコリー、カボチャ",
};

const translation = {
  protein: "タンパク質",
  carbon: "炭水化物",
  fat: "脂質",
  mineral: "ミネラル",
  vitamin: "ビタミン",
  fiber: "食物繊維",
};

const FoodRecommendation = (props) => {
  const threshold = 30;
  const names = Object.keys(props.nutritions);
  return (
    <ul>
      {names.map((name) => {
        if (props.nutritions[name] < threshold) {
          return (
            <li>
              <p>あなたは{translation[name]}が不足しています．</p>
              <p>{foods[name]}を食べましょう！</p>
            </li>
          );
        } else {
          return null;
        }
      })}
    </ul>
  );
};

export default FoodRecommendation;
