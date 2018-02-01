word_list = [
    {'word': "A", 'pinyin': "a", 'stage': 0, 'days': 0}, 
    
            ]
test = []
stages = [0, 1, 2, 3, 5, 7]

#temporary testing variables:
correct = True

#adds all rows in the word list with days < 1 to test
def build_test():
    del test[:] # clears the table test, as opposed to creating a NEW local table test = []
    for row in word_list: 
        if row['days'] < 1:
            test.append(row)
        print(test)

def grade_test():
    for row in word_list:
        if row in test:
            if correct:
                row['stage'] = row['stage'] + 1
                row['days'] = stages[row['stage']]
            else:
                row['stage'] = 0
                
def new_day():
    for row in word_list:
        row['days'] = row['days'] - 1

for i in range(15):   
    print("Stage {}".format(i))
    build_test()
    print(test)
    grade_test()
    print(word_list)
    new_day()
    print("\n\n")
