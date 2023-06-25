class Node:
    def __init__(self, country=None, capital=None, nextval=None):
        self.country = country
        self.capital = capital
        self.nextval = nextval


class SLinkedList:
    def __init__(self):
        self.headval = None

    def list_returner(self):
        spisok = []
        lister_var = self.headval
        while lister_var is not None:
            spisok.append([lister_var.country, lister_var.capital])
            lister_var = lister_var.nextval
        return spisok