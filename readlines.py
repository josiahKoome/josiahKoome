# Read the file line by line

def csv2dict(csv_file) -> list:
    with open(csv_file, 'r') as file:
        x = []
        # Create a list of the input streams
        for line in file:
            x.append(line.strip())

        # Remove empty trailing strings
        for i in x:
            if i == '':
                x.remove(x[len(x) - 1])

        keysList = x[0].split(',')

        x.remove(x[0])

        # Create a list to hold the split values:
        list1 = []
        for i in range(len(x)):
            vals = x[i].split(',')
            list1.append(vals)

        list_of_dictionaries = []

        for j in range(len(list1)):
            dictionary = {} 
            for k in range(len(keysList)):
                dictionary[keysList[k]] = list1[j][k]
            list_of_dictionaries.append(dictionary)

    return list_of_dictionaries

output = csv2dict('cities.csv')
print(output)







