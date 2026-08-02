PLACEHOLDER = "[name]"

with open("./DAY-24/ToInvite.txt") as names_file:
    names = names_file.readlines()
    
with open("./DAY-24/Input/starting.docx") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./DAY-24/ReadyToSend/letter_for_{stripped_name}.docx", "w") as completion:
            completion.write(new_letter)