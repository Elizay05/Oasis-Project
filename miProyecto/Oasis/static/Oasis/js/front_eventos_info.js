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