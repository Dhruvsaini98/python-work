name = " dhruv saini "
name_l = name.lstrip()
name_r = name.rstrip()
name_s = name.strip()
name_f = f"Name with different strip methods:\n\t{name_l.title()}\n\t{name_r.title()}\n\t{name_s.title()}" #Use f when need to use variable's value in a string
print(name_f)