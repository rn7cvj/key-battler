from pydantic import BaseModel


class RatingIn(BaseModel):
    text_id: int
    speed: int
    correct_rate: int
    user_id: int