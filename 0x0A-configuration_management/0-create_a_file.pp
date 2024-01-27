# creates a file in /tmp

file { '/tmp/scool':
  content => 'I Love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}