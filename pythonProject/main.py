class vehicle:
    """Defines the Vehycle type"""

    fuel_type = ["Gasoline", "Diesel", "Flex"]
    transmission_type = ["Manual", "Automatic"]

    def __init__(self, number_passengers: int, number_suitcases: int, fuel: str, transmission: str):

        # defines passengers
        if number_passengers > 0:
            self.number_passengers = number_passengers
        else:
            self.number_passengers = 1

        # defines suitcases
        if number_suitcases > 0:
            self.number_suitcases = number_suitcases
        else:
            self.number_suitcases = 1

        # defines fuel
        if fuel in vehicle.fuel_type:
            self.fuel = fuel
        else:
            self.fuel = "Gasoline"

        # defines transmission
        if transmission in vehicle.transmission_type:
            self.transmission = transmission
        else:
            self.transmission = "Manual"

        def __str__(self) -> object:
            return f'{self}: number_passengers: {self.number_passengers}, number_suitcases:{self.number_suitcases}, uses: {self.fuel}, has transmission: {self.transmission}.'
