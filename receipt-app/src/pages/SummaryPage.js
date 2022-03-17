import React from "react";
import NutritionGraph from "../components/nutrition/NutritionGraph";

const SummaryPage = () => {
  return (
    <div>
      <h1>Summary</h1>
      <ol>
        <li>Upload an image of a receipt</li>
        <li>You can find how much and what kind of nutritions you take</li>
      </ol>
      <NutritionGraph />
    </div>
  );
};

export default SummaryPage;
