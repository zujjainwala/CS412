def get_sequences(database, min_sup):

    with open(database) as file_object:
        lines = file_object.readlines()

    for line in lines:
        begin = line.find("<") + len("<")
        end = line.find(">")
        substring = line[begin:end]
        print(substring)
    

get_sequences('test.txt', 4)