## script.rpy
# (Reemplaza todo tu archivo con esto)

label start:

    # --- Configuración Inicial ---
    $ anticheat = persistent.anticheat
    $ chapter = 0
    $ _dismiss_pause = config.developer
    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"
    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True
    # --- Fin Configuración ---


    ## The Main Part of the Script
    if persistent.playthrough == 0:

        # --- INICIO DE NUESTRO SALTO DE DESARROLLADOR ---
        
        # 1. Definimos un nombre de jugador por defecto
        $ persistent.name = "Player"

        # 2. ¡ARREGLO DE NOMBRES! Definimos los nombres correctos.
        $ s_name = "Sayori"
        $ m_name = "Monika"
        $ n_name = "Natsuki"
        $ y_name = "Yuri"
        
        # 3. Saltamos DIRECTAMENTE a la etiqueta de nuestro menú modificado
        jump ch1_5
        # --- FIN DE NUESTRO SALTO DE DESARROLLADOR ---


        # 3. HEMOS COMENTADO EL INICIO NORMAL DEL JUEGO
        #    para que nuestro salto funcione.

        # This variable sets the chapter number to X depending on the chapter
        # your player is experiencing ATM.
        # $ chapter = 0

        # This call statement calls your script label to be played.
        # call ch0_main
        
        # This call statement calls the poem mini-game to be played.
        # call poem
        # ... (todo lo demás está comentado) ...
        # ...
        # call endgame
        # return

    # --- El resto de los Actos ---
    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch10_main
        jump playthrough2

    elif persistent.playthrough == 2:
        $ chapter = 0
        call ch20_main
        label playthrough2:
            call poem
            call ch21_main
            # ... (etc) ...
            call ch23_end
            return

    elif persistent.playthrough == 3:
        jump ch30_main

    elif persistent.playthrough == 4:
        $ chapter = 0
        call ch40_main
        jump credits

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return