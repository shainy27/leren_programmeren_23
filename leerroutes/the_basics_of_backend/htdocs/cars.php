<?php
$servername = "localhost";
$username = "root";
$password = "";

try {
  $conn = new PDO("mysql:host=$servername;dbname=carshop", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  // echo "Connected successfully";
} catch(PDOException $e) {
  echo "Connection failed: " . $e->getMessage();
  exit();
}

$brand = $_GET['brand'];
$color = $_GET['color'];
$type = $_GET['type'];
$kenteken = $_GET['kenteken'];


$stmt = $conn->prepare("INSERT INTO cars (`id`, `brand`, `color`, `type`, `kenteken`) VALUES (NULL, '$brand', '$color', '$type', '$kenteken');");
$stmt->execute();

// set the resulting array to associative
$result = $stmt->setFetchMode(PDO::FETCH_ASSOC);

$clients = $stmt->fetchAll();

// $response = json_encode($clients);
// header("Content-type:application/json");
header("Location: index.html")
// $response = 'Saul Goodman';
// echo $response;

?>