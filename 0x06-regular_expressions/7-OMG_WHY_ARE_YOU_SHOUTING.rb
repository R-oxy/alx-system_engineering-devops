#!/usr/bin/env ruby
# Accepts one argument and passes it to the regular expression matching method

puts ARGV[0].scan(/[A-Z]/).join
