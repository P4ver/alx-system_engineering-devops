#!/usr/bin/env ruby
#must match a 10 digit phone numbr,
# Ruby scrpt that accepts 1 arg and pass it to a regex,
puts ARGV[0].scan(/^\d{10}/).join
