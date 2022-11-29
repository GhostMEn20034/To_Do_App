document.querySelector(
    ".delete-task").addEventListener("click", function () {
    document.querySelector(".danger-msg").classList.add("active");
});

document.querySelector(
    ".close-window").addEventListener("click", function () {
    document.querySelector(".danger-msg").classList.remove("active");
});
