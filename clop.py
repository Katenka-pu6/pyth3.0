import csv

def read_contacts_from_csv(filename):
    contacts = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def write_contacts_to_csv(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)