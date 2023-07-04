def find_the_first_repeated(str):
    """this function is used to find the first repeated word in the string that given"""
    words={}
    arr=str.split(" ")    
    for i in arr:
        if i.startswith(",") or i.startswith("."):
            i=i[1:]
        if i.endswith(",") or i.endswith("."):
            i=i[:-1]
        if i in words:
            return i 
        words[i]=1

#Strech goal
def all_words_count(str):
    """this function takes a string as an argument and returns the count of each word in the string"""
    words_count={}
    if str == "":
        return words_count
    arr=str.split(" ")
    for i in arr:
        if i.startswith(",") or i.startswith("."):
            i=i[1:]
        if i.endswith(",") or i.endswith("."):
            i=i[:-1]
        if i in words_count:
            words_count[i]+=1
        else:
            words_count[i]=1
    return words_count

def the_most_repeated_word_list(str):
    """this method responsable to return a list of the most repeated words on a string"""
    # words_count={}
    # arr=str.split(" ")
    # most_repeated=[]
    # max=0
    # for i in arr:
    #     if i.startswith(",") or i.startswith("."):
    #         i=i[1:]
    #     if i.endswith(",") or i.endswith("."):
    #         i=i[:-1]
    #     if i in words_count:
    #         words_count[i]+=1
    #         if words_count[i]>max:
    #             max=words_count[i]
    #     else:
    #         words_count[i]=1
    #         if words_count[i]>max:
    #             max=words_count[i]
    # for i in words_count:
    #     if words_count[i]==max:
    #         most_repeated.append(i)
    # return most_repeated
    words_count=all_words_count(str) #cleaner code
    most_repeated=[]
    max=0
    for i in words_count:
        if words_count[i]>max:
            max=words_count[i]
            most_repeated=[]
        if words_count[i] == max:
            most_repeated.append(i)
    return most_repeated

