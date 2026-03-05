document.addEventListener("DOMContentLoaded", () => {
  const likeBtn = document.getElementById("likeBtn");
  const likeCountSpan = document.getElementById("likeCount");

  // 1. Cargar el contador y el estado del voto
  let likes = parseInt(localStorage.getItem("likeCount")) || 0;
  const hasLiked = localStorage.getItem("hasLiked") === "true";

  likeCountSpan.innerText = likes;

  // 2. Si ya votó anteriormente, deshabilitar el botón de inmediato
  if (hasLiked) {
    bloquearBoton(likeBtn);
  }

  likeBtn.addEventListener("click", () => {
    // 3. Doble verificación por seguridad
    if (localStorage.getItem("hasLiked") === "true") return;

    likes++;
    likeCountSpan.innerText = likes;

    // 4. Guardar el nuevo total y marcar que ya votó
    localStorage.setItem("likeCount", likes);
    localStorage.setItem("hasLiked", "true");

    bloquearBoton(likeBtn);
  });
});

function bloquearBoton(boton) {
  boton.disabled = true; // El usuario no puede volver a hacer click
  boton.innerText = "Ya diste like";
  boton.style.opacity = "0.5"; // Feedback visual opcional
}

document.getElementById("postBtn").addEventListener("click", function () {
  let postContent = document.getElementById("postText").value;

  if (postContent.trim() !== "") {
    // Crear el contenedor de la publicación
    let newPost = document.createElement("div");
    newPost.className = "feed-post";
    newPost.innerHTML = `<p>${postContent}</p>`;

    // Añadir la publicación al inicio del feed
    document.getElementById("feed").prepend(newPost);

    // Limpiar el textarea
    document.getElementById("postText").value = "";
  } else {
    alert("Por favor escribe algo");
  }
});
