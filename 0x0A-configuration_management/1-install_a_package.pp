# manifest installs flask from pip3

exec {'pip3':
command => '/usr/bin/pip3'
}

package {'flask':
ensure  => '2.1.0',
require => Exec['pip3']
}
