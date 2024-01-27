# creates a file in /tmp

file { '/tmp/scool':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I Love Puppet',
}