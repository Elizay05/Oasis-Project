function eliminar(url){
    if (confirm('Está seguro?')){
        location.href = url;
    }
}

function add_carrito(url, id_producto) {
    console.log('add_carrito llamado con url:', url, 'e id_producto:', id_producto);
    csrf_token = $("[name='csrfmiddlewaretoken']")[0].value;
    id = $(`#id_${id_producto}`).val()
    cantidad = $(`#cantidad_${id_producto}`).val()

    // Capturo referencia a dom de carrito del offCanvas
    contenido = $("#respuesta_carrito")
    loader = $("#loader")

    loader.removeClass("d-none");
    loader.addClass("d-block");

    offCanvas_carrito = $("#offcanvasRight");
    offCanvas_carrito.offcanvas('toggle');

    $.ajax({
        url: url,
        type: "POST",
        data: {"csrfmiddlewaretoken": csrf_token, "id": id, "cantidad": cantidad}
    })
    .done(function(respuesta) {

        if (respuesta != "Error") {

            loader.removeClass("d-block");
            loader.addClass("d-none");
            // Pintar respuesta en offCanvas
            contenido.html(respuesta);
        }
        else {
            location.href = "/Oasis/inicio/";
        }
    })
    .fail(function(respuesta) {
        location.href = "/Oasis/inicio/";
    });
}

function ver_carrito(url) {
    console.log('ver_carrito llamado con url:', url);
    // Capturo referencia a dom de carrito del offCanvas
    contenido = $("#respuesta_carrito")
    loader = $("#loader")

    loader.removeClass("d-none");
    loader.addClass("d-block");

    offCanvas_carrito = $("#offcanvasRight");
    offCanvas_carrito.offcanvas('toggle');

    $.ajax({
        url: url
    })
    .done(function(respuesta) {

        if (respuesta != "Error") {

            loader.removeClass("d-block");
            loader.addClass("d-none");
            // Pintar respuesta en offCanvas
            contenido.html(respuesta);
        }
        else {
            location.href = "/Oasis/inicio/";
        }
    })
    .fail(function(respuesta) {
        location.href = "/Oasis/inicio/";
    });
}

function eliminar_producto(url, id_producto) {
    console.log('eliminar_producto llamado con url:', url, 'e id_producto:', id_producto);
    csrf_token = $("[name='csrfmiddlewaretoken']")[0].value;
    // Capturo referencia a dom de carrito del offCanvas
    contenido = $("#respuesta_carrito")
    loader = $("#loader")

    loader.removeClass("d-none");
    loader.addClass("d-block");

    offCanvas_carrito = $("#offcanvasRight");
    offCanvas_carrito.offcanvas('toggle');

    $.ajax({
        url: url,
        type: "POST",
        data: {"csrfmiddlewaretoken": csrf_token, "id_producto": id_producto}
    })
    .done(function(respuesta) {

        if (respuesta != "Error") {

            loader.removeClass("d-block");
            loader.addClass("d-none");
            // Pintar respuesta en offCanvas
            contenido.html(respuesta);
        }
        else {
            location.href = "/Oasis/inicio/";
        }
    })
    .fail(function(respuesta) {
        location.href = "/Oasis/inicio/";
    });
}
