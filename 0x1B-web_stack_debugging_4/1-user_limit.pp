# changing the user limit
exec { 'change_value_to_60':
    command => "/bin/sed -i 's/5/60/g' /etc/security/limits.conf",
}

exec { 'change_value_to_40':
    command => "/bin/sed -i 's/4/40/g' /etc/security/limits.conf",
}
