function preguntar(id) {
    if (confirm("Estás seguro de que deseas eliminar al usuario ID: "+id)) {
        window.location.href = "/admin/users/CRUD/delete.php?id="+id;
        alert("El registro id: "+id+" ha sido eliminado.");
    }
}