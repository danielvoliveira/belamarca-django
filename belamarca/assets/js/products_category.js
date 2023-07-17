$(document).ready(function(){
    var filter_state = 'open'
    function open_or_close_products_category(){
        $('#open_filter').click(function(){
            if(filter_state == 'closed'){
                filter_state = 'open'
                $(this).removeClass('selected')
                $('#products_category').addClass('none')
            }else if(filter_state == 'open'){
                filter_state = 'closed'
                $(this).addClass('selected')
                $('#products_category').removeClass('none')
            }
        })
    }
    open_or_close_products_category()

    //.unselect_filter - classe para botão de fechar
})