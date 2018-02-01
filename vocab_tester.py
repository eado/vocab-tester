word_list = [
    {'word': "A", 'pinyin': "a", 'stage': 0, 'days': 0}, 
    {'word': "B", 'pinyin': "b", 'stage': 0, 'days': 0}, 
    {'word': "C", 'pinyin': "c", 'stage': 0, 'days': 0}, 
            ]
test = []

#config
stages = [1, 1, 2, 3, 5, 7]
test_filename = 'test.txt' #not used yet


#adds all rows in the word list with days < 1 to test
def build_test():
    del test[:] # clears the table test, as opposed to creating a NEW local table test = []
    for row in word_list: 
        if row['days'] < 1:
            test.append(row)

def grade_test():
    for row in word_list:
        if row in test:
            
                
            if input("{} {}: ".format(row['word'], row['pinyin'])):
                row['stage'] = 0
            else:
                row['stage'] = row['stage'] + 1
            row['days'] = stages[row['stage']]
                
def new_day():
    for row in word_list:
        row['days'] = row['days'] - 1
    
def write_test():
    test_file = open(test_filename, 'w')
    test_file.write("")
    for row in test:
        test_file.write("{}  ___\n".format(row['pinyin']))
    test_file.close()
        
while true:   
    print("Stage {}".format(i))
    build_test()
    write_test()
    grade_test()
    new_day()
    print("\n\n")
