# ==============================================================
# Script: reports.py
# Descrição: Este arquivo faz parte do sistema de controle da fazenda.
# Ele contém funções e classes para gerenciar entidades e operações específicas.
# ==============================================================

# Importação de módulos necessários
from files import *

# Função responsável por: gerar relatorio
def reports_menu():
    print("\n📊 RELATÓRIO GERAL DA FAZENDA")
    relatorio = {
        # "Animais": load_json("animals.json"),
        "Plantações": load_json("plants.json"),
        # "Insumos": load_json("inputs.json"),
        # "Movimentações": load_json("movements.json")
    }
    for k, v in relatorio.items():
        print(f"\n== {k} ==")
        for item in v:
            print(item)
    save_json("relatorio.json", relatorio)
    print("\n✅ Relatório gerado em 'data/relatorio.json'")

