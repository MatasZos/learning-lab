<?php
$host = "localhost";
$port = "3307";
$user = "root";
$pass = "";
$dbname = "simplelogin";

$conn = new mysqli($host, $user, $pass, $dbname, $port);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
