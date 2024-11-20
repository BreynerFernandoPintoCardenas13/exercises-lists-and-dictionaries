while True:    
    from menu.mainMenu import menuPrincipal

    rta=menuPrincipal()
    if rta==1:
        from menu.menuListas import menuListas
        rta=menuListas()