# Installs a Nginx server with custome HTTP header

package {'nginx':
    ensure => 'present',
}

exec {'install'
    command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
    provider => shell,
}

exec {'add_header':
    provider => shell,
    command => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
    environment => ["HOST=${hostname}"],
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
