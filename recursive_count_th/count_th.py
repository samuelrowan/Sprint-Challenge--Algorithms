'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # This version is better but better doesn't matter at Lambda.
    # x=word.split('th')
    # y=len(x)-1
    search= ['t', 'h']
    #This is the inferior version Lambda wants:
    if word == '':
        return 0
    if word[:2] == "th":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])