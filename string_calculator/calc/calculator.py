import re


def string_calculator(sequence: str):
    if sequence == "":
        return 0
    separatorList = [",", "\n"]
    regexResult = re.search("//\[(.*)]", sequence)
    if regexResult:
        separatorList.append(regexResult.group(1))
        sequence = sequence.split("]")[1]
    else:
        regexResult = re.search("//(\D+)\d", sequence)
        if regexResult:
            separatorList.append(regexResult.group(1))
            sequence = sequence.split(f"//{separatorList[-1]}")[1]
    for separator in separatorList:
        if separator in sequence:
            numbers = sequence.split(separator)
            return sum([int(number) for number in numbers if int(number) <= 1000])
    calculatedValue = int(sequence)
    if calculatedValue < 0:
        raise ValueError("sequence must be a positive integer")
    return calculatedValue
