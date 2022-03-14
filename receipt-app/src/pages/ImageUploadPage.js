import axios from "axios";
import React from "react";
import { useHistory } from "react-router-dom";
import NewImageForm from "../components/receipts/NewImageForm";

function ImageUploadPage() {
  const history = useHistory();

  function handleAddImage(submitData) {
    // fetch(
    //   "https://react-get-started-7f410-default-rtdb.firebaseio.com/meetups.json",
    //   {
    //     method: "POST",
    //     body: JSON.stringify(submitData),
    //     headers: {
    //       // "Content-type": "application/json",
    //       "Content-type": "multipart/form-data",
    //     },
    //   }
    // ).then(() => {
    //   history.replace("./");
    // });
    axios
      .post(
        "http://localhost:8000/api/upload",
        submitData,
        {
          headers: {
            "Content-type": "multipart/form-data",
          },
        }
      )
      .then(() => {
        history.replace("./");
      });
  }

  return (
    <section>
      <h1>Upload Receipt</h1>
      <NewImageForm onAddImage={handleAddImage} />
      {/* <NewImageForm /> */}
    </section>
  );
}

export default ImageUploadPage;
