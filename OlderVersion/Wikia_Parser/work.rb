$LOAD_PATH.unshift '.'

require 'rubygems'
require 'yaml'
Dir[".lib/*.rb"].each {|file| require file }

thing = YAML.load_file('C:\RPGMAKERSTUFF\Scripts_and_YAML\YAML\ActorTemp.yaml')
puts thing.inspect