# manifest installs flask from pip3

package { 'python3-pip':
  ensure => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'werkzeug':
  ensure   =>  '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
