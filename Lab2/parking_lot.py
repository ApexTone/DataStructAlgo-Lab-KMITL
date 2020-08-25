from Lab2.stack import Stack


class Parking:
    def __init__(self, cap):
        self.park = Stack(cap=cap)

    def is_full(self):
        return self.park.is_full()

    def arrive(self, car):
        if not self.park.is_full():
            self.park.push(car)
            print(f"Car {car} arrive\tSpace left {self.park.cap-self.park.size()}")
        else:
            print(f"Car {car} can't arrive: SOI FULL")

    def depart(self, car):
        if car in self.park.items:
            print(f"Car {car} depart:")
            print('\t', end="")
            temp = Stack()
            while self.park.peek() != car:
                buffer = self.park.pop()
                print(f"pop {buffer}", end=", ")
                temp.push(buffer)
            self.park.pop()
            while not temp.is_empty():
                buffer = temp.pop()
                print(f"push {buffer}", end=", ")
                self.park.push(buffer)
            print(f"\n\tSpace left {self.park.cap-self.park.size()}")
        else:
            print(f"Car {car} can't not depart: No car {car}")

    def __str__(self):
        return f"soi = {self.park}"


def test_park():
    pk = Parking(4)
    pk.depart(6)
    pk.arrive(1)
    pk.arrive(2)
    pk.arrive(3)
    pk.arrive(4)
    pk.arrive(5)
    print(pk)
    pk.depart(7)
    pk.depart(2)
    print(pk)

if __name__ == '__main__':
    test_park()
