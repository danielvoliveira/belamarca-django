$(document).ready(function(){
    /*function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });*/
    $("button#btn-news").click(function() {
        $("h2#modal-title").text("Atenção");
        url = document.getElementById('subscribe').getAttribute('value');
        /*token = $("input[type=hidden][name=csrfmiddlewaretoken]").val();
        nome = $("#nome").val();
        email = $("#email").val();
        termos = $("input[type=checkbox][name=fcheck]:checked").val();*/

        var formData = new FormData(document.getElementById("subscribe"));

        $.ajax({
            url: url,
            //data: { 'nome': nome, 'email': email, 'termos': termos, csrfmiddlewaretoken: token},
            type: 'POST',
            enctype: 'multipart/form-data',
            data: formData,
            processData: false,
            contentType: false,
            cache: false,
            //dataType: 'json',
            success: function (response) {
                if (response.status == 1) {
                    $('#nome').val("");
                    $('#email').val("");
                    $("#news-check").prop('checked', false);
                    $("h2#modal-title").text("Sucesso");
                }
                $("p#return-message").text(response.message);
                $(".modal-default").css("display", "block");
                $("body").css("overflow", "hidden");
                //document.body.style.overflow = "hidden"
                $(".modal-btn").click(function(){
                    $(".modal-default").css("display", "none");
                    $("body").css("overflow", "auto");
                });
            }
        });
    });
});