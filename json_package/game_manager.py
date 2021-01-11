import json

import pykson
from game.story import Story

story = Story([])


def load_story() -> Story:
    global story
    story = pykson.Pykson().from_json(json.load(open('./resources/story.json')), Story)
    return story


def get_story():
    return story
