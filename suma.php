<?php
    $DBhost="localhost";
    $DBuser="root";
    $DBpass="";
    $DBname="Trabajo_final";
    $DBcon=new PDO("mysql:host=$DBhost;dbname=$DBname",$DBuser,$DBpass); #Conexion a la base de datos
    $query = $conn->prepare("SELECT SUM(tarifa) FROM trabajo_final");
    $query->execute();
    foreach($query->fetchAll() as $row)
    {
        $total = $row['SUM(tarifa)'];
        break;
    }
?> 