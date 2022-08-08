<?php
    include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
    session_start();
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        
        # obtencion de datos desde el formulario
        $nombre = $_POST["name"];
        $apellido = $_POST["surname"];
        $correo = $_POST["email"];
        $contraseña = $_POST["pwd"];
        $pais = $_POST["country"];
        $fecha_registro = date('Y-m-d H:i:s',time());

        # obtencion del ultimo ide ingresado
        $consulta = pg_query($dbconn, 'SELECT MAX(id) FROM usuario');
        $array_result= pg_fetch_array($consulta);
        $id = $array_result[0]+1;
        $rol = 2;

        function VerificarUnicidad ($correo, $conexion) {
            $sql = "SELECT * from usuario WHERE usuario.correo='$correo'";
            $result = pg_query($conexion,$sql);
            if (pg_num_rows($result) > 0) {
                return 1;
            } else {
                return 0;
            }
        }
        # ingresar usuario a la db
    
        if (VerificarUnicidad($correo,$dbconn) == 1) {
            $_SESSION["message"] = 1;
            header("location: ../create.html");
        } else {
            $sql = 'INSERT INTO usuario (id, nombre, apellido, correo, contraseña, pais, fecha_registro, id_rol) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)';
            $hash = password_hash($contraseña,PASSWORD_DEFAULT);
            if(pg_query_params($dbconn, $sql, array($id, $nombre, $apellido, $correo, $hash, $pais, $fecha_registro, $rol)) !== FALSE ) {
                $_SESSION["message"] = 2;
                header("location: ../all.html");
                pg_close($dbconn);
            } else {
                $_SESSION["message"] = 3;
                header("location: ../create.html");
                pg_close($dbconn);
            }
        }
    }
?>