class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        def helper(word):
            alphabat = [0] * 26
            for c in word:
                alphabat[ord(c) - 97] += 1
            return tuple(alphabat)

        for i in range(len(strs)):
            tmp = helper(strs[i])
            result[tmp].append(strs[i])
        
        return list(result.values())