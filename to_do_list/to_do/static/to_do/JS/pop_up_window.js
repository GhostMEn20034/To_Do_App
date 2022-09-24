document.querySelector(
    "#show-window").addEventListener("click", function () {
    document.querySelector(".pop_up_window").classList.add("active");
});
document.querySelector(".pop_up_window .close-btn").addEventListener(
    "click", function () {
        document.querySelector(".pop_up_window").classList.remove("active");
    });