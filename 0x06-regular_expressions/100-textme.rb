#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# Your script should output: [SENDER],[RECEIVER],[FLAGS]
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used

from = ARGV[0].scan(/(?<=\[from:)[^ ]+(?=\])/).join
to = ARGV[0].scan(/(?<=\[to:)[^ ]+(?=\])/).join
flags = ARGV[0].scan(/(?<=\[flags:)[^ ]+(?=\])/).join
puts "#{from},#{to},#{flags}"