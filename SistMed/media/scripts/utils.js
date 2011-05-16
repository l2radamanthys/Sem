/*
    Autor: Ricardo D. Quiroga
    Licencia: GPL2
*/

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


function mostrar(key) {
    /*
    muestra el contenedor definido por key y oculta el resto
    de los contenedores
    */
    var datos = document.getElementById('datos');
    var espec = document.getElementById('especialidades');
    var turnos = document.getElementById('turnos');

    switch (key) {
        case 'datos':
            datos.className = 'show_cont';
            espec.className = 'hide_cont';
            turnos.className = 'hide_cont';
            break;

        case 'especialidades':
            datos.className = 'hide_cont';
            espec.className = 'show_cont';
            turnos.className = 'hide_cont';
            break;

        case 'turnos':
            datos.className = 'hide_cont';
            espec.className = 'hide_cont';
            turnos.className = 'show_cont';
            break;
    }
}
