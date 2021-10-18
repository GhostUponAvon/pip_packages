def hw():
    print('hello world')
    
def lettercount(doc, spaces='yes'):
    num = 0
    for i in doc :
        if i != ' ' and spaces == 'no':
            num = num + 1
        elif spaces == 'yes':
            num += 1    
    return num
