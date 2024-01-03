#!/usr/bin/env ruby
# must match: capital letters,
# Ruby scrpt that accepts 1 arg and pass it to a regex,
puts ARGV[0].scan(/[A-Z]/).join
