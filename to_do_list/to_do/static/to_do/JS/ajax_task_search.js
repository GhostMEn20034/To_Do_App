import {playAudio, getCookie, findGetParameters} from "./modules/dynamic_tasks.js";

$(".outerBlock").on("click", ".cBox", function(){
    let id_task = $(this).attr('id');
    const data = {
        "id": id_task,
    };
    $.ajax({
        url: "",
        type: "POST",
        dataType: "json",
        data: JSON.stringify({"payload":data}),
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie('csrftoken')
        },
        cache: false,
                success: (data) => {
            if (data.done == true) {
                playAudio();
            }
            if (data.status == 1) {
                $.get(window.location, function(html) {
                    $(".innerBlock").replaceWith($(html).find(".innerBlock"));
                });
            }
        }
    });
});

const is_completed_tasks_hidden = () => {
    if (findGetParameters("hide_completed") == null) {
        $(".hideCompletedTasks").html("Hide completed tasks");
    } else {
        $(".hideCompletedTasks").html("Show completed tasks");
    }
};

const hide_completed_task = () => {
    $('.hideCompletedTasks').click(
        function () {
            if (findGetParameters("hide_completed") == null) {
                window.location.href += "&hide_completed=True";
        } else {
                window.location.href = window.location.href.replace("&hide_completed=True", "");
            }
        }
    );
};

hide_completed_task();
is_completed_tasks_hidden();