import random

# --------------------------
# Nodes (123 total)
# --------------------------
nodes = {

    "Frodo": "Hobbit",
    "Sam": "Hobbit",
    "Merry": "Hobbit",
    "Pippin": "Hobbit",
    "Gandalf": "Wizard",
    "Aragorn": "Human",
    "Boromir": "Human",
    "Legolas": "Elf",
    "Gimli": "Dwarf",
    "Gollum": "Creature",
    "Saruman": "Wizard",
    "Elrond": "Elf",
    "Galadriel": "Elf",

    "The Shire": "Location",
    "Rivendell": "Location",
    "Moria": "Location",
    "Lothlorien": "Location",
    "Mordor": "Location",
    "Isengard": "Location",
    "Gondor": "Location",
    "Rohan": "Location",

    "The One Ring": "Artifact",
    "Sting": "Artifact",
    "Glamdring": "Artifact",

    "Bilbo": "Hobbit",
    "Théoden": "Human",
    "Éowyn": "Human",
    "Éomer": "Human",
    "Faramir": "Human",
    "Denethor": "Human",
    "Treebeard": "Ent",
    "Shelob": "Creature",
    "Sauron": "Dark Lord",
    "Gríma Wormtongue": "Human",
    "Arwen": "Elf",
    "Rosie Cotton": "Hobbit",
    "Balin": "Dwarf",
    "Radagast": "Wizard",

    "Helm's Deep": "Location",
    "Minas Tirith": "Location",
    "Barad-dûr": "Location",
    "Mount Doom": "Location",
    "Dead Marshes": "Location",
    "Fangorn Forest": "Location",
    "Bree": "Location",
    "Weathertop": "Location",
    "Osgiliath": "Location",

    "Andúril": "Artifact",
    "Palantír": "Artifact",
    "Phial of Galadriel": "Artifact",
    "Horn of Gondor": "Artifact",
    "Mithril Coat": "Artifact",
    "White Tree": "Artifact",
    "Black Arrow": "Artifact",

    "Glorfindel": "Elf",
    "Barliman Butterbur": "Human",
    "Tom Bombadil": "Mystery",
    "Goldberry": "Mystery",
    "Gothmog": "Orc",
    "Mouth of Sauron": "Creature",
    "Isildur": "Human",
    "Elendil": "Human",
    "Anárion": "Human",
    "Círdan": "Elf",
    "Beregond": "Human",
    "Haldir": "Elf",
    "Gamling": "Human",
    "Halbarad": "Human",
    "Shagrat": "Orc",
    "Gorbag": "Orc",

    "Grey Havens": "Location",
    "Dol Guldur": "Location",
    "Emyn Muil": "Location",
    "Anduin": "Location",
    "Pelennor Fields": "Location",
    "Caras Galadhon": "Location",
    "Tol Eressëa": "Location",
    "Dagorlad": "Location",
    "Númenor": "Location",
    "Erebor": "Location",
    "Lake-town": "Location",

    "Narsil": "Artifact",
    "Elendilmir": "Artifact",
    "Ring of Barahir": "Artifact",
    "Sword of Éowyn": "Artifact",
    "Stone of Erech": "Artifact",
    "Aeglos": "Artifact",
    "Red Arrow": "Artifact",
    "Keys of Barad-dûr": "Artifact",

    # Factions
    "Orcs of Mordor": "Faction",
    "Uruk-hai": "Faction",
    "Nazgûl": "Faction",
    "Dead Men of Dunharrow": "Faction",
    "Rangers of the North": "Faction",
    "Army of the West": "Faction",
    "Haradrim": "Faction",
    "Easterlings": "Faction",

    "Beorn": "Skin-changer",
    "Bard the Bowman": "Human",
    "Thranduil": "Elf",
    "Dáin Ironfoot": "Dwarf",
    "Azog": "Orc",
    "Bolg": "Orc",
    "Kili": "Dwarf",
    "Fili": "Dwarf",
    "Thorin Oakenshield": "Dwarf",
    "Gwaihir": "Eagle",
    "Landroval": "Eagle",
    "Smaug": "Dragon",

    "Esgaroth": "Location",
    "Beorn's House": "Location",
    "Iron Hills": "Location",
    "Thranduil's Halls": "Location",
    "Mount Gundabad": "Location",
    "Blue Mountains": "Location",
    "Forlindon": "Location",
    "Ettenmoors": "Location",

    "Arkenstone": "Artifact",
    "Black Sword of Túrin": "Artifact",
    "Three Elven Rings": "Artifact",
    "Crown of Gondor": "Artifact",
    "White Knife": "Artifact",
    "Durin's Axe": "Artifact",
}




def generate_semantic_relationships(nodes, target_count):
    # Map types to node names
    type_to_nodes = defaultdict(list)
    for name, ntype in nodes.items():
        type_to_nodes[ntype].append(name)

    schema = {
        "FRIENDS_WITH": ("Human", "Human"),
        "ENEMIES_WITH": ("Human", "Orc"),
        "TRAVELS_TO": ("Human", "Location"),
        "RULES": ("Human", "Location"),
        "LIVES_IN": ("Hobbit", "Location"),
        "BATTLES": ("Faction", "Faction"),
        "KIN_OF": ("Human", "Human"),
        "MENTORS": ("Wizard", "Human"),
        "FOLLOWS": ("Human", "Wizard"),
        "BETRAYS": ("Orc", "Human"),
        "PROTECTS": ("Human", "Hobbit"),
        "SEEKS": ("Creature", "Artifact"),
        "GUARDS": ("Human", "Location"),
        "WIELDS": ("Human", "Artifact"),
        "POSSESSES": ("Creature", "Artifact"),
        "CREATED_BY": ("Artifact", "Dark Lord"),
        "CONNECTED_TO": ("Location", "Location"),
        "BELONGS_TO": ("Artifact", "Faction"),
        "ALLY_OF": ("Faction", "Faction"),
        "CONTROLS": ("Wizard", "Faction")
    }

    relationships = []
    seen = set()

    while len(relationships) < target_count:
        rel_type, (src_type, tgt_type) = random.choice(list(schema.items()))
        src_candidates = type_to_nodes.get(src_type, [])
        tgt_candidates = type_to_nodes.get(tgt_type, [])

        if not src_candidates or not tgt_candidates:
            continue

        source = random.choice(src_candidates)
        target = random.choice(tgt_candidates)
        key = (source, target, rel_type)

        if source != target and key not in seen:
            relationships.append((source, target, rel_type, {"notes": random.choice(["ancient", "strong", "hidden"])}) )
            seen.add(key)

    return relationships

relationships = generate_semantic_relationships(nodes, 242)
