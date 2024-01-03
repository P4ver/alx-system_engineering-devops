#!/usr/bin/env ruby
# Ruby scrpt that accepts 1 arg and pass it to a regex,
#puts ARGV[0].scan(/hb(t|tt|ttt|tttt)tn/).join
puts ARGV[0].scan(/hbt{2,5}n/).join
