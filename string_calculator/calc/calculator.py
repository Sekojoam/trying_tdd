def string_calculator(sequence):
    if sequence == "":
        return 0
    for separator in [",", "\n"]:
        if separator in sequence:
            numbers = sequence.split(separator)
            return sum([int(number) for number in numbers])
    calculatedValue = int(sequence)
    if calculatedValue< 0:
        raise ValueError("sequence must be a positive integer")
    return calculatedValue