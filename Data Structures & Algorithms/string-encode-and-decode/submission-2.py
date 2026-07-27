class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            for char in word:
                asc = ord(char)
                out+= f"{asc}+" 
            out+="_"
        
        return out



    def decode(self, s: str) -> List[str]:
        arr = []
        words = s.split("_")[:-1]
        for word in words:
            out = ""
            chars = word.split("+")[:-1]
            for char in chars:
                char = int(char)
                letter = chr(char)
                out+=f"{letter}"
            arr.append(out)
        
        return arr
