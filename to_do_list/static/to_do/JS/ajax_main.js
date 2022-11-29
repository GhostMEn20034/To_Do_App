import {playAudio, getCookie} from "./modules/dynamic_tasks.js";

$(".primary-block-content").on("click", ".cBox", function(){
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
                    $("#tasks-container").replaceWith($(html).find("#tasks-container"));
                });
            }
        }
    });
});
