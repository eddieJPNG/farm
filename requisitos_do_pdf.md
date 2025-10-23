# Universidade Estadual do Piauí - UESPI  
## Curso de Tecnologia em Sistemas de Computação  
**Disciplina:** Algoritmos e Programação Estruturada  
**Professor:** Eyder Rios  

---

# 🧮 2ª AVALIAÇÃO - TRABALHO DE IMPLEMENTAÇÃO  
## SISTEMA DE CONTROLE DE INVENTÁRIO DE UMA FAZENDA DIGITAL  

---

## 1. OBJETIVO GERAL  
Desenvolver um sistema de software de média complexidade que realize o cadastro, monitoramento e controle de recursos de uma fazenda digital, utilizando a linguagem **Python 3**.  
O sistema deverá permitir o gerenciamento de **animais, plantações e insumos**, aplicando os conceitos de **estruturas de dados, manipulação de arquivos, funções, módulos, tratamento de erros e geração de relatórios ordenados**.  

---

## 2. DIRETRIZES GERAIS  
- Trabalho em equipes de até **4 alunos**.  
- Todos devem **contribuir e compreender** o sistema.  
- A identificação completa (nome e matrícula) deve constar:  
  - No arquivo principal (`main.py`), em forma de **comentário no início do código**;  
  - Em um arquivo obrigatório chamado **README**, contendo os nomes completos.  

O arquivo **README** servirá como identificação formal da equipe e será utilizado para fins de registro e avaliação.  

---

## 3. REQUISITOS DO SISTEMA  

### 3.1 Requisitos Funcionais  
O sistema deverá ser capaz de:

1. **Cadastrar Animais**  
   - Inserir dados como ID, espécie, peso e idade.  
   - Marcar o status do animal (ativo, vendido ou falecido).  

2. **Cadastrar Plantações**  
   - Registrar tipo de cultura, área (ha) e data de plantio.  
   - Calcular automaticamente a data estimada de colheita.  

3. **Gerenciar Insumos**  
   - Cadastrar insumos (ração, sementes, fertilizantes, medicamentos).  
   - Controlar o estoque (entrada e saída).  
   - Impedir saídas superiores à quantidade disponível.  

4. **Registrar Movimentações**  
   - Registrar operações como venda de animal, colheita e consumo de insumo.  
   - Associar data e descrição textual.  

5. **Gerar Relatórios**  
   - Relatório geral dos animais, plantações e insumos.  
   - Ordenar por Nome/ID (A–Z), Quantidade (↓), Status (ativo, colhido, etc).  
   - Salvar relatório em `report.txt` com:  
     - Cabeçalho com data e hora  
     - Totais por categoria  

6. **Pesquisar Registros**  
   - Localizar animais, plantações ou insumos pelo ID ou nome.  

7. **Persistir e Recuperar Dados**  
   - Usar arquivos JSON (`animals.json`, `plants.json`, `inputs.json`, `movements.json`).  
   - Carregar dados ao iniciar e salvar ao encerrar o sistema.  

8.
