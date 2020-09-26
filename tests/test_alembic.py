"""
Alembic-based tests.

Testing whether current database and code are in sync.
Below I am using alembics autogenerate to create a temporary migration file.
Then I basically assert that the migration is empty.
If it's not empty, database and code are not in sync.

This looks kind of hacky but it seems this is the most stable way to do this.
I saw some people doing the same thing using the alembic classes directly
from python. But there implementations didn't work for me, so I assume
the APIs of these classes were changed with some alembic upgrade.
Here, I am doing the most primitive thing and just use the alembic
command as I would do if I normally use alembic. I figured the CLI is
probably the most stable API. I am actually writing the migration file,
read it, and delete it again.
"""
import os
from pathlib import Path
from subprocess import run

REV_ID = '000000'
MSG = '__test__'
TEST_REVISION_PATH = Path('alembic') / 'versions' / f'{REV_ID}_{MSG}.py'


def remove_revision():
    try:
        os.remove(TEST_REVISION_PATH)
    except FileNotFoundError:
        pass


def read_revision():
    with open(TEST_REVISION_PATH, 'r') as fh:
        lines = fh.readlines()
    lines = [d.strip() for d in lines]
    return [d for d in lines if len(d) > 0 and d[0] != '#']


def test_database_in_sync_with_code():
    try:
        _ = run(['alembic', 'revision', '--autogenerate', '-m',
                 MSG, '--rev-id', REV_ID], capture_output=True, check=True)
        lines = read_revision()
    finally:
        remove_revision()
    idx = lines.index('def upgrade():')
    assert lines[idx + 1] == 'pass', 'no upgrades'
    idx = lines.index('def downgrade():')
    assert lines[idx + 1] == 'pass', 'no downgrade'
