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
        const fechaCompleta = `${i}-${mes}-${anio}`;
        const fechaClave = `${i}-${mes}`;

        // Fechas específics
        if (fechaCompleta === "2-1-2026" || fechaCompleta === "3-1-2026" || fechaCompleta === "4-1-2026") {
            descripcion = "Descanso";
        }
        if (fechaCompleta === "5-1-2026" || fechaCompleta === "6-1-2026" || fechaCompleta === "7-1-2026" || fechaCompleta === "8-1-2026" || fechaCompleta === "9-1-2026" || fechaCompleta === "12-1-2026"|| fechaCompleta === "13-1-2026" || fechaCompleta === "14-1-2026" || fechaCompleta === "15-1-2026" || fechaCompleta === "16-1-2026") {
            descripcion = "Periodo de Extraordianarios";
        } 
        if (fechaCompleta === "19-1-2026" || fechaCompleta === "20-1-2026" || fechaCompleta === "21-1-2026" || fechaCompleta === "22-1-2026"|| fechaCompleta === "23-1-2026" || fechaCompleta === "24-1-2026") {
            descripcion = "Periodo de Examenes Extraordinarios";
        }
        if (fechaCompleta === "26-1-2026" || fechaCompleta === "27-1-2026" || fechaCompleta === "28-1-2026" || fechaCompleta === "29-1-2026" || fechaCompleta === "30-1-2026") {
            descripcion = "Descanso";
        }
        if (fechaCompleta === "2-2-2026" || fechaCompleta === "3-2-2026" || fechaCompleta === "4-2-2026" || fechaCompleta === "5-2-2026" || fechaCompleta === "6-2-2026") {
            descripcion = "Descanso";
        }

        // Fechas que siempre se repiten cada año
        if (fechaClave === "1-1") {
            descripcion = "Año Nuevo";
        }
        if (fechaClave === "11-3") {
            descripcion = "Cumpleaños de Saúl";
        } else if (fechaClave === "25-12") {
            descripcion = "Navidad";
        } else if (fechaClave === "5-2") {
            descripcion = "Dia de la constitución";
        } else if (fechaClave === "18-3") {
            descripcion = "Natalicio de Benito Juárez";
        } else if (esFinDeSemana) {
            descripcion = "Descanso";
        }

        const colorGrisFuerte = "color: #444;";
        const colorfinde = esFinDeSemana ? 'class="fin-de-semana"' : '';

        html += `<tr ${colorfinde}>
                    <td style="text-align:center; ${colorGrisFuerte}">${i}</td>
                    <td style="${colorGrisFuerte}">${nombreDia}</td>
                    <td style="${colorGrisFuerte}" class="descripcion">${descripcion}</td>
                 </tr>`;
    }

    html += '</tbody></table>';
    document.getElementById('contenedor-tabla').innerHTML = html;
}
