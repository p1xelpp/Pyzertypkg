print("hello and welcome to the Pyzertypkg setup :D")
print("just wait and we do everything for u!")

#ok time for imports
try:
    print("importing pathlib/Path")
    from pathlib import Path
    print("importing urllib.request/urllib")
    from urllib.request import urlretrieve
    print("yay importing complete")
except ImportError:
    print("ohno importing failed!!!!!!!!!")

#now its time to make the foldersssss yayyyy (nooooo)
print("making Pyzetypkg/ya-i-need-dis-map/tmp")
Path("Pyzertypkg/ya-i-need-dis-map/tmp").mkdir(parents=True, exist_ok=True)
print("making Pyzertypkg/ya-i-need-dis-map/installed")
Path("Pyzertypkg/ya-i-need-dis-map/installed").mkdir(parents=True, exist_ok=True)

#get the main.py
print("downloading main.py")
urlretrieve("https://github.com/p1xelpp/Pyzertypkg/raw/refs/heads/main/main.py", "Pyzertypkg/main.py")

print("i think setup is finished for now so bye bye.")
