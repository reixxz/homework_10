import colorama

def introspect_colorama():

    attributes_and_methods = [name for name in dir(colorama) if not name.startswith('_')]

    print("Найважливіші атрибути та методи бібліотеки colorama:")
    for name in attributes_and_methods:
        obj = getattr(colorama, name)
        docstring = obj.__doc__ if hasattr(obj, '__doc__') else "Документація відсутня"
        print(f"{name}: {docstring}")

if __name__ == "__main__":
    introspect_colorama()
