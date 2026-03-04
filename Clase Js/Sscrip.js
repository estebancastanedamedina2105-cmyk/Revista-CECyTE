function btn_login(){
    location.href = "5-Login.html";
}
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
//Para mandar correos   /^[a-zA-Z0-9._%+-]+@[cecytemorelos]+\.[edu]+\.[mx]$/