def list_animals(animals):
    list = []
    for i in range(len(animals)):
        list.append(str(i + 1) + '. ' + animals[i] + '\n')
    return "".join(list)