#!/usr/bin/env ruby

# Accepts one argument and passes it to the regular expression matching method
text = ARGV[0]

# Define the regular expression pattern to extract sender, receiver, and flags
pattern = /\[from:(?<sender>.*?)\] \[to:(?<receiver>.*?)\] \[flags:(?<flags>.*?)\]/

# Match the pattern in the text and extract the required information
matches = text.match(pattern)

# Output the results in the desired format
puts "#{matches[:sender]},#{matches[:receiver]},#{matches[:flags]}"
