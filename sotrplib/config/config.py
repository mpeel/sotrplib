from typing import Any
from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pathlib import Path
import json

class Settings(BaseSettings):
	test: int = 1
	teststr: str = 'Test'

	model_config = SettingsConfigDict(env_prefix='sotrp_')

	@classmethod
	def from_file(cls, config_path: Path | str) -> "Settings":
		with open(config_path, "r") as handle:
			return cls.model_validate_json(handle.read())

