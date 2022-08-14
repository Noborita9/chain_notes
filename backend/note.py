from attrs import define, field, asdict


@define
class Note:
    id: int = field(default=0)
    title: str = field(default="New Title")
    content: str = field(default="Note Content")

    @classmethod
    def from_array(cls, row):
        if len(row) == 2:
            return cls(0, row[0], row[1])
        else:
            return cls(row[0], row[1], row[2])

# nota = Note(1, "Do bed", "Just Do It")
#
# print(nota.get_dict())
