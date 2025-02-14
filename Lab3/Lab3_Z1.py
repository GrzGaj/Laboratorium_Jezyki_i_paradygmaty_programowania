class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f"{self.name}, Wiek: {self.age}, Płaca: {self.salary:.2f}"


class EmployeesManager:
    def __init__(self):
        self.employees = []
    
    def dodaj_pracownika(self, employee: Employee):
        self.employees.append(employee)
        print(f"Pracownik {employee.name} został dodany.")
    
    def lista_pracownikow(self):
        if not self.employees:
            print("Nie znaleziono pracownika.")
        else:
            for emp in self.employees:
                print(emp)
    
    def usun_pracownika(self, min_age: int, max_age: int):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
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
            print(f"Płaca pracownika {employee.name} została zmieniona na {new_salary:.2f}.")
        else:
            print("Pracwonik nie znaleziony.")


class FrontendManager:
    def __init__(self, manager: EmployeesManager):
        self.manager = manager
    
    def run(self):
        while True:
            print("\nMenu:")
            print("1. Dodaj pracownika")
            print("2. Lista pracowników")
            print("3. Usuwanie pracownika po wieku")
            print("4. Zmiana płacy")
            print("5. Wyjście")
            
            choice = input("Wybierz: ")
            
            if choice == "1":
                name = input("Podaj imie: ")
                age = int(input("Podaj wiek: "))
                salary = float(input("Podaj płace: "))
                self.manager.dodaj_pracownika(Employee(name, age, salary))
            
            elif choice == "2":
                self.manager.lista_pracownikow()
            
            elif choice == "3":
                min_age = int(input("Podaj minimum wieku: "))
                max_age = int(input("Podaj maksimum wieku: "))
                self.manager.usun_pracownika(min_age, max_age)
            
            elif choice == "4":
                name = input("Podaj imie pracownika: ")
                new_salary = float(input("Wpisz płace: "))
                self.manager.zmien_place(name, new_salary)
            
            elif choice == "5":
                print("Wyjście z systemu.")
                break
            
            else:
                print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    manager = EmployeesManager()
    frontend = FrontendManager(manager)
    frontend.run()