<?php

/**
 * Indica si una linea de texto es UTF-8.
 */
function is_a_utf8_line($string)
{
    return preg_match('%(?:
        [\xC2-\xDF][\x80-\xBF]             # non-overlong 2-byte
        |\xE0[\xA0-\xBF][\x80-\xBF]        # excluding overlongs
        |[\xE1-\xEC\xEE\xEF][\x80-\xBF]{2} # straight 3-byte
        |\xED[\x80-\x9F][\x80-\xBF]        # excluding surrogates
        |\xF0[\x90-\xBF][\x80-\xBF]{2}     # planes 1-3
        |[\xF1-\xF3][\x80-\xBF]{3}         # planes 4-15
        |\xF4[\x80-\x8F][\x80-\xBF]{2}     # plane 16
        |\w*
        )+%xs',
    $string);
}


/**
 * Retorna TRUE si el contenido del archivo es UTF-8
 */ 
function is_utf8_file($filename)
{
    $result = file($filename);
    
    foreach ($result as $line) {
        if (is_a_utf8_line($line) == 0)
            return 0;
    }       
    
    return 1;
}   




ini_set('display_errors', 'on');
error_reporting(E_ALL);


var_dump(is_utf8_file('encoding_utf8.txt'));
var_dump(is_utf8_file('encoding_latin1.txt'));





?>
