import json
import urllib
import urllib.request
import urlopen


def main():
    print("ʕ •́؈•̀ ₎ your not anonymous ʕ •́؈•̀ ₎ ")
    print("Made By Soffty")
    print("Made your choice")
    text = input("Y(youtube), T(twitter), N(namemc), R(roblox), K(tiktok),A(annulaire téléphonique), I(iplookup) ,F(fakephone for call) : ")
    if text == "Y":
        Yname = input("Put the username here : ")
        print("https://www.youtube.com/results?search_query=",Yname,"&sp=EgIQAg%253D%253D", sep ="")
        mainmenu = input("1(exit) 2(mainmenu) ")
        if mainmenu == "1":
            print("Thanks for use my tools ! Bye")
            quit()
        if mainmenu == "2":
            print ("Go to the Main Menu")
            main()
    if text == "T":
        Tname = input("Put the username here : ")
        print("https://twitter.com/search?q=",Tname,"&src=typed_query", sep ="")
        mainmenu = input("1(exit) 2(mainmenu) ")
        if mainmenu == "1":
            print("Thanks for use my tools ! Bye")
            quit()
        if mainmenu == "2":
            print ("Go to the Main Menu")
            main()
    if text == "N":
        Nname = input("Put the username here : ")
        print("https://fr.namemc.com/search?q=",Nname, sep ="")
        mainmenu = input("1(exit) 2(mainmenu) ")
        if mainmenu == "1":
            print("Thanks for use my tools ! Bye")
            quit()
        if mainmenu == "2":
            print ("Go to the Main Menu")
            main()
    if text == "R":
        Rname = input("Put the username here : ")
        print("https://www.roblox.com/search/users?keyword=",Rname, sep ="")
        mainmenu = input("1(exit) 2(mainmenu) ")
        if mainmenu == "1":
            print("Thanks for use my tools ! Bye")
            quit()
        if mainmenu == "2":
            print ("Go to the Main Menu")
            main()
    if text == "K":
        Kname = input("Put the username here : ")
        print("https://www.tiktok.com/search?q=",Kname,"&lang=fr", sep ="")
        mainmenu = input("1(exit) 2(mainmenu) ")
        if mainmenu == "1":
            print("Thanks for use my tools ! Bye")
            quit()
        if mainmenu == "2":
            print ("Go to the Main Menu")
            main()
    if text == "F":
        print("https://ievaphone.com/")
        print("https://free-lookup.net/", "<<-- Select Free Call" )
        print("https://call2friends.com/free-calls")
        mainmenu = input("1(exit) 2(mainmenu) ")
        if mainmenu == "1":
            print("Thanks for use my tools ! Bye")
            quit()
        if mainmenu == "2":
            print ("Go to the Main Menu")
            main()
    if text == "I":
        ip= input("Enter an ip here : ")
        url = "http://ip-api.com/json/"
        response = urllib.request.urlopen(url + ip)
        data = response.read()
        values = json.loads(data)

        print(" IP: " + values['query'])
        print(" City: " + values['city'])
        print(" ISP: " + values['isp'])
        print(" Country: " + values['country'])
        print(" Region: " + values['region'])
        print(" Time zone: " + values['timezone'])
        mainmenu = input("1(exit) 2(mainmenu) ")
        if mainmenu == "1":
            print("Thanks for use my tools ! Bye")
            quit()
        if mainmenu == "2":
            print("Go to the Main Menu")
            main()
    if text == "A":
        nom = input("Entrez le nom/prénom de la personne : ")
        loc = input("Entrez la ville : ")
        print("https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=", nom, "&ou=", loc, "&univers=pagesblanches&idOu=", sep ="")
        mainmenu = input("1(exit) 2(mainmenu) ")
        if mainmenu == "1":
            print("Thanks for use my tools ! Bye")
            quit()
        if mainmenu == "2":
            print ("Go to the Main Menu")
            main()




if __name__ == '__main__':
     main()