<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Integer Input Form</title>
</head>
<body>
    <h1>Enter a List of Integers</h1>
    <form action="process.php" method="post">
        <label for="integers">Input integers</label><br>
        <input type="text" id="integers" name="integers" placeholder="e.g., 1,2,3,4" required><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>