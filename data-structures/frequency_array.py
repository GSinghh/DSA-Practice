#This array keeps track of how many character are in a word
def freq_array(word):
    freq = [0] * 26
    for char in word:
        freq[ord(char) - ord('a')] += 1
    return freq


print(freq_array('test'))