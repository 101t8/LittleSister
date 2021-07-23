import json
import urllib
import urllib.request
import webbrowser
import urlopen


def main():
    url = "https://bit.ly/3iFufdX"
    print("ʕ •́؈•̀ ₎ your not anonymous ʕ •́؈•̀ ₎ ")
    print("Made By Soffty")
    print("Made your choice")
    text = input("Y(youtube), T(twitter), N(namemc), R(roblox), K(tiktok), A(<<--all), P(annulaire téléphonique), I(iplookup) ,F(fakephone for call) : ")
    if text == "Y":
        Yname = input("Put the username here : ")
        if Yname == "soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if Yname == "Soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if Yname == "Riffteur":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        print("https://www.youtube.com/results?search_query=",Yname,"&sp=EgIQAg%253D%253D", sep ="")
        print("https://www.youtube.com/results?search_query=", Yname, sep="")
        mainmenu = input("1(exit) 2(mainmenu) ")
        if mainmenu == "1":
            print("Thanks for use my tools ! Bye")
            quit()
        if mainmenu == "2":
            print ("Go to the Main Menu")
            main()
    if text == "T":
        Tname = input("Put the username here : ")
        if Tname == "soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if Tname == "Soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if Tname == "Riffteur":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
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
        if Nname == "soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if Nname == "Soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if Nname == "Riffteur":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
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
        if Rname == "soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if Rname == "Soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if Rname == "Riffteur":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
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
        if kname == "soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if Kname == "Soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if Kname == "Riffteur":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
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
    if text == "P":
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
    if text == "A":
        name = input("Put the username here : ")
        if name == "soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if name == "Soffty":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        if name == "Riffteur":
            print("T'essaie de me dox la ? sale merde")
            webbrowser.open("https://bit.ly/3iFufdX")
            quit()
        print("https://www.youtube.com/results?search_query=", name, "&sp=EgIQAg%253D%253D", sep="")
        print("https://www.youtube.com/results?search_query=", name, sep="")
        print("https://twitter.com/search?q=", name, "&src=typed_query", sep="")
        print("https://fr.namemc.com/search?q=", name, sep="")
        print("https://www.roblox.com/search/users?keyword=", name, sep="")
        print("https://www.tiktok.com/search?q=", name, "&lang=fr", sep="")
        mainmenu = input("1(exit) 2(mainmenu) ")
        if mainmenu == "1":
            print("Thanks for use my tools ! Bye")
            quit()
        if mainmenu == "2":
            print("Go to the Main Menu")
            main()


if __name__ == '__main__':
     main()