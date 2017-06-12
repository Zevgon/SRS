def get_words(language, max_words=None):
    words = []
    with open('./bin/resources/%s/%s_words.txt' % (language, language), 'r') as f:
        for idx, line in enumerate(f.readlines()):
            if max_words is not None and idx == max_words:
                break
            if line.count('    ') != 1 or line.count(': ') != 1:
                raise Exception('Invalid format on line %s' % (idx + 1))
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
