class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "[]"
        last = len(strs) - 1
        single = ""
        for i, word in enumerate(strs):
            if i == last:
                single += word
            else:
                concate = word + ";"
                single += concate
        return single
    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        extract = s.split(";")
        return extract
