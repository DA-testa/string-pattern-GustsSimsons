def read_input():
    inputFormat = input().strip()
    if inputFormat == "F":
        with open("tests/06") as file:
            pattern = file.readline().strip()
            text = file.readline().strip()
        return pattern, text  
    elif inputFormat == "I":
        return (input().rstrip(), input().rstrip())

def print_occurrences(output):

    print(' '.join(map(str, output)))


def getHash(data):
    dataLength = len(data)
    B = 13
    Q = 256
    result = 0
    for i in range(dataLength):
        #Man liekas, ka B*result vienmeer bus 0, bet es atstasu, ka bija prezentacija
        result = (B * result + ord(data[i])) % Q
    return result

def get_occurrences(pattern, text):
    textLength = len(text)
    patternLength = len(pattern)
    
    patternHash = getHash(pattern)
    occuranceIndexes = []
    
    

    for i in range(textLength - patternLength + 1):
        window = text[i : i+patternLength]
        windowHash = getHash(window)
        if windowHash == patternHash:
            if window == pattern:
                occuranceIndexes.append(i)
    
    return occuranceIndexes



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

