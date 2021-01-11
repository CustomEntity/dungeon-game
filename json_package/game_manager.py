import json

from game.story import Story, from_json

story = Story()


def load_story() -> Story:
    global story
    story = from_json(open('./resources/story.json'))
    return story


def get_story():
    return story
