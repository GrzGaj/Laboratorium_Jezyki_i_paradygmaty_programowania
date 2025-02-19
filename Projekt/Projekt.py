import sqlite3
from datetime import datetime, timedelta

# Połączenie z bazą danych
def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount REAL,
                        category TEXT,
                        description TEXT,
                        date_added TEXT,
                        date_spent TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS balances (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        balance REAL,
                        savings REAL)''')
    conn.commit()
    conn.close()

def dodaj(amount, category, description, date_spent):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    date_added = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO expenses (amount, category, description, date_added, date_spent) VALUES (?, ?, ?, ?, ?)",
                   (amount, category, description, date_added, date_spent))
    conn.commit()
    conn.close()

def zmien(expense_id, amount, category, description, date_spent):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE expenses SET amount=?, category=?, description=?, date_spent=? WHERE id=?", 
                   (amount, category, description, date_spent, expense_id))
    conn.commit()
    conn.close()

def usun(expense_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()

def sprawdz():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    return expenses

def sprawdz_dzien(date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE date_spent=?", (date,))
    expenses = cursor.fetchall()
    conn.close()
    return expenses

def sprawdz_jutro():
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    return sprawdz_dzien(tomorrow)

def raport(start_date, end_date, category=None):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    if category:
        cursor.execute("SELECT * FROM expenses WHERE date_spent BETWEEN ? AND ? AND category=?", (start_date, end_date, category))
    else:
        cursor.execute("SELECT * FROM expenses WHERE date_spent BETWEEN ? AND ?", (start_date, end_date))
    report = cursor.fetchall()
    conn.close()
    return report

def main():
    init_db()
    while True:
        print("\nMenu:")
        print("1. Dodaj wydatek")
        print("2. Edytuj wydatek")
        print("3. Usuń wydatek")
        print("4. Wyświetl wszystkie wydatki")
        print("5. Sprawdź wydatki w konkretny dzień")
        print("6. Sprawdź wydatki na jutro")
        print("7. Generuj raport")
        print("8. Wyjście")
        choice = input("Wybierz opcję: ")
        
        if choice == "1":
            amount = float(input("Kwota: "))
            category = input("Kategoria (Opłaty, Ważne, Konieczne, Potrzebne): ")
            description = input("Opis: ")
            date_spent = input("Data wydatku (YYYY-MM-DD): ")
            dodaj(amount, category, description, date_spent)
        elif choice == "2":
            expense_id = int(input("ID wydatku do edycji: "))
            amount = float(input("Nowa kwota: "))
            category = input("Nowa kategoria: ")
            description = input("Nowy opis: ")
            date_spent = input("Nowa data wydatku (YYYY-MM-DD): ")
            zmien(expense_id, amount, category, description, date_spent)
        elif choice == "3":
            expense_id = int(input("ID wydatku do usunięcia: "))
            usun(expense_id)
        elif choice == "4":
            expenses = sprawdz()
            for exp in expenses:
                print(exp)
        elif choice == "5":
            date = input("Podaj datę (YYYY-MM-DD): ")
            expenses = sprawdz_dzien(date)
            for exp in expenses:
                print(exp)
        elif choice == "6":
            expenses = sprawdz_jutro()
            for exp in expenses:
                print(exp)
        elif choice == "7":
            start_date = input("Data początkowa (YYYY-MM-DD): ")
            end_date = input("Data końcowa (YYYY-MM-DD): ")
            category = input("Kategoria (opcjonalnie, Enter aby pominąć): ")
            report = raport(start_date, end_date, category if category else None)
            for exp in report:
                print(exp)
        elif choice == "8":
            break
        else:
            print("Nieprawidłowa opcja!")

if __name__ == "__main__":
    main()
