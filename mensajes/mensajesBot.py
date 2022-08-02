"""
MIT License

Copyright (c) 2021 Standby 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import re
import os


def limpiarPantalla():
    if os.name == "posix":
        return os.system("clear")
    else:
        return os.system("cls")


def mensajeAutor():
    limpiarPantalla()
    print("""
          ("`-/")_.-'"``-._
          . . `; -._    )-;-,_`)
          (v_,)'  _  )`-.\  ``-'
          _.- _..-_/ / ((.'
      ((,.-'   ((,/   By- NFV CY.
      """)


def mensajeBienvenida():
    limpiarPantalla()
    print("""
        ,/|         _.--''^``-...___.._.,;
        /, \'.     _-'          ,--,,,--'''
        { \    `_-''       '    /})
        `;;'            ;   ; ;
    ._.--''     ._,,, _..'  .;.'
    (,_....----'''     (,..--''

        Â¡Bienvenido mortal, puedes probar de este maravilloso bot! Pero recuerda, es una prueba, Â¿Te gusto? Â¡Compralo y estara 24/7!
    """)


def mensajeError(error):
    print(f"\n[An unexpected error occurred]â†’ {error}\n")


def mensajeAyuda_animals():
    animalesAyuda = open(
        "mensajes/mensajesAyuda/mensajesAyuda_Categorias/aminoAyuda_animales.txt",
        "r",
        encoding="utf8")
    aminoAyuda_animales = animalesAyuda.read()

    return aminoAyuda_animales


def mensajeAyuda_actions():
    accionesAyuda = open(
        "mensajes/mensajesAyuda/mensajesAyuda_Categorias/aminoAyuda_acciones.txt",
        "r",
        encoding="utf8")
    aminoAyuda_acciones = accionesAyuda.read()

    return aminoAyuda_acciones


def mensajeAyuda_helper():
    animalesAyudante = open(
        "mensajes/mensajesAyuda/mensajesAyuda_Categorias/aminoAyuda_ayudante.txt",
        "r",
        encoding="utf8")
    aminoAyuda_ayudante = animalesAyudante.read()

    return aminoAyuda_ayudante


def mensajeAyuda_entertainment():
    entretenimientoAyuda = open(
        "mensajes/mensajesAyuda//mensajesAyuda_Categorias/aminoAyuda_entretenimiento.txt",
        "r",
        encoding="utf8")
    aminoAyuda_entretenimiento = entretenimientoAyuda.read()

    return aminoAyuda_entretenimiento


def mensajeAyuda_script():
    guionAyuda = open(
        "mensajes/mensajesAyuda/mensajesAyuda_Categorias/aminoAyuda_guion.txt",
        "r",
        encoding="utf8")
    aminoAyuda_guion = guionAyuda.read()

    return aminoAyuda_guion


def mensajeAyuda_dronex():
    ravninAyuda = open(
        "mensajes/mensajesAyuda/mensajesAyuda_Categorias/aminoAyuda_Ravnin.txt",
        "r",
        encoding="utf8")
    aminoAyuda_ravnin = ravninAyuda.read()

    return aminoAyuda_ravnin


def mensajeAyuda_invisible():
    virguililaAyuda = open(
        "mensajes/mensajesAyuda/mensajesAyuda_Categorias/aminoAyuda_virguilila.txt",
        "r",
        encoding="utf8")
    aminoAyuda_virguilila = virguililaAyuda.read()

    return aminoAyuda_virguilila


def mensajeAyuda_everyone():
    return """[CB]everyone:
 [C]This command is to call everyone in the chat.  Use it well and remember to be careful, they can work for you.  Only use it in case of emergency and activity.  !  >w<
 [c]
 [CB]Usage: -everyone message"""


def mensajeAyuda_id():
    return """[CB]id:
[C]
[C]This is to have the ID of said chat.
[C]
[CB]Uso: -id"""


def mensajeAyuda_siri():
    return """[CB]dronex:
[C]
[C]This command is the same as -speak, but instead of text it tells you with a voice>:3
[C]
[CB]Uso: dronex message"""


def mensajeAyuda_gay():
    return """[CB]gay:
[C]
[C]will tell you how gay you are, muak. uwu
[C]
[CB]Uso: -gay"""


def mensajeAyuda_kick():
    return """[CB]kick:
[C]
[C]This command will kick the user you want to kick. uwu
[C]
[CB]Uso: -kick user"""


def mensajeAyuda_strike():
    return """[CB]Strike:
[C]
[C]This command only works if I am a leader
[C]
[CB]Uso: -strike message"""


def mensajeAyuda_coin():
    return """[CB]coin:
[C]
[C]The most exciting, the most perverse, the most adrelaniÃ±a, is to bet!!!  Remember to pay if you lose.>:3
[C]
[CB]Uso: -coin"""


def mensajeAyuda_leave():
    return """[CB]leave:
[C]
[C]This command will remove your bot from the chat!
[C]
[CB]Uso: -leave"""


def mensajeAyuda_like_comunidad():
    return """[CB]like_comunidad:
[C]
[C]I will put this community on my global profile! :3
[C]
[CB]Uso: -like_community"""


def mensajeAyuda_anfi():
    return """[CB]co-host:
[C]
[C]i will be the host of the chat! >:3
[C]
[CB]Uso: -cohost"""


def mensajeAyuda_coa():
    return """[CB]coa:
[C]
[C]I'll be your chat host!  That is, if I am a coa and you use this command, I will become the host. >:3
[C]
[CB]Uso: -host"""


def mensajeAyuda_chat():
    return """[CB]chat:
[C]
[C]Talk to me! -w-
[C]
[CB]Uso: -chat message
[C]
[C]If you want to know the chat-en info use: -help -chat_en :3"""


def mensajeAyuda_chat_siri():
    return """[CB]chat-en:
[C]
[C]Listen to this sensual voice of mine when responding to what you say to me!! -w-
[C]
[CB]Uso: -dronex message"""


def mensajeAyuda_chat_en():
    return """[CB]chat-en:
[C]
[C]Â¡Este comando quitara es para hablar conmigo en inglÃ©s! -w-
[C]
[CB]Uso: -chat-en mensaje
[C]
[C]Si quieres saber el info de chat-siri usa: -help -chat_siri :3"""


def mensajeAyuda_tr():
    return """[CB]translator:
[C]
[C]Languages?  Don't worry, I'll help you!  ðŸ˜‹
[C]
[CB]Uso: -tr message"""


def mensajeAyuda_purge():
    return """[CB]Purge:
[C]
[C]I delete the messages you want, only if you make me leader or curator ;3
[C]
[CB]Uso: -purge 3"""


def mensajeAyuda_fondo_bot():
    return """[CB]Fund:
[C]
[C]This will put a fund in the bot account.
 [C]
[CB]Uso: -background_bot link to image.jpg"""


def mensajeAyuda_icon_bot():
    return """[CB]icon profile:
[C]
[C]This will put an icon on the bot account.
[C]
[CB]Uso: -icon_bot link of the image.jpg"""


def mensajeAyuda_burbuja():
    return """[CB]icon perfil:
[C]
[C]Esto pondra una burbuja a tu bot.
[C]
[CB]Uso: -burbuja Nombre de la burbuja
[C]
[C]Para sabre el nombre de la burbuja poner:
[C]
[CB]Uso: -burbujas"""


def mensajeAyuda_confession():
    return """[CB]confession:
[C]
[C]Ve a mi priv, y pon una confesion para un usuario que ames mucho >w< o odies mucho, y se lo hare llegar tu mensaje [Todo anonimamente] -n-.
[C]
[CB]Uso: -confession linkdelusuario = mensaje
[C]
[CB]Uso: -confession mensaje"""


def mensajeAyuda_audio():
    return """[CB]audio:
  
[C]Â¿Quieres escuchar mi voz? owo
[C]
[CB] -audio """


def mensajeAyuda_comunidad():
    return """[CB]audio:
  
[C]Este comando hara que vaya a una comunidad mediante un link ywy
[C]
[CB]Uso -comunidad link de la comunidad"""


def mensajeAyuda_pokedex():
    return """[CB]pokedex:
  
[C]Â¡Te dare toda la info de tu pokemon favorito! OwO
[C]
[CB]Uso: -pokedex nombre del pokemon"""


def mensajeAyuda_pat():
    return """[CB]pat:
  
[C]Te daran un pat en la cabezita uwu
[C]
[CB]Uso: -pat"""


def mensajeAyuda_info():
    return """[CB]info:
  
[C]Tiene dos usos, uno para saber tu info y el otro es para saber la del otro usuario. uwu
[C]
[CB]Uso: -info
[C]
[C]El otro uso que le pueden dar es poniendo:
[C]
[CB]Uso: -info @Usuario"""


def mensajeAyuda_facePalm():
    return """[CB]facePalm:
  
[C]AY DIUS MIU
[C]
[CB]Uso: -facePalm"""


def mensajeAyuda_quizz():
    return """[CB]quizz:
[C]
[C]Resolvere cualquier quizz que me pidas.. -w-
[C]
[CB]Uso: -quizz http/aminoapps.com/linkdelquizz"""


def mensajeAyuda_wink():
    return """[CB]wink:
  
[C]GuiÃ±o guiÃ±o codo codo ;3
[C]
[CB]Uso: -wink"""


def mensajeAyuda_img():
    return """[CB]audio:
  
[C]Â¿Quieres ver mi pack...de media/img? owo
[C]
[CB]Uso: -img"""


def mensajeAyuda_kiss():
    return """[CB]kiss:
  
[C]Es un comando para besar apasionadamente aun usuario 7u7
[C]
[CB]Uso: -kiss user"""


def mensajeAyuda_kill():
    return """[CB]kill:
  
[C]Â¡Este comando le da K'O a su oponente enseguida! D':
[C]
[CB]Uso: -kill user"""


def mensajeAyuda_hug():
    return """[CB]hug:
  
[C]Este comando le dara un gran abrazo >w<
[C]
[CB]Uso: -hug user"""


def mensajeAyuda_comment():
    return """[CB]comment:
  
[C]Este comando te comenta tu muro y de un usuario que prefieras, todo anonimante, pero recuerda, Â¡Un gran poder es una gran responsabilidad!.
[C]
[CB]Primer uso, comentar en tu muro: comment MENSAJE
[C]
[CB]Segundo uso, comentar en el muro de otra persona: comment @Usuario = mensajeAutor

Donde es mensaje ponen lo que quieran, y en usuario deben poner el nick del usuario quÃ© esta en el chat. (Recuerden poner el = sino no va a funcionar. Tenkiuuu >w<"""


def mensajeAyuda_virguilila_kiss():
    return """[CB]kiss:
[C] 
[C]Beso fantasma <3
[C]
[CB]Uso: ~kiss user"""


def mensajeAyuda_virguilila_meter():
    return """[CB]meter:
  
E-esto... Es para meter cosas.."""


def mensajeAyuda_virguilila_hug():
    return """[CB]hug:
[C]
[C]Abachooooooooooo >:3
[C]
[BC]Uso: ~hug"""


def mensajeAyuda_virguilila_ban():
    return """[CB]ban:
  
[C]ban fantasma >:l
[C]
[CB]Uso: ~ban user"""


def mensajeAyuda_strikes():
    return """[CB]strike:
  
[C]Este comando...da strikes (?) 
[C]
[CB]Uso: -strike"""


def mensajeAyuda_join():
    return """[CB]join:
  
[C]Este comando es para unirme a tu chat nwn
[C]
[CB]Uso: -join linkdelchat """


def mensajeAyuda_virguilila_lick():
    return """[CB]lick:
  
[C]Este comando es para empezar a lamerte >u<
[C]
[CB]Uso: ~lick manzana """


def mensajeAyuda_virguilila_speak():
    return """[CB]lick:
  
[C]Primo de speak, o sea dira todo lo que tÃº quieras de forma invisible. >u<
[C]
[CB]Uso: ~speak mensaje"""


def mensajeAyuda_virguilila_hit():
    return """[CB]puÃ±etazo:
  
[C]Â¡Te dara una golpiza! >:
[C]
[CB]Uso: ~puÃ±etazo user """


def mensajeAyuda_sacarid():
    return """[CB]sacarid:
  
[C]Â¿Quieres sacar un id? owo
[C]
[CB]Uso: -sacarid http://amino.com/EXAMPLE. """


def mensajeAyuda_punto_fondo():
    return """[CB]Background
 [C]
 [C]Today I will teach you how to use this command!  The first thing you have to do is send an image in the chat (Remember, this command is to add a background to the chat, but only if I am a coa or anfi)
 [C]
 [C] At this point we already have many things clear, now that you sent the background, reply to that same message and put .background, this will put the background you sent in the chat.  (à¹‘â€¢Ì€ã…‚ â€¢Ì )Ùˆâœ§
 [C]
 [CB]Usage: .bg"""


def mensajeAyuda_punto_contenido():
    return """[CB]content
 [C]
 [C]Today I will teach you how to use this command!  The first thing you have to do is put .content Hello how are you and this will put in the biography of the chat Hello how are you, you can send any text you want.  (à¹‘â€¢Ì€ã…‚ â€¢Ì )Ùˆâœ§
 [C]
 [CB]Usage: .message content"""


def mensajeAyuda_punto_view():
    return """[CB]view
[C]
[C]Â¡Hoy te enseÃ±are a usar este comando! Lo primero que tienes que hacer es poner .view cualquier cosa y esto pondra el chat en modo visualizacion, y si pones .view quitara el modo visualizacion del chat. Recuerden, si ponen solo view se desactiva, y si ponen una palabra lo activan. (à¹‘â€¢Ì€ã…‚ â€¢Ì)Ùˆâœ§ 
[C]
[CB]Activar: .view palabra
[CB]Desactivar: .view"""


def mensajeAyuda_punto_anuncio():
    return """[CB]anuncio
[C]
[C]Â¡Hoy te enseÃ±are a usar este comando! Lo primero que tienes que hacer es poner .anuncio Hola como estas y esto pondra un anuncio del chat con Hola como estas, puedes mandar cualquier texto que quieras. (à¹‘â€¢Ì€ã…‚ â€¢Ì)Ùˆâœ§ 
[C]
[CB]Uso: .anuncio mensaje"""


def mensajeAyuda_punto_fijar():
    return """[CB]fijar
[C]
[C]Â¡Hoy te enseÃ±are a usar este comando! Lo primero que tienes que hacer es poner .fijar palabra (Puede ser cualquier cosa) y esto quitara el mensaje de anuncio, y si pones .fijar fijaras un anuncio.. Pero espera, Â¿Cual anuncio? Â¡Usa el comando .anuncio! (à¹‘â€¢Ì€ã…‚ â€¢Ì)Ùˆâœ§ 
[C]
[CB]Activar: .fijar palabra
[CB]Desactivar: .fijar"""


def mensajeAyuda_punto_invitar():
    return """[CB]invitar
[C]
[C]Â¡Hoy te enseÃ±are a usar este comando! Lo primero que tienes que hacer es poner .invitar palabra (Puede ser cualquier palabra) y esto hara que cualquiera pueda invitar a su amigo al chat, pero si pones .invitar solo los coa y anfi podran invitar. (à¹‘â€¢Ì€ã…‚ â€¢Ì)Ùˆâœ§ 
[C]
[CB]Activar: .invitar palabra
[CB]Desactivar: .invitar"""


def mensajeAyuda_punto_clave():
    return """[CB].clave
[C]
[C]Â¡Hoy te enseÃ±are a usar este comando! Lo primero que tienes que hacer es poner .clave Hola, y esto pondra palabras claves en el chat. (à¹‘â€¢Ì€ã…‚ â€¢Ì)Ùˆâœ§ 
[C]
[CB]Uso: .clave palabra"""


def mensajeAyuda_punto_portada():
    return """[CB]portada
[C]
[C]Â¡Hoy te enseÃ±are a usar este comando! Lo primero que tienes que hacer es mandar una imagen en el chat (Recuerda, este comando es para ponerle portada al chat, pero solo si soy coa o anfi)
[C]
[C]En este punto ya tenemos claros muchas cosas, ahora que enviaste el portada responde ese mismo mensaje y pon .portada, esto pondra la imagen que envias como foto de portada del chat. (à¹‘â€¢Ì€ã…‚ â€¢Ì)Ùˆâœ§ 
[C]
[CB]Uso: .portada"""


def mensajeAyuda_punto_ban():
    return """[CB].ban
[C]
[C]Â¡Hoy te enseÃ±are a usar este comando! Lo primero que tienes que hacer es poner .ban link del perfil del usuario = Razon del Baneo, y esto lo baneara de la comunidad. Usalo solo si es necesario y no esta algun lider. Â¡Recuerda poner el = con el motivo del baneo, se chico/a e informa! (Este comando no tiene efecto contra el staff) (à¹‘â€¢Ì€ã…‚ â€¢Ì)Ùˆâœ§ 
[C]
[CB]Uso: .ban https://aminoapps/linkdelusuario.com = razon del baneo"""


def mensajeAyuda_punto_strike():
    return """[CB].strike
[C]
[C]Today I will teach you how to use this command!  The first thing you have to do is put .strike link of the user's profile = Ban Reason, and this will ban him from the community.  Use it only if necessary and there is no leader.  Remember to put the = with the reason for the ban, be a kid and report!  (This command has no effect against staff) 
[C]
[CB]Uso: .strike https://aminoapps/link of user.com = reason for the ban"""


def mensajeAyuda_punto_bloquear():
    return """[CB].block
 [C]
 [C]Today I will teach you how to use this command!  The first thing you have to do is put .block user link, and this will block the user from using the commands.  
 [C]
 [CB]Usage: .block https://aminoapps/userlink.com"""


def mensajeAyuda_punto_titulo():
    return """[CB].title
 [C]
 [C]Today I will teach you how to use this command!  The first thing you have to do is put .title Hello how are you, and this will change the title of the chat to Hello how are you, it can be any message or title you want.  (à¹‘â€¢Ì€ã…‚ â€¢Ì )Ùˆâœ§
 [C]
 [CB] Usage: .message title"""


def mensajeAyuda_punto_warn():
    return """[CB].warn
 [C]
 [C]Today I will teach you how to use this command!  The first thing you have to do is put .warn link of the user = reason for the warning, remember it is important to put the link and the =, otherwise it will give you an error.  (à¹‘â€¢Ì€ã…‚ â€¢Ì )Ùˆâœ§
 [C]
 [CB]Usage: .warn user link = warning reason"""
