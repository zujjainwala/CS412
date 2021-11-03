import itertools
# def get_sequences(file, min_sup):

#     with open(file) as file_object:
#         lines = file_object.readlines()
#     #lines = open(file)

#     F1 = dict()
#     for line in lines:
#         begin = line.find("<") + len("<")
#         end = line.find(">")
#         substring = line[begin:end]

#         # Finding the 1-frequent itemset
#         for str in substring:
#             if str not in F1:
#                 F1[str] = 1
#             else:
#                 F1[str] += 1
    
#     print(F1)

#     # Prune itemsets that do not meet min support
#     keys = [k for k, v in F1.items() if v < min_sup]
#     for x in keys:
#         del F1[x]

#     return(F1)

#     # Finding the 2-frequent itemset
#     ## Want to loop through the dictionary and make all possible
#     ## combinations between the keys.
#     ## Then I want to go through the original input database and compare those
#     ## and determine if these combinations are in each of the substrings.
#     # for key, value in F1.items():
#     #     return 0
#     F2 = dict()
#     altered_input = list(F1)
#     result = [(x,y) for idx, x in enumerate(altered_input) for y in altered_input[idx + 1: ]]
#     result = [ x+y for (x, y) in result]
    
#     print(result)
#     for x in result:
#         for line in lines:
#             begin = line.find("<") + len("<")
#             end = line.find(">")
#             substring = line[begin:end]
#             #print(x, substring, x[0], x[1])
#             if x[0] in substring and x[1] in substring:
#                 #print(substring.index(x[0]), substring.index(x[1]))
#                 if substring.index(x[0]) < substring.index(x[1]):
#                     if x not in F2:
#                         F2[x] = 1
#                     else:
#                         F2[x] += 1
#     print(F2)
#     # merged = F1.copy()
#     # merged.update(F2)
#     # return(merged)


# # Testing with a simple database and minimum support
# #get_sequences('test.txt', 2)

# Practice with a new method
def get_sequences(file, min_sup):

    with open(file) as file_object:
        lines = file_object.readlines()

    combos = []
    count = 0
    Fk = {}
    for line in lines:
        begin = line.find("<") + len("<")
        end = line.find(">")
        substring = line[begin:end]

        temp = []

        for i in range(1, len(substring)+1):
            temp.append(list(itertools.combinations(substring, i)))

        for c in temp:
            for t in c:
                combos.append(''.join(t))

        for x in combos:
            if x in substring:
                if x not in Fk:
                    Fk[x] = 1
                else:
                    Fk[x] += 1

    return(Fk)

    #     # Finding the 1-frequent itemset
    #     for str in substring:
    #         if str not in F1:
    #             F1[str] = 1
    #         else:
    #             F1[str] += 1
    
    #print(F1)

    # # Prune itemsets that do not meet min support
    # # keys = [k for k, v in F1.items() if v < min_sup]
    # # for x in keys:
    # #     del F1[x]
    # F1 = {k:v for k,v in F1.items() if v >= min_sup}

    # print(F1)

    # # Finding the 2-frequent itemset
    # the_dict = F1.copy()
    # Fk = {}
    # for i in range(2,6):
    #     for k,v in the_dict.items():
    #         for i in range(len(k)):
    #             sub = substring[k[i][0]]
    #             if k[i][0] + 1 < len(sub):
    #                 new_sequence = ' '.join([k, sentence[k[i][1] + 1]])
    #                 if new_sequence not in candidates : candidates[new_sequence] = [(k[i][0], k[i][1]+1)]
    #                 else: candidates[new_sequence].append((k[i][0],k[i][1]+1))
                    
    #     if not candidates : break
    #     candidates = {k:v for k,v in candidates.items() if v >= min_sup}
    #     for elem in candidates:
    #         Fk[elem] = len(candidates[elem])
    #     the_dict = candidates.copy()

    # Fk_ = {}
    # for k,v in Fk.items():
    #     Fk_[k] = v
    
    # sorted_list = [v[0] for v in sorted(Fk_.items(), key=lambda kv:(-kv[1], kv[0]))][:20]
    # for i in range(len(sorted_list)):
    #     if i >= 100: break
    #     item = sorted_list[i]
    #     print("[" + str(Fk_[item]) + ", " + "'" + item + "'" + "]s")

# Testing with a simple database and minimum support
#get_sequences('test.txt', 2)
