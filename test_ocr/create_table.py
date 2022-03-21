# create_table.py
from models import *
import db
import os


if __name__ == "__main__":
    path = SQLITE3_NAME
    if not os.path.isfile(path):

        # テーブルを作成する
        Base.metadata.create_all(db.engine)
    receipt = Receipt(
        date = datetime.date(2022, 3, 18),
        protein = 3,
        carbon = 0,
        fat = 2,
        mineral = 2,
        vitamin = 2,
        fiber = 1,
        description = "金曜特売日"
    )
    db.session.add(receipt)
    db.session.commit()
    db.session.close()  # セッションを閉じる