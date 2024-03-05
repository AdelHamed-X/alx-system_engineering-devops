# A script that fixes apache server

exec { 'F':
  command  => ' sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}