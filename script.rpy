# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image casadostenma = "backgrounds/casa-dos-tenma.png"
image corredordaescolamimimi = "backgrounds/girls-academy-corredor.png"
image quartodotsukasa = "backgrounds/quarto-do-tsukasa.jpg"
image rua = "backgrounds/png"
image saladeaulagirls = "backgrounds/sala-das-garotas.png"
image WxSsekai = "backgrounds/WxS-sekai.png"
image preta = "backgrounds/preta.png"
define Tsukasa = Character("Tsukasa")
define Saki = Character("Saki")
define Emu = Character("Emu")
define Rui = Character("Rui")
define Nene = Character("Nene")
define Professora = Character("Professora")
define Ichika = Character("Ichika")
define Honami = Character("Honami")
define Shiho = Character("Shiho")
define Toya = Character("Toya")
define Akito = Character("Akito")
define Minori = Character("Minori")
#  sinal = "sinal.mp3"
#  KABOOOOOOOOOM = "KABOOOOOOOOOM.mp3"
# The game starts here.

label start:


    scene quartodotsukasa
    show irmao_acordando

    Tsukasa "-aaaaaah, que fome vo comer."
    hide irmao
    
    scene irmavendotv
    "ao descer Tsukasa ve a sua irma"

    scene casadostenma

    hide irmao_acordando
    show irmaofeliz at left
    show irmafeliz at right
    
    Tsukasa "BOM DIA! Uh? você esta vendo as noticias?"
    Saki "Bom dia! Sim, não tem nada para fazer, ta chovendo."
    Tsukasa "Oh, tabom.... eu acho"
    scene tv
    hide irmaofeliz
    hide irmafeliz
    "voce ouve um pouco das noticias"
    "um novo virus foi encontrado no laboratorio de ------ é recomendado ficar lon-"
    # tv desliga
    scene casadostenma
    show irmaocurioso
    show irmafeliz
    Tsukasa"-então como esta as meninas irma?"
    Saki "-nos estamos cantando super bem! você poderia ir la na live house ver um dos nossos shows!"
    Tsukasa"bem, nos devemos ir, voce vai ficar atrasada e eu tenho que me encontrar com os meus amigos"
    scene preta

    menu:
        "irma":
            jump cenairma
        "irmao":
            jump cenairmao
    return

label cenairma:
    
    scene corredordaescolamimimi

    "a irma vai ate a escola para garotas, la ela encontra suas três melhores amigas"
    show Ichika at right
    show irmafeliz at left
    Ichika"saki, voce chegou"
    hide Ichika
    show Honami at right
    Honami"nos estávamos ficando preocupadas você não e de se atrasar..."
    Saki"hehehe! a rua da minha casa estava meio alagada."
    hide Honami
    show Shiho at right
    Shiho"bem, ela esta aqui e isso é o que importa."
    play sound "audio/sinal.mp3"
    "TRI TRI TRI TRI!"
    scene saladeaulagirls
    hide Shiho
    hide irmafeliz
    show professora
    Professora"entao vamos começa-"
    hide professora
    play sound "audio/KABOOOOOOOOOM.mp3"
    "KABOOOOOOOOOM"
    return

label cenairmao:
    scene WxSsekai
    "ele vai ate o Sekai onde ele e seus amigos treinam show"
    show irmafeliz
    Tsukasa"hehehe! a futura estrela chegou!"
    hide irmafeliz
    show wonderhoy
    Emu"WONDERHOY! voce chegou, entao vamos praticar para o show de quinta?"
    hide wonderhoy
    show wonderhoysorriso at right
    show Rui at left
    Rui"bem, so faltava ele mesmo ne, nene?"
    hide wonderhoysorriso
    show n at right
    Nene"poise..."
    "depois de muito trabalho, o irmão e a wonderhoy vao para um lado e o 'r' e a 'n' vao para outro."
    hide n 
    hide r
    show wonderhoy
    Emu"bem, isso foi bem divertido! tchaaaaau!"
    hide wonderhoy
    scene rua
    "um tempo andando depois... o irmão e a wonderhoy passam perto do laboratório e então..."
    scene tropeco
    "e entao ouvem um pip e-"
    scene preta
    play sound "audio/KABOOOOOOOOOM.mp3"
    "KABOOOOOOOOOM!"

    menu:
        "continuar":
            jump capitolo2T
        "voltar para a escolha":
            jump start
    return


label capitolo2T:
    scene hospital
    "-voce acorda em um lugar estranho, sem onde esta, olhando pros lados ele percebe que esta em uma espécie de hospital, ele se senta na cama e sente uma grande dor de cabeça."
    show irmaocomsono
    Tsukasa"uhh... oque... aconteceu...?"
    hide irmaocomsono
    "-ele se levanta e vai em direção a porta, mas antes de conseguir abrir sua irmã aparece no quarto muito preocupada-"
    show irmacomnovaroupa
    Saki"irmão! ai meu deus eu fiquei tao preocupada!"
    hide irmacomnovaroupa
    show irmaoconfuso at left
    show irmacomnovaroupafeliz at right
    Tsukasa"Saki... oque... aconteceu..?"
    Saki"esta acontecendo um apocalipse!"
    hide irmaoconfuso
    show irmaoassustado at left
    Tsukasa"oque!"
    hide irmacomnovaroupafeliz
    show irmacomnovaroupatriste at right
    Saki"isso mesmo, tudo começou depois da explosão, você e a Emu foram levados para o hospital, ela acordou primeiro... so que estranha... ela apenas falava wonderhoy... então do nada. ELA COMEÇOU A ATACAR TODO MUNDO! tiveram de evacuar o hospital depois disso..."
    hide irmaoassustado
    show irmaoconfuso at left
    Tsukasa"...meu deus..."
    Saki"eu estou preocupada com as minhas amigas... nos não a encontramos em lugar nenhum..."
    Tsukasa"nos?"
    hide irmacomnovaroupatriste
    show irmacomnovaroupafeliz
    Saki"sim, nos, vem vamos falar com o resto do pessoal"
    hide irmaoconfuso
    hide irmacomnovaroupafeliz
    scene reuniao
    "-você e sua irma saem desse quarto de hospital e vao para a sala desse local encontrando alguns amigos" 
    scene basepartedasala
    show irmacomnovaroupafeliz
    Saki"Gente! Ele acordou"
    hide irmacomnovaroupafeliz
    show Toya
    Toya"Nos estavamos preocupados"
    hide Toya
    show Toya at left
    show Nene at right
    Nene"Nos estavamos preocupados"
    hide Toya
    show Minori at left
    Minori"Que alivio, pensei que voce nao  iria mais acordar..."
    hide Nene
    show irmaoinvergonhado at right
    Tsukasa"Meu deus, nao fala isso! hehehe"
    hide Minori
    show Akito at left
    Akito"tambem, depois de uma semana"
    hide irmaoinvergonhado
    show irmaoassustado
    Tsukasa"UMA SEMANA?!?!"
    hide Akito
    








