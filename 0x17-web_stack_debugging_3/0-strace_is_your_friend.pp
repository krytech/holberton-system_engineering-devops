#Apache returns 500; this script fixes the typo from .phpp to .php
exec { 'fix the errors':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
}
