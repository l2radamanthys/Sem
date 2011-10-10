/**
FielValidator
--------------
Autor: Ricardo D. Quiroga - L2Radamanthys@gmail.con
status: Alfa
Licencia: GPL2
**/


function Validator(argv) {
    //Clase base para validacion de Campos de Formularios
    this.argv = argv;
    
    this.eval_fields = function() {
        // evalua los campos designados en argv
        var error = false;
        for (i in this.argv) {
            result = validate_field(this.argv[i][0], this.argv[i][1]);
            error = error || result;
        }
        return (!error);
    }

    this.clear_all_cont = function() {
        //borra los nodos hijos de todos los contenedores
        for (i in this.argv) {
            reset_cont(this.argv[i][1]['cont_id'])
        }
    }

}


function FormValidator(form_id, argv) {
    //derivacion q permite validar formularios
    this.argv = argv;
    this.form = document.getElementById(form_id);

    this.eval_fields = function() {
        // evalua los campos designados en argv
        var error = false;
        for (i in this.argv) {
            result = validate_field(this.argv[i][0], this.argv[i][1]);
            error = error || result;
            //validate_field(this.argv[i][0], this.argv[i][1]);
        }
        return (!error);
    }

    this.clear_all_cont = function() {
        //borra los nodos hijos de todos los contenedores
        for (i in this.argv) {
            reset_cont(this.argv[i][1]['cont_id'])
        }
    }

    
    this.eval_and_send = function() {
        //evalua los campos, si son correctos envia el formulario
        if (this.eval_fields()) {
            this.form.submit(); //envia el formulario
            return true;
        }
        else {
            return false;
        }
    }
} 


function validate_field(field_id, argv) {
    //valida los campos
    var field = document.getElementById(field_id);
    var error = false;
    reset_cont(argv['cont_id']); //borro nodos hijos del contenedor de msj error
    switch (argv['method']) {
        case 'max_lenght':
            error = max_lenght(field_id, argv);
            break;

        case 'min_lenght':
            error = min_lenght(field_id, argv);
            break;

        case 'valid_email':
            error = valid_mail(field_id, argv);
            break;

        case 'cmp_field':
            error = compare_field(field_id, argv);
            break;

        case 'valid_pass':
            error = valid_pass(field_id, argv);
            break;
            
        case 'valid_date':
            error = false;
            break;

        case 'alert': //no comprueba nada emite un msj
            set_mensaje(argv['cont_id'], 'Prueba: error intencional');
            error = true;
            break;
            
        default:
            set_mensaje(argv['cont_id'], 'error methodo o argumentos ivalidos: ' + argv['method']);
            break;
    }
    return error;
}


function reset_cont(cont_id) {
    //elimina todos los nodos hijos
    var array_nodos = document.getElementById(cont_id).childNodes;
    if (array_nodos != undefined)  {
        for (var i=0; i < array_nodos.length; i++) {
            if(array_nodos[i].nodeType == 1) {
                array_nodos[i].parentNode.removeChild(array_nodos[i]);
            }
        }
    }
}


function set_mensaje(cont_id, text) {
    //escribe un msj en el contenedor designado
    var contenedor = document.getElementById(cont_id);
    var parrafo = document.createElement('p');
    parrafo.className = 'field_error';
    var contenido = document.createTextNode(text);
    parrafo.appendChild(contenido);
    contenedor.appendChild(parrafo);
}


/*****************************************
 metodos de validacion
*****************************************/

function max_lenght(field_id, argv) {
    //longitud maxima
    var field = document.getElementById(field_id);
    var error = false;
    if (argv['lenght'] != undefined)  {
        if (argv['lenght'] < field.value.toString().length) {
            error = true;
        }
    }
    if (error) {
        set_mensaje(argv['cont_id'], argv['msj_error']);
    }
    return error;
}

    
function min_lenght(field_id, argv) {
    //longitud minima
    var field = document.getElementById(field_id);
    var error = false;
    if (argv['lenght'] != undefined)  {
        if (argv['lenght'] > field.value.toString().length) {
            error = true;
        }
    }
    if (error) {
        set_mensaje(argv['cont_id'], argv['msj_error']);
    }
    return error;
}


function valid_mail(field_id, argv) {
    // validar una direcion de mail
    var field = document.getElementById(field_id);
    //var reg_exp = /^w+([.-]?w+)*@w+([.-]?w+)*(.w{2,3})+$/;
    var reg_exp = /^(.+\@.+\..+)$/;
    var texto = field.value.toString()
    var error = false;
    if (!reg_exp.test(texto)) {
        error = true;
    }
        
    if (error) {
        set_mensaje(argv['cont_id'], argv['msj_error']);
    }
    return error;
}


function valid_pass(field_id, argv) {
    //valida un campo password para q no posea caracteres extraños
    var field = document.getElementById(field_id);
    var reg_exp = /(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,10})$/;
    var texto = field.value.toString();
    var error = false;
    if (!reg_exp.test(texto)) {
        error = true;
    }
    
    if (error) {
        set_mensaje(argv['cont_id'], argv['msj_error']);
    }
    return error;
}


function compare_field(field_id, argv) {
    //compara si el texto contenido en 2 campos es igual
    var field_a = document.getElementById(field_id);
    var field_b = document.getElementById(argv['field_cmp']);
    var error = false;
    if (field_a.value.toString() != field_b.value.toString()) {
        error = true;
    }
    if (error) {
        set_mensaje(argv['cont_id'], argv['msj_error']);
    }
    return error;
}


