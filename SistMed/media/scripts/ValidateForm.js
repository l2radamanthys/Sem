/**
FielValidator
--------------
Autor: Ricardo D. Quiroga - L2Radamanthys@gmail.con
status: Alfa
Licencia: GPL2

Esta version utilizara la libreria JQuery

Nota:
-----
por el momento esta version solo soporta 1 formulario por pagina
**/


function Validator(argvs) {
    //clase validadora
    this.argvs = argvs;


    this.evalFields = function() {
        clearAllMsj() //borro todos los mensajes de error
        var error = false;
        for (id in this.argvs) {
            error = error | validateField(id, this.argvs[id]);
        }
        return error;
    }


    this.evalAndSend = function(form_id) {
        //si no encuentra errores envia el formulario
        if (!this.evalFields()) {
            $("#" + form_id).submit();
        }
    }
}


function validateField(id, argv) {
    //valida un campo de acuerdo a los parametros pasados
    var error = false;
    switch (argv['method']) {
        case "maxlength":
            error = maxLenght(id, argv);
            break;

        case "minlenght":
            error = minLenght(id, argv);
            break;

        case "rangelenght":
            error = rangeLenght(id, argv);
            break;


        case "compare":
            error = compare(id, argv);
            break;

        case "number":
            error = number(id, argv);
            break;

        case "min":
            error = Min(id, argv);
            break;

        case "max":
            error = Max(id, argv);
            break;

        case "range":
            error = range(id, argv);
            break;

        case "mail":
            error = mail(id, argv);
            break;

        case "url":
            error = url(id, argv);
            break;
    }
    return error;
}


/*****************************************
 Manejo de Mensajes
*****************************************/

//no se usara
function clearCont(id) {
    //borra todos los mensajes de error dentro del contenedor
    //var cont = $("#" + id + " label");
    var cont = $("#" + id);
    cont.empty();
}

//no se usara
function clearAllCont(argv) {
    //borra todos los mensajes de error, tiene prob -.-

}

//no se usara
function setMessaje(id, text) {
    //agrega el mensaje al final del contenedor
    var cont = $("#" + id);
    clearCont(id);
    cont.append("<p class='field_error'>" + text + "</p>");
}


function clearAllMsj() {
    //borra todos los mensajes de error
    $(".field_error").remove();
}


function insertMessage(id, text) {
    //inserta un mensaje despues de un elemento "campo de formulario" determinado
    $("<p class='field_error'>" + text + "</p>").insertAfter("#" + id);
}


/*****************************************
 metodos de validacion
*****************************************/

function inArray(value, list) {
    //si el elemento esta dentro de la lista
    for (i in list) {
        if (value == list[i]) {
            return true;
        }
    }
    return false;
}


function validArgv(id, argv, request) {
    //valida si el array posee los argumentos requeridos
    error = false;
    for (e in request) {
        if (!inArray(request[e], argv)) {
            insertMessage(id, "Parse Error Falta el Parametro: " + request[e]);
            error= true;
        }
    }
    return error;
}


function minLenght(id, argv) {
    //longitud minima del campo de texto
    var field = $("#" + id);
    if (field.attr("value").length < argv["lenght"]) {
        insertMessage(id, argv["msj"]);
        return true;
    }
    else {
        return false;
    }
}


function maxLenght(id, argv) {
    //longitud maxima del campo de texto
    var field = $("#" + id);
    if (field.attr("value").length > argv["lenght"]) {
        insertMessage(id, argv["msj"]);
        return true;
    }
    else {
        return false;
    }
}


function rangeLenght(id, argv) {
    //si el valor se encuentra dentro del rango
    var field = $("#" + id);
    if ((field.attr("value").length < argv["min"]) || (field.attr("value").length > argv["max"])) {
        insertMessage(id, argv["msj"]);
        return true;
    }
    else {
        return false;
    }
}


function compare(id, argv) {
    //compara si dos campos son iguales
    field_a = $("#" + id);
    field_b = $("#" + argv["other"]);
    if (field_a.attr("value") != field_b.attr("value")) {
        insertMessage(id, argv["msj"]);
        return true;
    }
    else {
        return false;
    }
}


function number(id, argv) {
    //si es numero
    var field = $("#" + id);
    var number = parseInt(field.attr("value"));
    if (isNaN(number)) {
        insertMessage(id, argv["msj"]);
        return true;
    }
    else {
        return false;
    }
}


function Min(id, argv) {
    //si es numero valor minimo
    var field = $("#" + id);
    var number = parseInt(field.attr("value"));
    if (isNaN(number)) {
        insertMessage(id, "Error el campo no Contiene un Valor Numerico");
        return true;
    }
    else if(number < argv["min"]) {
        insertMessage(id, argv["msj"]);
        return true;  
    }
    else {
        return false;
    }
}

function Max(id, argv) {
    //si es numero valor maximo
    var field = $("#" + id);
    var number = parseInt(field.attr("value"));
    if (isNaN(number)) {
        insertMessage(id, "Error el campo no Contiene un Valor Numerico");
        return true;
    }
    else if(number > argv["max"]) {
        insertMessage(id, argv["msj"]);
        return true;  
    }
    else {
        return false;
    }
}


function range(id, argv) {
    //si el valor se encuentra dentro del rango
    var field = $("#" + id);
    var number = parseInt(field.attr("value"));
    if (isNaN(number)) {
        insertMessage(id, "Error el campo no Contiene un Valor Numerico");
        return true;
    }
    else if ((number < argv["min"]) || (number > argv["max"])) {
        insertMessage(id, argv["msj"]);
        return true;  
    }
    else {
        return false;
    }
}


function mail(id, argv) {
    //si es un mail valido
    var field = $("#" + id);
    var reg_exp =  /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
    if (reg_exp.test(field.attr("value"))) {
        return false;
    }
    else {
        return true;
    }
}


function url(id, argv) {
    //si es una url valida
    var field = $("#" + id);
    var reg_exp = /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/;
    if (reg_exp.test(field.attr("value"))) {
        return false;
    }
    else {
        return true;
    }
}






