
function desplegar(key) {
    /*
     Muestra/Oculta el menu dependiendo del estado anterior
     */
    var menu = document.getElementById(key);
    if (menu.className == 'nav_menu') {
        menu.className = 'hide_nav_menu';
    } else {
        menu.className = 'nav_menu';
    }
}

function ocultar(key) {
    /*
     Oculta el menu
    */
    var menu = document.getElementById(key);
    menu.className = 'hide_nav_menu';
}


function answer_redirect(pregunta, url_redirect) {
    /*
     funcion sencilla para confirmar borrado de algun elemento
     en ves de tener q gastarme en armar una vista para confirmacion
     */
    answer_box = confirm (pregunta);
    if (answer_box) {
        window.location = url_redirect;
    }
}
