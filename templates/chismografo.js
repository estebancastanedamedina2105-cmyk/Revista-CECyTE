// 1. Función para dibujar cada comentario
function agregarPostAlMuro(c) {
    const feed = document.getElementById("feed");
    if (!feed) return;

    const postDiv = document.createElement("div");
    postDiv.className = "feed-post";

    // Insertamos el contenido y el botón con su propio contador interno
    postDiv.innerHTML = `
        <div class="post-header"><strong>@Usuario</strong></div>
        <p>${c.contenido}</p>
        <div class="post-actions">
            <button class="like-btn">❤️ Like</button>
            <span class="like-count">${c.likes || 0}</span>
        </div>
    `;

    const btn = postDiv.querySelector(".like-btn");
    const span = postDiv.querySelector(".like-count");

    // Lógica del Like conectada a Python
    btn.addEventListener("click", async () => {
        try {
            const res = await fetch('http://127.0.0.1:5000/dar_like', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id: c.id })
            });
            if (res.ok) {
                span.innerText = parseInt(span.innerText) + 1;
                btn.disabled = true;
                btn.innerText = "❤️";
            }
        } catch (err) { console.error("Error en like:", err); }
    });

    feed.appendChild(postDiv);
}

// 2. Cargar comentarios al iniciar
window.addEventListener("DOMContentLoaded", async () => {
    try {
        const res = await fetch('http://127.0.0.1:5000/obtener_comentarios');
        if (!res.ok) throw new Error("Error en el servidor");
        
        const comentarios = await res.json();
        const feed = document.getElementById("feed");
        if (feed) {
            feed.innerHTML = ""; // Limpiar
            comentarios.forEach(c => agregarPostAlMuro(c));
        }
    } catch (error) {
        console.error("Error al cargar:", error);
    }
});

// 3. Publicar comentario
document.getElementById("postBtn")?.addEventListener("click", async () => {
    const input = document.getElementById("postText");
    if (!input || input.value.trim() === "") return alert("Escribe algo");

    try {
        const res = await fetch('http://127.0.0.1:5000/publicar_comentario', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ contenido: input.value })
        });
        if (res.ok) location.reload();
    } catch (e) { alert("Error de conexión"); }
});