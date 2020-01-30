def load_data(path):
    words = {'Die': [], 'Das': [], 'Der': []}
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('Die '):
                word = line.split('-')[0].rstrip().split()[-1]
                words['Die'].append(word)
            elif line.startswith('Der '):
                word = line.split('-')[0].rstrip().split()[-1]
                words['Der'].append(word)
            elif line.startswith('Das '):
                word = line.split('-')[0].rstrip().split()[-1]
                words['Das'].append(word)

    return words
