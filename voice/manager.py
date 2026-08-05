from voice.listen import listen


voice_mode = False


def enable_voice():

    global voice_mode

    voice_mode = True


def disable_voice():

    global voice_mode

    voice_mode = False


def is_voice():

    return voice_mode


def get_command():

    if voice_mode:

        return listen()

    return input("Harry: ")