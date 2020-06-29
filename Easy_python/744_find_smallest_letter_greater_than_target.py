class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target<letters[0]:
            return letters[0]
        elif target>=letters[len(letters)-1]:
            return letters[0]
        else:
            for i in range(len(letters)):
                if letters[i]>target:
                    return letters[i]
