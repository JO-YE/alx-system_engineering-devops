# increasing ULIMIT in /etc/default (nginx file)

file { '/etc/default/nginx':
    ensure  => file,
    content => "ULIMIT='-n 3048'\n",
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/default/nginx'],
}
