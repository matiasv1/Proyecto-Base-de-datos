<?php 
    // Redirige a todos los usuario comunes (id_rol = 2) al index.html
    $dir = '../../index.html';
    if (isset($_SESSION["email"])){
        if ($_SESSION["id_rol"]==2) {
            header("Location: $dir");
        }
    }   
    else { // Restringe a cualquiera que no haya iniciado sesion (invitado)
        header("Location: $dir");
    } 
?>