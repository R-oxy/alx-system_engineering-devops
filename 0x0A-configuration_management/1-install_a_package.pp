# Install flask from pip

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin',
  creates => '/usr/local/lib/python3.*/dist-packages/Flask-2.1.0-py3.*.egg-info',
  require => Package['python3-pip'],
}
