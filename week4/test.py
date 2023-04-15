DIGIT_LETTERS = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

def phoneNumberMnemonicsRec(prevWord, phoneNumber, nextIndex, mainArray):
    if nextIndex == len(phoneNumber):
        mainArray.append(prevWord)
        return
    for char in DIGIT_LETTERS[phoneNumber[nextIndex]]:
        phoneNumberMnemonicsRec(prevWord + char, phoneNumber, nextIndex + 1, mainArray)


arr = []
phoneNumber = '1905'
prevWord = ''
phoneNumberMnemonicsRec(prevWord, phoneNumber, 0, arr)
print(arr)