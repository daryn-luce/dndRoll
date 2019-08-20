def backwords(string):
    if string[-3:] == ' /s':
        return string[-4::-1]
    else:
        words = string.split()
        newlist = []
        for word in words:
            newlist.append(word[-1::-1])
            
        return ' '.join(newlist)

print(backwords('This sentense is backwords /s'))
print(backwords('The words of the sentense are backwords'))    