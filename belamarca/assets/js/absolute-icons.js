$(document).ready(function(){
    jQuery(function() {
        window.onscroll = () => {
            if (window.scrollY > 200) {
                $("#back-top").addClass('show-icon');
            } else {
                $("#back-top").removeClass('show-icon');
            }
        }

        $("#back-top").click(function () {
            $('html, body').animate ({
                scrollTop: 0
            }, 50, 'linear');
        });
    });
});