import json

class Student:
    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
        self.marks = marks

    def average(self):
        try:
            return round(sum(self.marks) / len(self.marks), 2)
        except (ZeroDivisionError, TypeError):
            return 0

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
                lines = f.readlines()
            if not lines:
                print("""
╔══════════════════════════════════════╗
║   ⚠  No Students Found In File !    ║
╚══════════════════════════════════════╝
""")
                return
            for line in lines:
                data = json.loads(line)
                print(f"""
╔══════════════════════════════════════════╗
║           S T U D E N T   I N F O        ║
╠══════════════════════════════════════════╣
║  Name          : {data['name']:<24s}║
║  ID            : {str(data['id']):<24s}║
╠══════════════════════════════════════════╣
║  IOT           : {str(data['marks'][0]):<24s}║
║  Maths         : {str(data['marks'][1]):<24s}║
║  OS            : {str(data['marks'][2]):<24s}║
║  DSA           : {str(data['marks'][3]):<24s}║
║  C Programming : {str(data['marks'][4]):<24s}║
╠══════════════════════════════════════════╣
║  Average       : {str(data['average']):<24s}║
╚══════════════════════════════════════════╝
""")
        except FileNotFoundError:
            print("""
╔══════════════════════════════════╗
║   ⚠  File Not Found !           ║
╚══════════════════════════════════╝
""")


def welcome():
    print("""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║       S T U D E N T   E R P   S Y S T E M            ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
""")


def statements():
    print("""
╔══════════════════════════════════════╗
║           M A I N   M E N U          ║
╠══════════════════════════════════════╣
║   1  -->  Add Student                ║
║   2  -->  See All Students           ║
║   3  -->  See Topper Student         ║
║   4  -->  Exit                       ║
╚══════════════════════════════════════╝""")


welcome()

while True:

    statements()

    try:
        choice = int(input("\n  $ Enter Choice : "))
    except ValueError:
        print("""
╔══════════════════════════════════════╗
║   ⚠  Invalid Choice, Try Again !    ║
╚══════════════════════════════════════╝
""")
        continue

    if choice == 1:
        print("""
╔══════════════════════════════════════╗
║       A D D   S T U D E N T          ║
╚══════════════════════════════════════╝""")

        while True:
            try:
                Id = int(input("  $ Enter Student ID   : "))
                break
            except ValueError:
                print("  ⚠  Invalid ID, Please enter a number...")

        while True:
            Name = input("  $ Enter Student Name : ")
            if Name.isdigit() or Name.isspace() or Name == '':
                print("  ⚠  Invalid Name, Please try again...")
            else:
                break

        print("""
╔══════════════════════════════════════╗
║       E N T E R   M A R K S          ║
╚══════════════════════════════════════╝""")

        Marks = []
        subjects = ['IOT', 'Maths', 'OS', 'DSA', 'C Programming']

        for subject in subjects:
            while True:
                try:
                    mark = int(input(f"  $ {subject:<18s}: "))
                    Marks.append(mark)
                    break
                except ValueError:
                    print(f"  ⚠  Invalid marks for {subject}, try again...")

        s1 = Student(Name, Id, Marks)
        s1.save_in_file()

        print(f"""
╔══════════════════════════════════════╗
║   ✔  Student '{Name}' Added !
╚══════════════════════════════════════╝
""")

    elif choice == 2:
        print("""
╔══════════════════════════════════════════╗
║     A L L   S T U D E N T S             ║
╚══════════════════════════════════════════╝""")
        Student.read_from_file()

    elif choice == 3:
        try:
            topper = None
            with open("erp.txt", "r") as f:
                for line in f:
                    student_data = json.loads(line)
                    if (topper is None) or (student_data["average"] > topper["average"]):
                        topper = student_data

            if topper:
                print(f"""
╔══════════════════════════════════════════╗
║    🏆  T O P P E R   S T U D E N T      ║
╠══════════════════════════════════════════╣
║  Name          : {topper['name']:<24s}║
║  ID            : {str(topper['id']):<24s}║
╠══════════════════════════════════════════╣
║  IOT           : {str(topper['marks'][0]):<24s}║
║  Maths         : {str(topper['marks'][1]):<24s}║
║  OS            : {str(topper['marks'][2]):<24s}║
║  DSA           : {str(topper['marks'][3]):<24s}║
║  C Programming : {str(topper['marks'][4]):<24s}║
╠══════════════════════════════════════════╣
║  Average       : {str(topper['average']):<24s}║
╚══════════════════════════════════════════╝
""")
            else:
                print("""
╔══════════════════════════════════════╗
    ⚠  No Students Found !            
╚══════════════════════════════════════╝
""")
        except FileNotFoundError:
            print("""
╔══════════════════════════════════════╗
    ⚠  File Not Found !               
╚══════════════════════════════════════╝
""")

    elif choice == 4:
        print("""
╔══════════════════════════════════════════════╗
║                                              ║
    G O O D B Y E !  See You Next Time  👋    
║                                              ║
╚══════════════════════════════════════════════╝
""")
        break

    else:
        print("""
╔══════════════════════════════════════╗
║   ⚠  Invalid Choice, Try Again !    ║
╚══════════════════════════════════════╝
""")
