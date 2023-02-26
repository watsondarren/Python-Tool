items_to_run_through = ["item1"]
part_one = "=countif("
part_two = "!$C:$C,B$1)"


def formula_to_make(item):
    print(f"{part_one}{item}{part_two}")


def formula_loop(run_list):
    for item in run_list:
        formula_to_make(item)


formula_loop(items_to_run_through)