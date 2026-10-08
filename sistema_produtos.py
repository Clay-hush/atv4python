produtos = []

print("=== CADASTRO DE PRODUTOS ===")

while True:
    try:
        quantidade_produtos = int(input("Quantos produtos deseja cadastrar? "))
        if quantidade_produtos >= 0:
            break
        else:
            print("Por favor, digite um número maior ou igual a zero.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro válido.")

for indice in range(quantidade_produtos):
    print(f"\nProduto {indice + 1}")
    nome = input("Nome: ")
    
    while True:
        try:
            preco = float(input("Preço: R$ "))
            break
        except ValueError:
            print("Preço inválido! Digite um valor numérico.")
            
    categoria = input("Categoria: ")

    produto = {"nome": nome, "preco": preco, "categoria": categoria}
    produtos.append(produto)

if quantidade_produtos > 0:
    while True:
        try:
            valor_filtro = float(input("\nInforme um valor para filtrar: "))
            break
        except ValueError:
            print("Valor inválido! Digite um valor numérico para o filtro.")

    produtosacima = []
    produtosabaixo = []

    for produto in produtos:
        if produto["preco"] > valor_filtro:
            produtosacima.append(produto)
        if produto["preco"] < valor_filtro:
            produtosabaixo.append(produto)

    produtos_crescente = produtos.copy()
    produtos_crescente.sort(key=lambda produto: produto["preco"])

    produtos_decrescente = sorted(produtos, key=lambda produto: produto["preco"], reverse=True)

    categorias = []
    for produto in produtos:
        categorias.append(produto["categoria"])

    categorias_unicas = set(categorias)

    precos = []
    for produto in produtos:
        precos.append(produto["preco"])

    if len(precos) > 0:
        menorpreco = min(precos)
        maiorpreco = max(precos)
        media_precos = sum(precos) / len(precos)
        estatisticas = (menorpreco, maiorpreco, media_precos)
    else:
        estatisticas = (0, 0, 0)

    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL")
    print("=" * 60)

    print("\nPRODUTOS CADASTRADOS:")
    for produto in produtos:
        print(f"Nome: {produto['nome']} | Preço: R$ {produto['preco']:.2f} | Categoria: {produto['categoria']}")

    print(f"\nPRODUTOS ACIMA DE R$ {valor_filtro:.2f}:")
    if produtosacima:
        for produto in produtosacima:
            print(f"- {produto['nome']}: R$ {produto['preco']:.2f}")
    else:
        print("Nenhum produto encontrado.")

    print(f"\nPRODUTOS ABAIXO DE R$ {valor_filtro:.2f}:")
    if produtosabaixo:
        for produto in produtosabaixo:
            print(f"- {produto['nome']}: R$ {produto['preco']:.2f}")
    else:
        print("Nenhum produto encontrado.")

    print("\nPRODUTOS EM ORDEM CRESCENTE:")
    for produto in produtos_crescente:
        print(f"- {produto['nome']}: R$ {produto['preco']:.2f}")

    print("\nPRODUTOS EM ORDEM DECRESCENTE:")
    for produto in produtos_decrescente:
        print(f"- {produto['nome']}: R$ {produto['preco']:.2f}")

    print("\nCATEGORIAS ÚNICAS:")
    for categoria in categorias_unicas:
        print(f"- {categoria}")

    print("\nESTATÍSTICAS:")
    print(f"Menor preço: R$ {estatisticas[0]:.2f}")
    print(f"Maior preço: R$ {estatisticas[1]:.2f}")
    print(f"Média dos preços: R$ {estatisticas[2]:.2f}")

    print("\n" + "=" * 60)
    print("FIM DO RELATÓRIO")
    print("=" * 60)
else:
    print("\nNenhum produto foi cadastrado. Fim do programa.")
