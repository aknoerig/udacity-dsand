import sys

class HuffNode(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    @classmethod
    def from_tuple(self, char_freq_tuple):
        self.char = char_freq_tuple[0]
        self.freq = char_freq_tuple[1]
        self.left = None
        self.right = None

    def is_leaf(self):
        return not (self.left or self.right)


def create_frequency_list(data):
    frequency_map = {}
    for char in data:
        if char not in frequency_map.keys():
            frequency_map[char] = 1
        else:
            frequency_map[char] += 1
    frequencies = []
    for char, freq in frequency_map.items():
        frequencies.append( HuffNode(char, freq) )
    return frequencies


def sort_frequencies(frequencies):
    sorted_frequencies = sorted(frequencies, key=lambda x: x.freq, reverse=True)
    return sorted_frequencies


def build_huff_tree(text):
    frequencies = create_frequency_list( text )
    frequencies = sort_frequencies( frequencies )
    while len(frequencies) > 1:
        # take out two smallest nodes
        left = frequencies.pop()
        right = frequencies.pop()
        freq_sum = left.freq + right.freq
        # create new parent sum node
        parent = HuffNode( None, freq_sum )
        parent.left = left
        parent.right = right
        # update frequency list
        frequencies.append( parent )
        frequencies = sort_frequencies( frequencies )
    return frequencies[0]


def trim_huff_tree(tree, code):
    huff_map = {}
    if not tree:
        return huff_map
    if tree.is_leaf():
        huff_map[tree.char] = code
    huff_map.update( trim_huff_tree( tree.left, code + '0' ) )
    huff_map.update( trim_huff_tree( tree.right, code + '1' ) )
    return huff_map


def decode_next(data, index, tree):
    assert(tree)
    assert(len(data) > 0)
    if tree.is_leaf():
        return tree.char, index
    if data[index] == '0':
        return decode_next( data, index + 1, tree.left )
    else:
        return decode_next( data, index + 1, tree.right )


def huffman_encoding(text):
    huff_tree = build_huff_tree( text )
    huff_map = trim_huff_tree( huff_tree, '' )
    data = ''
    for char in text:
        data += huff_map[char]
    return data, huff_tree


def huffman_decoding(data,tree):
    text, next_index = decode_next( data, 0, tree )
    while next_index < len(data):
        next_char, next_index = decode_next( data, next_index, tree )
        text += next_char
    return text

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))