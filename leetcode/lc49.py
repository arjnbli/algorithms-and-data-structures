from signal import strsignal


class Solution:
    def groupAnagrams(self, strs):
        #n - number of words
        #w - length of longest word
        #O(n*w*log(w)) time | O(n*w) space
        anagrams = {}
        for word in strs:
            #O(w*log(w) + w + w)
            sortedWord = ''.join(sorted(word)) 
            #O(1)
            if sortedWord not in anagrams:
                anagrams[sortedWord] = [word]
            else:
                anagrams[sortedWord].append(word)
        return list(anagrams.values())


if __name__ == '__main__':
   solution = Solution()
   print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
   print(solution.groupAnagrams([""]))
   print(solution.groupAnagrams(["a"]))
   