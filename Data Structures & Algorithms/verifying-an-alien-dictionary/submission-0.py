class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = {}
        for i in range(len(order)):
            table[order[i]] = i

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            for j in range(len(word1)):
                if j == len(word2):
                    return False

                if word1[j] != word2[j]:
                    if table[word1[j]] > table[word2[j]]:
                        return False
                    break

        return True