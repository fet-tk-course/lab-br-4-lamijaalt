# Ime: Lamija Altumbabic
# Datum: 25.03.2026
# Lab 4 --- Python za FastAPI


# Zadatak 1 

student={

    "ime": "Lamija", "godina": 20, "email" : "lamija.altumbabic@fet.ba" , "fakultet": "Fakultet Elektrotehnike"

}

print(student)
print(student["ime"])
student["aktivan"]=True

studenti=[
    {"ime": "Lamija", "godina": 4, "email" : "lamija.altumbabic@fet.ba" , "fakultet": "Fakultet Elektrotehnike"},
    {"ime": "Student2", "godina": 3, "email" : "student.drugi@fet.ba" , "fakultet": "Fakultet Elektrotehnike"},
    {"ime": "Student3", "godina": 2, "email" : "student.treci@fet.ba" , "fakultet": "Fakultet Elektrotehnike"}
]

print(studenti)

# Zadatak 2

#Ovo definise funkciju get_student_info sa parametrima name, year i email (koje sam kasnije dodala ), 
# te koristimo dict sto vraca dictionary

def get_student_info(name: str, year: int, email:str) -> dict:
    return {
        "name": name,
        "year": year,
        "email":email,
        "greeting": f"Zdravo {name}, vi ste {year} godina studija"
    }

if __name__ == "__main__":
    # Kratki primjer kako funkcija radi
    primjer = get_student_info("Amina", 3,"lamija.altumbabic@fet.ba")
    print(primjer)


# Zadatak 3

def ispisi_poziv(func):
    def wrapper(*args, **kwargs):
        print(f"Pozivam : {func.__name__}")
        return func(*args, **kwargs)
        pass
    return wrapper

@ispisi_poziv
def info_o_studentu(name: str, year: int, email:str) -> dict:
    return {
        "name": name,
        "year": year,
        "email":email,
        "greeting": f"Zdravo {name}, vi ste {year} godina studija"
    }

rezultat=info_o_studentu("Amina" ,3,"lamija.altumbabic@fet.ba")
print(rezultat)

# Zadatak 4
# Ovdje sam definisala klasu Course sa atributima name, code, credits i professor.

class Course:
    # Konstruktor klase koji prima parametre 

    def __init__(self, name: str, code: str, credits: int, professor:str):
        self.name = name
        self.code = code
        self.credits = credits
        self.professor=professor

        # Metoda description koja vraca string sa informacijama o kursu
    def description(self) -> str:
        return f"{self.code} - {self.name} ({self.credits} kredita) professor: {self.professor}"


if __name__ == "__main__":
    kurs = Course("Razvoj telekomunikacijske programske podrške", "TK207", 6, "Alma Secerbegovic")
    kurs2=Course("Razvoj mobilnih aplikacija i servisa","TK206",6,"Alma Secerbegovic")
    print(kurs.description())
    print(kurs2.description())


# Zadatak 5 

students = [
    {"name": "Amina", "year": 3, "email": "amina@untz.ba"},
    {"name": "Lamija", "year": 4, "email": "lamija@untz.ba"},
    {"name": "Hasan", "year": 3, "email": "hasan@untz.ba"},
    {"name": "Eldar", "year": 2, "email": "eldar@untz.ba"}
] 

def filter_by_year(students: list, year: int) -> list: 
   
    return [student for student in students if student["year"] == year]

def print_registry(students: list) -> None:
    for student in students:
        print(f"Ime: {student['name']}, Email: {student['email']}")

print("Svi studenti u registru")
print_registry(students)

print("Studenti 3. godine ")
treca_godina = filter_by_year(students, 3)
print_registry(treca_godina)