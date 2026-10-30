#---------------------------------------------------
#                    cheezbuger
#---------------------------------------------------
try:
    print("importing os")
    import os
    print("importing sys")
    import sys
    print("importing urllib.request/urlretrieve")
    from urllib.request import urlretrieve
    print("importing jayson (json)")
    import json
    print("importing pathlib/Path")
    from pathlib import Path
    print("importing zipfile")
    import zipfile
    print("importing shutil")
    import shutil
except ImportError:
    print("OHNO, yo importing failed XD")
    exit()

#   _
# ((`)_.._     ,'-. _..._ _._
#  \,'    '-._.-\  '     ` .-'
# .'            /         (
#/             |     _   _ \
#|              \     e   e  |
#;                     .-.   /
# ;       ',       '-.( '')-'
 # '.      |           ;-'
  #  \    /           /
   # /   /-._  __,  7 |
    #\  `\  \``  |  | |
     #\   \_,\   |  |_,\
#  jgs '-`'      \_,\
#------------------------------------------------
#               credit asciiart
#------------------------------------------------
#https://asciiart.website/
#This ASCII pic can be found at
#https://asciiart.website/art/6592

def GETPKG(package):
    print(f"i am goingtoretriev {package}!!")

    with open("ya-i-need-dis-map/repo.json") as f:
        data = json.load(f)

    for pkg in data["packages"]:
        if pkg["name"] == package:
            print("it exists!!!!")
            print(pkg)
            print("curling from: " + pkg["url"])
            urlretrieve(pkg["url"], f"{depmap}/tmp/cachedpkg.azertypkg")
            print(f"curled {pkg['url']} to {depmap}/tmp/cachedpkg.azertypkg :)")
            return

    print("no this does not exsist too bad")

#THIS MAPS NAME IS WAYYYYYYYYYYYY TO LONG AND I AM NOT GONNA HARDCODE IT AAAARGGGH
depmap = "ya-i-need-dis-map"
   
print("you like the name " + sys.argv[0] + "?")
print("if yo dont like it, thats too bad lol :)")
print("\n")
#get the args, if there isn't any, i am just gonna use the string used for the -h :D
try:
    basearg = sys.argv[1]
except IndexError:
    print("welcome to Pyzertypkg, to start; type one of these things:")
    print("-i for installing, -ui for uninstalling, -lp for listing the available packages, -u to download an index of packages on a server, -gp for just downloading an package")
    print("still, Pyzertypkg doesnt have super cow powers")
    #why bro why do i needa do "exit()" XD
    exit()
try:
    FirstExtArg = sys.argv[2]
    ExtArg = True
except IndexError:
    print("nothing in FirstExtArg?? Doesn't matter ;)\n")
    ExtArg = False

#now its time for a ton of elif's yayyyyyyy (NOOOOO)
#first: install an azerty
if basearg == "--install" or basearg == "-i":
    if not ExtArg:
        print("please type an package pls")
    else:
        GETPKG(FirstExtArg)
        print(f"extracting {FirstExtArg}...")
        with zipfile.ZipFile(f"{depmap}/tmp/cachedpkg.azertypkg") as z:
            z.extractall(f"{depmap}/installed/{FirstExtArg}")
        print(f"i think it succesfully installed {FirstExtArg}???")
        print("cleaning up the mess in tmp..")
        Path(f"{depmap}/tmp/cachedpkg.azertypkg").unlink()
    
    
#second: help
elif basearg == "-h" or basearg == "--help":
    print("no functions are implemented yet, but hey u can try --install or -i :)")
#third: update package lists!!
elif basearg == "-u" or basearg == "--update":
    RepoUrl = input("which url do u want to get the repo from? (default is MY repo :D): ") or "https://p1xelpp.github.io/index.json"
    print("getting the repo.json from " + RepoUrl + "..................")
    try:
        urlretrieve(RepoUrl, "ya-i-need-dis-map/repo.json")
    except urllib.error.URLError:
        print("oh no it failede")
#fourth: list packages on da repo on your screen thingah
elif basearg == "-lp" or basearg == "--listpackages":
    with open(f"{depmap}/repo.json") as f:
        data = json.load(f)

    for package in data["packages"]:
        print(f"{package['name']} ({package['version']})")
        print(f"  {package['description']}")
        print(f"  {package['url']}")
        print()
#fifth: get an azerty
elif basearg == "-gp":
    if not ExtArg:
        print("for this one u need to type a package :)")
        exit()
    else:
        GETPKG(FirstExtArg)

elif basearg == "-ui" or basearg == "--uninstall":
    if not ExtArg:
        print("for this one u need to type an installed package :D")
    else:
        print(f"uninstalling {FirstExtArg}..")
        shutil.rmtree(f"{depmap}/installed/{FirstExtArg}")
        print(f"i sure hope it uninstalled {FirstExtArg}!")
else:
    print("what is this arg bro?? (maybe u made a typo but idk)")
