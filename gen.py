import pandas as pd
from unidecode import unidecode
names = pd.read_excel("./list.xlsx").to_numpy()[1:][:]
for name in names:
    print("gh repo create GameUITHackathon2022/" + str(int(name[0])) + "-" + unidecode(name[1].replace(" ", "-")) + " --add-readme --public -l mit")

