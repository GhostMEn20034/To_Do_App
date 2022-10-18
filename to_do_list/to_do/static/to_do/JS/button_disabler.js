const submitButton = document.getElementById("submit-form");
const input = document.getElementById("task-title");

input.addEventListener("keyup", (e) => {
    const value = e.currentTarget.value;
    submitButton.disabled = false;
    if (value === "") {
        submitButton.disabled = true;
    }
});

