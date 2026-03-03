console.log=("Saquen a esteban");

let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
    arrow[i].addEventListener("click", (e)=>[
    let arrowParent = e.target.parentElement.parentElement;
    arrowParent.classList.toggle("showMenu");
    ]);
}
let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", ()=>{
    sidebar.classList.toggle("close");
});

function btn_ingresa(){
    location.href="pag2.htm";
}

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
//Para mandar correos   /^[a-zA-Z0-9._%+-]+@[cecytemorelos]+\.[a-zA-Z]+\.[a-z]$/