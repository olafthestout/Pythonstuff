def vowelcount(s):
    vowels = "aeiouAEIOU"
    nvowels = ""
    for x in s:
        if x in vowels:
            nvowels += x
            nu = len(nvowels)
    return nu
   
print('Number of vowels: ' + str(vowelcount(s)))