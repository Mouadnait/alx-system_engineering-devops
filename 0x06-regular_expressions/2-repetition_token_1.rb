#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# The regular expression must match the given cases

puts ARGV[0].scan(/hb{0,1}tn/).join