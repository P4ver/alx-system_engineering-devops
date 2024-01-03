#!/usr/bin/env ruby
#msut be stars with 'h' and end with 'n' between thm any char,
# Ruby scrpt that accepts 1 arg and pass it to a regex,
puts ARGV[0].scan(/h.n/).join
