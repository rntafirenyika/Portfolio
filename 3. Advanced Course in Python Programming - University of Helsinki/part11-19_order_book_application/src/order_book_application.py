# Class named Task which models a single task in a software company's list of tasks.
class Task:
    id = 1
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.id = Task.id
        Task.id += 1
        self.__finished = False

    def __str__(self):
        if self.is_finished():
            status = "FINISHED"
        else:
            status = "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

    # Checks the state of the task (finished or not yet finished), returns a Boolean value.
    def is_finished(self):
        return self.__finished

    # Marks a task as finished.
    def mark_finished(self):
        self.__finished = True

# Class named OrderBook which collects all the tasks ordered from the software company.
class OrderBook:
    def __init__(self):
        self.orders = []

    # Adds a new order to the OrderBook.
    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    # Returns a list of all the tasks stored in the OrderBook.
    def all_orders(self):
        return self.orders

    # Returns a list of the names of all the programmers with tasks stored in the OrderBook.
    def programmers(self):
        team = set()
        for task in self.orders:
            team.add(task.programmer)
        return list(team)

    # Returns a list containing the finished orders from the OrderBook.
    def finished_orders(self):
        completed = []
        for task in self.orders:
            if task.is_finished():
                completed.append(task)
        return completed

    # Returns a list containing the unfinished orders from the OrderBook.
    def unfinished_orders(self):
        pending = []
        for task in self.orders:
            if not task.is_finished():
                pending.append(task)
        return pending

    # Takes the id of the task as its argument and marks the relevant task as finished.
    def mark_finished(self, id: int):
        count = 0
        for task in self.all_orders():
            if task.id == id:
                count += 1
                task.mark_finished()
                return
        if count == 0:
            raise ValueError("Task not found")

    # Returns a tuple that contains the number of finished and unfinished tasks the programmer has assigned to them, along with the estimated hours in both categories.
    def status_of_programmer(self, programmer: str):
        fin_count = 0
        fin_hours = 0
        unfin_count = 0
        unfin_hours = 0
        for task in self.finished_orders():
            if task.programmer == programmer:
                fin_count += 1
                fin_hours += task.workload
        for task in self.unfinished_orders():
            if task.programmer == programmer:
                unfin_count += 1
                unfin_hours += task.workload
        if fin_count >= 1 or unfin_count >= 1:
            return (fin_count, unfin_count, fin_hours, unfin_hours)
        raise ValueError("Programmer not found")

# Application to interact with the user.
class OrderBookApplication:
    def __init__(self):
        self.__database = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.finished_tasks()
            elif command == "3":
                self.unfinished_tasks()
            elif command == "4":
                self.mark_task()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.programmers_status()

    def add_order(self):
        description = input("description: ")
        try:
            pw = (input("programmer and workload estimate: ")).split()
            self.__database.add_order(description, pw[0], int(pw[1]))
            print("added!")
        except Exception:
            print("erroneous input")

    def finished_tasks(self):
        tasks = self.__database.finished_orders()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("no finished tasks")

    def unfinished_tasks(self):
        tasks = self.__database.unfinished_orders()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("no unfinished tasks")

    def mark_task(self):
        try:
            id = int(input("id: "))
            self.__database.mark_finished(id)
            print("marked as finished")
        except Exception:
            print("erroneous input")

    def programmers(self):
        for programmer in self.__database.programmers():
            print(programmer)

    def programmers_status(self):
        programmer = input("programmer: ")
        try:
            data = self.__database.status_of_programmer(programmer)
            print(f"tasks: finished {data[0]} not finished {data[1]}, hours: done {data[2]} scheduled {data[3]}")
        except Exception:
            print("erroneous input")

application = OrderBookApplication()
application.execute()