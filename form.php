<html>
<body>
    <h1>Assignment 6 - User Input Form</h1>
    <form method="GET" action="process.php">
        <label for="numbers">Enter integers separated by commas: </label>
        <input type="text" id="numbers" name="numbers" placeholder="e.g., 3,5,7,9" required><br><br>
        <label for="threshold">Enter threshold: </label>
        <input type="number" id="threshold" name="threshold" required><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>