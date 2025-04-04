import json
from importlib.resources import files

class DataLoader:

    def load_json(self, filename):
        path = files("slim_common_robot.test_data").joinpath(filename)
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def get_json_path(self, filename):
        return str(files("slim_common_robot.test_data").joinpath(filename))
