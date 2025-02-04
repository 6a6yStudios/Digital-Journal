import datetime

# Function to read entries from the journal file
def read_entries():
    try:
        with open('journal_entries.txt', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

# Function to write a new entry to the journal file
def write_entry(entry):
    with open('journal_entries.txt', 'a') as file:
        file.write(entry + '\n')

# Function to add a new journal entry
def add_entry():
    print("Enter your journal entry:")
    entry_text = input()
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"{date}: {entry_text}"
    write_entry(entry)
    print("Your entry has been saved!")

# Function to display all journal entries
def display_entries():
    entries = read_entries()
    if not entries:
        print("No entries found!")
        return
    for entry in entries:
        print(entry.strip())

# Function to search journal entries by date
def search_entries_by_date():
    date = input("Enter the date you want to search (YYYY-MM-DD): ")
    entries = read_entries()
    found = False
    for entry in entries:
        if date in entry:
            print(entry.strip())
            found = True
    if not found:
        print(f"No entries found for {date}")

# Main menu for the user to interact with
def main_menu():
    while True:
        print("\nDigital Journal")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Search Entries by Date")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            display_entries()
        elif choice == '3':
            search_entries_by_date()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()