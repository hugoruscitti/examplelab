<?php

// IMPORTANTE: 
//             Se esperan dos 
//             segundos antes de 
//             responder.
sleep(2);


$texto = $_POST['texto'];

echo str_replace(" ", "....", $texto);


echo "<hr>";
echo "Por cierto, al servidor me han llegado estos datos:";
var_dump($_POST);
echo "<pre>";
echo "Ultima actualización: ".date("h:m:s");
echo "</pre>";
?>
