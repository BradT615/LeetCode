class Solution(object):
    def reverseVowels(self, s):

        vowels = "AaEeIiOoUu"
        s = list(s)
        start = 0
        end = len(s) - 1
        
        while start < end:
            if s[start] not in vowels:
                start += 1
                continue
            if s[end] not in vowels:
                end -= 1
                continue

            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        
        return ''.join(s)