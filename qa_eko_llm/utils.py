from pathlib import Path

def get_root():
    return Path(__file__).parent.parent

def get_data_path():
    return get_root() / "data"


if __name__ == "__main__":
    print(
        get_data_path()
    )