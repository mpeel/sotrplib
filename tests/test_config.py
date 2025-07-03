from sotrplib.config.config import Settings, load_settings

print(Settings().model_dump())

print(Settings().test)
print(Settings().teststr)

load_settings()



print(Settings().test)
print(Settings().teststr)