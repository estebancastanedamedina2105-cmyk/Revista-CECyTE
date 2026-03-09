console.log("Hola_Mundo");
function toggleChatbot() {
    var chatBody = document.getElementById("chatbot-body");
    chatBod.style.display = chatBody.style.display === "none" ;
    }
function sednMensaje() {
    var input = document.getElementById("chat-input");
    var mensaje = input.value;
    input.value = "";
    fetch("/Chatbot")
}
function btn_revista(){
    location.href=("1_Anuncios.html");
}
// Cierra el menú al hacer clic fuera de él
document.addEventListener('click', function(event) {
  var menu = document.getElementById('miMenu');
  var boton = document.getElementById('miBoton');

  // Si el clic no fue en el menú ni en el botón, ocultar
  if (!menu.contains(event.target) && !boton.contains(event.target)) {
    menu.style.display = 'none';
  }
});
