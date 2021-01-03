#import Contact

name = raw_input("What would you like to call your address book?: >")+".txt"
c = open(name, "a")
print open(name, "a")

# c = open("Test.txt", "r")


def main_menu():
    # This initiates the address books and allows users to select which feature to use
    choice = raw_input("Press 1 to view your contacts, 2 to enter a new contact and 3 to search your contacts: >")
    if choice == "1":
        c = open(name, "r")
        file_contents = c.read()
        print (file_contents)
        c.close
    elif choice == "2":
        enter_contacts()
        main_menu()
    elif choice == "3":
        search_contacts()
        main_menu()


def search_contacts():
    # Searches contact list
    choice = raw_input("Search for a contact by any kind of information: >")
    c = []
    c = list(contact)
    for line in range(0, len(list)):
        if choice in line:
            print line
        else:
            choice = raw_input("There's no one named " + choice + " in your contact list. Press 2 to enter them now: >")
            if choice == "2":
                enter_contacts()
            else:
                print "Please choose an item from the menu: >"


def Person_first():
    # Ensures that the first name of a user is capitalized, only legal names accepted in this field no alias
    one = raw_input("First name: >")
    f = one[1:10]
    g = one[0]
    return g.upper() + f


def Person_last():
    # Ensures that the last name of a user is capitalized, only legal names accepted in this field no alias 
    two = raw_input("Last name: >")
    a = two[1:10]
    b = two[0]
    return b.upper() + a


def Person_phone():
    # Takes a 11 digit input and presents it in the [##### ######] format 
    phone = raw_input('Phone Number : >')
    if (len(phone) == 11) and phone[0:len(phone)] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0":
        telephone = "" + phone[0:5] + "" + " " + phone[5:11] + "" 
    else:
        telephone = "Only numerals are accepted in this field"
    return telephone


def Person_media():
    # Presents a person's social media in a clean manner, with an @ symbol 
    media = raw_input('Social media: >')
    if 15 >= len(media) - 1:
        social = "@" + media
    else:
        social = "Social media handles must be 15 characters or less"
    return social


def Person_mail():
    # Ensures that an email is valid before allowing a user to assign it to a contact
    addie = raw_input('E-mail: >')
    return addie


def enter_contacts():
    # Collects contact info
    # Saves contact info to a list
    f = Person_first()
    last = Person_last()
    telephone = Person_phone()
    email = Person_mail()
    addie = raw_input('Address: >')
    social = Person_media()
    contact = ("[" + f + " " + last + "|" + telephone + "|" + email + "|" + addie + "|" + social + "]")
    with open(name, "a") as text_file:
        text_file.write(contact)
    print "The contact " + contact + " has been added to your address book"

main_menu()
