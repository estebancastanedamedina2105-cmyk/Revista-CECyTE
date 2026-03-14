document.addEventListener('DOMContentLoaded', () => {
    cargarChismes(); // Carga los chismes nada más abrir la página

    document.getElementById('postBtn').onclick = () => {
        const cajaTexto = document.getElementById('postText');
        const contenido = cajaTexto.value;

        if (contenido.trim() === "") return;

        fetch('/guardar_chisme', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ contenido: contenido })
        })
        .then(res => res.json())
        .then(() => {
            cajaTexto.value = ""; // Limpia el área
            cargarChismes(); // Refresca la lista
        });
    };
});

function cargarChismes() {
    fetch('/obtener_chismes')
        .then(res => res.json())
        .then(chismes => {
            const contenedor = document.getElementById('feed');
            contenedor.innerHTML = ""; // Limpia antes de mostrar

            chismes.forEach(c => {
                const yaDioLike = localStorage.getItem(`liked_${c.id}`);
                
                contenedor.innerHTML += `
                    <div class="post-body" style="border: 1px solid #ccc; margin: 10px; padding: 10px; border-radius: 10px;">
                        <p>${c.contenido}</p>
                        <div class="post-actions">
                            <button id="likeBtn_${c.id}" 
                                    class="botones" 
                                    ${yaDioLike ? 'disabled style="opacity:0.6"' : ''} 
                                    onclick="darLike(${c.id}, this)">
                                ❤️ <span>${c.likes}</span> Like
                            </button>
                        </div>
                    </div>
                `;
            });
        });
}

function darLike(id, boton) {
    fetch('/dar_like', { // Esta es la ruta que te pasé en el mensaje anterior
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: id })
    })
    .then(() => {
        // Bloquear localmente
        localStorage.setItem(`liked_${id}`, 'true');
        boton.disabled = true;
        boton.style.opacity = "0.6";
        // Actualizar el número visualmente
        const span = boton.querySelector('span');
        span.innerText = parseInt(span.innerText) + 1;
    });
}