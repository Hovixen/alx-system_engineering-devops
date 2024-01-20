# manifest creates a file in /tmp directory

file {'/tmp/school':
ensure  => 'file',
content => 'I love Puppet',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744',
}
