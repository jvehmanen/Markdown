# PERIYTYMINEN
# ============

# KIRJASTOT JA MODUULIT
# ---------------------

import oliot # Tuodaan koko oliot.py moduulin sisältö
from oliot import Student # Tuodaan oliot moduulista Student-luokka

# YLILUOKKA ELI ÄITILUOKA (SUPER/PARENT CLASS)
# --------------------------------------------
class Person():
    """Common class for all person in Raseko."""

    def __init__(self, givenName: str, surName: str):
        """Creates a Person object

        Args:
            etunimi (str): a first name
            sukunimi (strarg): A last name
        """
        self.etunimi = givenName
        self.sukunimi = surName

    def calculateAge3(self, isobirthday str) -> float:
        birthday = datetime.datetime.fromisoformat(isobirthday)
        age = datetime.datetime.date() - birthday
        ageInYears = age.days / 365
        return ageInYears
    
     # Staattinen metodi, joka laskee iän. Staattisessa metodissa ei lasketa
     #vaan metodia voi käyttää suoraan luokasta käsin

    @staticmethod
    def calculateAge(birthday) -> float:
        """Calculates student's current age in full years

        Returns:
            float: age in years
        """
        birthDay = datetime.datetime.fromisoformat

# ALILUOKKA ELI LAPSILUOKKA (SUB/CHILD CLASS)
class RasekoStudent(Person):
    """The student class, inherits The Person class"""
    def __init__(self, givenName: str, surName: str, studentNumber: str)
        """creates a student object

        Args:
            givenName (str): student's first name
            surName (str: Student's Surname
            studentNumber (str): Studentnumber
        """
        super(ClassName, self).__init__() #
        self.studentnumber = studentNumber #

if __name__ == "__main__":
    main()


    person1 = Person('Calle', 'Keckelberg')
    ikä3 = person1.calculateAge3('2009-10-22')
    print(f'Henkilön{person1.etunimi} ikä on {ika3} vuotta')

    