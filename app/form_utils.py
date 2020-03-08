
def validate_form(form):
    form.data = {}
    form.errors = {}

    form_title = form.get("name", "").strip()
    if len(form_title) == 0:
        form.errors["error"] = "Name can not be blank."
    else:
        form.data["name"] = form_title

    form_year = form.get("age")
    if not form_year:
        form.data["age"] = None
    elif not form_year.isdigit():
        form.errors["error"] = "Age must consist of digits only."
    else:

        year = int(form_year)
        if (year < 0) :
            form.errors["error"] = "Year cannot be less than 0."
        else:
            form.data["age"] = year

    return len(form.errors) == 0


def get_age_group(age):
    """

    :param age: int
        Age of the person
    :return:
        age group
    """
    group = "invalid"
    if age in range(0, 21):
        group = "A"
    elif age in range(21, 41):
        group = "B"
    elif age in range(41, 61):
        group = "C"
    elif age > 60:
        group = "D"
    return group


def reverse_name(name: str):
    rev_name = name
    print("length",len(name))
    full_name = name.split()
    if len(full_name) > 1:

        first = full_name.pop(0)
        last = full_name.pop(-1)

        full_name.insert(0, last)
        full_name.append(first)

        rev_name = " ".join(full_name)
    return rev_name
