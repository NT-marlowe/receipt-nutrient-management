import React, { useRef } from "react";
import Card from "../ui/Card";
import classes from "./NewImageForm.module.css";

function NewMeetupForm(props) {
  const dateInputRef = useRef();
  // const imageInputRef = useRef();
  const fileInputRef = React.createRef();
  const descriptionInputRef = useRef();

  function handleSubmit(event) {
    event.preventDefault();

    const enteredDate = dateInputRef.current.value;
    // const enteredImage = imageInputRef.current.value;
    const enteredImage = fileInputRef.current.files[0];
    const enteredDescription = descriptionInputRef.current.value;
    // const imageData = {
    //   date: enteredDate,
    //   image: enteredImage,
    //   description: enteredDescription,
    // };
    // 
    const metaData = {
      data: enteredDate,
      description: enteredDescription
    }

    const submitData = new FormData();
    submitData.append("formData", JSON.stringify(metaData));
    submitData.append("image", enteredImage);

    props.onAddImage(submitData);
    // console.log(submitData.get("formData"));
    // console.log(submitData.get("image"));
  }

  return (
    <Card>
      <form className={classes.form} onSubmit={handleSubmit}>
        <div className={classes.control}>
          <label htmlFor="title">Date</label>
          <input type="date" required id="date" ref={dateInputRef} />
        </div>
        <div className={classes.control}>
          <label htmlFor="image">Receipt Image</label>
          <input
            type="file"
            required
            id="image"
            // ref={imageInputRef}
            ref={fileInputRef}
            accept="image/*"
          />
        </div>
        <div className={classes.control}>
          <label htmlFor="description">Description</label>
          <textarea
            id="description"
            required
            rows="5"
            ref={descriptionInputRef}
          ></textarea>
        </div>
        <div className={classes.action}>
          <button>Upload Receipt</button>
        </div>
      </form>
    </Card>
  );
}

export default NewMeetupForm;
