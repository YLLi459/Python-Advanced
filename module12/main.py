from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be greater than 0.")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be greater than 0.")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print("\n--------------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"BMI: {self.calculate_bmi():.2f}")
        print(f"Category: {self.get_bmi_category()}")
        print("--------------------")


class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal Weight"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    ADJUSTMENT_FACTOR = 0.95

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return bmi * self.ADJUSTMENT_FACTOR

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal Weight"
        elif bmi < 24:
            return "Overweight"
        else:
            return "Obese"


class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):
        try:
            name = input("Enter name: ").strip()

            if not name:
                print("Name cannot be empty.")
                return

            age = int(input("Enter age: "))
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))

            if age >= 18:
                person = Adult(name, age, weight, height)
            else:
                person = Child(name, age, weight, height)

            self.add_person(person)
            print("Person added successfully!")

        except ValueError as e:
            print(f"Invalid input: {e}")

        except KeyboardInterrupt:
            print("\nInput cancelled by user.")

    def print_results(self):
        if not self.people:
            print("\nNo data entered.")
            return

        print("\n===== BMI RESULTS =====")
        for person in self.people:
            person.print_info()

    def run(self):
        print("===== BMI Calculator =====")

        while True:
            self.collect_user_data()

            choice = input("\nAdd another person? (y/n): ").lower()

            if choice != 'y':
                break

        self.print_results()


if __name__ == "__main__":
    try:
        app = BMIApp()
        app.run()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")