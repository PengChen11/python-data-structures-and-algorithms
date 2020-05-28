class Cat:
    def __init__(self,name):
        self.name = name
        self.kind = "cat"
        self.next = None

    def __str__(self):
        return f"I am a cat, my name is {self.name}"

class Dog:
    def __init__(self,name):
        self.name = name
        self.kind = "dog"
        self.next = None

    def __str__(self):
        return f"I am a dog, my name is {self.name}"


class AnimalShelter:
    def __init__(self,front=None):
        self._front = front
        self._rear = self._front

    def enqueue(self,animal,name):
        if animal == "cat":
            new_animal = Cat(name)
        elif animal == "dog":
            new_animal = Dog(name)
        else:
            raise Exception("This sheltor only accepts cats and dogs")
        if self._rear is None:
            self._front = self._rear = new_animal
        else:
            self._rear.next = new_animal
            self._rear = new_animal

    def dequeue(self,pref=None):
        if pref is None:
            return "Null"
        else:
            try:
                if self._front.kind == pref:
                    dequeue_animal = self._front
                    self._front = self._front.next
                    return dequeue_animal
                else:
                    current = self._front
                    while True:
                        if current.next.kind == pref:
                            dequeue_animal = current.next
                            current.next = current.next.next
                            return dequeue_animal
                        current = current.next

            except:
                print(f'The shelter does not have {pref} now')

    def __str__(self):
            output = ""
            current = self._front

            while current:
                output += f"{current.kind} {current.name} & "
                current = current.next
            return output + "are in the shelter now"


