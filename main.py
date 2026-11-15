from os import path
from pathlib import Path
blood_stock = {
    "A+": 10,
    "A-": 0,
    "B+": 5,
    "B-": 0,
    "AB+": 2,
    "AB-": 0,
    "O+": 8,
    "O-": 0
}

valid_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

from pathlib import Path
file_name = Path(__file__).resolve().parent / "donors.txt"
initial_donors = [
    {"name": "Meena joshi", "group": "O+", "units": 1},
    {"name": "Suresh Rao", "group": "O+", "units": 2}
]

if not file_name.exists() or file_name.stat().st_size == 0:
    with open(file_name, "w") as file:
        for donor in initial_donors:
            file.write(f"{donor['name']}|{donor['group']}|{donor['units']}\n")

donors = []
with open(file_name, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            name, group, units = line.split("|")
            donor = ({
                "name": name,
                "group": group,
                "units": int(units)
            })
            donors.append(donor)

def add_donor():
    print("\n----------- ADD DONOR ------------")
    name = input("Enter donor name:").strip()
    if not name:
        print("Invalid donor name.")
        return
    group = input("Enter blood group:").strip().upper()
    if group not in valid_groups:
        print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return
    units_input = input("Enter units:").strip()
    if not units_input.isdigit() or int(units_input) <= 0:
        print("Invalid units. Enter a positive whole number.")
        return
    units = int(units_input)
    donor = {
        "name": name,
        "group": group,
        "units": units
    }
    donors.append(donor)
    with open(file_name, "a") as file:
        file.write(f"{name}|{group}|{units}\n")
    blood_stock[group] += units
    print(f"Donor saved to donors.txt."f"Stock of {group} is now {blood_stock[group]} units.")
def issue_blood():
        print("\n---------- ISSUE BLOOD ------------")
        group = input("Enter blood group:").strip().upper()
        if group not in valid_groups:
            print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-")
            return
        units_input = input("Enter units to issue: ").strip()
        if not units_input.isdigit() or int(units_input) <= 0:
            print("Invalid units. Enter a positive whole number.")
            return
        units = int(units_input)
        if blood_stock[group] >= units:
            blood_stock[group] -= units
            print(
                f"{units} unit(s) of {group} issued. "
                f"Stock of {group} is now {blood_stock[group]} units."
                )
        else:
            print(
                f"Insufficient stock: only {blood_stock[group]}"
                f"unit(s) of {group} available."
            )
def view_stock():
    print("\n-------- AVAILABLE BLOOD STOCK ----------")
    for group, units in blood_stock.items():
        print(f"{group}: {units} units")

def search_donors():
    print("\n------- SEARCH DONORS --------")
    group = input("Enter blood group to search: ").strip().upper()
    if group not in valid_groups:
        print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return

    found = []
    for donor in donors:
        if donor["group"] == group:
            found.append(donor)

    print(f"\nDonors with blood group {group}:")

    if len(found) == 0:
        print("No donors found.")
    else:
        for index, donor in enumerate(found, start=1):
            print(
                f"{index}. {donor['name']} - "
                f"{donor['units']} unit(s)"
            )
        print(f"Total donors found: {len(found)}")

while True:
    print("\n===========================================")
    print(" BLOOD BANK MANAGEMENT ")
    print("=============================================")
    print("1. Add donor")
    print("2. Issue blood")
    print("3. View stock")
    print("4. Search donors")
    print("5. Exit")

    choice = input("Enter your choice(1-5): ").strip()
    if choice == "1":
        add_donor()
    elif choice == "2":
        issue_blood()
    elif choice == "3":
        view_stock()
    elif choice == "4":
        search_donors()
    elif choice == "5":
        print("Thank you for using Blood Bank Management System!")
        break
    else:
        print("Invalid choice. Please select between 1 and 5.")