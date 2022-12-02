tables = [3, 6, 3, 4, 2, 2, 6]

class Table:
    def __init__(self, seats):
        pass

class Restaurant:
    def __init__(self, tables_list):
        self.tables: list[Table] = []
        for t in tables_list:
            self.tables.append(Table(t))


zoozbra = Restaurant([20, 10, 4, 8])