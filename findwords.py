import os, re
import logging




class words:
    def __init__(self):    
        
        logging.info(os.path.abspath(os.curdir))
        try:
            f = open(r'.\source\singular.txt')
        except:
            logging.error('Не удалось загрузить слова...')
            return None
        else:
            self.source = f.read()

# Задаем шаблон для незначащих букв. Незначащие буквы - это все кроме тех, которые кодируют цифры

        self.dig_pat = r"[нмгждткхчщбпшлсзвфрз]"
        self.dig_pat_ex = r"[^нмгждткхчщбпшлсзвфрз \n]"


# Задаем словарь для определения буквы

        self.dig_dict = {
            "0" : "[нм]",
            "1" : "[гж]",
            "2" : "[дт]",
            "3" : "[кх]",
            "4" : "[чщ]",
            "5" : "[пб]",
            "6" : "[шл]",
            "7" : "[сз]",
            "8" : "[вф]",
            "9" : "[рз]"
        }

# Объект регулярных выражений для проверки на то что строка является числом

        self.test_dig = re.compile(r'\d+')


    def get_mask(self, num):
        """
        Функция формирующая шаблон для поиска подходящего слова.
        num должна быть строкой
        """
        try:
            mask = self.test_dig.match(num)
        except :
            return None 
        else:
            if mask:
                num = mask.group(0)
        mask = r"\b" + self.dig_pat_ex + r'*'
        for i in num:
            mask += self.dig_dict[i] + self.dig_pat_ex + r'*'
        mask += r'\w*\b'

        return mask
   
    def get_words(self, num):
        try:
            num = f"{num:02}"
        except ValueError as ve:
            num = num
        mask = self.get_mask(num)  
        try:
            res = re.findall(mask, self.source)
        except:
            return None
        else:
            return res   
     




