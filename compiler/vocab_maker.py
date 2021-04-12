"""
A quick script to make our custom vocab
"""
import pickle

# Edit the token vocab here
my_data = {'\n': 0,
            ' ': 1,
            ',': 2,
            '<END>': 3,
            '<START>': 4,
            'btn-active': 5,
            'btn-green': 6,
            'btn-inactive': 7,
            'btn-orange': 8,
            'btn-red': 9,
            'double': 10,
            'header': 11,
            'quadruple': 12,
            'row': 13,
            'single': 14,
            'small-title': 15,
            'text': 16,
            '{': 17,
            '}': 18,
            'opening-tag': 19,
            'closing-tag': 20,
            'css-file-name': 21,
            'body': 22,
            'header-right': 23,
            'big-title': 24,
            'big-text': 25,
            'small-text': 26,
            'img': 27,
            'empty': 28,
            }

# Save the new vocab file
file_name='our_vocab.pkl'
f = open(file_name,'wb')
pickle.dump(my_data,f)
f.close()

# load : get the data from file
data = pickle.load(open(file_name, "rb"))
# loads : get the data from var
#data = pickle.load(var)