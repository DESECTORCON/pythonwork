def commaCode(xlist):
    returnL = []
    for i in range(len(xlist)):
        if i == 3:
            returnL.append(', and' + xlist[i])

        else:
            returnL.append(', ' + xlist[i])

spam = ['apples', 'bananas', 'tofu', 'cats']
a = commaCode(spam)
print(a)
''':argument
실패작'''