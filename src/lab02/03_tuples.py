def format_record(rec: tuple[str, str, float]):
    final_form = ""
    name = rec[0].title().split()
    group = rec[1]
    gpa = str(round(rec[2], 2))
    if len(name) == 3:
        final_form = (
            name[0]
            + " "
            + name[1][0]
            + ". "
            + name[2][0]
            + "., гр. "
            + group
            + ", GPA "
            + gpa
        )
    elif len(name) == 2:
        final_form = name[0] + " " + name[1][0] + "., гр. " + group + ", GPA " + gpa
    else:
        return "ValueError"
    if len(gpa.split(".")[1]) == 1:
        final_form += "0"
    return final_form


test_1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
test_2 = ("Петров Пётр", "IKBO-12", 5.0)
test_3 = ("Петров Пётр Петрович", "IKBO-12", 5.0)
test_4 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(format_record(test_1))
print(format_record(test_2))
print(format_record(test_3))
print(format_record(test_4))
