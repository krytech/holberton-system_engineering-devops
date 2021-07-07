#!/usr/bin/env ruby
# match "hbt{2-5}n"
puts ARGV[0].scan(/hbt{2,5}n/).join
