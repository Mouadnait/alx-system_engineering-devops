# Config SSH config file for automated passwordless connection using Puppet
file_line {
    'Password Authentication':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => '^PasswordAuthentication',
    ;
    'Identity File':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    match  => '^IdentityFile',
}