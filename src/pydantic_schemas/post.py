from pydantic import BaseModel, validator


class Post(BaseModel):
    id: int
    title: str

    @validator("id")
    def check_that_id_is_less_than_tow(cls, v):
        if v > 2:
            raise ValueError("id is not less than two")
        else:
            return v




# {'id': 1, 'title': 'Post 1'}