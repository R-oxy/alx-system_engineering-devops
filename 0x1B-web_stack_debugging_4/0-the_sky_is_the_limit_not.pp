# Fix the number of max open files per process
exec { 'fix-max-open-files':
  command => "/bin/sed -i '/^worker_rlimit_nofile/c\worker_rlimit_nofile = 3000;' /etc/nginx/nginx.conf",
}

# Set the Nginx ULIMIT to a higher value
file { '/etc/default/nginx':
  ensure => present,
}

exec { 'increase-nginx-ulimit':
  command => "sudo sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and restart if necessary
service { 'nginx':
  ensure => 'running',
  enable => true,
}
