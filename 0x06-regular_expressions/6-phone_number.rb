#!/usr/bin/env ruby
# match a 10 digit phone number no spaces or dashes
puts ARGV[0].scan(/^[0-9]{10}$/).join
