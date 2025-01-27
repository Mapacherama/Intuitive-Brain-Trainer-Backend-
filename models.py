from pydantic import BaseModel

class Reflection(BaseModel):
    id: str      # Unique ID for the reflection
    date: str    # Date of the reflection
    content: str # The reflection text