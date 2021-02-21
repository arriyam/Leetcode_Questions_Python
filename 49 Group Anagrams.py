class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[str]:
        book = {}
        for i in range(len(strs)):
            a = sorted(strs[i])
            a = str(a)
            a = a.replace("[", "")
            a = a.replace("]", "")
            a = a.replace(",", "")
            a = a.replace("'", "")
            a = a.replace(" ", "")
            if a in book:
                bob = book[a]
                bob.append(strs[i])
                book.update({a: bob})
                bob = []
            else:
                book.update({a: [strs[i]]})
        return (book.values())




