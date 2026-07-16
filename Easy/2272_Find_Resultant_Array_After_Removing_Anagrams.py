#Remove every word that is an anagram of the immediately preceding word, keeping only the first word from each consecutive anagram group.
class Solution(object):
    def removeAnagrams(self, words):
        res = [words[0]]
        
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i - 1]):
                res.append(words[i])
                
        return res