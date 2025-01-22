class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        signes = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                s = file.read().lower()
                for sign in signes:
                    s = s.replace(sign, '')
                s = s.replace('\n', ' ')
                s = s.split(' ')
            all_words[file_name] = s
        return all_words

    def find(self, word):
        counters = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            counter = 0
            while (words[counter] != word) and (counter + 1 < len(words)):
                counter += 1
            if counter + 1 < len(words):
                counters[file_name] = counter + 1
            else:
                counters[file_name] = 'Не найдено'
        return counters

    def count(self, word):
        counters = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            counter = 0
            for s in words:
                if s == word:
                    counter += 1
            counters[file_name] = counter
        return counters



finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))