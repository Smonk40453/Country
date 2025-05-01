#Stephanie Monk 
#CIS261
# Country Introduction 

def display_menu () : 
    print("\nCountry Dictionary Menu")
    print("1. View a country")
    print("2. Add a country")
    print("3. Delete a country")
    print("4. Exit")
def initialize_dictionary():
    return {
        "US": "United States",
        "FR": "France",
        "JP": "Japan"
    }
def view_country(country_dict) :
    print("\nAvailable country codes :")
    for code in country_dict:
        print(code)
    key = input("Enter a country code to view: ").upper()
    if key in country_dict:
        print(f"{key} ={country_dict[key]}")
    else: 
        print("Invalid country code.")
def add_country(country_dict) :
    key = input("Enter the new country code: ").upper()
    if key in country_dict:
        print("That country code already exists.")
    else:
        name = input("Enter the country name: ")
        country_dict[key] = name
        print(f"{key} added successfully.")
def delete_country(country_dict):
    key = input("enter the country code to delete: ").upper()
    if key in country_dict:
        del country_dict[key]
        print(f"{key} deleted succesfully.")
    else:
        print("Invalid country code.")
def main():
    print("===Welcome to the Country Dictionary===")
    country_dict = initialize_dictionary()
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            view_country(country_dict)
        elif choice == "2":
            add_country(country_dict)
        elif choice == "3":
            delete_country(country_dict)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break 
        else:
            print("Invalid command. Please try again.")
if __name__ == "__main__":
    main()