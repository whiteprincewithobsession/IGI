import re
import zipfile
import os

class TextHandler:
    def __init__(self, file_path: str = None):
        with open(file_path, "r") as text_file:
            self.text = text_file.read()
            
    def count_sentences(self):
        """
        Count sentences in the text
        """
        sentences = re.split(r'(?<=[.!?])\s', self.text)
        sentences = [s for s in sentences if s.strip()]
        return sentences
        
    def classify_sentences(self) -> tuple[int, int, int, int]:
        """
        Classify sentences in the text by 3 groups
        """
        sentences = self.count_sentences()
        narr_count = 0
        interrog_count = 0
        imper_count = 0

        for sentence in sentences:
            if sentence.endswith('.'):
                narr_count += 1
            elif sentence.endswith('?'):
                interrog_count += 1
            elif sentence.endswith('!'):
                imper_count += 1

        return len(sentences), narr_count, interrog_count, imper_count
    
    def count_smileys(self) -> int:
        """
        Find and count smileys in the text with required pattern
        """        
        l = len(re.findall(r'\s[:;]-*[)]{1,}\s', self.text))
        l += len(re.findall(r'\s[:;]-*[(]{1,}\s', self.text))
        l += len(re.findall(r'\s[:;]-*[\[]{1,}\s', self.text))
        l += len(re.findall(r'\s[:;]-*[\]]{1,}\s', self.text))
        return l
    
    def average_len_sentence(self) -> float:
        """
        Calculates average length of sentence in the text
        """        
        sentences = self.text.split(".") + self.text.split("?") + self.text.split("?")
        count_sentences = len(sentences)
        words = self.text.split()
        return len(words) / count_sentences
    
    def average_word_length(self) -> float:
        """
        Calculates average length of word in the text
        """        
        words = re.findall(r'\w+', self.text)
        total_word_length = sum(len(word) for word in words)      
        average_length = total_word_length / len(words)
        return average_length
    
    def print_lowercase_numbers(self) -> list[str]:
        """
        Find all words, that must contain only lowercase letters and numbers
        """   
        pattern = re.compile(r'\b(?:[a-z]+\d|\d+[a-z]+)([a-z0-9])*\b')
        words = re.findall(pattern, self.text)
        return words
    
    def count_lowercase_letters(self) -> int:
        """
        Count lowercase letters in the text
        """   
        pattern = re.compile(r'[a-z]')
        matches = re.findall(pattern, self.text)
        return len(matches)
    
    def find_v_word(self) -> tuple[str, int]:
        """
        Find first word, that starts with 'v' and returns it and its index
        """   
        words = re.findall(r'\w+', self.text)
        v_words = re.findall(r'\bv\w*\b', self.text)
        
        if len(v_words) == 0:
            return 'No such words', -1
        
        return v_words[0], words.index(v_words[0])
    
    def remove_s_words(self) -> str:
        """
        Remove all words, that starts with s
        """   
        new_text = self.text
        s_words = re.findall(r'\bs\w*\b', self.text)
        
        if len(s_words) == 0:
            return "No words starting with 's'"
        
        for i in range(len(s_words)):
            new_text.replace(s_words[i], '')
            
        return new_text
    
    def print_all_info_console(self) -> None:
        """
        Function for printing all info about text
        """   
        sentences = self.classify_sentences()
        print(f"Count of sentences: {sentences[0]}\nNarrative: {sentences[1]}\
\nInterrogative: {sentences[2]}\nIncentives: {sentences[2]}")
        print(f"Average length of sentences in the test: {self.average_len_sentence()}")
        print(f"Average length of word in the text: {self.average_word_length()}")
        print(f"Number of smileys in the text: {self.count_smileys()}")
        print(f"Words with only lowercase and numbers: {self.print_lowercase_numbers()}")
        print(f"Count of lowercase letters: {self.count_lowercase_letters()}")
        print(f"First word with 'v' on the start: {self.find_v_word()[0]}, index: {self.find_v_word()[1]}")
        print(f"Text without words, that starting with 's':\n{self.remove_s_words()}")
        
    def print_info_file(self) -> None:
        """
        Function for printing all info about text in the *.txt file and compress it into the *.zip
        """   
        try:
            with open("result.txt", 'w') as file:
                sentences = self.classify_sentences()
                file.write(f"Count of sentences: {sentences[0]}\nNarrative: {sentences[1]}\
\nInterrogative: {sentences[2]}\nIncentives: {sentences[2]}\n")
                file.write(f"Average length of sentences in the test: {self.average_len_sentence()}\n")
                file.write(f"Average length of word in the text: {self.average_word_length()}\n")
                file.write(f"Number of smileys in the text: {self.count_smileys()}\n")
                file.write(f"Words with only lowercase and numbers: {self.print_lowercase_numbers()}\n")
                file.write(f"Count of lowercase letters: {self.count_lowercase_letters()}\n")
                file.write(f"First word with 'v' on the start: {self.find_v_word()[0]}, index: {self.find_v_word()[1]}\n")
                file.write(f"\n===\nText without words, that starting with 's':\n===\n{self.remove_s_words()}\n")
        except Exception as e:
            print(f"Ошибка при создании файла: {e}")    
        with zipfile.ZipFile('task2_archive.zip', 'w') as my_zip:
            my_zip.write('result.txt')

    def print_info_about_archive(self):
        """
        Function for printing all info about archive with result *.txt file
        """   
        with zipfile.ZipFile('task2_archive.zip') as zf:
            for name in zf.namelist():
                info = zf.getinfo(name)
                print(f"File in archive: {os.path.basename(info.filename)},\t\
size: {info.compress_size}")
                
    @staticmethod
    def check_correct_ip_address(ip : str) -> bool:
        ip_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?)$')
        checker = bool(re.match(ip_pattern, ip))
        return checker