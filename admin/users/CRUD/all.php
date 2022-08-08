<?php
    include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
    $sql = "SELECT * FROM usuario ORDER BY id ASC";
    $result = pg_query_params($dbconn, $sql, array());
    // se escribe en una tabla la informacion de todos los usuarios presentes en la base de datos
    if( pg_num_rows($result) > 0 ) {
        while($row = pg_fetch_assoc($result)) {
            $id = $row["id"];
            echo 
                '<tr>
                    <td>'.$id.'</td>
                    <td>'.$row["nombre"].'</td>
                    <td>'.$row["apellido"].'</td>
                    <td>'.$row["correo"].'</td>
                    <td>
                        <a href="/admin/users/read.html?id='.$row["id"].'" class="btn btn-primary">Ver <i class="fas fa-search"></i></a>
                        <a href="/admin/users/update.html?id='.$row["id"].'" class="btn btn-warning">Editar <i class="fas fa-edit"></i></a>
                        <a href="#" class="btn btn-danger" onclick="preguntar('.$id.')">Borrar <i class="fas fa-trash-alt"></i></a>
                    </td>
                </tr>';      
            }
        pg_close($dbconn);
    } else {                                    
        echo "Hubo un error al solicitar los datos";
        pg_close($dbconn);
    }
?>