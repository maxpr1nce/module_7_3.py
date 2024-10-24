import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = string.punctuation.replace('-', '')  # Удаляем тире

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.lower().translate(str.maketrans('', '', punctuation))
                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при обработке файла {file_name}: {e}")

        return all_words

    def find(self, word):
        word = word.lower()
        result = {}

        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word)

        return result

    def count(self, word):
        word = word.lower()
        result = {}

        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)

        return result

# Пример использования:
# finder = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
# print(finder.find('слово'))
# print(finder.count('слово'))der.get_all_words())