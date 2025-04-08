class Car
  attr_accessor :brand, :model, :year

  def initialize(brand, model, year)
    @brand = brand
    @model = model
    @year = year
  end

  def start_engine
    puts "#{@brand} #{@model} (#{@year}) engine started! Vroom vroom!"
  end

  def car_details
    "Car: #{@brand} #{@model}, Year: #{@year}"
  end
end

# Creating objects of the Car class
car1 = Car.new("Toyota", "Camry", 2022)
car2 = Car.new("Tesla", "Model S", 2023)

# Calling methods
puts car1.car_details
car1.start_engine

puts car2.car_details
car2.start_engine
