def get_sequences(file, min_sup):

    with open(file) as file_object:
        lines = file_object.readlines()
    #lines = open(file)

    F1 = dict()
    for line in lines:
        begin = line.find("<") + len("<")
        end = line.find(">")
        substring = line[begin:end]

        # Finding the 1-frequent itemset
        for str in substring:
            if str not in F1:
                F1[str] = 1
            else:
                F1[str] += 1
    
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
    # for key, value in F1.items():
    #     return 0
    F2 = dict()
    altered_input = list(F1)
    result = [(x,y) for idx, x in enumerate(altered_input) for y in altered_input[idx + 1: ]]
    result = [ x+y for (x, y) in result]
    
    print(result)
    for x in result:
        for line in lines:
            begin = line.find("<") + len("<")
            end = line.find(">")
            substring = line[begin:end]
            #print(x, substring, x[0], x[1])
            if x[0] in substring and x[1] in substring:
                #print(substring.index(x[0]), substring.index(x[1]))
                if substring.index(x[0]) < substring.index(x[1]):
                    if x not in F2:
                        F2[x] = 1
                    else:
                        F2[x] += 1
    return(F2)


# Testing with a simple database and minimum support
#get_sequences('test.txt', 2)
