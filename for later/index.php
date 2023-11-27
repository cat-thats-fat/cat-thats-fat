<?php
$servername = "localhost";
$dbusername = "catthats_sassy";
$dbpassword = "testpassword4231";
$dbname = "catthats_logins";

$conn = new mysqli($servername, $dbusername, $dbpassword, $dbname);

session_start();

if ($conn->connect_error) {
	die("connection failed: " . $conn->connect_error);
}

if(isset($_POST['register'])){
	$username = $_POST['username'];
	$password = $_POST['password'];
	$stmt = $conn->prepare("INSERT INTO logins (id, username, password) VALUES (NULL, ?, ?)");
	
	if ($stmt === false) {
		die("Error in SQL statement: " . $conn->error);
	}
	$stmt->bind_param("ss", $username, $password);
	$stmt->execute();
}
elseif(isset($_POST['signin'])){
	$username = $_POST['username'];
	$password = $_POST['password'];
	$stmt = $conn->prepare("SELECT username, password FROM logins WHERE username = ? AND password = ?");
	if ($stmt === false) {
		die("Error in SQL statement: " . $conn->error);
	}
	$stmt->bind_param("ss", $username, $password);
	$stmt->execute();
	$result = $stmt->get_result();
	if($result->num_rows >= 1){
		$_SESSION['loggedin'] = true;
		header('location: home.php');
		echo "logged in";
	}
	else{
		echo "invalid entry";
	}
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>cat thats fat</title>
	<link rel="stylesheet" href="css/style.css">
</head>
<body>
	<div class="container">
		<div class="header">
			<h1></h1>
		</div>
		<div class="content">
			<div class="smurfcatimg">
				<img src="img\smurfcat.jpg" alt="smurfcat">
			</div>
				<form method="post">
					<div class="login">
						<div class="input">
							<input type="text" id="username" name="username" placeholder="enter username">
						</div>
						<div class="input">
							<input type="password" id="password" name="password" placeholder="enter password">
						</div>
						<div class="buttons">
							<!-- <button type="submit" name="register">register</button> -->
							<button type="submit" name="signin">sign in</button>
						</div>
					</div>
				</form>
		</div>
	</div>
	<div class="footer">
		<h1></h1>
	</div>
</body>
</html>
