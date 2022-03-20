import axios from "axios";
import React from "react";
import { useHistory } from "react-router-dom";
import NewImageForm from "../components/receipts/NewImageForm";

const ImageUploadPage = () => {
  const history = useHistory();

  const handleAddImage = (formData) => {
    axios
      .post(
        // "https://react-get-started-7f410-default-rtdb.firebaseio.com/meetups.json",
        "http://127.0.0.1:8000/uploadimg/",
        // JSON.stringify(formData),
        formData,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
      .then((response) => {
        console.log(response.data);
        alert("Image was uploaded successfully!");
        history.replace("./");
      });
  };

  return (
    <section>
      <h1>Upload Receipt</h1>
      <NewImageForm onAddImage={handleAddImage} />
    </section>
  );
};

export default ImageUploadPage;
