placeholder="[name]"

with open("./Assets/names.txt","r") as name_file:
    names=name_file.readlines()

with open("./Assets/main_mail.txt","r") as letter_file:
    data=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_mail=data.replace(placeholder,stripped_name)
        with open(f"./Assets/mail of {stripped_name}.txt","w") as f:
            f.write(new_mail)
