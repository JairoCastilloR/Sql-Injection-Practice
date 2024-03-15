<?php

  //ini_set('display_errors', 1);  

  $server = "localhost";
  $username = "r4v3n@localhost";
  $password = "r4v3n123";
  $database = "R4v3n";

  $conn = new mysqli($server, $username, $password, $database);

  $id = mysqli_real_escape_string($conn, $_GET['id']);

  $data = mysqli_query($conn, "select username from user where id = $id");

  $response = mysqli_fetch_array($data);

  if(!isset($response['username'])){
    http_response_code(404);
  }

?>
