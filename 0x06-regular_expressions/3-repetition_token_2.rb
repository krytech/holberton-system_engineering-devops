#!/usr/bin/env ruby
# match "hbtn, hbttn, hbtttn, hbttttn"
puts ARGV[0].scan(/hbt+n/).join
