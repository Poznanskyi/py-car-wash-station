from typing import List


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        if comfort_class not in range(1, 11):
            raise ValueError("Must be between 1 and 10")

        if clean_mark not in range(0, 11):
            raise ValueError("Must be between 0 and 10")

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        if distance_from_city_center <= 0:
            raise ValueError("Must be greater than 0")

        if clean_power not in range(0, 11):
            raise ValueError("Must be between 0 and 10")

        if not (0.0 <= average_rating <= 5.0):
            raise ValueError("Must be between 0.0 and 5.0")

        if count_of_ratings < 0:
            raise ValueError("Must be non-negative")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float) -> None:
        if not (0.0 <= new_rating <= 5.0):
            raise ValueError("Must be between 0.0 and 5.0")

        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating * (self.count_of_ratings - 1)
             + new_rating) / self.count_of_ratings,
            1
        )
