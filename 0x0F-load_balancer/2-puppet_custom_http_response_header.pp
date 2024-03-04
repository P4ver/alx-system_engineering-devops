#!/usr/bin/env bash


exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'present',
}

file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "add_header X-Served-By \"${hostname}\";",
  match => 'http {',
}

exec { 'run':
  command => '/usr/sbin/service nginx restart',
}