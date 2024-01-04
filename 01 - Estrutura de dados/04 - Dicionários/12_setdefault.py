contato = {"nome": "Leticia", "telefone": "3333-2221"}

contato.setdefault("nome", "João Vitor")  # "João Vitor"
print(contato)  # {'nome': 'Leticia', 'telefone': '3333-2221'}

contato.setdefault("idade", 21)  # 21
print(contato)  # {'nome': 'Leticia', 'telefone': '3333-2221', 'idade': 21}