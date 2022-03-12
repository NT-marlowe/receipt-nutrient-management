import React from "react";
import { useHistory } from "react-router-dom";
import NewImageForm from "../components/receipts/NewImageForm";

function NewMeetupPage() {
  const history = useHistory();
  function handleAddImage(imageData) {
    fetch(
      "https://react-get-started-7f410-default-rtdb.firebaseio.com/meetups.json",
      {
        method: "POST",
        body: JSON.stringify(imageData),
        headers: {
          "Content-type": "application/json",
        },
      }
    ).then(() => {
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

export default NewMeetupPage;