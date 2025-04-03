import pathlib
from typing import Literal

import pydantic

from ._hotkey import Hotkey


class HotkeySet(pydantic.BaseModel):
    model_config = {'populate_by_name': True}

    items: dict[str, Hotkey] = pydantic.Field(
        default_factory=dict
    )

    def add(self, name: str, hotkey: str):
        key = Hotkey.model_validate({'name': name, 'hotkey': hotkey})
        self.items[key.qualname] = key

    def load(
        self,
        path: pathlib.Path,
        mode: Literal['public', 'private', 'phrase']
    ):
        for hotkey in self.items.values():
            hotkey.load(path, mode=mode)