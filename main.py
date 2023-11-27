import sqlite3
import os
import time

DATABASE_FILE = "instituicoes.db"


# Limpa a tela para diferentes sistemas operacionais
def clear_screen():
    if os.name == "nt":
        os.system("cls")
        time.sleep(1)
    else:
        os.system("clear")
        time.sleep(1)


# Lê registros do banco de dados
def read_records_from_db():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM instituicoes ORDER BY preco")
    records = cursor.fetchall()

    conn.close()
    return records


# Exibe os registros com uma pausa para melhor visualização
def print_records(records):
    clear_screen()
    time.sleep(1)
    if not records:
        print("Nenhum registro encontrado.")
    else:
        print("\nRegistros de cursos de GTI no Recife:")
        print("{:<5} {:<20} {:<15} {:<10}".format("ID", "Nome", "Preço", "Avaliação"))
        print("-" * 60)
        for record in records:
            record_id, name, price, rating = record
            stars = "⭐️" * int(rating) if rating else "-"
            print("{:<5} {:<20} R$ {:<15} {}".format(record_id, name, price, stars))

    input("\nPressione Enter para continuar...")
    clear_screen()


# Avalia uma instituição
def evaluate_institution():
    clear_screen()
    time.sleep(1)
    print_records(read_records_from_db())
    try:
        record_id = int(input("Digite o ID da instituição que deseja avaliar: "))
        rating = float(input("Digite a avaliação (de 1 a 5): "))

        if 1 <= rating <= 5:
            conn = sqlite3.connect(DATABASE_FILE)
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE instituicoes SET avaliacao = ? WHERE id = ?",
                (rating, record_id),
            )

            conn.commit()
            conn.close()
            print("Avaliação registrada com sucesso!")
        else:
            print("Avaliação inválida. Deve ser um valor entre 1 e 5.")
    except ValueError:
        print("ID ou avaliação inválidos. Certifique-se de inserir números válidos.")
    except sqlite3.DatabaseError:
        print("Erro ao avaliar.")
    except Exception:
        print("Erro desconhecido.")
    finally:
        input("Pressione Enter para continuar...")
        clear_screen()


# Adiciona uma nova instituição
def add_institution():
    clear_screen()
    time.sleep(1)
    print_records(read_records_from_db())
    try:
        name = input("Digite o nome da nova instituição: ")
        price = float(input("Digite o preço: "))

        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO instituicoes (nome, preco, avaliacao) VALUES (?, ?, ?)",
            (name, price, None),
        )

        conn.commit()
        conn.close()
        print("Instituição adicionada com sucesso!")
    except ValueError:
        print("Preço inválido. Certifique-se de inserir um número válido.")
    except sqlite3.IntegrityError:
        print("Valor duplicado.")
    except sqlite3.DatabaseError:
        print("Erro ao inserir registro.")
    except Exception:
        print("Erro desconhecido.")
    finally:
        input("Pressione Enter para continuar...")
        clear_screen()


# Atualiza uma instituição
def update_institution():
    clear_screen()
    time.sleep(1)
    print_records(read_records_from_db())
    try:
        record_id = int(input("Digite o ID da instituição que deseja atualizar: "))
        field_to_update = input("Digite o campo que deseja atualizar (nome/preco): ")

        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        if field_to_update == "nome":
            new_name = input("Digite o novo nome: ")
            cursor.execute(
                "UPDATE instituicoes SET nome = ? WHERE id = ?",
                (new_name, record_id),
            )
        elif field_to_update == "preco":
            new_price = float(input("Digite o novo preço: "))
            cursor.execute(
                "UPDATE instituicoes SET preco = ? WHERE id = ?",
                (new_price, record_id),
            )
        else:
            print("Campo inválido.")

        conn.commit()
        conn.close()
        print("Registro atualizado com sucesso!")
    except ValueError:
        print("ID inválido ou valor incorreto inserido.")
    except sqlite3.OperationalError:
        print("Campo inválido.")
    except sqlite3.IntegrityError:
        print("Valor duplicado.")
    except sqlite3.DatabaseError:
        print("Erro ao atualizar registro.")
    except Exception:
        print("Erro desconhecido.")
    finally:
        input("Pressione Enter para continuar...")
        clear_screen()


# Deleta uma instituição
def delete_institution():
    clear_screen()
    time.sleep(1)
    print_records(read_records_from_db())
    try:
        record_id = int(input("Digite o ID da instituição que deseja excluir: "))

        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM instituicoes WHERE id = ?", (record_id,))

        conn.commit()
        conn.close()
        print("Instituição excluída com sucesso!")
    except ValueError:
        print("ID inválido. Certifique-se de inserir um número válido.")
    except sqlite3.DatabaseError:
        print("Erro ao excluir registro.")
    except Exception:
        print("Erro desconhecido.")
    finally:
        input("Pressione Enter para continuar...")
        clear_screen()


# Imprime padrão ASCII UniCompare
def print_ascii_pattern():
    print(
        """
   _   _       _ _____                                          ____   
  | | | |     (_)  __ \                                        / /\ \  
  | | | |_ __  _| /  \/ ___  _ __ ___  _ __   __ _ _ __ ___   / /  \ \ 
  | | | | '_ \| | |    / _ \| '_ ` _ \| '_ \ / _` | '__/ _ \ < <    > >
  | |_| | | | | | \__/\ (_) | | | | | | |_) | (_| | | |  __/  \ \  / / 
   \___/|_| |_|_|\____/\___/|_| |_| |_| .__/ \__,_|_|  \___|   \_\/_/  
                                      | |                              
                                      |_|                              

    Seu futuro não se compara.
    """
    )


# Função principal do programa
def main():
    while True:
        clear_screen()
        print_ascii_pattern()
        time.sleep(1)
        print("Opções:")
        print("1. Adicionar Registro")
        print("2. Exibir Registros (ordenados por preço)")
        print("3. Atualizar Registro")
        print("4. Excluir Registro")
        print("5. Sair")
        print("6. Avaliar Instituição")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            add_institution()
            time.sleep(1)
        elif choice == "2":
            print_records(read_records_from_db())
            time.sleep(1)
        elif choice == "3":
            update_institution()
            time.sleep(1)
        elif choice == "4":
            delete_institution()
            time.sleep(1)
        elif choice == "5":
            time.sleep(1)
            print("Saindo do programa.")
            time.sleep(2)
            break
        elif choice == "6":
            evaluate_institution()
            time.sleep(1)
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")


# Executa o programa
if __name__ == "__main__":
    main()
