require 'yaml'
thing = YAML.load_file('Actors.yaml')
puts thing.inspect