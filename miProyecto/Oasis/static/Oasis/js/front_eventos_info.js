document.addEventListener('input', function() {
    function updateTotals() {
        const precioEntradaGeneral = parseInt(document.getElementById('precio-entrada-general-oculto').textContent);
        const precioEntradaVip = parseInt(document.getElementById('precio-entrada-vip-oculto').textContent);

        const cantidadEntradaGeneral = parseInt(document.getElementById('entrada-general-cantidad').value);
        const cantidadEntradaVip = parseInt(document.getElementById('entrada-vip-cantidad').value);
        console.log(precioEntradaGeneral, precioEntradaVip);
        console.log(cantidadEntradaGeneral, cantidadEntradaVip);

        const totalEntradaGeneral = precioEntradaGeneral * cantidadEntradaGeneral;
        const totalEntradaVip = precioEntradaVip * cantidadEntradaVip;

        const totalGeneral = totalEntradaGeneral + totalEntradaVip;


        document.getElementById('precio-entrada-general').textContent = totalEntradaGeneral.toLocaleString('es-CO', { style: 'decimal', minimumFractionDigits: 0, maximumFractionDigits: 0 });
        document.getElementById('precio-entrada-vip').textContent = totalEntradaVip.toLocaleString('es-CO', { style: 'decimal', minimumFractionDigits: 0, maximumFractionDigits: 0 });
        document.getElementById('total-general').textContent = totalGeneral.toLocaleString('es-CO', { style: 'decimal', minimumFractionDigits: 0, maximumFractionDigits: 0 });
    }
    document.getElementById('entrada-general-cantidad').addEventListener('change', updateTotals);
    document.getElementById('entrada-vip-cantidad').addEventListener('change', updateTotals);
});

document.querySelector('.btn[data-bs-target="#confirmModal"]').addEventListener('click', function() {
    const cantidadGeneral = document.getElementById('entrada-general-cantidad').value;
    const precioGeneral = document.getElementById('precio-entrada-general').textContent;
    const cantidadVIP = document.getElementById('entrada-vip-cantidad').value;
    const precioVIP = document.getElementById('precio-entrada-vip').textContent;
    
    if (cantidadGeneral > 0) {
      document.getElementById('modal-entrada-general-cantidad').textContent = cantidadGeneral;
      document.getElementById('modal-entrada-general-precio').textContent = precioGeneral;
      document.getElementById('detalle-general').style.display = '';
    } else {
      document.getElementById('detalle-general').style.display = 'none';
    }
    
    if (cantidadVIP > 0) {
      document.getElementById('modal-entrada-vip-cantidad').textContent = cantidadVIP;
      document.getElementById('modal-entrada-vip-precio').textContent = precioVIP;
      document.getElementById('detalle-vip').style.display = '';
    } else {
      document.getElementById('detalle-vip').style.display = 'none';
    }
    
    document.getElementById('modal-total').textContent = document.getElementById('total-general').textContent;
  });


function verificarCantidades() {
    var cantidadGeneral = document.getElementById('entrada-general-cantidad').value;
    var cantidadVip = document.getElementById('entrada-vip-cantidad').value;
    var botonComprar = document.getElementById('botonComprar');

    if (parseInt(cantidadGeneral) > 0 || parseInt(cantidadVip) > 0) {
        botonComprar.disabled = false;
    } else {
        botonComprar.disabled = true;
    }
}

document.getElementById('entrada-general-cantidad').addEventListener('input', verificarCantidades);
document.getElementById('entrada-vip-cantidad').addEventListener('input', verificarCantidades);

document.addEventListener('DOMContentLoaded', verificarCantidades);



function getCSRFToken() {
  const cookieValue = document.cookie.match(/csrftoken=([^ ;]+)/)[1];
  return cookieValue;
}

document.getElementById('confirmarCompraBtn').addEventListener('click', function() {
  const cantidadGeneral = document.getElementById('entrada-general-cantidad').value;
  const cantidadVIP = document.getElementById('entrada-vip-cantidad').value;
  const totalGeneral = document.getElementById('total-general').textContent;
  const eventoId = document.querySelector('#confirmarCompraBtn').getAttribute('data-evento-id');

  const datos = {
      cantidad_general: cantidadGeneral,
      cantidad_vip: cantidadVIP,
      total_general: totalGeneral
  };

  fetch(`http://127.0.0.1:8000/Oasis/comprar_entradas/${eventoId}/`, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
    },
    body: JSON.stringify(datos)
})
.then(response => response.json())
.then(data => {
    const messagesDiv = document.getElementById('messages');
    data.messages.forEach(message => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('alert');
        if (message.message_type === 'success') {
            messageDiv.classList.add('alert-success');
            alert(message.message);
        } else if (message.message_type === 'error') {
            messageDiv.classList.add('alert-danger');
            alert(message.message);
        } else if (message.message_type === 'warning') {
            messageDiv.classList.add('alert-warning');
            alert(message.message);
        }
        messageDiv.innerHTML = `
          <span>${message.message}</span>
          <button type="button" class="btn-close close-button" aria-label="Close"></button>
        `;
        messagesDiv.appendChild(messageDiv);

        // Escuchar clic en el botón de cierre para eliminar el mensaje
        const closeButton = messageDiv.querySelector('.btn-close');
        closeButton.addEventListener('click', () => {
            messageDiv.remove();
        });
    });
})
.catch(error => {
    console.error('Error:', error);
    alert('Error al procesar la solicitud' + error);
});
});