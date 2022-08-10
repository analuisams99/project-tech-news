import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)
from tech_news.scraper import get_tech_news


def call_selected_function(option, data):
    options = {
        "0": get_tech_news,
        "1": search_by_title,
        "2": search_by_date,
        "3": search_by_tag,
        "4": search_by_category,
    }
    print(options[option](data))


# Requisito 12
def analyzer_menu():
    options = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a tag:",
        "4": "Digite a categoria:",
        "5": lambda: top_5_news(),
        "6": lambda: top_5_categories(),
        "7": lambda: "Encerrando script",
    }

    print(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )

    try:
        selected_option = input()

        if selected_option not in options or selected_option == "":
            raise ValueError("Opção inválida\n")

        if int(selected_option) > 4:
            print(options[selected_option]())

        else:
            print(options[selected_option])
            response = input()
            call_selected_function(selected_option, response)

    except Exception:
        return print("Opção inválida", file=sys.stderr)
