import uuid
from attrs import define, field, asdict


@define
class Note:
    id_note: uuid.UUID
    title: str
    content: str

    @classmethod
    def from_array(cls, row):
        return cls(row[0], row[1], row[2])

    def to_dict(self):
        return asdict(self)

# nota = Note(1, "Do bed", "Just Do It")
#
# print(nota.get_dict())
