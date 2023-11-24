# Nome do arquivo para armazenar os registros
DATABASE_FILE = "database.txt"


# Função para criar um novo registro
def create_record(data, record):
    record_data = record.split(",")

    # Verifica se a entrada contém dois elementos separados por vírgula
    if len(record_data) != 2 or not record_data[1].strip():
        print("Formato de entrada inválido. Use o formato 'nome, preço'.")
        return

    # Tenta converter o segundo elemento para um número decimal (preço)
    try:
        float(record_data[1].strip())
    except ValueError:
        print("O preço deve ser um número válido.")
        return

    data.append(record)
    save_to_file(data)
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
        save_to_file(data)
        print("Registro atualizado com sucesso!")
    else:
        print("ID de registro inválido.")


# Função para excluir um registro existente
def delete_record(data, record_id):
    if 0 <= record_id < len(data):
        deleted_record = data.pop(record_id)
        save_to_file(data)
        print(f"Registro excluído com sucesso: {deleted_record}")
    else:
        print("ID de registro inválido.")


# Função para salvar os registros em um arquivo
def save_to_file(data):
    sorted_data = sorted(data, key=lambda x: float(x.split(",")[1]))

    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(sorted_data))


# Função para ler os registros de um arquivo
def load_from_file():
    data = []
    try:
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if (
                    line
                ):  # Verifica se a linha não está em branco antes de adicionar aos dados
                    data.append(line)
    except FileNotFoundError:
        print(f"Arquivo '{DATABASE_FILE}' não encontrado.")
    except EOFError:
        print("Erro ao ler o arquivo: End of File (EOF) alcançado.")
    return data


# Função principal
def main():
    database = load_from_file()

    while True:
        print("\nOpções:")
        print("1. Adicionar Registro")
        print("2. Exibir Registros (ordenados por preço)")
        print("3. Atualizar Registro")
        print("4. Excluir Registro")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            record = input("Digite o novo registro (nome, preço): ")
            create_record(database, record)
            database = load_from_file()
        elif choice == "2":
            read_records(database)
        elif choice == "3":
            try:
                record_id = int(input("Digite o ID do registro a ser atualizado: "))
                new_record = input("Digite o novo registro (nome, preço): ")
                update_record(database, record_id, new_record)
                database = load_from_file()
            except ValueError:
                print(
                    "ID de registro inválido. Certifique-se de inserir um número válido."
                )
        elif choice == "4":
            try:
                record_id = int(input("Digite o ID do registro a ser excluído: "))
                delete_record(database, record_id)
            except ValueError:
                print(
                    "ID de registro inválido. Certifique-se de inserir um número válido."
                )
                database = load_from_file()
        elif choice == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
