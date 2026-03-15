let correoActual = "";
console.log("Tilin");


  //Para mandar correos   /^[a-zA-Z0-9._%+-]+@[cecytemorelos]+\.[edu]+\.[mx]$/

async function manejarLogin() {

    const correoInput = document.getElementById("correo").value;
    const repro = /^[a-zA-Z0-9._%+-]+@cecytemorelos\.edu\.mx$/; 
    
     if (!repro.test(correoInput)) {
        alert("Por favor, ingresa un correo institucional válido.");
        return;
    }

    try {

        const respuesta = await fetch('http://127.0.0.1:5000/verificar_correo', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ correo: correoInput })
        });

        const datos = await respuesta.json();

        if (respuesta.ok) {
            correoActual = correoInput; 
            alert(datos.mensaje); 

        } else {
            alert(datos.mensaje);
        }
    } 
    catch (error) {

        console.error("Error de conexión:", error);
        alert("Asegúrate de que tilin.py esté corriendo en la terminal.");
    }
}
async function verificar_Codigo() {
    const codigoIngresado = document.getElementById("code").value;
    const correo = document.getElementById("correo").value;

    try {
        const respuesta = await fetch('http://127.0.0.1:5000/comprobar_codigo', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ correo: correo, codigo: codigoIngresado })
        });

        const resultado = await respuesta.json();

        if (respuesta.ok) {
            localStorage.setItem('usuario_email', correo);
            alert("¡Código correcto! Bienvenida/o.");
            // ESTA LÍNEA HACE LA MAGIA:
            window.location.href = "/"; 
        } else {
            alert(resultado.mensaje);
        }
    } catch (error) {
        console.error("Error:", error);
    }
}
