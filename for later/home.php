<?php
session_start(); // Start the session at the beginning of your script

if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) { // If the session variable is not set
    header('location: index.php'); // Redirect to the login page
    exit;
}
?>
  
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>fat cat's home</title>
	<link rel="stylesheet" href="css/style.css">
</head>
<body>
	<div class= "content">
    	<h1>fat cat's home</h1>

		<div class= "options">
			<div class= "option">
				<div class= "optionImage">
					<image src="img/catTracker.jpg" alt="catimg" width = 200 height = 160></image>
				</div>
				<div class= "optionButton">
					<button type="button" id = "trackBTN" name = "trackBTN" >Dab Tracker</button>
				</div>
			</div>

			<div class= "option">
				<div class= "optionImage">
					<image src="img/catWeed.jpg" alt="catimg" width = 200 height = 160 ></image>
				</div>
				<div class= "optionButton">
					<button type="button" id = "cheapBTN" name = "cheapBTN" >Cheap Weed Finder</button>
				</div>
			</div>
		</div>
	</div>
</body>
</html>

