<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';?>
<?php
    // se saca la informacion del usuario, para poder escribirlas en las casillas como predeterminado
    if(isset($_GET["id"])){
        $id= $_GET["id"];
        $sql= "SELECT * FROM usuario WHERE usuario.id=$id";
        $result = pg_query_params($dbconn, $sql, array());
        $row = pg_fetch_assoc($result);
        $pais = $row["pais"];
        $sql = "SELECT nombre FROM pais WHERE cod_pais=$pais" ;
        $result = pg_query($dbconn, $sql);
        $nombre_pais = pg_fetch_assoc($result);
    }

    //se cambia la informacion por la nueva ingresada por el admin.
    if($_SERVER["REQUEST_METHOD"]=="POST"){
        $nombre=$_POST["name"];
        $apellido=$_POST["surname"];
        $correo=$_POST["email"];
        $contraseña=$_POST["contraseña"];
        if($contraseña == $row["contraseña"]){
            $sql="UPDATE usuario set nombre ='$nombre', apellido='$apellido', correo='$correo', contraseña='$contraseña' where id=$id ";
            pg_query_params($dbconn, $sql, array());
            
        }
        else{
            //se hashea la contraseña en caso que se cambie
            $fuerte=password_hash($contraseña,PASSWORD_DEFAULT);
            $sql="UPDATE usuario set nombre ='$nombre', apellido='$apellido', correo='$correo', contraseña='$fuerte' where id=$id ";
            pg_query_params($dbconn, $sql, array());
            
        }
        header("Location: /admin/users/all.html");
        pg_close($dbconn);
    }
    //se escribe la tabla con la informacion predeterminada
    echo '<form action="/admin/users/CRUD/update.php?id='.$id.'" method="POST">
            <div class="form-group">
                <label for="name">Nombre</label>
                <input type="text" class="form-control" value='.$row["nombre"].' " placeholder="Nombre" name="name" id="name" required>
            </div>
            <div class="form-group">
                <label for="surname">Apellido</label>
                <input type="text" class="form-control" value='.$row["apellido"].' placeholder="Apellido" name="surname" id="surname">
            </div>
            <div class="form-group">
                <label for="email">Correo Electrónico</label>
                <input type="email" class="form-control" value='.$row["correo"].' placeholder="correo@electronico.com" name="email" id="email" required>
            </div>
            <div class="form-group">
                <label for="pwd">Contraseña</label>
                <input type="password" class="form-control" value='.$row["contraseña"].' placeholder="Contraseña" name="contraseña" id="pwd" required>
            </div>
            <!-- NOTA: Los valores están en duro para esta tarea. -->
            <div class="form-group">
                <label for="country">País</label>
                <select class="form-control" id="country">
                <option disabled selected>'.$nombre_pais["nombre"].'</option>
                <option value="1">Angola</option>
                <option value="2">Sudáfrica</option>
                <option value="3">Canadá</option>
                <option value="4">Estados Unidos</option>
                <option value="5">Chile</option>
                <option value="6">Australia</option>
                <option value="7">India</option>
                <option value="8">Corea del Sur</option>
                <option value="9">Rusia</option>
                <option value="10">Suiza</option>
                </select>
            </div>
            <div class="d-flex justify-content-end">
                <a class="btn btn-secondary mx-3" href="/admin/users/all.html">Volver</a>
                <button type="submit" class="btn btn-primary"  >Guardar cambios</button>
            </div>
        </form>';
?>