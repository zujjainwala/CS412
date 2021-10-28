def get_sequences(database, min_sup):

    with open(database) as file_object:
        lines = file_object.readlines()

    min_support = min_sup
    for line in lines:
        begin = line.find("<") + len("<")
        end = line.find(">")
        substring = line[begin:end]

        F1 = {}
        count = 0
        total_count = 0
        for str in substring:
            if str in F1:
                count += 1
                F1[str] += count
            else:
                F1[str] = count

        #print(substring)
        #print(count)
        print(F1)
    

get_sequences('test.txt', 4)