<?php
$DBhost="localhost";
$DBuser="root";
$DBpass="";
$DBname="Trabajo_final";
$DBcon=new PDO("mysql:host=$DBhost;dbname=$DBname",$DBuser,$DBpass); #Conexion a la base de datos
$query="select * from Trabajo_final"; #Query para seleccionar todos los registros de la tabla
$stmt=$DBcon->prepare($query); #Prepara la consulta
$stmt->execute(); #ejecuta la consulta
$data=array(); #creamos un array
while($row=$stmt->fetch(PDO::FETCH_ASSOC)) 
{

    $data[]=$row;

}
echo (json_encode($data)); #convertimos el array en json

?>