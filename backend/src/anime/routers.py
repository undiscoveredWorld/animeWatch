from fastapi.routing import APIRouter

from .schemes import AnimeGenreCreate, AnimeGenre
from .schemes import AnimeTagCreate, AnimeTag
from .schemes import AnimeCategoryCreate, AnimeCategory
from .schemes import AnimeStudioCreate, AnimeStudio
from .schemes import SeasonCreate, Season
from common.routers import create_model_types
from common.routers import RouterGenerator

anime_router = APIRouter(tags=["Anime"])
generator = RouterGenerator(anime_router)

genre_models = create_model_types(AnimeGenreCreate, AnimeGenreCreate, AnimeGenre)
generator.generate_all_routers("/genre", genre_models)

tag_models = create_model_types(AnimeTagCreate, AnimeTagCreate, AnimeTag)
generator.generate_all_routers("/tag", tag_models)

category_models = create_model_types(AnimeCategoryCreate, AnimeCategoryCreate, AnimeCategory)
generator.generate_all_routers("/category", category_models)

studio_models = create_model_types(AnimeStudioCreate, AnimeStudioCreate, AnimeStudio)
generator.generate_all_routers("/studio", studio_models)

season_models = create_model_types(SeasonCreate, SeasonCreate, Season)
generator.generate_all_routers("/season", season_models)
