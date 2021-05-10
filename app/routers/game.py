from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/game",
    tags=["Game"],
    responses={404: {"message": "Not found"}}
)

game_db = [
    {
        "name" : "Dota2",
        "price" : 0
    },
    {
        "name" : "SF",
        "price" : 0
    },
    {
        "name" : "HoN",
        "price" : 0
    },
    {
        "name" : "Fifa 2021",
        "price" : 1800
    },
    {
        "name" : "Naruto",
        "price" : 340
    }
]

class Game(BaseModel):
    name: str
    price: float\

@router.get("/")
async def get_games():
    return game_db

@router.get("/game/{game_id}")
async def get_game(game_id: int):
    return game_db[game_id-1]

# create new game
@router.post("/game")
async def create_game(game: Game):
    game_db.append(game.dict())
    return game_db[-1]

@router.put("/game/{game_id}")
async def edit_game(game_id: int, game: Game):
    result = game.dict()
    game_db[game_id-1].update(result)
    return result

@router.delete("/game/{game_id}")
async def delete_game(game_id: int):
    game = game_db.pop(game_id-1)
    return game