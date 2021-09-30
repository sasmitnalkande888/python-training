person1 = {
    'name': 'bruno',
    'age': '20'
}
person2 = {
    'name': 'vitor',
    'age': '18'
}
people = [person1, person2]
for person in people:
    print(f"Name:{person['name']}")
    print(f"Age:{person['age']}")

print("\n")

favorite_places = {
    'bruno': ['brasil', 'australia'],
    'vitor': ['china', 'japan']
}

for name, places in favorite_places.items():
    print(f"Name: {name}")
    for place in places:
        print(f"{place}")


print("\n")

cities = {
    'indaiatuba': {
        'country': 'brazil',
        'population': 100_000,
        'fact': 'good citie'
    },
    'salto': {
        'country': 'brazil',
        'population': 200_000,
        'fact': 'bad citie'
    }
}

for citie , infos in cities.items():
    print(f"Name:{citie.title()}")
    data_info = f"{infos['country'].title()} | {infos['population']} | {infos['fact']}"
    print(data_info)
