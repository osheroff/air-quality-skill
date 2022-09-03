from mycroft import MycroftSkill, intent_file_handler


class AirQuality(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('quality.air.intent')
    def handle_quality_air(self, message):
        self.speak_dialog('quality.air')


def create_skill():
    return AirQuality()

