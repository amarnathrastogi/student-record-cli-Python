import json

class student:
    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
        self.marks = marks

    def average(self):
        return float(sum(self.marks) / len(self.marks))

    def save_in_file(self):
        data = {
            'name': self.name,
            'id': self.id,
            'marks': self.marks,
            'average': self.average()
        }

        with open("erp.txt", "a") as f:
            json.dump(data, f)
            f.write('\n')

    @staticmethod
    def read_from_file():

        try:
            with open("erp.txt", "r") as f:
                for line in f:
                    data = json.loads(line)
                    print(f"Student_name - {data['name']}")
                    print(f"Student_ID - {data['id']}")

                    print(f"IOT_Marks - {data['marks'][0]}")
                    print(f"Maths_Marks- {data['marks'][1]}")
                    print(f"OS_Marks - {data['marks'][2]}")
                    print(f"DSA_Marks - {data['marks'][3]}")
                    print(f"C_Programming Marks - {data['marks'][4]}")

                    print(f"Student_average - {data['average']}")

        except FileNotFoundError:
            print('File Not Found')


def statements():
    print('1 - Add student...')
    print('2 - See all students...')
    print('3 - See Topper student...')
    print('4 - Exit from here...')


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

        try:
            Marks.append(int(input('Enter IOT Marks: ')))
            Marks.append(int(input('Enter Maths Marks: ')))
            Marks.append(int(input('Enter OS Marks: ')))
            Marks.append(int(input('Enter DSA Marks: ')))
            Marks.append(int(input('Enter C Programming Marks: ')))

        except ValueError:
            print('Invalid Marks,Please fill again...')

        s1 = student(Name, Id, Marks)
        s1.save_in_file()

    elif choice == 2:
        student.read_from_file()


    elif choice == 3:

        try:
            topper = None

            with open("erp.txt", "r") as f:
                for line in f:
                    student_data = json.loads(line)

                    if (topper is None) or (student_data["average"] > topper["average"]):
                        topper = student_data

            if topper:
                print("\n🏆 Topper Student:")
                print("Name:", topper["name"])
                print("ID:", topper["id"])
                print("Marks:", topper["marks"])
                print("Average:", topper["average"])
            else:
                print("No students found")

        except FileNotFoundError:
            print("File not found")

    elif choice == 4:
        break

    else:
        print('Invalid Choice,Please try again...')
