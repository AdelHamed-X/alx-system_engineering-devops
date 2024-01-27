# creates a file in /tmp/

file { 'school':
  path    => '/tmp/scool',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I Love Puppet',
}
