import React, { useRef } from "react";
import Card from "../ui/Card";
import classes from "./NewImageForm.module.css";

function NewMeetupForm(props) {
  const dateInputRef = useRef();
  // const imageInputRef = useRef();
  const fileInputRef = React.createRef();
  const descriptionInputRef = useRef();
  let base64Txt = "";

  const onChange = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
      base64Txt = e.target.result.replace(/data:.*\/.*;base64,/, "");
    };
    reader.readAsDataURL(file);
  };

  function handleSubmit(event) {
    event.preventDefault();

    const enteredDate = dateInputRef.current.value;
    // const enteredImage =fileInputRef.current.files[0];
    const enteredDescription = descriptionInputRef.current.value;

    const formData = {
      date: enteredDate,
      base64Txt: base64Txt,
      description: enteredDescription,
    };

    props.onAddImage(formData);
    // console.log(formData);
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
            onChange={onChange}
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
