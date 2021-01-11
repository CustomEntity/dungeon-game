import json_package.progression_manager as progress
from game.actions.action import TalkAction
from game.story import Story

story = Story([])


def load_story() -> Story:
    global story
    # TODO: Load from story.json
    # story = pykson.Pykson().from_json(json.load(open('./resources/story.json')), Story)
    story.actions = {
        TalkAction("Chapitre 1: Le début d'un long périple", "Kirito",
                   ["Où suis-je ?", "Ce n'est pas ma chambre"]): TalkAction("Chapitre 1: Le début d'un long périple",
                                                                            "Kirito", ["Je vais essayer de rentrer"]),
        TalkAction("Chapitre 1: Le début d'un long périple", "Kirito", ["Oups"]): [
            TalkAction("Chapitre 1: Le début d'un long périple", "Kirito", ["Test 1 2 1 2"])],
    }
    return story


def get_current_action_object():
    progression = progress.get_progression().get_current_action()
    return next(v for i, v in enumerate(iter(story.actions.items())) if i == progression[0])[progression[1]]


def get_previous_action_object():
    progression = progress.get_progression().get_previous_action()
    return next(v for i, v in enumerate(iter(story.actions.items())) if i == progression[0])[progression[1]]




def get_story():
    return story
