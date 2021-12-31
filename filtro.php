<?php
// Revisamos que nos envíe el sector, sino detenemos la ejecución.
if(isset($_GET['sector'])){
    // Revisamos que los datos que nos envía estén completos.
    if(!empty($_GET['sector'])){
        $sector = $_GET['sector'];
        include_once 'conexion.php';
        $query = $conn->prepare("SELECT * from trabajo_final WHERE Sector LIKE '%$sector%'");
        $query->bindParam(':sector', $sector, PDO::PARAM_STR);
        $query->execute();
        $result = $query->fetchAll();
        if(count($result)){
            die(json_encode($result));
        }else{
            die("error");  
        }  
    }else{
        die(json_encode(array("error" => "no puedes dejar el campo sector en blanco", true)));
    }
}else{
    die(json_encode(array("error" => "se precisa un sector para continuar", true)));
}
?>