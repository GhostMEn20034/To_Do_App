const task_title = document.getElementById("task-title");

task_title.addEventListener('click', () => {
        console.log(window.location)
        document.querySelector(".hidden-fields.hidden").classList.remove("hidden")
});

