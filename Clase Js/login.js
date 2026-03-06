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