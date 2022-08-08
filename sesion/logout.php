<?php
    /* Este archivo debe manejar la lógica de cerrar una sesión */
    session_start();
    unset($_SESSION["email"]);
    header("Location: /index.html");
    session_destroy();
?>