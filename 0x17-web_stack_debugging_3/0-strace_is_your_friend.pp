# finding out why an apache is returning 500 error using tmux and strace

file { '/var/www/html/wp-settings.php':
    ensure => present,
    content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub(/\.phpp/, ".php") %>'),
}
