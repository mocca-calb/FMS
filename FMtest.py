class Car:
    def __init__(self, registration_number, model, year, mileage):
        self.registration_number = registration_number
        self.model = model
        self.year = year
        self.mileage = mileage
        self.assigned_driver = None
    
    def assign_driver(self, driver):
        if self.assigned_driver:
            self.assigned_driver.assigned_car = None
        self.assigned_driver = driver
        driver.assign_car(self)

    def __str__(self):
        driver_name = self.assigned_driver.name if self.assigned_driver else 'None'
        return f"{self.model} ({self.year}) - {self.registration_number}, Mileage: {self.mileage}, Driver: {driver_name}"

class Driver:
    def __init__(self, license_number, name, experience_years):
        self.license_number = license_number
        self.name = name
        self.experience_years = experience_years
        self.assigned_car = None

    def assign_car(self, car):
        if self.assigned_car:
            self.assigned_car.assigned_driver = None
        self.assigned_car = car

    def __str__(self):
        car_model = self.assigned_car.model if self.assigned_car else 'None'
        return f"{self.name} - License: {self.license_number}, Experience: {self.experience_years} years, Car: {car_model}"

class FleetManagementSystem:
    def __init__(self):
        self.cars = {}
        self.drivers = {}
    
    def add_car(self, registration_number, model, year, mileage):
        if registration_number in self.cars:
            print(f"Car with registration number {registration_number} already exists.")
        else:
            car = Car(registration_number, model, year, mileage)
            self.cars[registration_number] = car
            print(f"Car {model} added successfully.")
    
    def add_driver(self, license_number, name, experience_years):
        if license_number in self.drivers:
            print(f"Driver with license number {license_number} already exists.")
        else:
            driver = Driver(license_number, name, experience_years)
            self.drivers[license_number] = driver
            print(f"Driver {name} added successfully.")
    
    def assign_driver_to_car(self, license_number, registration_number):
        if license_number not in self.drivers:
            print(f"No driver found with license number {license_number}.")
        elif registration_number not in self.cars:
            print(f"No car found with registration number {registration_number}.")
        else:
            driver = self.drivers[license_number]
            car = self.cars[registration_number]
            car.assign_driver(driver)
            print(f"Driver {driver.name} assigned to car {car.model}.")
    
    def list_cars(self):
        if not self.cars:
            print("No cars in the system.")
        else:
            for car in self.cars.values():
                print(car)
    
    def list_drivers(self):
        if not self.drivers:
            print("No drivers in the system.")
        else:
            for driver in self.drivers.values():
                print(driver)

def main():
    fleet = FleetManagementSystem()
    
    while True:
        print("\nFleet Management System")
        print("1. Add Car")
        print("2. Add Driver")
        print("3. Assign Driver to Car")
        print("4. List Cars")
        print("5. List Drivers")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            registration_number = input("Enter registration number: ")
            model = input("Enter model: ")
            year = input("Enter year: ")
            mileage = input("Enter mileage: ")
            fleet.add_car(registration_number, model, year, mileage)
        
        elif choice == '2':
            license_number = input("Enter license number: ")
            name = input("Enter name: ")
            experience_years = int(input("Enter years of experience: "))
            fleet.add_driver(license_number, name, experience_years)
        
        elif choice == '3':
            license_number = input("Enter driver's license number: ")
            registration_number = input("Enter car's registration number: ")
            fleet.assign_driver_to_car(license_number, registration_number)
        
        elif choice == '4':
            fleet.list_cars()
        
        elif choice == '5':
            fleet.list_drivers()
        
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()