import axios from "axios";
import React from "react";
import { useHistory } from "react-router-dom";
import NewImageForm from "../components/receipts/NewImageForm";

const ImageUploadPage = () => {
  const history = useHistory();

  const handleAddImage = (formData) => {
    // fetch(
    //   "https://react-get-started-7f410-default-rtdb.firebaseio.com/meetups.json",
    //   {
    //     method: "POST",
    //     body: JSON.stringify(formData),
    //     headers: {
    //       "Content-type": "application/json",
    //       // "Content-type": "multipart/form-data",
    //     },
    //   }
    // ).then(() => {
    //   history.replace("./");
    // });
    axios
      .post(
        "https://react-get-started-7f410-default-rtdb.firebaseio.com/meetups.json",
        JSON.stringify(formData),
        {
          headers: {
            "Content-type": "application/json",
          },
        }
      )
      .then(() => {
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
