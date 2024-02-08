def search_paragraph(search_term):
    with open("Constitution.txt", 'r', encoding='utf-8') as file:
        file = file.read()
        ls = file.split("\n")
        for par in ls:
            if search_term in par:
                print(par)
                return par
    return False
