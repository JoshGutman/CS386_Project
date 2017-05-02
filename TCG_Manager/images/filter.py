x = """	Name	Type	Rarity
1/102	Alakazam		Holographic
2/102	Blastoise		Holographic
3/102	Chansey		Holographic
4/102	Charizard		Holographic
5/102	Clefairy		Holographic
6/102	Gyarados		Holographic
7/102	Hitmonchan		Holographic
8/102	Machamp		Holographic
9/102	Magneton		Holographic
10/102	Mewtwo		Holographic
11/102	Nidoking		Holographic
12/102	Ninetales		Holographic
13/102	Poliwrath		Holographic
14/102	Raichu		Holographic
15/102	Venusaur		Holographic
16/102	Zapdos		Holographic
17/102	Beedrill		Rare
18/102	Dragonair		Rare
19/102	Dugtrio		Rare
20/102	Electabuzz		Rare
21/102	Electrode		Rare
22/102	Pidgeotto		Rare
23/102	Arcanine		Uncommon
24/102	Charmeleon		Uncommon
25/102	Dewgong		Uncommon
26/102	Dratini		Uncommon
27/102	Farfetch'd		Uncommon
28/102	Growlithe		Uncommon
29/102	Haunter		Uncommon
30/102	Ivysaur		Uncommon
31/102	Jynx		Uncommon
32/102	Kadabra		Uncommon
33/102	Kakuna		Uncommon
34/102	Machoke		Uncommon
35/102	Magikarp		Uncommon
36/102	Magmar		Uncommon
37/102	Nidorino		Uncommon
38/102	Poliwhirl		Uncommon
39/102	Porygon		Uncommon
40/102	Raticate		Uncommon
41/102	Seel		Uncommon
42/102	Wartortle		Uncommon
43/102	Abra		Common
44/102	Bulbasaur		Common
45/102	Caterpie		Common
46/102	Charmander		Common
47/102	Diglett		Common
48/102	Doduo		Common
49/102	Drowzee		Common
50/102	Gastly		Common
51/102	Koffing		Common
52/102	Machop		Common
53/102	Magnemite		Common
54/102	Metapod		Common
55/102	Nidoran M		Common
56/102	Onix		Common
57/102	Pidgey		Common
58/102	Pikachu		Common
59/102	Poliwag		Common
60/102	Ponyta		Common
61/102	Rattata		Common
62/102	Sandshrew		Common
63/102	Squirtle		Common
64/102	Starmie		Common
65/102	Staryu		Common
66/102	Tangela		Common
67/102	Voltorb		Common
68/102	Vulpix		Common
69/102	Weedle		Common
70/102	Clefairy Doll		Rare
71/102	Computer Search		Rare
72/102	Devolution Spray		Rare
73/102	Imposter Professor Oak		Rare
74/102	Item Finder		Rare
75/102	Lass		Rare
76/102	Pokémon Breeder		Rare
77/102	Pokémon Trader		Rare
78/102	Scoop Up		Rare
79/102	Super Energy Removal		Rare
80/102	Defender		Uncommon
81/102	Energy Retrieval		Uncommon
82/102	Full Heal		Uncommon
83/102	Maintenance		Uncommon
84/102	PlusPower		Uncommon
85/102	Pokémon Center		Uncommon
86/102	Pokémon Flute		Uncommon
87/102	Pokédex		Uncommon
88/102	Professor Oak		Uncommon
89/102	Revive		Uncommon
90/102	Super Potion		Uncommon
91/102	Bill		Common
92/102	Energy Removal		Common
93/102	Gust of Wind		Common
94/102	Potion		Common
95/102	Switch		Common
96/102	Double Colorless Energy		Uncommon
97/102	Fighting Energy		 
98/102	Fire Energy		 
99/102	Grass Energy		 
100/102	Lightning Energy		 
101/102	Psychic Energy		 
102/102	Water Energy"""


x = x.replace("\t\t", "\t")
x = x.replace("\n", "\t")
lst = x.split("\t")

nums = "1234567890/"
avoid = ["", "Common", "Uncommon", "Rare", "Holographic", "Name", "Type", "Rarity", "\n"]

for item in lst:
    if item not in avoid and item[0] not in nums:
        print(item)
