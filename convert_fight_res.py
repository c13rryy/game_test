def convert_res(fight_result, warrior1, warrior2):
    print(fight_result)
    if fight_result:
        print(f"Победитель - {warrior1.__class__.__name__}")
    else:
        print(f"Победитель - {warrior2.__class__.__name__}")