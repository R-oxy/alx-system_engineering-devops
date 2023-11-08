# Fix an issue when Wordpress is trying to initialize

exec { 'fix-wordpress':
  command => "/bin/sed -i -e 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    => '/bin',
}
