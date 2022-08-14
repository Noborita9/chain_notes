from attrs import asdict, define
import uuid


@define
class User:
    id_user: uuid.UUID
    name: str
    email: str
    password: str

    @classmethod
    def from_array(cls, row):
        return cls(row[0], row[1], row[2], row[3])

    def to_dict(self):
        return asdict(self)


if __name__ == "__main__":
    pedro = User.from_array(
        [uuid.uuid4(), "pedro", "pedro@gmail.com", "1234qwer"])
    print(pedro.to_dict())
