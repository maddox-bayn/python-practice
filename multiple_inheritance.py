class Human:
    def __init__(self, num_heart) -> None:
        print("calling the human")
        self.eyes=2
        self.nose=1
        self.numheart=num_heart
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")

class Male:
    def __init__(self, name) -> None:
        print("calling the male")
        self.name=name
    def flirt(self):
        print("i can flirt")
    def work(self):
        print("i can code")

class Boy(Human, Male):
    def __init__(self, name, heart, language) -> None:
        Human.__init__(self, heart)
        Male.__init__(self, name,)
        self.language=language
    def sleep(self):
        print("i can slep")
    def work(self):
        print("i can tast")
    def display(self):
        print(f"hi i am {self.name}and i work on the language {self.language}")
boy_1=Boy('maddox',1,'python')
print(boy_1.nose)
#Male.work(boy_1)
print(boy_1.numheart)
print(boy_1.language)
boy_1.display()