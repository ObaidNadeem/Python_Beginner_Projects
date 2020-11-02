# Contact Book Program
# Author: Obaid Nadeem
# Python 3.8

def main():
    
    contacts = {}
    while True:

       
        choose = input("\nEnter '1' to Save a Contact \nEnter '2' to edit a Contact \nEnter '3' to Delete a Contact \nEnter '4' to show the contact list \nEnter '5' to search for a contact \nPlease select what you want to do? or type 'exit' to exit! ")
        
        if choose == "1":
            # print(type(choose))
            # CONTACT SAVING
            contact_number = input("Enter the number :")
            contact_name = input("Enter the name of the contact: ")
            contacts[contact_name] = contact_number
            print("Contact {} saved! ".format(contact_name))

        elif choose == "2":
            # Editing Contact
            if len(contacts.keys()) == 0:
                print("There are't any contacts saved!")
            else:
                print("Contacts in your contact book are:")
                print("\n"''.join(list(contacts.keys())))
                contact_to_be_edited = input("Enter the contact to be edited: ")
                if contact_to_be_edited in contacts.keys():
                    ask = input("Edit 'name' or 'number'? ")
                    if ask == "name":
                        changed_name = input("Enter new name: ")
                        contacts[changed_name] = contacts[contact_to_be_edited]
                        del contacts[contact_to_be_edited]
                        print("The contact {}'s name is updated to {}".format(contact_to_be_edited , changed_name))

                        # print(contact_to_be_edited.values())
                        continue
                    elif ask == "number":
                        changed_number = input("Enter new number: ")
                        contacts[contact_to_be_edited] = changed_number
                        print("The contact {}'s number is updated to {}".format( contact_to_be_edited ,contacts[contact_to_be_edited]))


        elif choose == "3":
            # Delete a contact
            print("Contacts in your contact book are:")
            print("\n"''.join(list(contacts.keys())))
            contact_to_be_deleted = input("Enter the contact to be deleted: ")
            if contact_to_be_deleted in contacts.keys():
                print("yes")
                del contacts[contact_to_be_deleted]
                print("The selected contact has been deleted! Contacts in your contact book are:")
                print("\n"''.join(list(contacts.keys())))

        elif choose == "4":
            for keys,values in contacts.items():
                print(keys, values)

        elif choose == "5":
            contact_to_be_searched = input("Enter the contact you want to search: ")
            if contact_to_be_searched not in contacts.keys():
                print("This contact dosen't exists in your conact book! ")
            else:
                for keys,values in contacts.items():
                    if keys == contact_to_be_searched:
                        print(keys, values)

        else:
            choose == "exit"
            break
        


# calling the function
main()
