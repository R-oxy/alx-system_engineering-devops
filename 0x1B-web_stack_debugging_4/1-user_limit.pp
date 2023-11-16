# Change the system-wide hard limit
exec { 'change-max-open-files-hard-limit':
  command => "/bin/sed -i '/^\\s*\\*\\s*hard\\s*nofile/s/[0-9]\\+/4000/' /etc/security/limits.conf",
}

# Change the system-wide soft limit
exec { 'change-max-open-files-soft-limit':
  command => "/bin/sed -i '/^\\s*\\*\\s*soft\\s*nofile/s/[0-9]\\+/3000/' /etc/security/limits.conf",
}

# Set limits for the holberton user

file { '/etc/security/limits.conf':
  ensure => present,
} -> exec { 'Limit HARD for holberton':
  command => 'sed -i "/^\\s*holberton\\s*hard\\s*nofile/s/5/unlimited/" /etc/security/limits.conf',
  path    => '/bin',
} -> exec { 'Limit SOFT for holberton':
  command => 'sed -i "/^\\s*holberton\\s*soft\\s*nofile/s/4/1000/" /etc/security/limits.conf',
  path    => '/bin',
}
