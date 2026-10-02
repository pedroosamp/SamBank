"""add account user foreign key

Revision ID: 479bc53f5bcd
Revises: a65a34f4d3a3
Create Date: 2026-10-02 15:20:14.076777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '479bc53f5bcd'
down_revision: Union[str, Sequence[str], None] = 'a65a34f4d3a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("accounts") as op_batch:
        op_batch.create_foreign_key('fk_accounts_user_id_users', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("accounts") as op_batch:
        op_batch.drop_constraint('fk_accounts_user_id_users', type_='foreignkey')
    # ### end Alembic commands ###
