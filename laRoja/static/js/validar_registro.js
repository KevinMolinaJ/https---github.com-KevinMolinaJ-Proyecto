function validarFormularioReg() {
    var resp = validarNombre();
    if (resp == false) {
        return false;
    }

    var resp = validarApellido();
    if (resp == false) {
        return false;
    }
    /*resp = validarRut();
    if (resp == false) {
        return false;
    }
    resp = validarFechaNac();
    if (resp == false) {
        return false;
    }
    resp = validarGenero();
    if (resp == false) {
        return false;
    }*/
    resp = validarNameUser();
    if (resp == false) {
        return false;
    }
    resp = validarNuevaPass();
    if (resp == false) {
        return false;
    }
    return true;

}

function validarNombre() {
    var nombre = document.getElementById('txtNombre').value;

    if (nombre.trim().length <= 3) {
        //alert('Ingrese Nombre Completo'); 
        Swal.fire({
            icon: 'error',
            title: 'Nombre ',
            text: 'Ingrese nombre',
          });
        return false;       
    }
    if (nombre.trim().length > 50) {
        //alert('Ingrese Nombre Completo'); 
        Swal.fire({
            icon: 'error',
            title: 'Nombre',
            text: 'Nombre muy largo',
          });
        return false;       
    }
    return true;
}

function validarApellido() {
    var apellido = document.getElementById('txtApellido').value;

    if (apellido.trim().length <= 3) {
        //alert('Ingrese Nombre Completo'); 
        Swal.fire({
            icon: 'error',
            title: 'Apellido ',
            text: 'Apellido nombre',
          });
        return false;       
    }
    if (apellido.trim().length > 50) {
        //alert('Ingrese Nombre Completo'); 
        Swal.fire({
            icon: 'error',
            title: 'Apellido',
            text: 'Apellido muy largo',
          });
        return false;       
    }
    return true;
}

/*function validarRut() {
    var rut = document.getElementById('txt-rut').value;

    var num = 3;
    var suma = 0;

    for (let index = 0; index < 8; index++) {
        var caracter = rut.slice(index,index+1); 
        suma = suma +(caracter * num);
        num = num - 1;
        
        if (num == 1) {
            num = 7;
        }
    }

    var resto = suma % 11;
    var dv = 11 - resto;
    
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        }
        else{
            dv = 0;
        }
    }

    var dv_usuario = rut.slice(-1).toUpperCase();

    if (dv != dv_usuario) {
        //alert('Ingrese Rut correcto')
        Swal.fire({
            icon: 'error',
            title: 'Validar Rut',
            text: 'Rut ingresado incorrecto',
          });
    }
    return true;
}

function validarFechaNac() {
    var fecha_nac = document.getElementById('txt-fechanac').value;
    var fecha_sist = new Date();
    var anio = fecha_nac.slice(0,4);
    var mes = fecha_nac.slice(5,7);
    var dias = fecha_nac.slice(8,10);

    var fecha_nuv_nac = new Date(anio,(mes-1),dias);

    if(fecha_nuv_nac > fecha_sist) {
        //alert('Fecha mayor a la del sistema');
        Swal.fire({
            icon: 'error',
            title: 'Fecha de Nacimiento',
            text: 'Fecha mayor a la del sistema',
          });
        return false;
    }

    var dia_segundos = 24*60*60*1000;
    var dif_dia = Math.trunc((fecha_sist.getTime() - fecha_nuv_nac.getTime())/dia_segundos);

    var anios_usuario = Math.trunc(dif_dia/365);

    if(anios_usuario < 18) {
        //alert('Es menor de edad, solo tiene '+anios_usuario+' años.');
        Swal.fire({
            icon: 'error',
            title: 'Fecha de Nacimiento',
            text: 'Es menor de edad, solo tiene '+anios_usuario+' años.',
          });
        return false;
    }
    return true;
}

function validarGenero() {
    var genero = document.getElementById('genero');
    if (genero.value == 0) {
        //alert('Seleccione Genero');
        Swal.fire({
            icon: 'error',
            title: 'Genero',
            text: 'Seleccione Genero',
          });
        return false;
    }
    return true;
}*/

function validarNameUser() {
    var name_user = document.getElementById('txt-nameuser').value;
    if (name_user.trim().length < 2) {
        //alert('Nombre de usuario muy corto, minimo de caracteres es de 5');
        Swal.fire({
            icon: 'error',
            title: 'Nombre Usuario',
            text: 'Nombre de usuario muy corto, minimo de caracteres es de 3',
          });
        return false;
    }
    if (name_user.trim().length > 20) {
        //alert('Nombre de usuario muy corto, minimo de caracteres es de 5');
        Swal.fire({
            icon: 'error',
            title: 'Nombre Usuario',
            text: 'Nombre de usuario muy largo, maximo de caracteres es de 20',
          });
        return false;
    }
    return true;
}

function validarNuevaPass() {
    var pass = document.getElementById('txt-pass').value;
    var conf_pass = document.getElementById('txt-con-pass').value;

    if (pass.trim().length < 8 && conf_pass.trim().length < 8) {
        //alert('Contraseña poco segura, minimo de caracteres es de 8')
        Swal.fire({
            icon: 'error',
            title: 'Contraseña',
            text: 'Contraseña poco segura, minimo de caracteres es de 8',
          });
        return false;
    }

    if(pass != conf_pass) {
        //alert('Contraseñas no coinciden')
        Swal.fire({
            icon: 'error',
            title: 'Contraseña',
            text: 'Contraseñas no coinciden',
          });
        return false;
    }
    return true;
}