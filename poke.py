import json
import os
import datetime

class Database:
    def __init__(self, data):
        self.data = data

    def query(self, condition):
        return [entry for entry in self.data if condition(entry)]

class Pokedex:
    def __init__(self, database):
        self.database = database

    def writeAJson(self, data, filename):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filepath = f"{filename}_{timestamp}.json"
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Log saved to {filepath}")

    def get_pokemon_by_type(self, poke_type):
        result = self.database.query(lambda p: poke_type in p.get('type', []))
        self.writeAJson(result, 'pokemon_by_type')
        return result

    def get_pokemon_by_name(self, name):
        result = self.database.query(lambda p: p.get('name', '').lower() == name.lower())
        self.writeAJson(result, 'pokemon_by_name')
        return result

    def get_pokemon_by_generation(self, generation):
        result = self.database.query(lambda p: p.get('generation') == generation)
        self.writeAJson(result, 'pokemon_by_generation')
        return result

    def get_pokemon_by_hp_range(self, min_hp, max_hp):
        result = self.database.query(lambda p: min_hp <= p.get('hp', 0) <= max_hp)
        self.writeAJson(result, 'pokemon_by_hp_range')
        return result

    def get_legendary_pokemon(self):
        result = self.database.query(lambda p: p.get('is_legendary', False))
        self.writeAJson(result, 'legendary_pokemon')
        return result

# Exemplo de como utilizar as classes
if __name__ == "__main__":
    # Exemplo de dados do banco de dados
    sample_data = [
        {"name": "Bulbasaur", "type": ["Grass", "Poison"], "generation": 1, "hp": 45, "is_legendary": False},
        {"name": "Mewtwo", "type": ["Psychic"], "generation": 1, "hp": 106, "is_legendary": True},
        {"name": "Pikachu", "type": ["Electric"], "generation": 1, "hp": 35, "is_legendary": False},
        # Adicione mais Pokémon aqui...
    ]

    db = Database(sample_data)
    pokedex = Pokedex(db)

    # Exemplos de uso
    pokedex.get_pokemon_by_type("Grass")
    pokedex.get_pokemon_by_name("Pikachu")
    pokedex.get_pokemon_by_generation(1)
    pokedex.get_pokemon_by_hp_range(30, 50)
    pokedex.get_legendary_pokemon()
