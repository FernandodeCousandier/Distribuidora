let apellido = document.getElementById('apellido');
let nombre = document.getElementById('nombre');
let cuit = document.getElementById('cuit');
let email = document.getElementById('email');
let telefono = document.getElementById('telefono');
let direccion = document.getElementById('direccion');
let ciudad = document.getElementById('ciudad');
let clientes = [];

let validar_mail = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/

function validar(e) {
    e.preventDefault();

    if (apellido.value === "") {
        alert("Ingrese su apellido");
        apellido.focus();
        return false;
    }
    if (nombre.value === "") {
        alert("Ingrese su nombre");
        nombre.focus();
        return false;
    }
    if (cuit.value === "" || cuit.value.length < 11) {
        alert("Ingrese un CUIT válido");
        cuit.focus();
        return false;
    }
    if (!validar_mail.test(email.value)) {
        alert("Ingrese un email válido");
        email.focus();
        return false;
    }
    if (telefono.value === "" || telefono.value.length < 10) {
        alert("Ingrese un teléfono válido");
        telefono.focus();
        return false;
    }
    if (direccion.value === "") {
        alert("Ingrese su dirección");
        direccion.focus();
        return false;
    }
    if (ciudad.value === "") {
        alert("Ingrese su ciudad");
        ciudad.focus();
        return false;
    }
    else
        alert("Alta de cliente correcta, gracias: " + apellido.value);
        clientes.push(apellido.value,nombre.value,cuit.value,email.value,telefono.value,direccion.value,ciudad.value,);
        console.log(clientes);
        form.reset();
        return true;
}
let form = document.getElementById('form');
form.addEventListener('submit', validar);