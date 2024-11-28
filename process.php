<?php
if (isset($_GET['numbers']) && isset($_GET['threshold'])) {
    $numbers = escapeshellarg($_GET['numbers']);
    $threshold = escapeshellarg($_GET['threshold']);

    $command = escapeshellcmd("python3 bitwise_operations.py $numbers $threshold");
    $output = shell_exec($command);

    echo "<h1>Results - Assignment 6: </h1>";
    echo nl2br($output);
} else {
    echo "<h2>Please provide both integers and threshold values.</h2>";
}
?>