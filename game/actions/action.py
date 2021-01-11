from abc import abstractmethod

from game.chapter import Chapter
from pykson import JsonObject, StringField, ObjectField


# class Action(JsonObject):
#     chapter = ObjectField(Chapter)
#     type = StringField()
#     content = StringField()
#
#     def __init__(self, chapter, type, content):
#         super(Action, self).__init__()
#         self.chapter = chapter
#         self.type = type
#         self.content = content

class Action:

    @abstractmethod
    def __init__(self, chapter):
        super(Action, self).__init__()
        self.chapter = chapter


class TalkAction(Action):

    def __init__(self, chapter, talker, messages):
        super().__init__(chapter)
        self.talker = talker
        self.messages = messages


class ChoiceAction(Action):

    def __init__(self, chapter, ):
        super().__init__(chapter)

