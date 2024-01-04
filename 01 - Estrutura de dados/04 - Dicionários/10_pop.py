contatos = {"leticiamilan.dev@gmail.com": {"nome": "Leticia", "telefone": "3333-2221"}}

resultado = contatos.pop("leticiamilan.dev@gmail.com")  # {'nome': 'Leticia', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("leticiamilan.dev@gmail.com", {})  # {}
print(resultado)