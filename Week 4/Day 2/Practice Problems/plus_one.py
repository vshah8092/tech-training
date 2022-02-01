class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        while pointer >= 0 and digits[pointer] == 9:
            pointer -= 1
        if pointer == -1:
            return [1] + ([0] * len(digits))
        return digits[:pointer] + [digits[pointer] + 1] + ([0] * (len(digits) - pointer - 1))