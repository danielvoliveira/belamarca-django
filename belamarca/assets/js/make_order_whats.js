$(document).ready(function(){
    $("button#make_order_whats").click(function () {
        var message = $(this).data('message')
        var number = '5513997977005'
        let url = 'https://wa.me/'
        let end_url = `${url}${number}?text=${message}`
        window.open(end_url, '_blank');
    });
});