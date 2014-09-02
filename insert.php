<?php
$con=mysqli_connect("localhost","rob","m@riju@n@!","stubbornform");
// Check connection
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

// escape variables for security
$name = mysqli_real_escape_string($con, $_POST['name']);
$email = mysqli_real_escape_string($con, $_POST['email']);
$zip = mysqli_real_escape_string($con, $_POST['zip']);

$sql="INSERT INTO Persons (name, email, zip)
VALUES ('$name', '$email', '$zip')";

//mysqli_query($con,"INSERT INTO Persons (name, email, zip)
//VALUES ('Peter', 'Griffin',35)");

//mysqli_query($con,"INSERT INTO Persons (name, email, zip)
//VALUES ('Glenn', 'Quagmire',33)");

$result = mysqli_query($con,"SELECT * FROM Persons");

echo "<table border='1'>
<tr>
<th>Firstname</th>
<th>Zipcode</th>
</tr>";

while($row = mysqli_fetch_array($result)) {
  echo "<tr>";
  echo "<td>" . $row['name'] . "</td>";
  echo "<td>" . $row['zip'] . "</td>";
  echo "</tr>";
}

echo "</table>";

if (!mysqli_query($con,$sql)) {
  die('Error: ' . mysqli_error($con));
}



echo "1 record added";

mysqli_close($con);
?>