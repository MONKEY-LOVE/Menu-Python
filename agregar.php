<?php
$id=$_REQUEST["id"];
$sector=$_REQUEST["sector"];
$asiento=$_REQUEST["asiento"];
$tarifa=$_REQUEST["tarifa"];
$DBhost="localhost";
$DBuser="root";
$DBpass="";
$DBname="Trabajo_final";
$DBcon=new PDO("mysql:host=$DBhost;dbname=$DBname",$DBuser,$DBpass);
$query="insert into trabajo_final (id,sector,asiento,tarifa) values(:id,:sector,:asiento,:tarifa)";
$stmt=$DBcon->prepare($query);
$stmt->bindParam(':id',$id,PDO::PARAM_STR,100);
$stmt->bindParam(':sector',$sector,PDO::PARAM_STR,100);
$stmt->bindParam(':asiento',$asiento,PDO::PARAM_STR,100);
$stmt->bindParam(':tarifa',$tarifa,PDO::PARAM_STR,100);
$stmt->execute(); 
?>
