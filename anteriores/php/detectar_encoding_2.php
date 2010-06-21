<?php

ini_set('display_errors', 'on');
error_reporting(E_ALL);


/**
 * Retorna true tiene la cadena tiene codificacion UTF-8
 */
function is_utf8_line($string)
{
    return preg_match('%^(?:
          [\x09\x0A\x0D\x20-\x7E]            # ASCII
        | [\xC2-\xDF][\x80-\xBF]             # non-overlong 2-byte
        |  \xE0[\xA0-\xBF][\x80-\xBF]        # excluding overlongs
        | [\xE1-\xEC\xEE\xEF][\x80-\xBF]{2}  # straight 3-byte
        |  \xED[\x80-\x9F][\x80-\xBF]        # excluding surrogates
        |  \xF0[\x90-\xBF][\x80-\xBF]{2}     # planes 1-3
        | [\xF1-\xF3][\x80-\xBF]{3}          # planes 4-15
        |  \xF4[\x80-\x8F][\x80-\xBF]{2}     # plane 16
    )*$%xs', $string);
}


/**
 * Retorna TRUE si el contenido del archivo es UTF-8
 */ 
function is_utf8_file($filename)
{
    $result = file($filename);
    
    foreach ($result as $line)
        if (! is_utf8_line($line))
            return false;

    return true;
}   


var_dump(is_utf8_file('encoding_utf8.txt'));
var_dump(is_utf8_file('encoding_latin1.txt'));

?>
