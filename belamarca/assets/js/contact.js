$(document).ready(function(){
    function Register_Contact(){
        $("button#btn-contact").click(function(){
            $("h2#modal-title").text("Atenção");
            url = $("#contact-url").val();
            var formData = new FormData(document.getElementById("contact"));
            $.ajax({
                url: url,
                type: "POST",
                enctype: 'multipart/form-data',
                data: formData,
                processData: false,
                contentType: false,
                cache: false,
                success: function (response) {
                    if (response.status == 1){
                        $('#contact-name').val("");
                        $('#contact-email').val("");
                        $('#contact-telephone').val("");
                        $('#contact-subject').val("");
                        $('#contact-textarea').val("");
                        $("#contact-check").prop('checked', false);
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
    }
    Register_Contact();
});