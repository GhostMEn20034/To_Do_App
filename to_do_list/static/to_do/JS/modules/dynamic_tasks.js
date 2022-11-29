const modules = {
    playAudio: function () {
   const audio = new Audio("../../../static/to_do/Audio/ping-82822.mp3");
   audio.play().then();
    },
    getCookie: function (name) {
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
},
    findGetParameters: function (parameterName) {
        let result = null,
            tmp = [];
        let items = location.search.substr(1).split("&");
        for (let index = 0; index < items.length; index++) {
            tmp = items[index].split("=");
            if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
        }
        return result;
    }
};

export const playAudio = modules.playAudio;
export const getCookie = modules.getCookie;
export const findGetParameters = modules.findGetParameters;
