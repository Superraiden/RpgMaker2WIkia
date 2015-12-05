class RpgMakerVxToWikia
  def initialize(name = "World")
    @name = name
  end
  def say_hi
    puts "Hi #{@name}!"
  end
  def say_bye
    puts "Bye #{@name}, come back soon."
  end
end

g = RpgMakerVxToWikia.new("Pat")
g.say_hi