#!/usr/bin/env ruby
# Ruby scrpt that accepts one argument and pass it to a regular expression,
puts ARGV[0].scan(/\bSchool\b/).join
