#!/usr/bin/env ruby
# match a string that starts with "h" and ends with "n"
# with a single char in between
puts ARGV[0].scan(/h.n/).join
