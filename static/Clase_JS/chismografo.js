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
