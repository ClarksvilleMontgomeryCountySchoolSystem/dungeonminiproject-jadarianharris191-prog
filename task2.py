has_key = False
if has_key:
    outcome = "Click: The lock turns smoothly, and the door swings open to reveal a hidden message."
else:
    if not has_key:
        outcome = "Doom: The lock does not turn and no message is revealed"
print(outcome)
