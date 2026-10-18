import warriors
from convert_fight_res import convert_res

def show_menu():
    print("""
1 — Орк против Эльфа
2 — Воин против Орка
3 — Воин против Эльфа
0 — выход
""")

def main():
    while True:
        show_menu()
        choice = input("Выберите вариант боя ")
        if choice not in "12345670":
               return

        choice = int(choice)

        match choice:
            case 1:
                elf = warriors.Elf()
                orc = warriors.Orc()
                res = warriors.fight(elf, orc)
                convert_res(res, elf, orc)
            case 2:
                warrior = warriors.Warrior()
                orc = warriors.Orc()
                res = warriors.fight(warrior, orc)
                convert_res(res, warrior, orc)
            case 3:
                elf = warriors.Elf()
                warrior = warriors.Warrior()
                res = warriors.fight(warrior, elf)
                convert_res(res, warrior, elf)
            case _:
              return


if __name__ == "__main__":
    main()
