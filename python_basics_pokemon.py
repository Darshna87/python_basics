def pokemonfun(numbers):

    pokemon = {
        1: "pokemon",
        2: "picachu",
        3: "sabasaur"
    }
    for i in numbers:
        if pokemon.get(i) is None:
            print("pokemon not found")
        else:
            print(pokemon[i])


numbers_list = [int(x) for x in input().split()]

print(numbers_list)
pokemonfun(numbers_list)
