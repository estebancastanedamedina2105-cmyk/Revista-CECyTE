document.addEventListener("DOMContentLoaded", function () {
  // elementos del chatbot
  let boton = document.getElementById("chatbot-boton");
  let ventana = document.getElementById("chatbot-ventana");
  let mensajes = document.getElementById("chatbot-mensajes");
  let input = document.getElementById("mensaje");

  // abrir chatbot
  boton.addEventListener("click", function () {
    ventana.style.display = "flex";
  });

  // enviar mensaje con ENTER
  input.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      enviarMensaje();
    }
  });
});

// cerrar chatbot
function cerrarChat() {
  document.getElementById("chatbot-ventana").style.display = "none";
}

// enviar mensaje
function enviarMensaje() {
  let input = document.getElementById("mensaje");
  let mensajes = document.getElementById("chatbot-mensajes");

  let texto = input.value;

  if (texto.trim() === "") {
    return;
  }

  // mensaje usuario
  let mensajeUsuario = document.createElement("div");
  mensajeUsuario.className = "mensaje usuario";
  mensajeUsuario.innerText = texto;

  mensajes.appendChild(mensajeUsuario);

  // limpiar input
  input.value = "";

  // enviar al servidor Flask
  fetch("/chatbot", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ mensaje: texto }),
  })
    .then((res) => res.json())
    .then((data) => {
      let mensajeBot = document.createElement("div");
      mensajeBot.className = "mensaje bot";
      mensajeBot.innerText = data.respuesta;

      mensajes.appendChild(mensajeBot);

      // bajar scroll
      mensajes.scrollTop = mensajes.scrollHeight;
    });
}
