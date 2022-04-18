color_names = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
               "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
               "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}

color_name = input("Enter the color: ")
while color_name != "":
    print("The code for \"{}\" is {}".format(color_name, color_names.get(color_name)))
    color_name = input("Enter a color: ")
