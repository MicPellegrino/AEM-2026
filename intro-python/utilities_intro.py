# Definizione di una funzione
def get_primes(n_max: int, display: bool = True) -> list:

    """Get the prime numbers from 1 to ``n_max``

    Args:
        n_max (int): the function search for all primes < ``n_max``.
        display (bool, optional): if True, print a message with the found prime numbers. Defaults to True.

    Raises:
        AssertionError: if ``n_max`` is not an integer.
        ValueError: if ``n_max`` is greater that 100000.

    Returns:
        list: the list with the found prime numbers
    """
    
    # E' una buona pratica controllare che la funzione riceva input coretti
    if not isinstance(n_max, int):
        raise AssertionError(
            f"First argument must be an integer, instead we recive a {type(n_max)}"
        )
    if n_max > 100000:
        raise ValueError(f"The first argument is too big ({n_max} > 100000)")
    prime = []
    for i in range(1, n_max):
        is_prime = True
        for p in prime:
            if i % p == 0 and p != 1:
                is_prime = False
                break
        if is_prime:
            prime.append(i)
    if display:
        print(f"prime numbers < {n_max}:")
        # Altra magia di python, cicli `for`` dentro una lista (qui usata per convertire i numeri in stringhe)
        print(
            " ".join([f"{p}" for p in prime])
        )
    # Senza l' instance `return` la funzione ritorna `None` (cioè niente)
    return prime


# Definizione di una variabile globale
TODAY = "03/05/2024"


# Definizione di una classe (padre)
class Person:

    """Person class define virtually a person.

    We are not here to answer the philosophical question, "What is a person?".
    Here a person is defined by the following attributes.

    Attributes:
        name (str): Name of the person
        family name (str): Family name of the person
        age (int, optional): How old is the person
        birthday (str, optional): The person's birthday
    """

    def __init__(
        self, name: str, familyname: str, age: int = None, birthday: str = None
    ):
        """Initialize the Person object.

        The ``__init__`` method "initialize" the object, i.e., allocates a portion
        of the memory (object construction). The ``__init__`` function is called every
        time an object is created from a class.

        Args:
            name (str): Name of the person
            family name (str): Family name of the person
            age (int, optional): How old is the person. Defaults to None.
            birthday (str, optional): The person's birthday. Defaults to None.
        """
        self.name = name
        self.familyname = familyname
        self.age = age
        self.birthday = birthday

    # Quando un metodo inizia con "_" è considerato privato
    # (i.e. non viene ereditato da 'Student')
    def _convert_date(
        self, date: str
    ):
        for sep in [" ", "-", "\\"]:
            date = date.replace(sep, "/")
        day, month, year = (int(s) for s in date.split("/"))
        return day + month * 30 + year * 30 * 12

    def get_age(self):
        if self.age is None:
            age = round(
                (self._convert_date(TODAY) - self._convert_date(self.birthday))
                / (30 * 12)
            )
        else:
            age = self.age
        return age


# Definizione di una classe (figlio)
class Student(Person):

    """Student class defines virtually a student.

    A student is a person with a "matricola".

    Attributes:
        name (str): Name of the person
        family name (str): Family name of the person
        matricola (int): Student identification number
        age (int, optional): How old is the person
        birthday (str, optional): The person's birthday
    """

    def __init__(
        self,
        name: str,
        familyname: str,
        matricola: int,
        age: int = None,
        birthday: str = None,
    ):
        """Initialize the Person object.

        The ``__init__`` method "initialize" the object, i.e., allocates a portion
        of the memory (object construction). The ``__init__`` function is called every
        time an object is created from a class.

        Args:
            name (str): Name of the person
            family name (str): Family name of the person
            matricola (int): Student identification number
            age (int, optional): How old is the person. Defaults to None.
            birthday (str, optional): The person's birthday. Defaults to None.
        """
        super().__init__(
            name, familyname, age=age, birthday=birthday
        )  # con `super()` richiama `__init__`` della classe Person
        self.matricola = matricola
        self.grade = None

    def set_exam_grade(self, grade: int):
        self.grade = grade

    def exam_passed(self):
        if self.grade is None:
            print(f"{self.name} {self.familyname} do the written exam first.")
        elif self.grade < 15:
            print(
                f"{self.name} {self.familyname}, sorry but you fail the exam.\nTry it again the next date."
            )
        elif self.grade < 18:
            print(f"Dear {self.name} {self.familyname}, you need to do the oral exam.")
        elif self.grade <= 30:
            print(f"Good job {self.name} {self.familyname}! you passed the exam!")
        else:
            print(
                f"Good job {self.name} {self.familyname}! you passed the exam CUM LAUDE!"
            )