class JsonDict(dict):
    """
    A dictionary that can be serialized to JSON.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"JsonDict({super().__repr__()})"
