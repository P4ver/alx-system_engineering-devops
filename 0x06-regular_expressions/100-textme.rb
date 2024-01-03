#!/usr/bin/env ruby
# must match: capital letters,
# Ruby scrpt that accepts 1 arg and pass it to a regex,
i_fr = ARGV[0].scan(/from:(\S+)\]/).join
j_t = ARGV[0].scan(/to:(\S+)\]/).join
k_snd = ARGV[0].scan(/flags:(\S+)\]/).join
puts "#{i_fr},#{j_t},#{k_snd}"
