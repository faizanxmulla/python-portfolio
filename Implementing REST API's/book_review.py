import os
from pyairtable import Api


class BookReview:
    BASE_ID = "app72keSmvKwByPte"
    TABLE_ID = "tblAibIxEDFa6QjPW"

    def __init__(self):
        self.api = Api(os.environ["AIRTABLE_KEY"])
        self.table = self.api.table(self.BASE_ID, self.TABLE_ID)


    def get_book_ratings(self, sort="ASC", max_records=10):
        rating = ["Rating"] if sort == "ASC" else ["-Rating"]
        table = self.table.all(sort=rating)[:max_records]

        return table


    def add_book_ratings(self, book_title, author, book_rating, notes=None):
        fields = {
            "Title": book_title,
            "Author": author,
            "Rating": book_rating,
            "Notes": notes,
        }
        self.table.create(fields=fields)


    def update_book_ratings(self, book_title, author, book_rating, notes=None):
        records = self.table.all(formula=f"{{Title}} = '{book_title}'", max_records=1)

        if records:
            # Assuming there is only one record with the given title.
            record_id = records[0]["id"]

            existing_record = self.table.get(record_id)

            if existing_record:
                fields = {
                    "Title": book_title if book_title is not None else existing_record["fields"].get("Title", None),
                    "Author": author if author is not None else existing_record["fields"].get("Author", None),
                    "Rating": book_rating if book_rating is not None else existing_record["fields"].get("Rating", None),
                    "Notes": notes if notes is not None else existing_record["fields"].get("Notes", None),
                }

                self.table.update(record_id, fields, replace=True)
                return {"message": "Book-review updated successfully !!!"}

            else:
                return {"ERROR": "Book-review not found !!!"}, 404

        else:
            return {"ERROR": "Book-review not found !!!"}, 404


    def delete_book_ratings(self, book_title):
        records = self.table.all(formula=f"{{Title}} = '{book_title}'", max_records=1)

        if records:
            record_id = records[0]["id"]

            # Confirm that the record exists beofre attempting to delete the record.
            existing_record = self.table.get(record_id)

            if existing_record:
                self.table.delete(record_id)
                return {"message": "Book review deleted successfully !!!"}

            else:
                return {"message": "Book review not found !!"}, 404

        else:
            return {"error": "Book review not found !!"}, 404


if __name__ == "__main__":
    review = BookReview()
    print(review.get_book_ratings(sort="DESC", max_records=3))
