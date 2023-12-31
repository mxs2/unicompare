# UniCompare - Seu futuro não se compara

<p align="center">
<a href=""><img src="docs/resources/logo.png" alt="Logotipo do UniCompare." width=350px"></a>
</p>

<p align="center">
<a href="docs/README_EN.md">English</a> | <a href="./README.md">Português</a>
</p>

## Descrição

UniCompare é um projeto desenvolvido como parte da disciplina de Projetos no curso de Gestão de Tecnologia da Informação na Cesar School. Este sistema permite que usuários realizem operações básicas de CRUD (Criar, Ler, Atualizar, Excluir) em registros universitários, como nomes de cursos e preços.

## Fluxograma

<p align="center" style="border: 1px solid #333; background-color: white;">
  <a href="">
    <img src="./docs/resources/fluxograma.svg" alt="Fluxograma Unicompare">
  </a>
</p>

## Recursos

UniCompare oferece os seguintes recursos:

1. **Adicionar Registro:** Permite que usuários adicionem novos registros, incluindo o nome do curso e o preço.

2. **Exibir Registros (Ordenados por Preço):** Apresenta todos os registros existentes, ordenados por preço em ordem crescente.

3. **Atualizar Registro:** Permite a atualização de um registro existente fornecendo o ID do registro e os novos dados.

4. **Excluir Registro:** Permite a exclusão de um registro existente com base no ID fornecido.

5. **Avaliar Instituição:** Permite avaliar uma instituição existente com base no ID fornecido.

## Como Executar

Certifique-se de ter o Python instalado no seu sistema. Clone o repositório e execute o script Python `main.py` no prompt de comando.

```bash
python main.py
```

Siga as instruções no prompt para interagir com o sistema.

## Variáveis e Tipos:

- `DATABASE_FILE`: String. Nome do arquivo do banco de dados (utilizando SQLite3) para armazenar registros.
- `data`: Lista de strings. Armazena os registros carregados na memória durante a execução.
- `record`, `new_record`: String. Novos registros a serem criados ou atualizados no banco de dados.
- `record_id`: Inteiro. ID do registro a ser atualizado ou excluído no banco de dados.
- `record_data`: Lista de strings. Divisão do registro em nome e preço.

## Funções:

- `clear_screen() -> None`: Limpa a tela para diferentes sistemas operacionais.
- `read_records_from_db() -> List[str]`: Lê registros do banco de dados e retorna uma lista de registros.
- `print_records(records: List[str]) -> None`: Exibe os registros formatados na tela.
- `evaluate_institution() -> None`: Avalia uma instituição presente no banco de dados.
- `add_institution() -> None`: Adiciona uma nova instituição ao banco de dados.
- `delete_institution() -> None`: Deleta uma instituição do banco de dados.
- `print_ascii_pattern() -> None`: Imprime o padrão ASCII do UniCompare.
- `main() -> None`: Função principal do programa que controla o fluxo de execução.

O `DATABASE_FILE` é utilizado como um arquivo de banco de dados SQLite3 para armazenar e gerenciar os registros do sistema UniCompare. Isso permite a manipulação eficiente de dados e consultas por meio da biblioteca `sqlite3` do Python.

## Contribuições

Contribuições são bem-vindas! Se encontrar problemas ou tiver sugestões de melhoria, por favor, abra um problema neste repositório.

## Desenvolvedores

- mxs2@cesar.school
- vrln2@cesar.school
- jhrbfl@cesar.school
- cfcl@cesar.school
- bag@cesar.school
- tmf2@cesar.school
- cjam@cesar.school

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Lista de Tarefas

- [x] Realizar os primeiros testes do protótipo
- [x] Realizar entrevistas
- [x] Corrigir erro de linha vazia no database.txt
- [x] Corrigir erro de variável Y no database.txt
- [x] Adicionar mais dados ao database.txt
- [x] Corrigir erro de UTF-8
- [x] Adicionar função de avaliação
- [x] Utilizar um banco de dados ao invés de um arquivo de texto.
