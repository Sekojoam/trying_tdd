import re


def string_calculator(sequence: str):
    if sequence == "":
        return 0
    separatorList = [",", "\n"]
    regexResult = re.findall("\[([^\[\]]*)\]", sequence)
    if regexResult:
        separatorList.extend(regexResult)
        sequence = sequence.split("]")[-1]
    else:
        regexResult = re.search("//(\D+)\d", sequence)
        if regexResult:
            separatorList.append(regexResult.group(1))
            sequence = sequence.split(f"//{separatorList[-1]}")[1]
    regex_pattern = "|".join(map(re.escape, separatorList))
    numbers = re.split(regex_pattern, sequence)
    calculatedValue = sum([int(number) for number in numbers if int(number) <= 1000])
    if calculatedValue < 0:
        raise ValueError("sequence must be a positive integer")
    return calculatedValue
