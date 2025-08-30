from random import randint
class Train:

    def __init__(self, train_no):
        self.train_no = train_no

    def book_ticket(self, train_no, fro, to):
        print(f"Ticket is booked in train no: {train_no} from {fro} to {to}")

    def get_status(self, train_no, fro, to):
        print(f"Train no: {train_no} from {fro} to {to} is running...")

    def get_fare(self, train_no, fro, to):
        print(f"Ticket fare in train no: {train_no} from {fro} to {to} is {randint(1000, 5000)}")


t1 = Train(123)
t1.book_ticket("Karachi", "Rohri")
t1.get_status("Karachi", "Rohri")
t1.get_fare("Karachi", "Rohri")