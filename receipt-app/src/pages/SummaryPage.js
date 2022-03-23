import React, { useState, useEffect } from "react";
import axios from "axios";
import NutritionGraph from "../components/nutrition/NutritionGraph";
import FoodRecommendation from "../components/nutrition/FoodRecommendation";
// import fetchNutritionSummary from "../components/nutrition/fetchNutritionSummary";

const SummaryPage = () => {
  const [newSummary, setNewSummary] = useState([]);
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/summary/")
      .then((response) => {
        setNewSummary(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>Summary</h1>
      <h2>Your Score</h2>
      <NutritionGraph data={newSummary} />
      <br />
      <h2>Food Recommendation</h2>
      <FoodRecommendation nutritions={newSummary} />
    </div>
  );
};

export default SummaryPage;
