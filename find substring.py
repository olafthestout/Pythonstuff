s = 'azcbobobegghakl'

def findabc(s):
    if s is None or len(s) <= 1:
        return s

    barney = dog = s[0]

    for i in range(1, len(s)):
        if ord(s[i]) >= ord(s[i - 1]):
            dog += s[i]
        else:
            if len(barney) < len(dog):
                barney = dog
            dog = s[i]
    if len(barney) < len(dog):
        barney = dog
    return barney
    
print('Longest substring in alphabetical order is: ' + str(findabc(s)))