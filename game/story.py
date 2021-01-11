import json
from json import JSONEncoder


class Story(object):
    def __init__(self, chapters):
        self.chapters = chapters


class StoryEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Story):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)


def from_json(data):
    p = Story()
    p.__dict__.update(data)
    return p
