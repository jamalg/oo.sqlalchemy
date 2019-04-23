from datetime import datetime, timezone, timedelta

import pytest
from sqlalchemy import Column, Integer
from sqlalchemy.exc import StatementError

from oo.sqlalchemy import UTCDateTime
from oo.sqlalchemy.helpers import session_manager
from oo.sqlalchemy.test import db


class Model(db.Base):
    __tablename__ = "models"
    id = Column(Integer, primary_key=True)
    date = Column(UTCDateTime)


db.Base.metadata.create_all(db.engine)


def test_utc_datetime():
    with session_manager(db.session) as db_session:
        good_user = Model(date=datetime.now(tz=timezone.utc))
        db_session.add(good_user)
        db_session.commit()

        assert db_session.query(Model).get(good_user.id).date.tzinfo is not None

    # Not using session_manager because it doesn't work well with pytest.raises()
    db_session = db.session()
    bad_user = Model(date=datetime.now())
    db_session.add(bad_user)
    with pytest.raises(StatementError):
        db_session.commit()


def test_datetime_are_written_in_utc():
    with session_manager(db.session) as db_session:
        now_in_utc_less_3 = datetime.now(tz=timezone(timedelta(hours=3)))
        good_user = Model(date=now_in_utc_less_3)
        db_session.add(good_user)
        db_session.commit()

        date = db_session.query(Model).get(good_user.id).date
        assert date.tzinfo == timezone.utc
        assert date == now_in_utc_less_3.astimezone(timezone.utc)
