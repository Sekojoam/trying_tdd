def string_calculator(sequence: str):
    if sequence == "":
        return 0
    separatorList = [",", "\n"]
    if sequence.startswith("//"):
        newSequence = sequence.split("//")[1]
        delimiter = newSequence[0]
        separatorList.append(delimiter)
        sequence = newSequence[1:]
    for separator in separatorList:
        if separator in sequence:
            numbers = sequence.split(separator)
            return sum([int(number) for number in numbers if int(number) <= 1000])
    calculatedValue = int(sequence)
    if calculatedValue < 0:
        raise ValueError("sequence must be a positive integer")
    return calculatedValue
