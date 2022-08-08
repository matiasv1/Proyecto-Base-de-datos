function preguntarCierreSesion() {
    if (confirm("¿Desea cerrar sesión?")) {
        window.location.href = "http://localhost/sesion/logout.php";
    }
}
function preguntar(tabla,id) {
    if (confirm("Estás seguro de eliminar esta fila?")) {
        window.location.href = "http://127.0.0.1:5000/api/"+tabla+"/delete/"+id;
        alert("Una fila ha sido eliminada con éxito.");
    }
}