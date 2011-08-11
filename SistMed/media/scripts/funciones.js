
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


