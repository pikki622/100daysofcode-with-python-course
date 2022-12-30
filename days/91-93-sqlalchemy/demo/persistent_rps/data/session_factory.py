import sqlalchemy
import sqlalchemy.orm
# noinspection PyPackageRequirements
import db.db_folder as db_folder
# noinspection PyPackageRequirements
from models.model_base import ModelBase
# noinspection PyUnresolvedReferences,PyPackageRequirements
from models import move, player, roll

__factory = None


def global_init():
    global __factory

    full_file = db_folder.get_db_path('rock_paper_scissors.sqlite')
    conn_str = f'sqlite:///{full_file}'

    engine = sqlalchemy.create_engine(conn_str, echo=False)
    ModelBase.metadata.create_all(engine)

    __factory = sqlalchemy.orm.sessionmaker(bind=engine)


def create_session():
    global __factory

    if __factory is None:
        global_init()

    return __factory()
