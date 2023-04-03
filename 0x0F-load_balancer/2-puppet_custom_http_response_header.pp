# Installs a Nginx server with custome HTTP header

exec {'install'
    command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
    provider => shell,
}

exec {'add_header':
    provider => shell,
    environment => ["HOST=${hostname}"],
    command => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
}

exec {'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
