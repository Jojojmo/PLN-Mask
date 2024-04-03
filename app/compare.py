import random
import rich
import random
from complete import complete_sentence


class Compare:
    def __init__(self,sentence) -> None:
        self.sentence = sentence
        self.list_sentence = self.sentence.split()
        self.put_mask()
        self.complete_sentence = complete_sentence(self.mask_sentence)

        self.colors_original_sentence = self.colors_sentence(self.sentence,'red')
        self.colors_mask_sentece = self.colors_sentence(self.mask_sentence,'blue')
        self.colors_complete_sentece = self.colors_sentence(self.complete_sentence,'green')

    def times_mask(self,char=60):
        for i in range(1, 4):
            if len(self.sentence) <= char * i:
                return i
        return i

    def put_mask(self):
        self.index_used = []
        times = self.times_mask() 
        for i in range(times):
            index = random.randint(0, len(self.list_sentence) - 1)
            while index in self.index_used:
                index = random.randint(0, len(self.list_sentence) - 1)
            self.index_used.append(index)
            self.list_sentence[index] = '[MASK]'
        self.mask_sentence = ' '.join(self.list_sentence)


    def colors_sentence(self,sentence,color):
        sentece_split = sentence.split()
        for index in self.index_used:
            sentece_split[index] = f'[{color}]' + sentece_split[index] + '[/]'
        return ' '.join(sentece_split)


    def __str__(self) -> str:
        return f'[bold red]Frase Original:[/] {self.colors_original_sentence}\n[bold blue]Frase [MASK]:[/] {self.colors_mask_sentece}\n[bold green]Frase com Complete:[/] {self.colors_complete_sentece}'




if __name__ == "__main__":

    lista = ['Apesar dessas realizações ele nunca foi totalmente reconhecido em seu país de origem durante sua vida por ser homossexual e porque grande parte de seu trabalho foi coberto pela Lei de Segredos Oficiais', 
    ' Turing trabalhou para a Escola de Código e Cifras do Governo (GC&CS) em Bletchley Park', 
    ' é difícil estimar o efeito preciso que a inteligência ultra teve na guerra mas foi estimado que este trabalho encurtou a guerra na Europa em mais de dois anos e salvou mais de 14 milhões de vidas', 
    'Após a guerra Turing trabalhou no Laboratório Nacional de Física']

    item_a = lista[0].strip().capitalize()
    rich.print(Compare(item_a).__str__())
