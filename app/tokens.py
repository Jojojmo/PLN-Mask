import re
import spacy
from supply import target_sintagmas

nlp = spacy.load("pt_core_news_md")

class Sack_tokens:
    def __init__(self,text:str):
        self.doc = nlp(text)
        self.word_sack = self.count_word()


    def select_target_sintagmas(func):
        def wrapper(self):
            count_sack = {}
            for token in self.doc:
                if token.pos_ in target_sintagmas:
                    key = func(self,token) # Funcao
                    count_sack[key] = count_sack.get(key, 0) + 1
                
            sorted_sack = dict(sorted(count_sack.items(), 
                                      key=lambda item: item[1],
                                      reverse=True
                                     ))
            return sorted_sack
        return wrapper


    @select_target_sintagmas
    def count_lemma_and_token(self,token):
        return (token.lemma_, token.pos_)


    @select_target_sintagmas
    def count_word(self,token):
        return token.lemma_


class Resume():
    def __init__(self,word_sack,text):
        self.doc = nlp(text)
        for word_name, frequency in word_sack.items():
            add_attribute = self.reduce_sentence(word_name, frequency)
            setattr(self, word_name, add_attribute)

    
    def frequency_token(self,frequency):
        for i in range(1,4):
            limit = i * 3
            if frequency < limit:
                return i
        if i == 3 and frequency >= limit:
            return 4


    def reduce_sentence(self,word_name, frequency):
        lista = []
        limit = self.frequency_token(frequency)
        for item in self.doc.sents:
            if limit == 0:
                return lista
            item_text = item.text
            pattern = re.compile(r'[^\.\!\?,]*?(?={word}){word}.*?(?=[\.\!\?,])'.format(word=word_name))
            match = re.search(pattern, item_text)
            if match:
                lista.append(match.group())
                limit -= 1
        return lista





if __name__ == "__main__":
    from wiki_classes import Clear_bibliography
    text = Clear_bibliography('/wiki/Alan_Turing').content
    tk = Sack_tokens(text).word_sack
    v1 = Resume(tk,text)
    print(v1.trabalho)
