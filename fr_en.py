import config_selfbot

#######################
#  selfbot            #
#    translation >.<  #
#######################

enable = {
    "fr": "activé",
    "en": "enabled"
}

disable = {
    "fr": "désactivé",
    "en": "disabled"
}



####################
#  launch          #
# translation !!!  #
####################

start_text = {
    "fr": "Démarrage du SelfBot en cours...",
    "en": "Starting the SelfBot..."
}

ready_text = {
    "fr": "Connecté en tant que",
    "en": "Connected as"
}

ready_text_two = {
    "fr": "démarré en",
    "en": "started in"
}

error_check_version_one = {
    "fr": "Une nouvelle version",
    "en": "A new version"
}

error_check_version_two = {
    "fr": "est disponible:",
    "en": "is out at:"
}

error_check_version_three = {
    "fr": "Vous utilisez actuellement la version",
    "en": "You are currently using"
}

####################
#  help            #
# translation !!!  #
####################



help_voice = {
    "fr": "Vocal",
    "en": "Voice"
}

help_general_snipe = {
    "fr": "(tout les serveurs)",
    "en": "(all servers)"
}

help_general_hype = {
    "fr": "Défini votre badge HypeSquad",
    "en": "Set your HypeSquad badge"
}

help_general_ping = {
    "fr": "Affiche la latence du SelfBot",
    "en": "Display the Selfbot's ping"
}

help_general_sniper = {
    "fr": "Active / désactive le NitroSniper",
    "en": "Enable / disable NitroSniper"
}

help_config_restart = {
    "fr": "Redémarre le SelfBot (peut régler un bug)",
    "en": "Restart the SelfBot. (it can fix a bug)"
}

help_config_stop = {
    "fr": "Stop le SelfBot",
    "en": "Stop the SelfBot"
}

help_general_bio = {
    "fr": "Change la biographie du compte",
    "en": "Change account's bio"
}


help_voice_vc = {
    "fr": "Rejoins le salon vocal",
    "en": "Join the voice channel"
}

help_voice_cam = {
    "fr": "Rejoins le salon vocal avec une fausse caméra",
    "en": "Join the voice channel with a fake camera"
}

help_voice_stream = {
    "fr": "Rejoins le salon vocal avec un faux stream",
    "en": "Join the voice channel with a fake stream"
}

help_voice_leave = {
    "fr": "Quitte le salon vocal",
    "en": "Leave the voice channnel"
}

help_fun_cat = {
    "fr": "Chat mignon 🐈",
    "en": "Cute cat 🐈"
}

help_fun_good = {
    "fr": "Vous transforme en une Bonne Personne ! (*censure les insultes*)",
    "en": "Transform you into a Good Person ! (*no insults*)"
}

help_fun_call = {
    "fr": "Spam d'appel (le salon doit être un salon vocal !)",
    "en": "Join and Leave the voice (the channel must be a voice channel!)"
}

help_fun_gift = {
    "fr": "Envoie un faux lien Nitro",
    "en": "Send a fake Nitro"
}


####################
#  commands        #
# translation !!!  #
####################

restart_command = {
    "fr": "✅ Le SelfBot a bien été redémarré (patientez quelques secondes...) !",
    "en": "✅ Succesfully restarted the SelfBot (wait a couple of seconds...)!"
}

stop_command = {
    "fr": "⭕ Le SelfBot a bien été stopper.",
    "en": "⭕ Succesfully stopped the SelfBot."
}

ai_response = {
    "fr": "Réponse",
    "en": "Answer"
}

ai_wait = {
    "fr": "patientez", 
    "en": "wait"
}

ai_help = {
    "fr": "Posez une question à l'IA", 
    "en": "Ask a question to an IA"
}

ai_error = {
    "fr": "❌ Vous devez configurer l'e-mail et le mot de passe dans ``config_selfbot.py`` !",
    "en": "❌ You must configure e-mail and password in ``config_selfbot.py``!"
}

leave_voice = {
    "fr": "Déconnection du salon",
    "en": "Disconnected from"
}

leave_voice_error = {
    "fr": "Error while leaving the voice channel",
    "en": "Erreur lors de la déconnexion au salon vocal"
}

hype_command = {
    "fr": "modifié en",
    "en": "changed to"
}

bio_command = {
    "fr": "changée en",
    "en": "changed to"
}

spam_cooldown = {
    "fr": f"❌ Un spam est déjà en cours ! Pour l'arrêter, faites `{config_selfbot.prefix}restart`.",
    "en": f"❌ A spam is already active! To spam the current spam, do `{config_selfbot.prefix}restart`."
}

spam_invalid = {
    "fr": f"❌ Veuillez indiquer un nombre valide !",
    "en": f"❌ You must enter a valid number!"
}

voice_join = {
    "fr": "Connecté au salon vocal",
    "en": "Connected to"
}

voice_join_error = {
    "fr": "Erreur lors de la connexion au salon vocal",
    "en": "Error while trying to connect to the voice channel"
}

voice_join_cam = {
    "fr": "Connecté au salon vocal",
    "en": "Connected to"
}

voice_join_cam_two = {
    "fr": "avec la caméra activée",
    "en": "with camera"
}

voice_stream_join = {
    "fr": "avec le stream activé",
    "en": "with stream"
}




####################
#  rpc             #
# translation !!!  #
####################




rpc_status_translate = {
    "fr": "Défini le statut du RPC",
    "en": "Set RPC's status"
}

rpc_name_translate = {
    "fr": "Défini le nom du RPC",
    "en": "Set RPC's name"
}

rpc_details_translate = {
    "fr": "Défini les details du RPC",
    "en": "Set RPC's details"
}

rpc_state_translate = {
    "fr": "Défini le \"state\" du RPC",
    "en": "Set RPC's state"
}

rpc_url_translate = {
    "fr": "Défini l'url de steaming du RPC ``(https://twitch.tv/nom)``",
    "en": "Set RPC's streaming URL ``(https://twitch.tv/name)``"
}

rpc_id_translate = {
    "fr": "Défini l'ID de l'application pour le RPC",
    "en": "Set RPC's Application ID"
}

rpc_image_translate = {
    "fr": "Défini l'image du RPC",
    "en": "Set RPC's image"
}

rpc_button_text_one_translate = {
    "fr": "Défini le texte du premier bouton du RPC",
    "en": "Set RPC's first button text"
}

rpc_button_link_one_translate = {
    "fr": "Défini le lien du premier bouton du RPC",
    "en": "Set RPC's first button link"
}

rpc_button_text_two_translate = {
    "fr": "Défini le texte du second bouton du RPC",
    "en": "Set RPC's second button text"
}

rpc_button_link_two_translate = {
    "fr": "Défini le lien du second bouton du RPC",
    "en": "Set RPC's second button link"
}




####################
# template         #
# translation !!!  #
####################

template_help_reset = {
    "fr": "Réinitialise votre RPC.",
    "en": "Reset your RPC."
}

template_help_default = {
    "fr": "Modifie votre RPC par défaut (`config_selfbot.py`).",
    "en": "Edit your RPC to default (`config_selfbot.py`)."
}

template_help_cod = {
    "fr": "Utilise la template \"Call Of Duty\".",
    "en": "Use \"Call Of Duty\"'s template."
}

template_help_dark = {
    "fr": "Utilise la template \"dark\".",
    "en": "Use \"dark\" template."
}

template_help_python = {
    "fr": "Utilise la template \"Python\".",
    "en": "Use \"Python\" template."
}

template_help_js = {
    "fr": "Utilise la template \"JavaScript\".",
    "en": "Use \"JavaScript\" template."
}

template_help_omori = {
    "fr": "Utilise la template \"Omori\".",
    "en": "Use \"Omori\" template."
}

template_help_car = {
    "fr": "Utilise la template \"Car\".",
    "en": "Use \"Car\" template."
}

template_help_self = {
    "fr": "Utilise la template \"Nuclear\".",
    "en": "Use \"Nuclear\" template."
}

template_help_webdeck = {
    "fr": "Utilise la template \"WebDeck\".",
    "en": "Use \"WebDeck\" template."
}

template_help_hi = {
    "fr": "Utilise la template \"Hi !\".",
    "en": "Use \"Hi !\" template."
}

template_help_youtube = {
    "fr": "Utilise la template \"Python\".",
    "en": "Use \"Python\" template."
}

template_help_gta = {
    "fr": "Utilise la template \"GTA VI\".",
    "en": "Use \"GTA VI\" template."
}



rpc_cod_details = {
    "fr": "En attente de mission...",
    "en": "Waiting for a mission..."
}

rpc_cod_state = {
    "fr": "En attente de mission...",
    "en": "In the main menu"
}


tutorial_rpc = {
    "fr": f""" Pour obtenir une image personnalisé:
  1. Envoyer une image (gif, png...) dans Discord. (dans n'importe quelle salon)
  2. Clique droit et "Copier l'adresse de l'image".
  3. Faites `{config_selfbot.prefix}rpc_image mp:attachements/67484738743874387438/657438923487543/exemple.png`.
  4. Fini !""",
    "en": f""" To get a custom rpc image, you should:
  1. Upload an image (gif, png...) into Discord. (in any channel)
  2. Right Click and "Copy Image Link".
  3. Do `{config_selfbot.prefix}rpc_image mp:attachements/67484738743874387438/657438923487543/example.png`.
  4. Done !"""
}