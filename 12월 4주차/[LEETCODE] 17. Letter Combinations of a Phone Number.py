def letterCombinations(self, digits):

    numbers = {"2":['a', 'b', 'c'], "3":['d', 'e', 'f'], "4":['g', 'h', 'i'],
            "5":['j', 'k', 'l'], "6":['m', 'n', 'o'], "7":['p', 'q', 'r', 's'],
            "8":['t', 'u', 'v'], "9":['w', 'x', 'y', 'z']}

    answer = ['']
    if digits == "":
        return []

    else:
        if len(digits) == 1:
            return numbers[digits]

        else:
            for digit in digits:
                temp = []
                for a in answer:
                    for number in numbers[digit]:
                        temp.append(a+number)
                answer = temp
    return answer