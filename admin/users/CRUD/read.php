<?php
    include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
    // Se saca la informacion de los usuario al momento que el admin ingresa a la informacion
    if(isset($_GET["id"])){
        $id= $_GET["id"];
        $sql= "SELECT * FROM usuario WHERE usuario.id='$id'";
        $result = pg_query_params($dbconn, $sql, array());
        $row = pg_fetch_assoc($result);
        $name=$row["nombre"];
        $correo=$row["correo"];
        $apellido=$row["apellido"];
        $pais=$row["pais"];
        $fecha=$row["fecha_registro"];

        $sql= "SELECT * FROM pais WHERE pais.cod_pais=$pais";
        $result2 = pg_query_params($dbconn, $sql, array());
        $row2 = pg_fetch_assoc($result2);
    }  
    pg_close($dbconn);
?>