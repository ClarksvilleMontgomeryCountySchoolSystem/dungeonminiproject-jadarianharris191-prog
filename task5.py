escaped = True
if escaped:
    outcome = "Legend: You escaped the dungeon."
else:
    if not escaped:
        outcome ="Doom: You didn't escape the dungeon."
print(outcome)