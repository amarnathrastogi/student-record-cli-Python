class student:
    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def save_in_file(self):
        with open("erp.txt", "a") as f:
            f.write(f"{self.name},{self.id},{self.marks},{self.average()}\n")

def statements():
    print('1 - Add student...')
    print('2 - See all students...')


def read_from_file():
    try:
        with open("erp.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print('File Not Found')


while True:

    statements()

    try:
        choice = int(input('Enter Choice: '))
    except ValueError:
        print('Invalid Choice,Please try again...')
        continue

    if choice == 1:

        try:
            Id = int(input('Enter Student ID: '))
        except ValueError:
            print('Invalid ID,Please try again...')
            continue

        Name = input('Enter Student Name: ')
        if not Name.strip() or Name.isdigit():
            print('Invalid Name,Please try again...')
            continue

        Marks = []

        while len(Marks) < 5:
            try:
                Marks.append(int(input('Enter Student Marks: ')))
            except ValueError:
                print('Invalid Marks,Please fill again...')

        s1 = student(Name, Id, Marks)
        s1.save_in_file()

    elif choice == 2:
        read_from_file()