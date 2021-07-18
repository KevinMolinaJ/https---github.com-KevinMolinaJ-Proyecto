function validarFromContactenos() {
    var resp = validarNombre();
    if (resp == false) {
        return false;
    }
    resp = validarFono();
    if (resp == false) {
        return false;
    }
    resp = validarComenta();
    if (resp == false) {
        return false;
    }
    return true;
}

function validarNombre() {
    var nombre = document.getElementById('txtNombre').value;
    if (nombre.trim().length < 2) {
        //alert('Ingrese Nombre Completo');
        Swal.fire({
            icon: 'error',
            title: 'Nombre Completo',
            text: 'Ingrese nombre y apellido',
          });
        return false;
    }
    return true;
}

function validarFono() {
    var fono = document.getElementById('txt-fono').value;
    if (fono.trim().length != 9) {
        //alert('Fono incorrecto, el formato es de 9 digitos')
        Swal.fire({
            icon: 'error',
            title: 'Telefono',
            text: 'Fono incorrecto, el formato es de 9 digitos',
          });
        return false;
    }
    return true;
}

function validarComenta() {
    var comentario = document.getElementById('txt-comen').value;
    if (comentario.trim().length < 1) {
        //alert('Debe ingresar un comentario')
        Swal.fire({
            icon: 'error',
            title: 'Telefono',
            text: 'Debe ingresar un comentario',
          });
        return false;
    }
    return true;
}