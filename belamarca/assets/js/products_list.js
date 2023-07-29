$(document).ready(function(){
    function set_default_filter_url(){
        let path = window.location.pathname

        let searchParams = new URLSearchParams(window.location.search)
        if(
            path == '/produtos/' &&
            searchParams.has('categories') == false &&
            searchParams.has('sizes') == false &&
            searchParams.has('types') == false &&
            searchParams.has('colors') == false &&
            searchParams.has('prints') == false &&
            searchParams.has('materials') == false
        ){
            default_filters = '?categories=[]&sizes=[]&types=[]&colors=[]&prints=[]&materials=[]'
            history.pushState({}, null, default_filters)
        }
    }
    set_default_filter_url()

    function get_products_list(){
        let searchParams = new URLSearchParams(window.location.search)

        let categories
        let sizes
        let types
        let colors
        let prints
        let materials

        data = {}

        if(searchParams.has('categories') == true){
            categories = searchParams.get('categories')
            data.categories = categories
        }
        if(searchParams.has('sizes') == true){
            sizes = searchParams.get('sizes')
            data.sizes = sizes
        }
        if(searchParams.has('types') == true){
            types = searchParams.get('types')
            data.types = types
        }
        if(searchParams.has('colors') == true){
            colors = searchParams.get('colors')
            data.colors = colors
        }
        if(searchParams.has('prints') == true){
            prints = searchParams.get('prints')
            data.prints = prints
        }
        if(searchParams.has('materials') == true){
            materials = searchParams.get('materials')
            data.materials = materials
        }

        $.ajax({
            url: '/produto/product_list/',
            data: data,
            type: 'GET',
            cache: false,
            dataType: 'html',
            success: function (response) {
                $('.product_list').html(response)
            }
        })
    }
    get_products_list()

    function get_filters_from_url(){
        let searchParams = new URLSearchParams(window.location.search)
        let selected_filters = [];

        if(searchParams.has('categories') == true){
            selected_filters.category = searchParams.get('categories')
        }
        if(searchParams.has('sizes') == true){
            selected_filters.size = searchParams.get('sizes')
        }
        if(searchParams.has('types') == true){
            selected_filters.type = searchParams.get('types')
        }
        if(searchParams.has('colors') == true){
            selected_filters.color = searchParams.get('colors')
        }
        if(searchParams.has('prints') == true){
            selected_filters.print = searchParams.get('prints')
        }
        if(searchParams.has('materials') == true){
            selected_filters.material = searchParams.get('materials')
        }

        return selected_filters
    }

    function change_url_filters(filter='', id_filter='', action='select'){
        if(filter != '' && Number.isInteger(id_filter) == true){
            selected_filters = get_filters_from_url()
            array_selected_filters = JSON.parse(selected_filters[filter])

            if(action == 'select'){
                array_selected_filters.push(id_filter)
            }else if(action == 'unselect'){
                position = array_selected_filters.indexOf(id_filter);
                if (~position) array_selected_filters.splice(position, 1)
            }
            selected_filters[filter] = '[' + array_selected_filters.toString() + ']'

            final_filters = '?categories=' + selected_filters.category + '&sizes=' + selected_filters.size + '&types=' + selected_filters.type + '&colors=' + selected_filters.color + '&prints=' + selected_filters.print + '&materials=' + selected_filters.material
            history.pushState({}, null, final_filters)
        }
    }

    function select_and_unselect_filter(){
        $('.filters ul li').click(function(){
            let filter_name = $(this).data('filter')
            let id = $(this).data('id')
            let filter_text = $(this).data('text')
            let filter_color = $(this).data('color')
            let filterimage_url = $(this).data('imageurl')
            let filter_image_alt = $(this).data('imagealt')

            if($(this).hasClass('selected')){
                $(this).removeClass('selected')
                change_url_filters(filter=filter_name, id_filter=id, action='unselect')
                remove_filter_from_selecteds(filter=filter_name, id_filter=id)
            }else{
                $(this).addClass('selected')
                change_url_filters(filter=filter_name, id_filter=id, action='select')
                add_filter_to_selecteds(filter=filter_name, id_filter=id, filter_text, filter_color, filterimage_url, filter_image_alt)
            }
            show_or_close_selected_filters()
            get_products_list()
        })
    }
    select_and_unselect_filter()

    function add_filter_to_selecteds(filter='', id_filter='', filterText='', filterColor='', imageUrl='', imageAlt=''){
        if(filter == 'category'){
            let filter_html = "<li class='category unselect_filter' data-filter='category' data-id='"+ id_filter +"'>"
                                    + "<div class='container'>"
                                        + "<p>" + filterText + "</p>"
                                        + "<img class='close-filter' src='/static/assets/images/close-icon.svg' alt='Seta para baixo'>"
                                    + "</div>"
                                + "</li>"
            $('div#selected_filters ul').append(filter_html)
        }

        if(filter == 'size'){
            let filter_html = "<li class='size unselect_filter' data-filter='size'  data-id='"+ id_filter +"'>"
                                    + "<div class='container'>"
                                        + "<p>" + filterText + "</p>"
                                        + "<img class='close-filter' src='/static/assets/images/close-icon.svg' alt='Seta para baixo'>"
                                    + "</div>"
                                + "</li>"
            $('div#selected_filters ul').append(filter_html)
        }

        if(filter == 'type'){
            let filter_html = "<li class='size unselect_filter' data-filter='type'  data-id='"+ id_filter +"'>"
                                    + "<div class='container'>"
                                        + "<p>" + filterText + "</p>"
                                        + "<img class='close-filter' src='/static/assets/images/close-icon.svg' alt='Seta para baixo'>"
                                    + "</div>"
                                + "</li>"
            $('div#selected_filters ul').append(filter_html)
        }

        if(filter == 'color'){
            let filter_html = "<li class='color unselect_filter' data-filter='color'  data-id='"+ id_filter +"'>"
                                    + "<div class='container'>"
                                        + "<div>"
                                            + "<p style='background-color: " + filterColor + "; border: solid 0.5px #eee;'></p></p>"
                                        + "</div>"
                                        + "<p class='name'>" + filterText + "</p>"
                                        + "<img class='close-filter' src='/static/assets/images/close-icon.svg' alt='Seta para baixo'>"
                                    + "</div>"
                                + "</li>"
            $('div#selected_filters ul').append(filter_html)
        }

        if(filter == 'print'){
            let filter_html = "<li class='print unselect_filter' data-filter='print' data-id='"+ id_filter +"'>"
                                    + "<div class='container'>"
                                        + "<div>"
                                            + "<img src='" + imageUrl + "' alt='" + imageAlt + "'>"
                                        + "</div>"
                                        + "<p class='name'>" + filterText + "</p>"
                                        + "<img class='close-filter' src='/static/assets/images/close-icon.svg' alt='Seta para baixo'>"
                                    + "</div>"
                                + "</li>"
            $('div#selected_filters ul').append(filter_html)
        }

        if(filter == 'material'){
            let filter_html = "<li class='size unselect_filter' data-filter='material'  data-id='"+ id_filter +"'>"
                                    + "<div class='container'>"
                                        + "<p>" + filterText + "</p>"
                                        + "<img class='close-filter' src='/static/assets/images/close-icon.svg' alt='Seta para baixo'>"
                                    + "</div>"
                                + "</li>"
            $('div#selected_filters ul').append(filter_html)
        }

        close_filter_button()
    }

    function remove_filter_from_selecteds(sended_filter='', sended_id_filter=''){
        $('#selected_filters').children().children().each(function () {
            let selected_filter_id = $(this).data('id')
            let selected_filter_type = $(this).data('filter')

            if(selected_filter_id == sended_id_filter && selected_filter_type == sended_filter){
                $(this).remove()
            }
        });
    }

    function remove_class_selected_from_filters(sended_filter='', sended_id_filter=''){
        $('.filter').children('ul').children().each(function () {
            let selected_filter_id = $(this).data('id')
            let selected_filter_type = $(this).data('filter')

            if(selected_filter_id == sended_id_filter && selected_filter_type == sended_filter){
                $(this).removeClass('selected')
            }
        });
    }

    function close_filter_button(){
        $('li.unselect_filter').click(function(){
            let filter_name = $(this).data('filter')
            let id = $(this).data('id')
            change_url_filters(filter=filter_name, id_filter=id, action='unselect')
            $(this).remove()
            remove_class_selected_from_filters(filter_name, id)
            show_or_close_selected_filters()
            get_products_list()
        })
    }
    close_filter_button()

    function show_or_close_selected_filters(){
        let selected_filters = $('#selected_filters').children().children()
        if(selected_filters.length == 0){
            $('#selected_filters').addClass('none')
        }else{
            $('#selected_filters').removeClass('none')
        }
    }
    show_or_close_selected_filters()
})