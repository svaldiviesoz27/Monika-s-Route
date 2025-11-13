## script.rpy
# (Reemplaza todo tu archivo con esto)

# --- INICIO DEL ARREGLO DE DEFINICIONES ---
# Tenemos que definir manualmente todo lo que nos saltamos
# con nuestro "Developer Jump".
    
# ARREGLO PARA ERROR 2 (Tracebacks 3-6): Definir al jugador 'p'
define p = Character("[persistent.name]", color="#c8c8c8")

# ARREGLO PARA ERROR 1 (Tracebacks 1-2): Definir posiciones
define t11 = Transform(xpos=0.5, ypos=1.0, xanchor=0.5, yanchor=1.0)
define t21 = Transform(xpos=0.25, ypos=1.0, xanchor=0.5, yanchor=1.0)
define t22 = Transform(xpos=0.75, ypos=1.0, xanchor=0.5, yanchor=1.0)
define s11 = Transform(xpos=0.25, ypos=1.0, xanchor=0.5, yanchor=1.0)
define n11 = Transform(xpos=0.4, ypos=1.0, xanchor=0.5, yanchor=1.0)
define y11 = Transform(xpos=0.6, ypos=1.0, xanchor=0.5, yanchor=1.0)
# --- FIN DEL ARREGLO DE DEFINICIONES ---

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
        $ persistent.name = "Player"
        $ s_name = "Sayori"
        $ m_name = "Monika"
        $ n_name = "Natsuki"
        $ y_name = "Yuri"
        
        jump ch1_5
        # --- FIN DE NUESTRO SALTO DE DESARROLLADOR ---


        # --- El juego original ESTÁ COMENTADO ---
        # $ chapter = 0
        # call ch0_main
        # call poem
        # ... (todo lo demás está comentado) ...
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
