class Livro:
    def __init__(self, titulo, autor, ano, preço): 
        self.titulo = titulo #"Inclusão_Social"
        self.autor = autor #"Pedro da Costa"
        self.ano = ano #"2020"
        self.preço = preço #"R$150"
    
    def caracteristica_livro(self):
        objeto_titulo =f"\n{self.titulo}"
        objeto_autor =f"\n{self.autor}" 
        objeto_ano =f"\n{self.ano}"
        objeto_preço =f"\n{self.preço}"

        return objeto_titulo + objeto_autor + objeto_ano + objeto_preço
    
livro = Livro("Inclusão_Social", "Pedro da Costa","2020", "R$150")
livro1 = Livro("Amor","Carla Oliveira", "2019", "R$125")

objeto_livro1 = livro.caracteristica_livro()
objeto_livro = livro1.caracteristica_livro()
print(objeto_livro)
print(objeto_livro1)
