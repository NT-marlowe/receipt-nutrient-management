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
        date = datetime(2022, 3, 20, 0, 00, 00),
        protein = 0,
        carbon = 0,
        fat = 0,
        mineral = 0,
        vitamin = 0,
        fiber = 0,
        description = "sample"
    )
    db.session.add(receipt)
    db.session.commit()
    db.session.close()  # セッションを閉じる