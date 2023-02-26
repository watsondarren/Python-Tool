expected = ''
was = ''
separate_by = ","


split_expected = expected.split(separate_by)
split_was = was.split(separate_by)

for i in range(len(split_expected)):
    try:
        if split_expected[i] != split_was[i]:
            print(f"Expected: {split_expected[i]}\nWas: {split_was[i]}\n")
    except IndexError:
        print("Different lengths")
