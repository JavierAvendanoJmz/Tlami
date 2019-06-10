
define c1 = Character("Cruzado 1")
define c2 = Character("Cruzado 2")
define cd = Character("Cruzado desconocido")

define chica = Character("Chica")
define chico = Character("Chico")
define padre = Character("Padre")

define tzilacatzin = Character("Tzilacatzin")
define guerrero = Character("Guerrero")
define malinalli = Character("Malinalli")
define hernan = Character("Hernan")

label start:

    scene prologo

    play music "<from 16 to 256>music/bg/prologo.ogg"

    "Año 1199, el papa actual pone en marcha la cuarta cruzada"
    "En 1202 los cruzados fueron empleados para luchar contra los hùngaros de  zadar"
    "Esto causa la excomulgación de los cruzados."

    play sound "music/efectos/guerra.mp3"

    c1 "¡Nos han rodeado!"
    c2 "¡debemos retirarnos a la fortaleza!"
    c1 "Cuidado a tu izquierda"

    scene corte1

    play sound "music/efectos/espadas.mp3"

    "En ese momento se escucho el viento ser cortado por el filo de una espada"

    scene corte2

    "Lo que le siguió fue un grito"

    scene corte3
    
    c2 "aaagh"

    scene espada

    c1 "maldito"
    
    "el cruzado mato a quien cortó a su compañero"
    
    c2 "dejame aqui, huye al cast..i..llo"
    
    "el cruzado que aun seguía en pie con lágrimas en los ojos corrió a la fortaleza"
    
    c1 "maldición, la puerta está atascada"
    
    scene cruzado
    
    "en ese momento volteo y se veían a 5 húngaros corriendo hacia él, lo único que le quedó fue orar"
    "el cruzado cerró sus ojos esperando el final cuando de pronto escuchó múltiples gritos"
    "al abrir los ojos vio los cadáveres de los húngaros y una figura parada de espaldas a él"
    
    cd "En estos momentos deberías pelear aunque veas la muerte"
    cd "No hay tiempo para orarle a alguien que nos abandonó"
    
    "El cruzado salvado, quedó en shock al oír las palabras, no sabía si agradecerle a su fe o a ese soldado que repudia la iglesia por el abandono"
    
    cd "Si quieres esperar al final te recomiendo que te resguardas,"
    cd "yo seguiré peleando, no quiero ir a un lugar el cual me expulsó"
    
    "Comprendiendo que se refería a la tierra prometida por su religión, su decisión fue unirse al combate"
    
    c1 "Te acompañare, tienes razón, solo quedamos nosotros"
    cd "Ya no luchamos por la causa, si no por sobrevivir"
    
    scene hungaros

    "En ese momento los dos cruzados corrieron hacia unos húngaros que parecían acercarse"
    play sound "music/efectos/guerra.mp3"
    "Después de otras horas de lucha, los cruzados estaban fatigados"
    "Los enemigos a su alrededor estaban sorprendidos por la fuerza de sus adversarios"
    "Pero al notar que estaban cansados, todos los enemigos restantes se lanzaron contra ellos…"
    "El piso se torno rojo carmesí y se escucharon dos voces tenues pronunciar su último sonido"
    
    c1 "Espero que la iglesia pierda"
    c2 "ORACIONES INENTENDIBLES"
    
    "Eso fue lo último que se supo de aquellos dos soldados…"

    stop sound
    stop music fadeout 1.0

label capitulo1:

    scene noche

    "Año 1500, Tenochtitlan"
    "Era una noche de tormenta, los vientos eran fuertes y había un extraño ambiente en la comunidad"
    
    chica "¡aghhhhh!"
    
    "Una chica luchaba por dar a luz a a su bebé, se escuchaban sus gritos a través de la aldea"
    
    chica "¡Ayudame!"
    chico "¿Qué debería hacer?"

    menu:
        "Pedir ayuda":
            $ opcion = "1"
        "Asistirle en el parto":
            $ opcion = "2"

if opcion == "1": 
    
    label opcion1:

        chico "Espera, iré por ayuda..."
        
        "El joven aldeano, quien parece ser el padre y esposo de la chica, salió corriendo a buscar ayuda."
        "unos minutos pasaron, los cuales le parecieron eternos a la chica"        
        
        chica "¡¿Dónde estás?!"
        
        "En ese momento se escucharon los pasos agitados del joven y unos acompañantes"
        
        chico "Traje ayuda, tranquila, todo estará bien"
        
        "El chico venía acompañado de quienes parecían ser los médicos de la aldea"
        "Pasaron unas cuantas horas..."
        "De pronto se escuchó el llanto de un bebé..."
        "Ese fue el momento en el que nació el mejor guerrero azteca, conocido hasta ahora"

        padre "Te pondré Tzilacatzin"

        "Al mismo tiempo a miles de km, en europa, otra madre daba a luz a un bebé llamado Hernán y de apellido Cortez,"
        "El cual se convertiría en uno de los conquistadores más famosos dentro de la historia"
        "Aquellos bebés recién nacidos, no sabían que estaban destinados a encontrarse"
        "Uno nació en un pueblo de muchos dioses, el otro en el de un único dios"

if opcion == "2":
    
    label opcion2:
        
        chico "Tranquila, todo estará bien"
        chica "No puedo soportar este dolor"
        chico "Trata de pujar"
        chica "agh!!"
        
        "Pasaron unas cuantas horas...."
        "De pronto se escuchó el llanto de un bebé"
        "ese fue el momento en el que nació el mejor guerrero azteca, conocido hasta ahora"

        padre "Te pondré Tzilacatzin"

        "Al mismo tiempo a miles de km, en europa, otra madre daba a luz a un bebé llamado Hernán y de apellido Cortez,"
        "El cual se convertiría en uno de los conquistadores más famosos dentro de la historia"
        "Aquellos bebés recién nacidos, no sabían que estaban destinados a encontrarse"
        "Uno nació en un pueblo de muchos dioses, el otro en el de un único dios"

label capitulo2:
    
    "año actual 1524"

    tzilacatzin "Esos que llegaron, por qué creen que son dioses"
    guerrero "No lo se pero los sabios nos ordenaron cuidarlos"

    "Dos guerreros discutían acerca de la llegada de unos extraños a sus tierras, uno cuestionaba que fueran dioses, como creía su pueblo."
    "En ese momento fueron interrumpidos por una chica conocida como Malinali"

    malinalli "No tienen de qué preocuparse, mi marido es buena persona, ya verán"
    tzilacatzin "Eso lo hace más extraño, porque un dios se juntaria con una mortal"
    guerrero "Tranquilízate nos meterás en problemas"

    "Al oír la discusión a lo lejos la persona en cuestión observó al joven guerrero, lo cual causó curiosidad en el"
    "En ese momento, el guerrero sintió la mirada de aquel sujeto, lo cual le dio una extraña sensación de nostalgia."

    hernan "¿De quÉ estais hablando?"
    malinalli "De nada importante, estos sujetos solo tenían dudas de nuestro destino"
    hernan "Ya veo, todo seria mas facil si entendiera su idioma"
    hernan "Por cierto, ¿quién es el?"
    malinalli "Tzilacatzin, es el líder guerrero de los aztecas"
    hernan "Es muy extraño, pero siento que ya lo he visto antes"

    "Ambos tuvieron una extraña sensación, no sabían que hace mucho tiempo se conocieron y que próximamente serian rivales" 
    
    scene batalla:

    "Algunos meses después..."
    
    tzilacatzin "Acaso no te lo dije, sabia que anlgo estaba mal"
    guerrero "Si, quieren acabar con toda la ciudad"
    
    "Una guerra se había desatado en las calles de Tenochtitlan "
    "Los responsables, aquellos extraños que habían llegado a nuestras tierras, liderados por ese tal Hernan…"
    
    tzilacatzin "Rápido, debemos ayudar a los que podamos, y eliminar esos escupe fuego"
    guerrero "Vamos"
    
    "El ruido y daño causado por las armas de estos extraños, llamadas cañones"
    "Eran algo que se debía terminar y estos guerreros lo tenían claro"
    "Guiándose por el sonido, lograron llegar a un bastión enemigo, fuente de algunos cañonazos"
    "Muchos gritos, sonidos de espadas, metal y huesos siendo aplastados fue lo último que se escuchó antes de que el sonido de los cañones cesaran"
    "Sangre y cráneos abiertos, cuerpos mutilados era lo que quedaba de aquellos responsables de cargar y disparar esas armas"
    "El responsable Tzilacaltzin, quien permanecía parado y cubierto en sangre, ante la mirada sorprendida de su compañero guerrero"
    
    guerrero "¿Como hiciste eso?, es lo más rápido que he visto morir a alguien, no me diste tiempo de hacer nada"
    
    "En ese momento se escuchó la alerta de que varios invasores intentaban huir por medio de canoas"
    
    tzilacatzin "Vamos, debemos acabar con ellos."
    
    "Al llegar en una canoa y alcanzar a algunos, el guerrero logró ver al líder de los invasores en la punta"
    "Una ira extraña lo invadió y salgo de su canoa a una de los invasores, y de un movimiento reventó la cabeza de tres de los ocupantes de esa canoa."
    "Salto de canoa en canoa eliminando a los que intentaban huir con el fin de llegar al líder"
    "Pero Hernán logró escapar al dejar atrás las otras canoas que los tontos soldados habían cargado con oro y hacían más lenta su movilidad."
    "Cortés comprendió la gravedad de los eventos y se dio cuenta de su derrota al contemplar su ejército diezmado a la sombra de un árbol…"
    "Un año pasó para que aquellos dos volvieran a encontrarse"
    
    tzilacatzin "Esa cruz que llevas, me es demasiado familiar, me produce nostalgia e irá inexplicable"
    hernan "Y tu te me haces tan conocido, de igual manera me produces nostalgia"
    
    "Ellos no sabían que habían luchado juntos para sobrevivir hace cientos de años, bajo una misma causa"
    
    hernan "Parece que ya no puedes seguir..."
    
    "El guerrero estaba tirado lleno de sangre, con muchas cortadas y uno que otro agujero causado por balas..."
    "A su alrededor toda la calle estaba tapizada de cuerpos de españoles víctimas de sus propias manos"
    
    tzilacatzin "Parece que de nuevo vuelve a pasar"
    hernan "¿ah?"
    
    "De pronto la memoria de una vida pasada invadió al joven guerrero..."
    "Es verdad que al morir ves toda tu vida pasar, pero también tus vidas pasadas.."
    
    tzilacatzin "Ya veo, de nuevo muero por la mano del señor, al menos te vi otra vez viejo amigo"
    
    "Cortés se sorprendió al escuchar y entender al guerrero, el cual hablaba ahora una lengua desconocida por ambos, pero de igual manera entendida."
    "Eso fue el último recuerdo que Cortés tuvo del día en que por fin conquistaron el nuevo continente"
    "El mismo recuerdo y palabras, que en su lecho de muerte al final comprendió"

return