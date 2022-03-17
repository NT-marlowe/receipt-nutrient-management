import React from "react";
import NutritionGraph from "../components/nutrition/NutritionGraph";
import fetchNutritionSummary from "../components/nutrition/fetchNutritionSummary";

const dummy_info = {
  protein: 35,
  carbon: 50,
  fat: 23,
  mineral: 27,
  vitamin: 60,
  fiber: 15,
};

const SummaryPage = () => {
  // const newSummary = fetchNutritionSummary();
  return (
    <div>
      <h1>Summary</h1>
      <ol>
        <li>Upload an image of a receipt</li>
        <li>You can find how much and what kind of nutritions you take</li>
      </ol>
      <NutritionGraph data={dummy_info} />
      {/* <NutritionGraph data={newSummary} /> */}
    </div>
  );
};

export default SummaryPage;
