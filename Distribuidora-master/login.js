let usuario = document.getElementById('usuario');
let password = document.getElementById('password');


function registrar(e) {
    e.preventDefault();

    if (usuario.value === '' && usuario.value <= 4) {
        alert('Ingrese un usuario..');   
        usuario.focus();    
        return false;
    }
    if (password.value === '' && password.value <= 4){
        alert('Ingrese una contraseña...');
        password.focus();
        return false;
    }
    else {
        alert('Bienvenido ' +  usuario.value);
        window.location.href = 'menu_clientes.html';
        return true;
    }


}

let form = document.getElementById('form');

form.addEventListener('submit', registrar);