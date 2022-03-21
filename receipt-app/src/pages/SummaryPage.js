import React, { useState, useEffect } from "react";
import axios from "axios";
import NutritionGraph from "../components/nutrition/NutritionGraph";
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
      <ol>
        <li>Upload an image of a receipt</li>
        <li>You can find how much and what kind of nutritions you take</li>
      </ol>
      <NutritionGraph data={newSummary} />
    </div>
  );
};

export default SummaryPage;
