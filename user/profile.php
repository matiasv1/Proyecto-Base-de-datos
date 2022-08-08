<?php
    include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
    //si hay una sesion inicia. La seccion profile se le agrega la informacion de cada usuario particular  y se rellena la tabla.
    if(isset($_SESSION["id"])){
        $id_sesion=$_SESSION["id"];
        $sql = "SELECT * FROM usuario where id=$id_sesion";
        $result = pg_query_params($dbconn, $sql, array());
        $row = pg_fetch_assoc($result);
        $cod_pais=$row["pais"];

        $sql2="SELECT nombre from pais where cod_pais=$cod_pais";
        $result2 = pg_query_params($dbconn, $sql2, array());
        $row2 = pg_fetch_assoc($result2);

        echo 
        '<div class="container shadow-lg rounded m-auto p-5" id="hoja">
            <p> <span class="letraN">Nombre Completo: </span>'.$row["nombre"].' '.$row["apellido"].'</p>
            <p> <span class="letraN">Correo: </span>'.$row["correo"].' </p>
            <p> <span class="letraN">País: </span>'.$row2["nombre"].'</p>
            <p> <span class="letraN">Fecha de Ingreso: </span>'.$row["fecha_registro"].'</p>
        </div>';           
    }
    pg_close($dbconn);
?>