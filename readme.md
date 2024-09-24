https://leetcode.com/problems/length-of-last-word/

```
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = list(s.split())
        return len(l[len(l) - 1])
```

https://leetcode.com/problems/plus-one/
```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for v in digits:
            s += str(v)
        l = int(s) + 1
        result = []
        for v in str(l):
            result.append(int(v))
        return result
```
