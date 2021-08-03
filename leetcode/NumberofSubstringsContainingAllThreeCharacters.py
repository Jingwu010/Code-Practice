from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Given a string, find the number of substrings that 
        contains at least one occurrence of all unique letters in string
        
        string only contains a, b, c
        """
        n = len(s)
        # set of unqiue letters in string
        letter_set = set(['a', 'b', 'c'])
        # count each letter occurences
        letter_occurrence = defaultdict(int, {letter:0 for letter in letter_set})
        start_idx = 0
        end_idx = 0
        counts = 0
        while start_idx <= n-len(letter_set):
            # print(letter_occurrence)
            while self.is_any_value_missing(letter_occurrence) and end_idx < n:
                letter_occurrence[s[end_idx]] += 1
                end_idx += 1
            if not self.is_any_value_missing(letter_occurrence):
                counts += n-(end_idx-1)
            letter_occurrence[s[start_idx]] -= 1
            start_idx += 1
        return counts
    
    def is_any_value_missing(self, my_dict):
        """
        Given a dictionary with string to int key-value pair 
        return true if any value in the dictionary is greater than 0
        """
        return 0 in set(my_dict.values())
            
        
