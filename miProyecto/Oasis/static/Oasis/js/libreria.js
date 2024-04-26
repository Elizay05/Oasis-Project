function eliminar(url){
    if (confirm('Está seguro?')){
        location.href = url;
    }
}

function remove_producto(url){
    location.href = url;
}

//jquery-3.7.1.min
function ver_carrito(url){
    //Capturo referencia a dom de carrito del offcanvas
    contenido = $("#respuesta_carrito")
    loader = $("#loader")

    loader.removeClass("d-none");
    loader.addClass("d-block");


    offCanvas_carrito = $("#carritoCompras");
    offCanvas_carrito.offcanvas('toggle');

    $.ajax({
        url: url
    })
    .done(function(respuesta){
        if (respuesta != "Error"){
            loader.removeClass("d-block");
            loader.addClass("d-none");
            //Pintar respuesta en offcanvas
            contenido.html(respuesta)
        }
        else{
            location.href="/Oasis/front_productos/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/front_productos/";
    });
}


function add_carrito(url, id_producto){
    
    csrf_token = $("[name='csrfmiddlewaretoken']")[0].value;
    id = $(`#id_${id_producto}`).val()
    cantidad = $(`#cantidad_${id_producto}`).val()


    //Capturo referencia a dom de carrito del offcanvas
    contenido = $("#respuesta_carrito")
    loader = $("#loader")

    loader.removeClass("d-none");
    loader.addClass("d-block");


    offCanvas_carrito = $("#carritoCompras");
    offCanvas_carrito.offcanvas('toggle');

    $.ajax({
        url: url,
        type: "POST",
        data: {"csrfmiddlewaretoken": csrf_token, "id": id, "cantidad": cantidad}
    })
    .done(function(respuesta){
        if (respuesta != "Error"){
            loader.removeClass("d-block");
            loader.addClass("d-none");
            //Pintar respuesta en offcanvas
            contenido.html(respuesta)
        }
        else{
            location.href="/Oasis/front_productos/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/front_productos/";
    });
    
}

function carrito_eliminar(url){
    contenido = $("#respuesta_carrito")
    loader = $("#loader")

    loader.removeClass("d-none");
    loader.addClass("d-block");

    $.ajax({
        url: url,
    })
    .done(function(respuesta){
        if (respuesta != "Error"){
            loader.removeClass("d-block");
            loader.addClass("d-none");
            //Pintar respuesta en offcanvas
            contenido.html(respuesta)
        }
        else{
            location.href="/Oasis/front_productos/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/front_productos/";
    });
}


function actualizar_totales_carrito(url,id){
    contenido = $("#respuesta_carrito")
    loader = $("#loader")
    cantidad = $("#cantidad_carrito_"+id)


    loader.removeClass("d-none");
    loader.addClass("d-block");
    
    $.ajax({
        url: url,
        type: "GET",
        data: {"cantidad": cantidad.val()}
    })
    .done(function(respuesta){
        if (respuesta != "Error"){
            loader.removeClass("d-block");
            loader.addClass("d-none");
            //Pintar respuesta en offcanvas
            contenido.html(respuesta)
        }
        else{
            location.href="/Oasis/front_productos/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/front_productos/";
    });
}
