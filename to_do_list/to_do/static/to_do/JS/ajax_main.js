function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$(".primary-block-content").on("click", ".cBox", function(){
    let id_task = $(this).attr('id')
    const data = {
        "id": id_task,
    }
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
            if (data.status == 1) {
                $.get(window.location, function(html) {
                    $("#tasks-container").replaceWith($(html).find("#tasks-container"));
                });
            }
        }
    })
});
