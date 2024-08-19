def process_data(data):
    result = []
    for i in range(len(data)):
        if data[i] % 2 == 0:
            result.append(data[i] * 2)
        else:
            result.append(data[i] + 1)
    return result
