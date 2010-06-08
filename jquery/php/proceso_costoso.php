<?php
// espera un segundo
sleep("1");

$dir = opendir("../");
echo "<ul> \n";

while ( $content = readdir($dir))
{
    echo "<li> $content</li> \n";
}

echo "</ul>";

echo "Horario actual: ".date("h:m:s");
?>
