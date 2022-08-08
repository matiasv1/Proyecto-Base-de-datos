<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';?>
<?php 
    //Se inicia la sesion validando la informacion con la base de datos.
    session_start();
    if($_SERVER["REQUEST_METHOD"]=="POST"){
        $email=$_POST["email"];
        $contraseña=$_POST["pwd"];
        $sql= "SELECT * FROM usuario WHERE usuario.correo='$email'";
        $result = pg_query_params($dbconn, $sql, array());
         //si la contraseña es iniciada correctamente se envia al index y se le ingresa a la sesion las variables
        if(pg_num_rows($result)>0){
            $row = pg_fetch_assoc($result);
            if(password_verify($contraseña,$row['contraseña'])){
                $_SESSION["email"]=$email;
                $_SESSION["id"]=$row["id"];
                $_SESSION["id_rol"]=$row["id_rol"];
                header('Location: /index.html');
                pg_close($dbconn);
            }
            else{
                //ingresar contraseña nuevamente
                $_SESSION["message"] = "Correo o contraseña incorrecta, intente de nuevo.";
                header('Location: log-in.html');
                pg_close($dbconn);
            }
        }
    }
?>