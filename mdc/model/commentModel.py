import json
import datetime
from typing import Optional

from dataclasses import dataclass, asdict, field
from data_model.common import Comment as dmComment


class CommentModel():

    @dataclass(frozen=False)
    class Comment():

        author: str = None
        timestamp_utc: Optional[datetime.datetime] = None
        comment: str = None

        @property
        def as_dict(self):
            """Get Comment as dictionary"""

            return asdict(self)

        @property
        def as_json(self):
            return json.dump(self.as_dict)

        def isValid(self) -> tuple[bool, Comment | None]:
            """Validate comment"""

            try:
                return True,CommentModel.Comment(**dmComment(**self.as_dict()).dict())
            except Exception as e:
                print("Validation failed")
                return False,None

    def __init__(self):
        self.comment = self.Comment()


if __name__== "__main__":
    cm = CommentModel()
    cm.comment.author = "valaki"
    print(cm.comment.as_json)
