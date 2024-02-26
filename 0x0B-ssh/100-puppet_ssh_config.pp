# Puppet manifest for configuring SSH client
file_line {  'disable_password_authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line {  'set_identity_file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
