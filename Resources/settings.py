import json

file_path = "settings"


def check_settings():  # Check if settings there else create
    try:
        with open(file_path, "r"):
            return True
    except FileNotFoundError:
        with open(file_path, "w") as f:
            f.write("{\n\n}")
        return False


def save(file):  # Save data to settings
    with open(file_path, "w") as f:
        json.dump(file, f, indent=2)


def read():  # Read all Settings to process
    with open(file_path, "r") as f:
        settings = json.load(f)
    return settings


def get(request, cfg=None):  # get data from settings
    if cfg is None:
        cfg = "default"
    settings = read()
    value = settings[str(cfg)][request]
    return value


def edit(data, value, cfg=None):  # edit in settings
    if cfg is None:
        cfg = "default"
    settings = read()
    settings[str(cfg)][data] = value
    save(settings)


def default_settings():  # set default settings
    f = read()
    f["default"] = {}
    f["default"]["user_profile"] = "default"
    f["default"]["resolution_x"] = 500
    f["default"]["resolution_y"] = 500
    f["default"]["dynamic_market"] = True
    f["default"]["auto_save"] = True
    f["default"]["auto_save_duration"] = 180
    f["default"]["sound_enable"] = False
    f["default"]["sound_volume"] = 0
    f["default"]["bgm_enable"] = False
    f["default"]["bgm_volume"] = 0

    save(f)

print(check_settings())
