# Import the tracery library
import tracery
from tracery.modifiers import base_english

# Define the grammar rules
rules = {
    'origin': '#observe# #name# #move#; #observe# #name# #move#',
    'name': ['Jane', 'Jack', 'Jarvis', 'Jermaine', 'Jermaine', 'Jorgen'],
    'move': ['trot', 'run', 'sauntering', '#observe#'],
    'observe': ['see', 'observe', 'spy']
}

# Create the grammar object
grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

# Expand the grammar
print(grammar.flatten("#origin#"))
