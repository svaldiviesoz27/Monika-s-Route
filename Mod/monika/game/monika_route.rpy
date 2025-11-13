# Archivo: game/monika_route.rpy
# Este archivo contendrá todas nuestras escenas personalizadas.

# --- INSERCIÓN DE RUTA DE MONIKA ---
# La etiqueta original del juego para esta escena es 'ch1_5'.
# Al definirla aquí, Ren'Py usará NUESTRA versión en lugar de la original.

label ch1_5:
    scene bg club_day
    show monika 1a at t11
    with dissolve

    # Este es el diálogo original del juego
    m "Well, since everyone's here..."
    m "This weekend is the school festival, remember?"
    m "And we still have a lot to prepare."
    m "Natsuki's making cupcakes. And Yuri's in charge of atmosphere and decorations."
    m "As president, I'm managing the event and making the pamphlets."
    m "We're all going to be pretty busy."

    p "Sounds like it."
    p "So, who needs the most help?"

    # --- ¡NUESTRO MENÚ MODIFICADO! ---
    menu:
        # Opción original
        "I'll help Natsuki."

        # Opción original
        "I'll help Yuri."

        # ¡NUESTRA NUEVA OPCIÓN!
        "What about you, Monika?":

            # Saltamos a nuestra escena personalizada
            jump monika_route_start

    # Si eligen a Natsuki o Yuri, el juego salta a las etiquetas
    # 'ch1_n' o 'ch1_y' (que están en ch1_main.rpy) y continúa normal.
    
    jump ch1_6 # Este es el salto original para continuar el día


# --- NUESTRA RUTA COMIENZA