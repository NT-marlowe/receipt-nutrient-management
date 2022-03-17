import axios from "axios";

const fetchNutritionSummary = () => {
  let jsonData;
  axios
    .get("http://127.0.0.1:8000/fetch-summary/")
    .then((response) => {
      jsonData = response.data;
    })
    .catch((err) => {
      console.error(err);
    });

  return jsonData;
};

export default fetchNutritionSummary;