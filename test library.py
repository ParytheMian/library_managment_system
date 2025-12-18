from datetime import datetime



class Library:
    """
    Initializing a library

    Attributes:
    membership(str): the person whom is joint to the library
    nameB(str): name of the book

    Methods:
    borrow(): borrowing books to memberships
    returnB(): withdrawing books from memberships
    add(): danating books to the library

    """

    def __init__(self, membership, nameB):
        self.membership = membership
        self.nameB = nameB

    def borrow(self):
        print(f"{self.membership} borrowed {self.nameB} at: {datetime.now()}")

    def returnB(self):
        print(f"{self.membership} returned {self.nameB} at: {datetime.now()}")

    def add(self):
        print(
            f"{self.membership} donated a book named :{self.nameB} at: {datetime.now()}")


membership1 = Library("Zahra", "Harry Potter")
membership1.borrow()
print(membership1)
membership2 = Library("Parastoo", "Crime and punishment")
membership2.add()
print(membership2)

