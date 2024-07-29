from utils.database import get_db



class Expense:
    def __init__(self, eid, amount, split_method, participants,splits=[]):
      
        #user.id is the one who pays
        #A slight assumption is made which doesn't align with real life scenario
        #in here we assume a single user pays the entire bill and then makes splits like exact , equal or by pecentage
        #however in real life, person keeps adding expense at the moments not at the end of the party/event.

        self.payer= eid
        self.amount = amount
        self.split_type = split_method
        self.participants = participants
        self.splits=splits


    def save(self):
        db = get_db()
        expenses = db.expenses
        expenses.insert_one({
            'payer': self.payer,
            'amount': self.amount,
            'split_type': self.split_type,
            'participants': self.participants,
            'splits':self.splits
        })
