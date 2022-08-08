<?php
    include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
    //se elima la informacion de los usuarios en la base de datos
    if(isset($_GET["id"])){
        $id= $_GET["id"];
        $sql="DELETE FROM cuenta_bancaria WHERE id_usuario=$id";
        $sql2="DELETE FROM usuario_tiene_moneda WHERE id_usuario=$id";
        $sql3="DELETE FROM usuario WHERE id=$id";
        
        pg_query_params($dbconn, $sql, array());
        pg_query_params($dbconn, $sql2, array());
        pg_query_params($dbconn, $sql3, array());
        header("Location: /admin/users/all.html");
        pg_close($dbconn);
    }
?>