import base64

from src.exc.server_exception import UnsupportedModelException
from ..base_chat import AbstractEntryPoint
from openai import OpenAI
import typing as t
import contextlib
from time import sleep
import requests
from urllib.parse import urljoin

class AiriInstructEntryPoint(AiriEntryPoint):
    def __init__(
        self, base_url: str, api_key: str, emb_dim: int = 1024, providers: list[str] = [], 
    ) -> None:
        self.simple_generatuon_url: str = urljoin(base_url, "chat", "completions")
        self._ERROR_MESSAGE: str = ""
        self.model = ''
    

    def get_response(self, sentence: str):
        with contextlib.suppress(Exception):
            return (
                self._model.chat.completions.create(
                    model=self.model,
                    messages=self.create_payload(system_prompt="", user_prompt=sentence),
                    extra_body=self.extra_body,
                )
                .choices[0]
                .message.content
            )
        return self._ERROR_MESSAGE