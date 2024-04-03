target_session = ["div", {"id": "bodyContent"}]

target_sintagmas = ["ADJ", "NOUN"]

default_compare = ['Apesar dessas realizações ele nunca foi totalmente reconhecido em seu país de origem durante sua vida por ser homossexual e porque grande parte de seu trabalho foi coberto pela Lei de Segredos Oficiais', 
' Turing trabalhou para a Escola de Código e Cifras do Governo (GC&CS) em Bletchley Park', 
' é difícil estimar o efeito preciso que a inteligência ultra teve na guerra mas foi estimado que este trabalho encurtou a guerra na Europa em mais de dois anos e salvou mais de 14 milhões de vidas', 
'Após a guerra Turing trabalhou no Laboratório Nacional de Física']

bibliography_components ={
     "infobox": {
         "tag": "table",
         "attribute": {"class": "infobox infobox_v2"},
         "method": "extract"
     },
     "nav_box": {
         "tag": "table",
         "attribute": {"class": "vertical-navbox nowraplinks"},
         "method": "extract"
     },
     "navbox_all": {
         "tag": "div",
         "attribute": {"class": "navbox"},
         "method": "extract"
     },
     "reflist": {
         "tag": "div",
         "attribute": {"class": "reflist"},
         "method": "extract"
     },
     "catlinks": {
         "tag": "div",
         "attribute": {"id": "catlinks"},
         "method": "extract"
     },
     "ul_all": {
         "tag": "ul",
         "method": "extract"
     },
     "h1": {
         "tag": "h1",
         "method": "decompose"
     },
     "h2": {
         "tag": "h2",
         "method": "decompose"
     },
     "h3": {
         "tag": "h3",
         "method": "decompose"
     },
     "figure": {
         "tag": "figure",
         "method": "decompose"
     },
     "figcaption": {
         "tag": "figcaption",
         "method": "decompose"
     },
     "sisterproject": {
         "tag": "div",
         "attribute": {"class": "infobox sisterproject"},
         "method": "decompose"
     },
     "printfooter": {
         "tag": "div",
         "attribute": {"class": "printfooter"},
         "method": "decompose"
     },
     "noprint": {
         "tag": "div",
         "attribute": {"class": "noprint"},
         "method": "decompose"
     }
 }

