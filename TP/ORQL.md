# One Ring Query Language (ORQL) Specification

One Query Language to rule them all,  
One Query Language to find them,  
One Query Language to bring all data together,  
And in the database bind them.

## Overview
ORQL (One Ring Query Language) is a simple yet powerful query language for the OneRingDB graph database, inspired by Middle-earth lore. It provides basic CRUD operations and path finding capabilities.

## Syntax

### Node Operations

#### CREATE
Create new nodes with properties:
```sql
CREATE (Morgoth:Character{Species:Valar, Power:Infinite})
CREATE (Sauron:Character{Species:Maiar, Master:Morgoth})
```

#### READ
Read nodes by ID, class, or properties:
```sql
-- Read all nodes
READ ()

-- Read by ID
READ (Frodo)

-- Read by class
READ (:Hobbit)

-- Read with property filter
READ (:Character) WHERE Species = Hobbit

-- Read with multiple filters
READ (:Character) WHERE Species = Elf AND Realm = Lothlorien
```

#### UPDATE
Update node properties:
```sql
UPDATE (Frodo:Hobbit{Location:Mordor})
UPDATE (Gandalf{Color:White}) WHERE Color = Grey
```

#### DELETE
Delete nodes (and their relationships):
```sql
DELETE (Morgoth)
DELETE (:Character) WHERE Species = Orc
```

### Edge Operations

#### CREATE
Create relationships between nodes:
```sql
CREATE [Morgoth, Sauron:is_the_master{Years:1000}]
CREATE [Frodo, Ring:bears{Duration:Temporary}]
```

#### READ
Read relationships:
```sql
-- Read all relationships
READ []

-- Read specific relationship
READ [Frodo, Sam]

-- Read relationships by type
READ [:FRIENDS_WITH]

-- Read with properties
READ [:ALLIES_WITH] WHERE status = strong
```

#### UPDATE
Update relationship properties:
```sql
UPDATE [Frodo, Sam:FRIENDS_WITH{Trust:Unbreakable}]
```

#### DELETE
Delete relationships:
```sql
DELETE [Frodo, Ring]
DELETE [:BETRAYS]
```

### Path Operations

#### LINK
Find paths between nodes:
```sql
-- Find shortest path
LINK [Frodo, Mordor]

-- Find all paths
LINK [Gollum, Ring] ALL

-- Find paths with maximum length
LINK [Gandalf, Frodo] MAX_LENGTH 3
```

## Examples from Current Dataset

### Node Queries
```sql
-- Create a new character
CREATE (Bilbo:Hobbit{Age:111, Home:"Bag End"})

-- Find all Hobbits
READ (:Hobbit)

-- Find characters from the Shire
READ (:Character) WHERE Home = "The Shire"

-- Update Gandalf's status
UPDATE (Gandalf{Color:White}) WHERE Color = Grey

-- Delete Gollum
DELETE (Gollum)
```

### Relationship Queries
```sql
-- Create friendship
CREATE [Merry, Pippin:FRIENDS_WITH{Since:Childhood}]

-- Find all alliances
READ [:ALLIES_WITH]

-- Find strong relationships
READ [:FRIENDS_WITH] WHERE Trust = High

-- Update relationship
UPDATE [Frodo, Sam:FRIENDS_WITH{Loyalty:Unbreakable}]

-- Delete betrayal
DELETE [Saruman, Gandalf]
```

### Path Queries
```sql
-- Find path from Frodo to Mordor
LINK [Frodo, Mordor]

-- Find all paths between Gollum and the Ring
LINK [Gollum, "The One Ring"] ALL

-- Find short paths between locations
LINK [Rivendell, Mordor] MAX_LENGTH 3
```

## Error Handling
- Invalid syntax returns detailed error messages
- Non-existent nodes/relationships return appropriate errors
- Property type mismatches are caught and reported
- Circular references in path queries are handled gracefully

## Best Practices
1. Use meaningful node and relationship names
2. Be specific with property filters
3. Consider using MAX_LENGTH for path queries in large graphs
4. Delete nodes carefully as it affects relationships
5. Use quotes for property values containing spaces
