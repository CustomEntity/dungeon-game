import json

from game.story import Story

story = Story()


def load_story() -> Story:
    global story
    story = json.load(open('./resources/story.json'))
    return story


def get_story():
    return story
