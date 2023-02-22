address_book = {}

def add_details(name, phone_no, email):
    contact = {}
    contact["Phone no"] = phone_no
    contact["email"] = email
    address_book[name] = contact
    print(address_book)

def update_detail(args):

    print(args)
    name = args[0]
    phone = args[1]
    email = args[2]

    if name in address_book:
        if phone != "":
            address_book[name]["Phone no"] = phone
        if email != "":
            address_book[name]["email"] = email
    else:
        print(f"{name} is not in address book.")
    return f"{name}: {address_book[name]}"

def delete_data(name):
    if input("are you sure, requested data cannot be recovered once deleted(y or n): ") == "y":
        del address_book[name]
        print("requested data has been deleted.")
    else:
        print("request canceled.")

def search(args):
    name = args[0]
    phone = args[1]
    email = args[2]
    if name != "" and name in address_book:
        return f"{name}: {address_book[name]}"
    elif phone != "" or email != "":
        for data in address_book:
            if address_book[data]["Phone no"] == phone or address_book[data]["email"] == email:
                return f"{data}: {address_book[data]}"
    else:
        print("no data found.")

def request_details():
    name = input("Enter Name: ")
    phone_no = input("Enter phone no.: +91 ")
    email = input("Enter Email: ")
    return name, phone_no, email

Run = True
while Run:
    User_request = input("""
    Please select the service:
    1. add contact
    2. update contact (name required, leave blank requested data if no change required)
    3. delete contact (required name)
    4. search details
    Enter the number:
    """)

    if User_request == "1":
        add_details(*request_details())

    elif User_request == "2":
        print(update_detail(request_details()))
    
    elif User_request == "3":
        delete_data(request_details()[0])
    
    elif User_request == "4":
        print(search(request_details()))

