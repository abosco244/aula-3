from pydantic import BaseModel
from typing import Literal, Any

class Risposta(BaseModel):
    risultato: Any
    esito: Literal["OK", "KO"]