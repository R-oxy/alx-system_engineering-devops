# Client configuration only through SSH keys
include stdlib

file_line { 'Disable passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication'
}

file_line { 'Identity file declaration':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile'
}
