<?php 
    // Redirige a todos los admin al index.html
    $dir = '../index.html';
    if (isset($_SESSION["email"])){
        if ($_SESSION["id_rol"]==1) {
            header("Location: $dir");
        }
    }   
    else { // Restringe a cualquiera que no haya iniciado sesion (invitado)
        header("Location: $dir");
    } 
?>