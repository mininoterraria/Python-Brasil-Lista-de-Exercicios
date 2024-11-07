#01) Você está desenvolvendo seu portfólio para exibir seus projetos de Python. Cada projeto está listado em uma seção específica, mas alguns itens podem não estar disponíveis, aparecendo como None na lista. Para garantir que a exibição dos projetos seja clara e sem erros, você precisa verificar se cada item da lista possui um valor válido antes de exibi-lo.
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
for projeto in projetos:
  if projeto:
    print(f"Nome do projeto: {projeto}")
  else:
    print("Projeto não disponível!")
