from typing import Dict, List, Any


def answer(list_monster : List[Dict[str, Any]]):
    for monster in filter(lambda x : x['level'] >= 20, list_monster):
        print(monster['name'])