def wordcount(doc):
    num = 0
    doc = doc.split()
    for word in doc :
        num += 1    
    print(str(num))
    return
