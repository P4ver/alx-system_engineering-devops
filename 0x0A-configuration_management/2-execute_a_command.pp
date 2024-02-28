#Ensure the etnce of a file in the specified location
 exec {'kill-killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin';
}
