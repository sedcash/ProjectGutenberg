from collections import Counter
import re, random, string
class BookAnalyzer:
    def __init__(self, file):
        self.file = file
        self.word_bank = None
        self.chapters = None
        self.setUpMemeberVariables()

    def getTotalNumberOfWords(self):
        return sum(self.word_bank.values())

    def printTotalNumberOfWords(self):
        print(" Total words in novel : ", self.getTotalNumberOfWords())

    def getTotalUniqueWords(self):
        return len(self.word_bank.keys())

    def printTotalUniqueWords(self):
        print(" Total unique words in novel : ", self.getTotalUniqueWords())

    def get20MostFrequentWords(self):
        return self.word_bank.most_common(20)

    def print20MostFrequentWords(self):
        print("Most frequent words:")
        for result in self.get20MostFrequentWords():
            print(result[0],": ",result[1])

    def get20MostInterestingFrequentWords(self):
        common_used = ['a', 'an', 'any', 'about', 'all', 'also', 'and', 'as', 'at', 'be', 'been', 'because', 'but', 'by', 'can', 'come',
                       'could', 'day', "did", 'do', 'even', 'find', 'first', 'for', 'from', 'get', 'give', 'go', 'had', 'has', 'have', 'he',
                       'her', 'here', 'him', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'know', 'like',
                       'look', 'make', 'man', 'many', 'me', 'more', 'my', 'new', 'no', 'not', 'now', 'of', 'on', 'one',
                       'only', 'or', 'other', 'our', 'out', 'people', 's', 'said', 'say', 'see', 'she', 'so', 'some', 'take', 'tell',
                       'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'thing', 'think', 'this',
                       'those', 'time', 'to', 'two', 'up', 'use', 'very', 'was','want', 'way','we', 'were', 'well', 'what', 'when',
                       'which', 'who', 'will', 'with', 'would', 'year', 'you', 'your', " ",]

        items = list(self.word_bank.items())
        non_common = [x for x in items if x[0] not in common_used]
        non_common = sorted(non_common, key = lambda x: x[1], reverse=True)
        return non_common[:20]

    def print20MostInterestingFrequentWords(self):
        print("Most interesting frequent words:")
        for result in self.get20MostInterestingFrequentWords():
            print(result[0],": ",result[1])

    def get20LeastFrequentWords(self):
        items = list(self.word_bank.items())
        items = sorted(items, key = lambda x: x[1])
        return items[:20]

    def print20LeastFrequentWords(self):
        print("20 Least Frequent words:")
        for result in self.get20LeastFrequentWords():
            print(result[0],": ",result[1])

    def getFrequencyOfWord(self, word):
        result = []
        for value in self.chapters.values():
            num_occur = value.count(word)
            result.append(num_occur)
        return result

    def printFrequencyOfWord(self, word):
        print(" Number of usages in each chapter of book:")
        print(self.getFrequencyOfWord(word))

    def getChapterQuoteAppears(self, target):
        result = -1
        for key, value in self.chapters.items():
            if target in value:
                result = key
                break
        return result

    def generateSentence(self):
        target = "the"
        count = 0
        sent = ""
        while count < 20:
            holder = []
            for value in self.chapters.values():
                words = value.split(" ")
                for i in range(len(words) - 1):
                    if target in words[i]:
                        next_word = words[i+1]
                        holder.append(next_word)
            sent += target + " "
            target = random.choice(holder)
            count += 1
        return sent

    def printGenerateSentence(self):
        print("Generated sentence:")
        print(self.generateSentence())



    def setUpMemeberVariables(self):
        words = []
        chapter = "CHAPTER"
        roman_pattern = "\s(.*?)\."
        pun_pattern = "[^A-Za-z0-9]+"
        text = ""
        chapters = {}
        curr_chap = 0

        with open(self.file) as f:
            content = f.readlines()
            f.close()

        content = [x.strip() for x in content if not x.isspace()]
        skip = [content[0], content[-1]]

        for i in range(len(content)):
            sent = content[i]
            if chapter in sent:
                chapters[curr_chap] = text
                text = ""
                roman = re.findall(roman_pattern, sent)[0]
                curr_chap = self.romanToInt(roman)
                words.append(chapter)
            else:
                if sent not in skip:
                    text += sent + " "
                temp = re.sub(pun_pattern, " ", sent).lower()
                temp = temp.split(" ")
                words.extend(temp)
        chapters[curr_chap] = text

        self.word_bank = Counter(words)
        del self.word_bank[""]
        self.chapters = chapters

    def romanToInt(self, roman):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        k = list(map(lambda x: roman_dict[x], list(roman)))
        return (sum([-k[x] if k[x + 1] > k[x] else k[x] for x in range(0, len(k) - 1)]) + k[-1])

file = "/Users/sedrick/Documents/The-Man-in-Black-An-Historical-Novel-of-the-Days-of-Queen-Anne_51174/data/data.txt"
analyzer = BookAnalyzer(file)
analyzer.printTotalNumberOfWords()
print()
analyzer.printTotalUniqueWords()
print()
analyzer.print20MostFrequentWords()
print()
analyzer.print20MostInterestingFrequentWords()
print()
analyzer.print20LeastFrequentWords()
print()
analyzer.printFrequencyOfWord("and")
print()
analyzer.printGenerateSentence()