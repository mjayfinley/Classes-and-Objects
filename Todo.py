class Todo:
    def __init__(self, name):
        self.user = name
        self.tasks = []

    def add_task(self):
        userInput = input(f"{self.user}, Please enter a task: ")
        self.tasks.append(userInput)

    def view_tasks(self):
        print(f"Here are your tasks: {self.tasks}")

    def remove_task(self):
        userInput = input(f"Please enter a task to be removed: ")
        self.tasks.remove(userInput)
        print(f"Your new task list is: {self.tasks}")

    def quit_app(self):
        userInput = input(f"Please press 'q' to quit the app. ")
        if userInput == 'q':
            return exit

micah = Todo("Micah")

#micah.add_task()
#micah.add_task()
#micah.view_tasks()
#micah.remove_task()
#micah.quit_app()

#Bonus - task priority sorting
