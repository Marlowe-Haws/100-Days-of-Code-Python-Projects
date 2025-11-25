with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
    names = [name.strip() for name in names]

with open("Input/Letters/starting_letter.txt", "r") as letter:
    letter = letter.read()

for name in names:
    new_letter = letter.replace("[name]", name)
    file_path = f"Input/Letters/letter_for_{name}.txt"
    with open(file_path, "w") as file:
        file.write(new_letter)
