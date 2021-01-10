import json

from game.story import Story


def load_story() -> Story:
    return json.load(open('./resources/story.json'))


