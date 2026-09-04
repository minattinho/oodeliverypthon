class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._situacao = False
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f' - {self.nome} | {self.categoria} | {self.situacao}'
    
    def listar_restaurantes():
        print('Restaurantes cadastrados: ')
        for restaurante in Restaurante.restaurantes:
            print(f'- {restaurante.nome} | {restaurante.categoria} | {restaurante.situacao}')

    @property
    def situacao(self):
        return 'Ativo' if self._situacao else 'Desativado'
    
    
restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pizza = Restaurante('Pizza express','Pizzaria')

Restaurante.listar_restaurantes()
