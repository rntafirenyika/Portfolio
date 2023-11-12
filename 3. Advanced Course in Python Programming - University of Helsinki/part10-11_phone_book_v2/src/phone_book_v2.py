# Person class which takes care of the phone numbers and addresses of persons.
class Person:
    def __init__(self, name: str, number=None, address=None):
        numbers = []
        self._name = name
        if number != None:
            numbers.append(number)
        self._numbers = numbers
        self._address = address

    def name(self):
        return self._name
        
    def numbers(self):
        return self._numbers
        
    def address(self):
        return self._address
        
    def add_number(self, number: str):
        if number:
            self._numbers.append(number)

    def add_address(self, address: str):
        if address:
            self._address = address

# PhoneBook class that uses objects of class Person to store the data in the phone book.
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = None
            self.__persons[name] = Person(name, number)
        else:
            self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = None
            self.__persons[name] = Person(name, address=address)
        else:
            self.__persons[name].add_address(address)
        
    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].numbers(), self.__persons[name].address()

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        if self.__phonebook.get_entry(name) != None:
            numbers, address = self.__phonebook.get_entry(name)
        else:
            numbers = None
            address = None
        if numbers == None or numbers == []:
            print("number unknown")
        else:
            for number in numbers:
                print(number)
        if address == None:
            print("address unknown")
        else:
            print(address)
                
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address) 
            
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()