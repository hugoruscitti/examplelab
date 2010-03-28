<?php
function get_days_in_month($month_name, $year)
{
    $i = 0;
    $names = array(
        'January' => 1, 
        'February' => 2,
        'March' => 3,
        'April' => 4,
        'May' => 5,
        'June' => 6,
        'July' => 7,
        'August' => 8,
        'September' => 9,
        'October' => 10,
        'November' => 11,
        'December' => 12
    );

    $month = $names[$month_name];
    $first_of_month = mktime(0, 0, 0, $month, 1, $year);
    $maxdays = date('t', $first_of_month);
    return $maxdays;
}


echo get_days_in_month('February', 2009);

?>

