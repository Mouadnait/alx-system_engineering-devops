# changes the OS configuration so that it is posible to login with the holberton user and open a file without any error message

exec { 'change soft limit':
    command  => "sed -i 's/^holberton hard nofile.*/holberton hard nofile 4096' /etc/security/limits.conf",
    provider => shell,
}

exec { 'change hard limit':
    command  => "sed -i 's/^holberton soft nofile.*/holberton soft nofile 4096' /etc/security/limits.conf",
    provider => shell,
}
