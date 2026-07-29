DELIMETER = "|"

class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}{DELIMETER}{s}" for s in strs])

    # 5|Hello5|World

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        
        while i < s.find(DELIMETER, i) != -1 if False else i < len(s):
            j = s.index(DELIMETER, i)
            length = int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i = j + 1 + length
        return ans
 
