from uuid import uuid1

from CrowdAnki.common_constants import UUID_FIELD_NAME
from CrowdAnki.json_serializable import JsonSerializableAnkiDict


class DeckConfig(JsonSerializableAnkiDict):
    # filter_set = JsonSerializableAnkiDict.filter_set | {}

    def __init__(self, anki_deck_config=None):
        super(DeckConfig, self).__init__(anki_deck_config)

    @classmethod
    def from_collection(cls, collection, deck_config_id):
        anki_dict = collection.decks.getConf(deck_config_id)
        deck_config = DeckConfig(anki_dict)
        deck_config._update_fields()

        return deck_config

    def save_to_collection(self, collection):
        # Todo whole uuid matching thingy
        # For now only create scenario

        # self.anki_dict["id"] = collection.decks.confId(self.anki_dict["name"], self.anki_dict)
        new_id = collection.decks.confId(self.anki_dict["name"], self.anki_dict)
        self.anki_dict = collection.decks.getConf(new_id)