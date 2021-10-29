def get_sequences(database, min_sup):

    with open(database) as file_object:
        lines = file_object.readlines()

    F1 = {}
    for line in lines:
        begin = line.find("<") + len("<")
        end = line.find(">")
        substring = line[begin:end]

        # Finding the 1-frequent itemset
        count = 0
        for str in substring:
            if str in F1:
                F1[str] = F1[str] + 1
                count = F1[str]
            else:
                F1[str] = 1

    print(F1)

    # Prune itemsets that do not meet min support
    keys = [k for k, v in F1.items() if v < min_sup]
    for x in keys:
        del F1[x]

    print(F1)


    # Finding the 2-frequent itemset
    ## Want to loop through the dictionary and make all possible
    ## combinations between the keys.
    ## Then I want to go through the original input database and compare those
    ## and determine if these combinations are in each of the substrings.
    for key, value in F1.items():
        return 0

# Testing with a simple database and minimum support
get_sequences('test.txt', 2)
