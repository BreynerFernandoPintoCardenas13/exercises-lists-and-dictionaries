def mainMenu():    
    while True:    
        from menu.mainMenu import menuPrincipal

        rta=menuPrincipal()
        if rta==1:
            from menu.menuListas import menuListas
            menuListas()
        elif rta==2:
            from menu.menuDict import menuDict
            menuDict()
        elif rta==3:
            from menu.bye import bye
            bye()
            break
mainMenu()