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
