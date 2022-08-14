from attrs import define


@define
class Status:
    number: int
    code: str

    @classmethod
    def from_code(cls, code):
        params = {
            'OK': 200,
            'FAILED': 400
        }
        return cls(params[code], code)
