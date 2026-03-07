console.log("Bienvenido a ingresar");


function generarCodigo() {
  const codigo = Math.floor(1000 + Math.random() * 9000);
  return codigo.toString(); // Convierte a cadena por si se requiere manipulación
}

console.log("Código generado: " + generarCodigo());
    
function codigo () {
    
}
function entrarCode() {
    window.location.href = "../templates/1_Anuncios.html";
}
//Para mandar correos   /^[a-zA-Z0-9._%+-]+@[cecytemorelos]+\.[edu]+\.[mx]$/

async function manejarLogin() {
   
    const correoInput = document.getElementById("correo").value;

    const repro = /^[a-zA-Z0-9._%+-]+@[cecytemorelos]+\.[edu]+\.[mx]$/;
    
    if (!repro.test(correoInput)) {
        alert("Por favor, ingresa un correo institucional válido.");
        return;
    }

    try {
        const respuesta = await fetch('http://localhost:5000/verificar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ correo: correoInput })
        });

        const datos = await respuesta.json();

        if (respuesta.ok) {
            alert(datos.mensaje); 
            
            entrarCode(); 
        } else {
            alert("Error: " + datos.mensaje);
        }

    } catch (error) {
        console.error("Error de conexión:", error);
        alert("Asegúrate de que tu servidor Flask (tilin.py) esté encendido.");
    }
}