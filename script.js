document.addEventListener('DOMContentLoaded', function () {
    // Obtener el sufijo de la URL
    const url = window.location.href;
    const suffix = url.split('/').pop();

    // Mostrar el sufijo en el elemento con id 'suffix'
    document.getElementById('suffix').textContent = suffix;
});
