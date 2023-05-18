# increasing ULIMIT in /etc/default (nginx file)

file { '/etc/default/nginx':
    ensure  => file,
    content => "ULIMIT='-n 3048'\n",
}
