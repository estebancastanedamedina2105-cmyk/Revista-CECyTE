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
        } else if (fechaClave === "1-7" || fechaClave === "2-7" || fechaClave === "3-7" || fechaClave === "4-7" || fechaClave === "5-7" || fechaClave === "6-7" || fechaClave === "7-7" || fechaClave === "8-7" || fechaClave === "9-7" || fechaClave === "10-7" || fechaClave === "11-7" || fechaClave === "12-7" || fechaClave === "13-7" || fechaClave === "14-7" || fechaClave === "15-7" || fechaClave === "16-7" || fechaClave === "17-7" || fechaClave === "18-7" || fechaClave === "19-7" || fechaClave === "20-7" || fechaClave === "21-7" || fechaClave === "22-7" || fechaClave === "23-7" || fechaClave === "24-7" || fechaClave === "25-7" || fechaClave === "26-7" || fechaClave === "27-7" || fechaClave === "28-7" || fechaClave === "29-7" || fechaClave === "30-7" || fechaClave === "31-7") {
            descripcion = "Descanso";
        } else if (fechaClave === "14-12" || fechaClave === "15-12" || fechaClave === "16-12" || fechaClave === "17-12" || fechaClave === "18-12" || fechaClave === "19-12" || fechaClave === "20-12" || fechaClave === "21-12" || fechaClave === "22-12" || fechaClave === "23-12" || fechaClave === "24-12" || fechaClave === "26-12" || fechaClave === "27-12" || fechaClave === "28-12" || fechaClave === "29-12" || fechaClave === "30-12" || fechaClave === "31-12") {
            descripcion = "Descanso";
        } else if (esFinDeSemana) {
            descripcion = "Descanso";
        }

        const colorGrisFuerte = "color: #000000;";
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
