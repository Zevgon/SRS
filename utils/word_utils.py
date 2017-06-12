def get_words(language, max_words=None):
    words = []
    path = './bin/resources/%s/%s_words.txt' % (language, language)
    with open(path, 'r') as f:
        for idx, line in enumerate(f.readlines()):
            if max_words is not None and idx == max_words:
                break
            if line.count('    ') != 1 or line.count(': ') != 1:
                raise Exception(
                    'Invalid format on line %s in file %s' % ((idx + 1), path))
            line = line.strip()
            foreign, pron_eng = line.split('    ')
            pron, eng = pron_eng.split(': ')
            new_word = {
                'foreign': foreign,
                'pronunciation': pron,
                'english': eng
            }
            words.append(new_word)
    return words
