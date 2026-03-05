console.log("hola mundo");
function procesarMes() {
    const input = document.getElementById('mes').value;
    if (!input) return;

    const [anio, mes] = input.split('-').map(Number);
    
    const fechaAux = new Date(anio, mes - 1);
    const nombreMes = fechaAux.toLocaleString('es-ES', { month: 'long' });
    document.getElementById('nombreMesText').textContent = nombreMes.toUpperCase();

    const diasEnMes = new Date(anio, mes, 0).getDate();
    document.getElementById('totalDias').textContent = diasEnMes;

    imprimirTabla(diasEnMes, mes, anio);
}

function imprimirTabla(total, mes, anio) {
    const nombresDias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
    
    let html = `<table>
                <thead>
                    <tr>
                        <th>Día</th>
                        <th>Nombre</th>
                        <th>Descripción</th>
                    </tr>
                </thead>
                <tbody>`;

    for (let i = 1; i <= total; i++) {
        const fechaActual = new Date(anio, mes - 1, i);
        const numDiaSemana = fechaActual.getDay();
        const nombreDia = nombresDias[numDiaSemana];
        const esFinDeSemana = (numDiaSemana === 0 || numDiaSemana === 6);
        
        let descripcion = "Día de escuela";
        const fechaClave = `${i}-${mes}`;

        // Días específicos
        if (fechaClave === "1-1") {
            descripcion = "Año Nuevo";
        } else if (fechaClave === "11-3") {
            descripcion = "Cumpleaños de Saul";
        } else if (fechaClave === "25-12") {
            descripcion = "Navidad";
        } else if (esFinDeSemana) {
            descripcion = "💤 Descanso";
        }

        const colortxt = "color: #222222;";
        const colorfinde = esFinDeSemana ? 'class="fin-de-semana"' : '';

        html += `<tr ${colorfinde}>
                    <td style="text-align:center ${colortxt}">${i}</td>
                    <td style="${colortxt}">${nombreDia}</td>
                    <td style="${colortxt}" class="descripcion">${descripcion}</td>
                 </tr>`;
    }

    html += '</tbody></table>';
    document.getElementById('contenedor-tabla').innerHTML = html;
}
