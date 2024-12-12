#03) Você está desenvolvendo um sistema de controle de estoque para o "Buscante". Um dos requisitos é verificar a quantidade de exemplares de um livro em estoque e continuar vendendo até que o estoque se esgote. Sempre que uma venda é realizada, o sistema deve informar o usuário e atualizar a quantidade disponível. Considere a seguinte variável inicial:
estoque = 5
while estoque > 0:
  print(f"Estoque disponível: {estoque}")
  estoque -= 1
print("Livros vendidos!")
