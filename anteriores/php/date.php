<?php

$today = strftime("%Y-%m-%d", time());

$one_day = 24*60*60; # horas * m * s
$yesterday = strftime("%Y-%m-%d", time() - $one_day);

$one_week_later = strftime("%Y-%m-%d", time() - $one_day * 7);

echo "Hoy es: $today \n";
echo "Hace una semana: $one_week_later \n";
echo "Hace una hora: $yesterday \n";
?>
