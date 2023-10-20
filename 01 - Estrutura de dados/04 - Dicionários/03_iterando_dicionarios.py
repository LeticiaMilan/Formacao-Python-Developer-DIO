contatos = {
    "leticiamilan.dev@gmail.com": {"nome": "Letícia", "telefone": "3333-2221"},
    "joaovitor@gmail.com": {"nome": "João Vitor", "telefone": "3443-2121"},
    "larissa@gmail.com": {"nome": "Larissa", "telefone": "3344-9871"},
    "henrique@gmail.com": {"nome": "Henrique", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)