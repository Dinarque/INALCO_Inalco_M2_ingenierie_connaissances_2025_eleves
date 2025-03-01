
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
        "Rohan": "Location"  ,
        "The One Ring": "Artifact",
        "Sting": "Artifact",
        "Glamdring": "Artifact"
    }
    

    

relationships = [
        # Fellowship connections
        ("Frodo", "Sam", "FRIENDS_WITH", {"loyalty": "unbreakable"}),
        ("Frodo", "Merry", "FRIENDS_WITH", {"since": "childhood"}),
        ("Frodo", "Pippin", "FRIENDS_WITH", {"since": "childhood"}),
        ("Frodo", "Gandalf", "GUIDED_BY", {"trust": "high"}),
        ("Sam", "Gandalf", "RESPECTS", {}),
        ("Aragorn", "Legolas", "FRIENDS_WITH", {"trust": "high"}),
        ("Aragorn", "Gimli", "FRIENDS_WITH", {"trust": "high"}),
        ("Legolas", "Gimli", "FRIENDS_WITH", {"unlikely_friendship": True}),
        
        # Character-Location relationships
        ("Frodo", "The Shire", "LIVES_IN", {"status": "home"}),
        ("Sam", "The Shire", "LIVES_IN", {"status": "home"}),
        ("Elrond", "Rivendell", "RULES", {"years": "many"}),
        ("Galadriel", "Lothlorien", "RULES", {"years": "many"}),
        
        # The Ring's path
        ("Frodo", "The One Ring", "BEARS", {"duration": "temporary"}),
        ("Gollum", "The One Ring", "DESIRES", {"obsession": "extreme"}),
        ("The One Ring", "Mordor", "BELONGS_IN", {"created_by": "Sauron"}),
        
        # Weapons and artifacts
        ("Frodo", "Sting", "WIELDS", {"given_by": "Bilbo"}),
        ("Gandalf", "Glamdring", "WIELDS", {"origin": "Gondolin"}),
        
        # Political and military relationships
        ("Gondor", "Rohan", "ALLIES_WITH", {"status": "strong"}),
        ("Isengard", "Mordor", "ALLIES_WITH", {"status": "evil"}),
        ("Saruman", "Isengard", "CONTROLS", {"through": "corruption"}),
        
        # Character movements
        ("Frodo", "Mordor", "TRAVELS_TO", {"purpose": "destroy_ring"}),
        ("Sam", "Mordor", "TRAVELS_TO", {"purpose": "help_frodo"}),
        ("Gollum", "Mordor", "KNOWS_WAY", {"knowledge": "detailed"}),
        
        # Mentor relationships
        ("Gandalf", "Frodo", "MENTORS", {"role": "guide"}),
        ("Aragorn", "Frodo", "PROTECTS", {"sworn": "oath"}),
        
        # Antagonistic relationships
        ("Saruman", "Gandalf", "BETRAYS", {"reason": "power"}),
        ("Gollum", "Frodo", "BETRAYS", {"reason": "ring"}),
        
        # Location connections
        ("The Shire", "Rivendell", "CONNECTED_TO", {"via": "East Road"}),
        ("Rivendell", "Moria", "CONNECTED_TO", {"via": "Misty Mountains"}),
        ("Moria", "Lothlorien", "CONNECTED_TO", {"via": "Dimrill Dale"}),
        ("Rohan", "Gondor", "CONNECTED_TO", {"via": "Great West Road"}),  
        ("Rohan", "Isengard", "CONNECTED_TO", {"via": "Gap of Rohan"})    
    ]
    

