"""
based on https://github.com/wafflecomposite/15.ai-Python-API
by wafflecomposite
MIT license
"""
from pathlib import Path
from typing import TypedDict, List, Union

import requests
from requests import Session


class Response(TypedDict):
    batch: List[float]
    wavNames: List[str]
    scores: List[float]
    torchmoji: List[Union[float, str]]
    text_parsed: List[str]
    tokenized: List[str]
    dict_exists: List[List[str]]




class FifteenAPI:
    tts_url = "https://api.15.ai/app/getAudioFile5"
    audio_url = "https://cdn.15.ai/audio/"
    max_text_len = 500

    def __init__(self, character: str, emotion: str = "Contextual"):
        self.character = character
        self.emotion = emotion
        self.s = Session()

    def set_progress(self, num: int, of: int) -> None:
        self.s.headers.update({"User-Agent": f"VacuumVoicePack ({num}/{of})"})


    def get_tts(self, text: str) -> Response:
        assert len(text) <= self.max_text_len

        data = {
            "text": text,
            "character": self.character,
            "emotion": self.emotion
        }
        print(data)
        r = self.s.post(self.tts_url, data=data)
        r.raise_for_status()
        return r.json()

    def tts_to_wavs(self, dir: Path, text: str) -> None:
        data = self.get_tts(text)
        dir.mkdir(exist_ok=True)
        print("fetching wav files")
        for i, filename in enumerate(data["wavNames"]):
            print(filename)
            r = requests.get(self.audio_url + filename)
            with open(dir / f"{i}.wav", "wb") as f:
                f.write(r.content)


if __name__ == '__main__':
    api = FifteenAPI(character="GLaDOS")
    print(api.get_tts("This is an example!"))
