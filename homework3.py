import itertools

# Finding the frequent patterns of a 'file' with a specified 'min_sup'
def get_sequences(file, min_sup):

    with open(file) as file_object:
        lines = file_object.readlines()

    # Initialize a list of all possible combinations of strings in the database
    # Create an empty dictionary that will keep all the frequent patterns
    combos = []
    count = 0
    Fk = {}
    for line in lines:
        # Read through each line of the file and clean it up to only reveal the wanted string
        begin = line.find("<") + len("<")
        end = line.find(">")
        substring = line[begin:end]

        temp = []

        # Create all the possible combinations from the current string
        # Store each combination in a temp array
        for i in range(1, len(substring)+1):
            temp.append(list(itertools.combinations(substring, i)))

        # This will be a list of lists of separate strings, so this 
        # combines each to form the desired frequent itemsets
        for c in temp:
            for t in c:
                combos.append(''.join(t))

        # Create the 'set' of the combos array that makes sure there are
        # no repeats of frequent itemsets
        # Loop through each combo and compare it to the current string
        # and check if it is part of the string and whether it is in the dict or not
        # print(set(combos))
        for x in set(combos):
            if x in substring:
                if x not in Fk:
                    Fk[x] = 1
                else:
                    Fk[x] += 1

    #print(combos)
    
    # Cleanup the filled dictionary and remove the keys-values that do not meet the min_sup
    Fk = {k:v for k,v in Fk.items() if v >= min_sup}

    return(Fk)

# Testing with a simple database and minimum support
#get_sequences('test.txt', 2)
