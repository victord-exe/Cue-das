""" Mini-Proyecto N.O 1.
    World War II quiz :o
"""
import win32api
import win32api as msg

controlador = True

msg.MessageBox(0, "¡Estás a punto de empezar el quiz!", "World War II quiz")
msg.MessageBox(0, "¡Estás listo?", "World War II quiz")

print("""
      ¡Antes de comenzar, deberás resolver este acertijo!
    #####################################################################

    Blanca por dentro, verde por fuera, si quieres que te lo diga, espera. 

    #####################################################################""")
while (controlador == True):
    acertijo = input("---> ")

    if ((acertijo == "pera") or (acertijo == "Pera")):
        print("     ¡Correcto!")
        print("     Está bien, puedes continuar.")
        controlador = False
    else:
        print("\n   Bruto, respuesta incorrecta. Intenta de nuevo")

controlador == False
while (controlador == False):
    print("""
    Pregunta n. 1: ¿Cómo comenzó la Segunda Guerra Mundial?

    A) La guerra más destructiva de la historia comenzó con la invasión de la URSS por parte de Alemania el 1 de septiembre de 1939

    B) La Segunda Guerra Mundial comenzó con el pacto expansionista firmado por Japón, Italia y Alemania el 1 de septiembre de 1939

    C) Comenzó con la invasión de Polonia por parte de Alemania el 1 de septiembre de 1939""")
    resp1 = input("---> ")
    if ((resp1 == 'B') or (resp1== 'b')):
        print("¡Correcto! Puedes continuar")
        controlador = True
    else:
        print("\n   Bruto, respuesta incorrecta. Intenta de nuevo")

while (controlador == True):
    print("""
    Pregunta n. 2: ¿En qué año accedió Hitler y el partido nacional-socialista al poder?

    A) 1933

    B) 1936

    C) 1939""")
    resp2 = input("---> ")
    if ((resp2 == 'A') or (resp2 == 'a')):
        print("¡Correcto! Puedes continuar")
        controlador = False
    else:
        print("\n   Bruto, respuesta incorrecta. Intenta de nuevo")

while (controlador == False):
    print("""
    Pregunta n. 3: ¿Con qué nombre fue conocido el pacto de no agresión entre alemanes y soviéticos?

    A) Pacto Ribbentrop-Mólotov

    B) Pacto de Varsovia

    C) Pacto de Brandeburgo1939 """)
    resp3 = input("---> ")
    if ((resp3 == 'A') or (resp3 == 'a')):
        print("¡Correcto! Puedes continuar")
        controlador = True
    else:
        print("\n   Bruto, respuesta incorrecta. Intenta de nuevo")

while (controlador == True):
    print("""
    Pregunta n. 4: ¿En qué consistía la "guerra relámpago" o blitzkrieg llevada a cabo por los alemanes?

    A) Consistía en la acción coordinada de unidades de artillería blindadas, aviación y comunicaciones
       para debilitar rápidamente las defensas del enemigo

    B) Consistía en atacar los objetivos clave siempre coincidiendo con tormentas y mal tiempo para mermar
       más fácilmente las defensas del enemigoPacto de Varsovia

    C) Consistía en usar armas químicas junto con bombardeos continuos """)
    resp4 = input("---> ")
    if ((resp4 == 'A') or (resp4 == 'a')):
        print("¡Correcto! Puedes continuar")
        controlador = False
    else:
        print("\n   Bruto, respuesta incorrecta. Intenta de nuevo")

while (controlador == False):
    print("""
    Pregunta n. 5 Hitler sufrió muchos atentados (todos ellos fallidos). ¿Cuántos exactamente?

    A) 23

    B) 32

    C) 43""")
    resp5 = input("---> ")
    if ((resp5 == 'C') or (resp5 == 'c')):
        print("¡Correcto! Puedes continuar")
        controlador = True
    else:
        print("\n   Bruto, respuesta incorrecta. Intenta de nuevo")

while (controlador == True):
    print("""
    Pregunta n. 6: ¿Cómo se llamaba el avión que transportó la bomba atómica que se lanzó sobre Hiroshima?

    A) Little Boy

    B) Enola Gay
    
    C) Little Wings """)
    resp6 = input("---> ")
    if ((resp6 == 'B') or (resp6 == 'b')):
        print("¡Correcto! Puedes continuar")
        controlador = False
    else:
        print("\n   Bruto, respuesta incorrecta. Intenta de nuevo")

while (controlador == False):
    print("""
    Pregunta n. 7 ¿Cómo se llama la máquina que utilizaban los alemanes para encriptar sus mensajes
                  y que los aliados no supieran qué decían?

    A) Enigma

    B) Die Maschine (La Máquina en alemán)

    C) Unübersetzbar (intraducible en alemán)""")
    resp7 = input("---> ")
    if ((resp7 == 'A') or (resp7 == 'a')):
        print("¡Correcto! Puedes continuar")
        controlador = True
    else:
        print("\n   Bruto, respuesta incorrecta. Intenta de nuevo")

while (controlador == True):
    print("""
    Pregunta n. 8: ¿Cuál fue el último país en rendirse concluyendo de este modo la Segunda Guerra Mundial?

    A) Alemania
    
    B) Italia
    
    C) Japón """)
    resp8 = input("---> ")
    if ((resp8 == 'C') or (resp8 == 'c')):
        print("¡Correcto! Puedes continuar")
        controlador = False
    else:
        print("\n   Bruto, respuesta incorrecta. Intenta de nuevo")

while (controlador == False):
    print("""
    Pregunta n. 9 ¿Cuándo comenzó la operación Barbarroja, el ataque de las tropas de Hitler a la URSS?

    A) El 22 de junio de 1941, exactamente el mismo día en qué Napoleón había anunciado su intención de invadir Rusia en 1812

    B) El 16 de enero de 1941, en pleno invierno, lo que decantó la balanza a favor de la URSS

    C) El 4 de julio de 1941, coincidiendo con el día de la Independencia de Estados Unidos""")
    resp9 = input("---> ")
    if ((resp9 == 'A') or (resp9 == 'a')):
        print("¡Correcto! Puedes continuar")
        controlador = True
    else:
        print("\n   Bruto, respuesta incorrecta. Intenta de nuevo")

while (controlador == True):
    print("""
    Pregunta n. 10: El Holocausto, el asesinato masivo y sistemático de población judía ¿con cuántas vidas terminó?

    A) Entre 2.000.000 y 3.000.000 de personas fueron ejecutadas en el Holocausto

    B) Entre 5.900.000 y 7.100.000 personas fueron asesinadas vilmente

    C) Entre 15.00.000 y 18.000.000 personas fueron asesinadas en el HolocaustoJapón """)
    resp10 = input("---> ")
    if ((resp10 == 'B') or (resp10 == 'b')):
        print("¡Correcto! Puedes continuar")
        controlador = False
    else:
        print("\n   Bruto, respuesta incorrecta. Intenta de nuevo")

print("""
    *************************
    *                       *
    *     ¡LO LOGRASTE!     *
    *                       *
    *************************
""")

win32api.MessageBox(0,"¡Bien! Lograste terminar el quiz existosamente, no eres tan brute", "World War II Quiz")