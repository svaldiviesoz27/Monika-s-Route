# Archivo: game/monika_route.rpy
# (Reemplaza todo tu archivo con esto)

# --- INSERCIÓN DE RUTA - PARTE 1: EL MENÚ ---
label ch1_5:
    scene bg club_day
    
    # --- ¡ARREGLO DE SPRITES (v2)! ---
    # Usamos las posiciones estándar para que no se pisen.
    show monika 1a at center
    show yuri 1a at right
    show natsuki 1a at left
    with dissolve
    # --- FIN DEL ARREGLO ---

    m "Well, since everyone's here..."
    m "This weekend is the school festival, remember?"
    m "And we still have a lot to prepare."
    m "Natsuki's making cupcakes. And Yuri's in charge of atmosphere and decorations."
    m "As president, I'm managing the event and making the pamphlets."
    m "We're all going to be pretty busy."
    p "Sounds like it."
    p "So, who needs the most help?"

    menu:
        "I'll help Natsuki.":
            jump ch1_n
        "I'll help Yuri.":
            jump ch1_y
        "What about you, Monika?":
            jump monika_route_start

# --- INICIO DE NUESTRA RUTA ---
label monika_route_start:
    
    # No usamos 'scene' para no borrar a Yuri y Natsuki
    show monika 1m at center
    with dissolve

    m "Huh? Me?"
    m "Oh, don't worry about me. I just have a lot of boring club paperwork to do."
    m "It wouldn't be much fun for you..."
    p "I insist. I want to help you."
    show monika 1l at center
    m "..."
    m "Wow, [player]. I don't know what to say."
    m "Okay... if you really want to. I guess I'll see you this weekend, then."
    m "Thank you so much!"
    $ club_monika = True
    $ club_yuri = False
    $ club_natsuki = False
    p "No problem. It'll be fun."
    jump ch1_6

# --- INSERCIÓN DE RUTA - PARTE 2: LA POST-PELEA ---
label ch1_7:
    if club_monika:
        m "Okay, everyone! Let's all just take a deep breath."
        show natsuki 4a at left
        show yuri 5a at right
        n "Hmph!"
        y "..."
        m "Listen. We're all just a little stressed about the festival."
        m "Let's not take it out on each other."
        m "For today, let's just clean up and go home."
        m "[player], thanks again for offering to help me."
        m "I'll text you the details later, okay?"
        p "Sounds good, Monika."
        jump ch1_8
    else:
        m "Okay, everyone! Let's all just take a deep breath."
        show natsuki 4a at left
        show yuri 5a at right
        n "Hmph!"
        y "..."
        m "Yuri, Natsuki, can you just try to get along?"
        m "We're all friends here."
        m "Anyway, [player], you still haven't decided who you're helping yet."
        # ... (diálogo original) ...
        m "Don't make me choose for you."
        menu:
            "Natsuki.":
                $ club_natsuki = True
                jump ch1_8
            "Yuri.":
                $ club_yuri = True
                jump ch1_8
            "Sayori.":
                $ club_sayori = True
                jump ch1_8