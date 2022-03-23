import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const options = {
  responsive: true,
  plugins: {
    legend: {
      position: "top",
      display: false,
    },
    title: {
      display: true,
      text: "Nutrition Summary",
      font: {
        size: 18,
        weight: "bold",
      },
    },
  },
  scales: {
    y: {
      min: 0,
      max: 80,
    },
  },
};

const NutritionGraph = (props) => {
  if (props.data === null) {
    return <p>loading...</p>;
  }

  const labels = Object.keys(props.data);
  const data = {
    labels,
    datasets: [
      {
        label: "score",
        data: labels.map((label) => props.data[label]),
        backgroundColor: [
          "rgba(255, 99, 132, 0.5)",
          "rgba(255, 159, 64, 0.5)",
          "rgba(255, 205, 86, 0.5)",
          "rgba(75, 192, 192, 0.5)",
          "rgba(54, 162, 235, 0.5)",
          "rgba(153, 102, 255, 0.5)",
        ],
        borderColor: [
          "rgb(255, 99, 132)",
          "rgb(255, 159, 64)",
          "rgb(255, 205, 86)",
          "rgb(75, 192, 192)",
          "rgb(54, 162, 235)",
          "rgb(153, 102, 255)",
        ],
      },
    ],
  };

  return <Bar options={options} data={data} />;
};

export default NutritionGraph;
