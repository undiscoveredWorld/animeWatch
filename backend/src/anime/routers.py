from fastapi.routing import APIRouter

from common.routers import RouterGenerator
from common.routers import create_model_types
from .schemas import AnimeGenreCreate, AnimeGenre
from .schemas import AnimeTagCreate, AnimeTag
from .schemas import AnimeCategoryCreate, AnimeCategory
from .schemas import AnimeStudioCreate, AnimeStudio
from .schemas import SeasonCreate, Season
from .schemas import AnimeCreate, Anime

anime_router = APIRouter(tags=["Anime"])
generator = RouterGenerator(anime_router)

genre_models = create_model_types(AnimeGenreCreate, AnimeGenreCreate, AnimeGenre)
generator.generate_all_end_points("/genre", genre_models)

tag_models = create_model_types(AnimeTagCreate, AnimeTagCreate, AnimeTag)
generator.generate_all_end_points("/tag", tag_models)

category_models = create_model_types(AnimeCategoryCreate, AnimeCategoryCreate, AnimeCategory)
generator.generate_all_end_points("/category", category_models)

studio_models = create_model_types(AnimeStudioCreate, AnimeStudioCreate, AnimeStudio)
generator.generate_all_end_points("/studio", studio_models)

season_models = create_model_types(SeasonCreate, SeasonCreate, Season)
generator.generate_all_end_points("/season", season_models)

anime_models = create_model_types(AnimeCreate, AnimeCreate, Anime)
generator.generate_all_end_points("/anime", anime_models)
