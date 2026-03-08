let correoActual = "";
console.log("Bienvenido a ingresar");


  //Para mandar correos   /^[a-zA-Z0-9._%+-]+@[cecytemorelos]+\.[edu]+\.[mx]$/

async function manejarLogin() {

    const correoInput = document.getElementById("correo").value;
    const repro = /^[a-zA-Z0-9._%+-]+@cecytemorelos\.edu\.mx$/; 
    
     if (!repro.test(correoInput)) {
        alert("Por favor, ingresa un correo institucional válido.");
        return;
    }

    try {

        const respuesta = await fetch('http://127.0.0.1:5000/verificar', {
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
        // Este alert SOLO saldrá si de verdad el servidor está apagado
        console.error("Error de conexión:", error);
        alert("Asegúrate de que tilin.py esté corriendo en la terminal.");
    }
}
async function verificarCodigo() {
    const codigoIngresado = document.getElementById("code").value; // ID de tu input de código

    if (!correoActual) {
        alert("Primero debes ingresar tu correo.");
        return;
    }

    try {
        const respuesta = await fetch('http://127.0.0.1:5000/verificar_codigo', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                correo: correoActual, 
                codigo: codigoIngresado 
            })
        });

        const datos = await respuesta.json();

        if (respuesta.ok) {
            alert(datos.mensaje);
            window.location.href = "1_Anuncios.html"; 
        } else {
            alert(datos.mensaje);
        }
    } catch (error) {
        alert("Error al verificar el código.");
    }
}