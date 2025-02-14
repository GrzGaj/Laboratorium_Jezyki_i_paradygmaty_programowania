import json

class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary
    
    def to_dict(self):
        return {"name": self.name, "age": self.age, "salary": self.salary}
    
    @staticmethod
    def from_dict(data):
        return Employee(data["name"], data["age"], data["salary"])
    
    def __str__(self):
        return f"{self.name}, Wiek: {self.age}, Płaca: {self.salary:.2f}"


class EmployeesManager:
    FILE_PATH = "employees.json"
    
    def __init__(self):
        self.employees = []
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.FILE_PATH, "r") as file:
                data = json.load(file)
                self.employees = [Employee.from_dict(emp) for emp in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.employees = []
    
    def save_data(self):
        with open(self.FILE_PATH, "w") as file:
            json.dump([emp.to_dict() for emp in self.employees], file, indent=4)
    
    def dodaj_pracwonika(self, employee: Employee):
        if not isinstance(employee.name, str) or not employee.name.strip():
            print("Nieprawidłowe imie.")
            return
        if not isinstance(employee.age, int) or employee.age <= 0:
            print("Nieprawidłowy wiek.")
            return
        if not isinstance(employee.salary, float) or employee.salary <= 0:
            print("Nieprawidłowa płaca.")
            return
        
        self.employees.append(employee)
        self.save_data()
        print(f"Pracownik {employee.name} dodany pomyślnie.")
    
    def lista_pracownikow(self):
        if not self.employees:
            print("Nie znaleziono pracowników.")
        else:
            for emp in self.employees:
                print(emp)
    
    def usun_pracownika(self, min_age: int, max_age: int):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
        self.save_data()
        print(f"Pracownik w zakresie wieku {min_age}-{max_age} został usunięty.")
    
    def znajdz_pracownika(self, name: str):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                return emp
        return None
    
    def zmien_place(self, name: str, new_salary: float):
        employee = self.znajdz_pracownika(name)
        if employee:
            employee.salary = new_salary
            self.save_data()
            print(f"Płaca pracownika {employee.name} została zmieniona na {new_salary:.2f}.")
        else:
            print("Pracwonik nie istnieje.")


class FrontendManager:
    def __init__(self, manager: EmployeesManager):
        self.manager = manager
    
    def authenticate(self):
        username = input("Podaj login: ")
        password = input("Podaj hasło: ")
        return username == "admin" and password == "admin"
    
    def run(self):
        if not self.authenticate():
            print("Złe dane. Dostęp nieudany.")
            return

        while True:
            print("\nMenu:")
            print("1. Dodaj pracownika")
            print("2. Lista pracowników")
            print("3. Usuwanie pracownika po wieku")
            print("4. Zmiana płacy")
            print("5. Wyjście")
            
            choice = input("Wybierz: ")
            
            if choice == "1":
                name = input("Podaj imię: ")
                try:
                    age = int(input("Podaj wiek: "))
                    salary = float(input("Podaj płace: "))
                    self.manager.dodaj_pracwonika(Employee(name, age, salary))
                except ValueError:
                    print("Nieprawidłowe dane.")
            
            elif choice == "2":
                self.manager.lista_pracownikow()
            
            elif choice == "3":
                try:
                    min_age = int(input("Podaj minimum wieku: "))
                    max_age = int(input("Podaj maksimum wieku: "))
                    self.manager.usun_pracownika(min_age, max_age)
                except ValueError:
                    print("Nieprawidłowe dane.")
            
            elif choice == "4":
                name = input("Podaj imie pracwonika: ")
                try:
                    new_salary = float(input("Wpisz płace: "))
                    self.manager.zmien_place(name, new_salary)
                except ValueError:
                    print("Nieprawidłowe dane.")
            
            elif choice == "5":
                print("Wyjście z systemu.")
                break
            
            else:
                print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    manager = EmployeesManager()
    frontend = FrontendManager(manager)
    frontend.run()
