function validarFormInisesion() {
   var resp =  validarNombreUser();
   if (resp == false) {
       return false;
   }
   resp =  validarPassword();
   if (resp == false) {
       return false;
   }
   return true;
}

function validarNombreUser() {
    var nombre_user = document.getElementById('txt-user').value;
    if (nombre_user.trim().length < 5) {
        //alert('Usuario erreoneo, el minimo de caracteres es de 5');
        Swal.fire({
            icon: 'error',
            title: 'Nombre Usuario',
            text: 'Nombre de usuario muy corto, minimo de caracteres es de 5',
          });
        return false;        
    }
    if (nombre_user.trim().length > 20) {
        //alert('Usuario erreoneo, el minimo de caracteres es de 5');
        Swal.fire({
            icon: 'error',
            title: 'Nombre Usuario',
            text: 'Nombre de usuario muy corto, maximo de caracteres es de 50',
          });
        return false;
    }
    return true;
}

function validarPassword() {
    var pass = document.getElementById('txt-password').value;
    if(pass.trim().length < 8) {
        //alert('Contraseña no cumple con el largo de caracteres')
        Swal.fire({
            icon: 'error',
            title: 'Contraseña',
            text: 'Contraseña no cumple con el largo de caracteres',
          });
        return false;
    }
    return true;
}