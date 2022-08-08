<?php
    include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
    $list = array('Bitcoin','Ethereum','Litecoin','Dogecoin','Tether USD','Stellar Lumens','Ripple','Bitconnect','Prestigiocoin','Riot Points');
    $n = 0;
    while ($n < 10){
        $name = $list[$n];
        
        $sql = "SELECT	
                        moneda.sigla,
                        moneda.nombre,
                        precio_moneda.valor
                    FROM
                        moneda INNER JOIN precio_moneda ON moneda.id = precio_moneda.id_moneda
                    WHERE
                        moneda.nombre = '".$name."'
                    GROUP BY
                        moneda.nombre,moneda.sigla,
                        precio_moneda.valor,
                        precio_moneda.fecha
                    order by max(precio_moneda.fecha) desc
                    limit 1 ";
        $result = pg_query_params($dbconn, $sql, array());
        $row = pg_fetch_assoc($result);
        echo 
            '<tr>
                <td>'.$row["sigla"].'</td>
                <td>'.$row["nombre"].'</td>
                <td>'.$row["valor"].'</td>
            </tr>'; 
        
        $n = $n+1;
    }
    
?>