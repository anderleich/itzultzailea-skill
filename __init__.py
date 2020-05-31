from mycroft import MycroftSkill, intent_file_handler


class Itzultzailea(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('itzultzailea.intent')
    def handle_itzultzailea(self, message):
        self.speak_dialog('itzultzailea')


def create_skill():
    return Itzultzailea()

