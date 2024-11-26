<?php
// process.php

// Check if the form data has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['integers'])) {
    // Retrieve the input integers from the form
    $input = $_POST['integers'];

    // Validate the input format (ensure it only contains numbers and commas)
    if (!preg_match('/^\d+(,\d+)*$/', $input)) {
        die("Invalid input. Please enter a series of integers separated by commas.");
    }

    // Prepare the input to pass to the Python script
    $escaped_input = escapeshellarg($input);

    // Define the path to the Python script
    $python_script = 'bitwise_operations.py';

    // Execute the Python script with the input
    $command = "python3 $python_script $escaped_input";
    $output = shell_exec($command);

    // Check if the output is empty
    if ($output === null) {
        die("Error executing Python script.");
    }

    // Display the output from the Python script
    echo "<h1>Bitwise Operations Result</h1>";
    echo "<pre>$output</pre>";
} else {
    die("No input received. Please go back and submit the form.");
}
?>