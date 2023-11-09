# Função para criar um novo registro
def create_record(data, record):
    data.append(record)
    print("Registro adicionado com sucesso!")


# Função para exibir todos os registros ordenados por preço
def read_records(data):
    if not data:
        print("Nenhum registro encontrado.")
    else:
        print("\nRegistros:")
        print("{:<5} {:<20} {:<10}".format("ID", "Nome", "Preço"))
        print("-" * 40)
        sorted_data = sorted(data, key=lambda x: float(x.split(",")[1]))
        for i, record in enumerate(sorted_data):
            name, price = record.split(",")
            print("{:<5} {:<20} {:<10}".format(i, name, price))


# Função para atualizar um registro existente
def update_record(data, record_id, new_record):
    if 0 <= record_id < len(data):
        data[record_id] = new_record
        print("Registro atualizado com sucesso!")
    else:
        print("ID de registro inválido.")


# Função para excluir um registro existente
def delete_record(data, record_id):
    if 0 <= record_id < len(data):
        deleted_record = data.pop(record_id)
        print(f"Registro excluído com sucesso: {deleted_record}")
    else:
        print("ID de registro inválido.")


# Função principal
def main():
    database = []

    while True:
        print("\nOpções:")
        print("1. Adicionar Registro")
        print("2. Exibir Registros (ordenados por preço de universidade)")
        print("3. Atualizar Registro")
        print("4. Excluir Registro")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            record = input("Digite o novo registro (nome, preço): ")
            create_record(database, record)
        elif choice == "2":
            read_records(database)
        elif choice == "3":
            record_id = int(input("Digite o ID do registro a ser atualizado: "))
            new_record = input("Digite o novo registro (nome, preço): ")
            update_record(database, record_id, new_record)
        elif choice == "4":
            record_id = int(input("Digite o ID do registro a ser excluído: "))
            delete_record(database, record_id)
        elif choice == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
