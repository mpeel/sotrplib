from sotrplib.config.config import Settings

# These are the default settings
print(Settings)
print(Settings().model_dump())

# This is reading in from a file
MySettings = Settings.from_file("/Users/mpeel/Documents/git/sotrplib/sotrplib/config/test_config.json")

print(MySettings)
print(MySettings.test)