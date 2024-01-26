"""Initial revision

Revision ID: 02789e76bd46
Revises: 
Create Date: 2024-01-26 15:15:04.220447

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02789e76bd46'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'anime', ['id'])
    op.create_unique_constraint(None, 'anime_categories', ['id'])
    op.create_unique_constraint(None, 'anime_tags', ['id'])
    op.create_unique_constraint(None, 'genre_to_anime', ['id'])
    op.create_unique_constraint(None, 'genres', ['id'])
    op.create_unique_constraint(None, 'navigation_elements', ['id'])
    op.create_unique_constraint(None, 'players', ['id'])
    op.create_unique_constraint(None, 'seasons', ['id'])
    op.create_unique_constraint(None, 'seasons_of_anime', ['id'])
    op.create_unique_constraint(None, 'series', ['id'])
    op.create_unique_constraint(None, 'studios', ['id'])
    op.create_unique_constraint(None, 'tag_to_anime', ['id'])
    op.create_unique_constraint(None, 'translates', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'translates', type_='unique')
    op.drop_constraint(None, 'tag_to_anime', type_='unique')
    op.drop_constraint(None, 'studios', type_='unique')
    op.drop_constraint(None, 'series', type_='unique')
    op.drop_constraint(None, 'seasons_of_anime', type_='unique')
    op.drop_constraint(None, 'seasons', type_='unique')
    op.drop_constraint(None, 'players', type_='unique')
    op.drop_constraint(None, 'navigation_elements', type_='unique')
    op.drop_constraint(None, 'genres', type_='unique')
    op.drop_constraint(None, 'genre_to_anime', type_='unique')
    op.drop_constraint(None, 'anime_tags', type_='unique')
    op.drop_constraint(None, 'anime_categories', type_='unique')
    op.drop_constraint(None, 'anime', type_='unique')
    # ### end Alembic commands ###
