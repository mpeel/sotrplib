from typing import Any
from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pathlib import Path
import json

class Settings(BaseSettings):
	test: int = 1
	teststr: str = 'Test'

	config_json: str = '/Users/mpeel/Documents/git/sotrplib/sotrplib/config/test_config.json'

	model_config = SettingsConfigDict(env_prefix='sotrp_')

	@classmethod
	def from_file(cls, config_path: Path | str) -> "Settings":
		with open(config_path, "r") as handle:
			return cls.model_validate_json(handle.read())


def load_settings() -> Settings:
	"""
	Load the settings from the config file.
	"""

	path = Settings().config_json
	if path is not None:
		path = Path(path)
		if path.exists():
			try:
				_settings = Settings.from_file(path)
			except ValidationError as e:
				print(f"Error loading settings from {path}: {e}")
				raise e

			return _settings
		try:
			_settings = Settings()
		except ValidationError as e:
			print(f"Not all settings have defaults: {e}")
			raise e

	return _settings



def __getattr__(name):
	"""
	Try to load the settings if they haven't been loaded yet.
	"""

	if name == "HELLO_WORLD":
		return "Hello World!"

	if name == "server_settings":
		global _settings

		if _settings is not None:
			return _settings

		return load_settings()

	raise AttributeError(f"module '{__name__}' has no attribute '{name}'")