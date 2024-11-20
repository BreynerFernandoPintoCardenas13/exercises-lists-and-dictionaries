while True:    
    from menu.mainMenu import menuPrincipal

    rta=menuPrincipal()
    if rta==1:
        from menu.menuListas import menuListas
        rta=menuListas()
    elif rta==2:
        from menu.menuDict import menuDict
        rta=menuDict()
