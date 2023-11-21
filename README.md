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

## Como Executar

Certifique-se de ter o Python instalado no seu sistema. Clone o repositório e execute o script Python `main.py` no prompt de comando.

```bash
python main.py
```

Siga as instruções no prompt para interagir com o sistema.

## Variáveis e Tipos:

- `DATABASE_FILE`: String. Nome do arquivo para armazenar registros.
- `data`: Lista de strings. Armazena os registros.
- `record`, `new_record`: String. Novos registros a serem criados ou atualizados.
- `record_id`: Inteiro. ID do registro a ser atualizado ou excluído.
- `record_data`: Lista de strings. Divisão do registro em nome e preço.

## Funções:

- `create_record(data: List[str], record: str) -> None`: Cria um novo registro com base na entrada.
- `read_records(data: List[str]) -> None`: Exibe todos os registros ordenados por preço.
- `update_record(data: List[str], record_id: int, new_record: str) -> None`: Atualiza um registro existente.
- `delete_record(data: List[str], record_id: int) -> None`: Exclui um registro existente.
- `save_to_file(data: List[str]) -> None`: Salva os registros em um arquivo.
- `load_from_file() -> List[str]`: Carrega os registros de um arquivo.

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
- [ ] Realizar entrevistas
- [x] Corrigir erro de linha vazia no database.txt
- [x] Corrigir erro de variável Y no database.txt
- [x] Adicionar mais dados ao database.txt
- [x] Corrigir erro de "ã".
