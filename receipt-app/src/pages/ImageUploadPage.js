import React from "react";
import NewImageForm from "../components/receipts/NewImageForm";

function NewMeetupPage() {
  // const history = useHistory();
  // function handleAddMeetup(meetupData) {
  //   fetch(
  //     "https://react-get-started-7f410-default-rtdb.firebaseio.com/meetups.json",
  //     {
  //       method: "POST",
  //       body: JSON.stringify(meetupData),
  //       headers: {
  //         "Content-type": "application/json",
  //       },
  //     }
  //   ).then(() => {
  //     history.replace("./");
  //   });
  // }

  return (
    <section>
      <h1>Add New Meetup</h1>
      {/* <NewMeetupForm onAddMeetup={handleAddMeetup} /> */}
      <NewImageForm />
    </section>
  );
}

export default NewMeetupPage;