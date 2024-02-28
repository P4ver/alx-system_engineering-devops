# Ensure the existence of a file in specified lcation
file { '/tmp/university':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
