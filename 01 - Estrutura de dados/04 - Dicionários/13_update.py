contatos = {"leticiamilan.dev@gmail.com": {"nome": "Leticia", "telefone": "3333-2221"}}

contatos.update({"leticiamilan.dev@gmail.com": {"nome": "Le"}})
print(contatos)  # {'leticiamilan.dev@gmail.com': {'nome': 'Le'}}

contatos.update({"joaovitormine@gmail.com": {"nome": "João Vitor", "telefone": "3322-8181"}})
# {'leticiamilan.dev@gmail.com': {'nome': 'Le'}, 'joaovitormine@gmail.com': {'nome': 'João Vitor', 'telefone': '3322-8181'}}
print(contatos)