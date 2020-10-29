cars = [
     {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
     {"make": "Ford", "model": "urbo", "mileage": 1500, "fuel_consumed": 460},
     {"make": "Mazda", "model": "Miata", "mileage": 29000, "fuel_consumed": 560},
]

#function to calculate mpg
def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg #returns the value

#function that prints car make and model
def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name

#function that prints 
def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name} does {mpg} miles per gallon.")

for car in cars:
    print_car_info(car)
    #don't do below.  it returns 'none'
    print(print_car_info(car))


def divide (x,y):
    if y == 0:
        return "You tried to divide by 0"
    else:
        return x / y
    
print(divide(10,10))
print(divide(0,0))
print(divide(100, 10))