"""Change users table

Revision ID: da97701bef66
Revises: f7d61be24f3b
Create Date: 2026-10-02 01:16:10.240918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da97701bef66'
down_revision: Union[str, Sequence[str], None] = 'f7d61be24f3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("users") as batch_op:
        batch_op.create_unique_constraint("uq_users_phone_number", ["phone_number"])
        batch_op.create_unique_constraint("uq_users_national_id", ["national_id"])


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_constraint("uq_users_phone_number", type_="unique")
        batch_op.drop_constraint("uq_users_national_id", type_="unique")
