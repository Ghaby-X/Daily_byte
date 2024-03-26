# This question is asked by Amazon. Given two strings representing sentences, return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). You may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters.

# Ex: given the following strings...

# sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
# sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
# sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]

def uncommon_words(s1: str, s2: str):
    archive = {}
    s1_list = set(s1.split())
    s2_list = set(s2.split())
    
    for i in s1_list:
        archive[i] = 1
        
    for j in s2_list:
        if archive.get(j) != None:
            archive.pop(j)
        else:
            archive[j] = 1
            
    print(list(set(archive.keys())))
    return

uncommon_words("the quick", "brown fox")  # ->>> ["the", "quick", "brown", "fox"]
uncommon_words("the tortoise beat the haire", "the tortoise lost to the haire")  # ->>> ["beat", "to", "lost"]
uncommon_words("copper coffee pot", "hot coffee pot")   # ->>> ["copper", "hot"]