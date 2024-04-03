import re
import requests
import bs4
from bs4 import BeautifulSoup
from supply import bibliography_components as bibli_components, target_session

class Wiki_pages():
    def __init__(self, url:str):
        self.url = url
        self.__page = self.soup_request()

    def soup_request(self):
        response = requests.get('https://pt.wikipedia.org' + self.url)
        assert response.status_code == 200, f"Erro ao acessar a página. Código de status: {response.status_code}"
        return BeautifulSoup(response.content, 'html.parser')

    def page_content(self):
        return self.__page

    
class Clear_bibliography(Wiki_pages):
    def __init__(self, url:str):
        super().__init__(url)
        self.__raw = self.page_content()
        self.__content = self.__raw.find(*target_session)

        for name_component in bibli_components:
            self.call_clear(name_component)

        self.content = re.sub(r'\[(.*?)\]', '', self.__content.text)
        self.content = re.sub(r'\n+', '\n', self.content)


    def call_clear(self,name_component:str):
        component = bibli_components[name_component]
        
        is_extract = component["method"] == "extract"
        is_decompose = component["method"] == "decompose"
        
        if is_extract:
            add_attribute = self.extract_components(component)
            setattr(self, name_component, add_attribute)
        elif is_decompose:
            self.decompose_component(component)
        else:
            print(f"Método '{component["method"]}' não localizado!")


    def preprocess_component(func):
        def wrapper(self, component:dict):
            if component.get("attribute"):
                elements = self.__content.find_all(component["tag"], component["attribute"])
            else:
                elements = self.__content.find_all(component["tag"])
            if elements:
                return func(self, elements)
        return wrapper


    @preprocess_component
    def extract_components(self, elements:bs4.element.ResultSet):
        return [ext.extract() for ext in elements]


    @preprocess_component
    def decompose_component(self, elements:bs4.element.ResultSet):
        for ext in elements:
            ext.decompose()


if __name__ == '__main__':
    v1 = Clear_bibliography("/wiki/Alan_Turing")
    print(repr(v1.content))



#setattr(self, key, add)