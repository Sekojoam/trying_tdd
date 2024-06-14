def fb_translator(finalNumber: int):
    finalSentence = ""
    for index in range(1, finalNumber + 1):
        translatedInt = ""
        if index % 3 == 0:
            translatedInt = "Fizz"
        if index % 5 == 0:
            translatedInt += "Buzz"
        if translatedInt == "":
            translatedInt = str(index)
        finalSentence += translatedInt
    return finalSentence
