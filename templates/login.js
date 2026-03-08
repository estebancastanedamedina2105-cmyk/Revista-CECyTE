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
    // 1. Obtener el correo del input
    const correoInput = document.getElementById("correo").value;
    
    // 2. Tu validación (la que ya tienes en la línea 17)
    // Una regla más sencilla que acepta cualquier correo de cecytemorelos.edu.mx
const repro = /^[a-zA-Z0-9._%+-]+@cecytemorelos\.edu\.mx$/;    
    if (!repro.test(correoInput)) {
        alert("Por favor, ingresa un correo institucional válido.");
        return;
    }

    try {
        // 3. El FETCH: Aquí es donde conectas con tilin.py
        const respuesta = await fetch('http://127.0.0.1:5000/verificar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ correo: correoInput })
        });

        const datos = await respuesta.json();

        if (respuesta.ok) {
            // Si el correo existe en la DB
            alert(datos.mensaje); 
            
            // Generamos el código visualmente para probar
            const nuevoCodigo = generarCodigo();
            console.log("Código generado: " + nuevoCodigo);
            
            // Opcional: podrías mostrar el código en el HTML
            // document.getElementById("mensaje").innerText = "Tu código es: " + nuevoCodigo;
        } else {
            alert("Error: " + datos.mensaje);
        }

    } catch (error) {
        console.error("Error de conexión:", error);
        alert("Asegúrate de que tilin.py esté corriendo en la terminal.");
    }
}