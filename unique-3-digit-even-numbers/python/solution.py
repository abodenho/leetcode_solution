from typing import List

class Solution:
    @staticmethod
    def _clean_array(digits: list[int]) -> list[int]:
        """Clean the array, to avoid duplicata"""
        new_array = []

        for digit in digits:
            if digit not in new_array:
                new_array.append(digit)
        return new_array
    
    @staticmethod
    def _find_all_solution(partial_solution: str,digits: list[int],list_solution: list[str]) -> None:
        if len(partial_solution) == 3 :
            if Solution.test_solution(partial_solution):
                list_solution.append(partial_solution)
        else:
            for i in range(len(digits)):
                digit = digits.pop(i)
                print(digits)
                if not (digit == 0 and len(partial_solution) == 0):
                    partial_solution += str(digit)
                    Solution._find_all_solution(partial_solution,digits,list_solution)
                    partial_solution = partial_solution[:-1]
                digits.insert(i,digit)



    @staticmethod
    def test_solution(potential_solution:str):
        "Test if the potential solution found is correcte" 
        potential_solution = int(potential_solution)
        return potential_solution%2 == 0

    
    def totalNumbers(self, digits: list[int]) -> int:
        list_solution = []
        Solution._find_all_solution("",digits,list_solution)
        list_solution = Solution._clean_array(list_solution)
        return len(list_solution)
