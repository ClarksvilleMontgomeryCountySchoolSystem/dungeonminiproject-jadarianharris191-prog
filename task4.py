drawbridge_raised = True
if drawbridge_raised:
    outcome = "Doom: They cant get out."
else:
    if not drawbridge_raised:
        outcome = "Thunder: They can get out."
print(outcome)