// Usamos nombres únicos para no chocar con el botón del modo oscuro
const chatAbrir = document.getElementById("chatbot-boton");
const chatVentana = document.getElementById("chatbot-ventana");
const chatCerrar = document.getElementById("cerrar");

const chatEnviar = document.getElementById("enviar");
const chatInput = document.getElementById("mensaje");
const chatContenedor = document.getElementById("chatbot-mensajes");

// Abrir y cerrar la ventana
chatAbrir.addEventListener("click", () => {
  chatVentana.style.display = "flex";
});

chatCerrar.addEventListener("click", () => {
  chatVentana.style.display = "none";
});

// Crear y mostrar los mensajes en la interfaz
function agregarMensaje(texto, tipo) {
  const div = document.createElement("div");
  div.classList.add(tipo);
  div.textContent = texto;

  chatContenedor.appendChild(div);
  chatContenedor.scrollTop = chatContenedor.scrollHeight; // Auto-scroll
}

// Enviar la petición al backend de Flask
function enviarMensaje() {
  const texto = chatInput.value.trim();

  if (texto === "") return;

  agregarMensaje(texto, "mensaje-user");
  chatInput.value = ""; // Limpiar el input

  // Mandar los datos al servidor
  fetch("/chatbot", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ mensaje: texto }),
  })
    .then((res) => res.json())
    .then((data) => {
      // Simular un pequeño retraso de lectura
      setTimeout(() => {
        agregarMensaje(data.respuesta, "mensaje-bot");
      }, 300);
    })
    .catch((error) => {
      console.error("Error:", error);
      agregarMensaje(
        "Ups, perdí conexión con el servidor principal.",
        "mensaje-bot",
      );
    });
}

// Escuchar clicks y la tecla Enter
chatEnviar.addEventListener("click", enviarMensaje);

chatInput.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    enviarMensaje();
  }
});
