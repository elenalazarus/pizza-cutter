class Pizza:
    def __init__(self, rows, columns, mini, maxi, pizza):
        self.rows = rows
        self.columns = columns
        self.mini = mini
        self.maxi = maxi
        self.pizza = pizza


def read(path):
    pizza = []
    with open(path) as file:
        data = file.readlines()
    rules = data[0].split()
    for row in data[1:]:
        pizza.append(list(row)[:-1])
    return Pizza(rules[0], rules[1], rules[2], rules[3], pizza)




if __name__ == '__main__':
    pizza = read('/Users/zlatahayvoronska/Documents/hashcode-2019-practice/task/a_example.in')
    print(pizza.pizza)