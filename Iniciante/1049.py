arvore = {
           "vertebrado": {"ave": {"carnivoro": "aguia","onivoro": "pomba"},"mamifero": {"onivoro": "homem","herbivoro": "vaca"}},
           "invertebrado": {"inseto": {"hematofago": "pulga","herbivoro": "lagarta"},"anelideo": {"hematofago": "sanguessuga","onivoro": "minhoca"}}
           }

coluna = input()
reino = input()
alimento = input()

print (arvore[coluna][reino][alimento])
