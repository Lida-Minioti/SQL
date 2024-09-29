from database import create_table, add_entry, get_entries

menu = """ Please select one of the following:
1) Add new entry for today
2) View entries
3) Exit.

Your selection: """

welcome = "Welcome"

# User communication
def prompt_new_entry():
    entry_content = input("what have you learned today?")
    entry_date = input("Enter the date:")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n") # entry is a tuple with length=No of columns

# Main algorithm / menu

print("Welcome")

create_table()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid")
    # We know it is not 3 because we checked it with the while


