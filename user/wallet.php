<?php
    include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
    // si hay una seccion iniciada. Se le consulta a la base de datos todas las monedas que tenga el usuario con el ultimo valor de la moneda.
    if(isset($_SESSION["id"])){
        $id_sesion=$_SESSION["id"];
        $sql="SELECT * FROM moneda";
        $result = pg_query_params($dbconn, $sql, array());
        //se consulta el ultimo valor de la moneda 
        if( pg_num_rows($result) > 0 ) {   
            while($row = pg_fetch_assoc($result)){
                $id_moneda=$row["id"];
                $sql2="SELECT precio_moneda.id_moneda as id, precio_moneda.fecha as maxima, precio_moneda.valor as valor
                FROM precio_moneda
                where precio_moneda.id_moneda= $id_moneda
                group by
                    precio_moneda.id_moneda,
                    precio_moneda.valor,
                    precio_moneda.fecha
                order by
                    max(precio_moneda.fecha) desc
                limit 1";
                $result2 = pg_query_params($dbconn, $sql2, array());
                $row2= pg_fetch_assoc($result2);

                //se consulta si el usuario tiene la moneda y por otro lado cual es su balance
                $sql3="SELECT balance from usuario_tiene_moneda where id_usuario=$id_sesion AND id_moneda= $id_moneda";
                $result3 = pg_query_params($dbconn, $sql3, array());
                $row3= pg_fetch_assoc($result3);

                //se escribe la tabla con la informacion
                if(pg_num_rows($result3) > 0){
                    $cantidad_dinero=$row3["balance"];
                    $multi=$cantidad_dinero * $row2["valor"];
                    echo'
                    <tr><tbody>
                        <td >'.$row["sigla"].'</td>
                        <td>'.$row["nombre"].'</td>
                        <td>'.$cantidad_dinero.'</td>
                        <td>'.$row2["valor"].'</td>
                        <td>'.$multi.'</td>
                    </tr></tbody>
                    ';
                }
            }
        }
        pg_close($dbconn);    
    }
?>