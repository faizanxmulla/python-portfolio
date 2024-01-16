from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

import book_review

# ---------------------------------------------------------------

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

br = book_review.BookReview()


class BookReviewsResource(Resource):
    def get(self):
        """
        This method responds to the GET request for retrieving book reviews.
        ---
        tags:
        - Book Reviews
        parameters:
            - name: sort
              in: query
              type: string
              required: false
              description: Sorting order, either "ASC" or "DESC"
            - name: max_records
              in: query
              type: int
              required: false
              description: Maximum number of records to retrieve
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            reviews:
                                type: array
                                description: List of book reviews
                                items:
                                  type: object
                                  properties:
                                    book_title:
                                      type: string
                                      description: Title of the book
                                    author:
                                      type: string
                                      description: Author of the book
                                    rating:
                                      type: int
                                      description: Rating of the book
                                    notes:
                                      type: string
                                      description: Additional notes for the book
        """

        sort = request.args.get("sort", default=None)
        max_records = int(request.args.get("max_records", 10))

        valid_sort_values = {"ASC", "DESC"}

        if sort not in valid_sort_values:
            return {"ERROR": "Invalid sort value."}, 400

        # Sorting the reviews based on the parameter.
        reviews = (
            br.get_book_ratings(sort=sort, max_records=max_records)
            if sort in valid_sort_values
            else br.get_book_ratings(max_records=max_records)
        )

        return reviews, 200


class PostReviewResource(Resource):
    def post(self):
        """
        This method responds to the POST request for adding a book review.
        ---
        tags:
        - Book Reviews
        parameters:
            - in: body
              name: review
              description: The book review details
              schema:
                type: object
                required:
                  - book_title
                  - author
                  - rating
                properties:
                  book_title:
                    type: string
                    description: Title of the book
                  author:
                    type: string
                    description: Author of the book
                  rating:
                    type: int
                    description: Rating of the book
                  notes:
                    type: string
                    description: Additional notes for the book
        responses:
            201:
                description: Book review added successfully
            400:
                description: Bad request, invalid input
        """

        data = request.get_json()

        book_title = data.get("book_title")
        author = data.get("author")
        rating = data.get("rating")
        notes = data.get("notes")

        if not all([book_title, author, rating]):
            return {"error": "Invalid input, missing required fields"}, 400

        try:
            rating = int(rating)

        except ValueError:
            return {"error": "Invalid rating value, must be an integer"}, 400

        br.add_book_ratings(book_title, author, rating, notes)
        return {"message": "Book added successfully !!!"}, 201


class UpdateReviewResource(Resource):
    def put(self):
        """
        This method responds to the PUT request for updating a book review.
        ---
        tags:
        - Book Reviews
        parameters:
            - name: book_title
              in: query
              type: string
              required: true
              description: Title of the book to be updated
            - in: body
              name: review
              description: The updated book review details
              schema:
                type: object
                required:
                  - author
                  - rating
                properties:
                  author:
                    type: string
                    description: Updated author of the book
                  rating:
                    type: int
                    description: Updated rating of the book
                  notes:
                    type: string
                    description: Updated additional notes for the book
        responses:
            200:
                description: Book review updated successfully
            400:
                description: Bad request, invalid input
        """

        # Get the parameters from the query string.
        book_title = request.args.get("book_title")

        data = request.get_json()
        author = data.get("author")
        rating = data.get("rating")
        notes = data.get("notes")

        try:
            rating = int(rating)

        except ValueError:
            return {"error": "Invalid rating value, must be an integer"}, 400

        br.update_book_ratings(book_title, author, rating, notes)
        return {"message": "Book-review updated successfully !!!"}, 201


class DeleteReviewResource(Resource):
    def delete(self):
        
        """
        This method responds to the DELETE request for deleting a book review.
        ---
        tags:
        - Book Reviews
        parameters:
            - name: book_title
              in: query
              type: string
              required: true
              description: Title of the book to be deleted
        responses:
            200:
                description: Book review deleted successfully
            400:
                description: Bad request, invalid input
        """

        # Get the parameters from the query string
        book_title = request.args.get("book_title")

        br.delete_book_ratings(book_title)

        return {"message": "Book-review deleted successfully !!!"}, 200


api.add_resource(BookReviewsResource, "/book-reviews")
api.add_resource(PostReviewResource, "/book-reviews/post")
api.add_resource(UpdateReviewResource, "/book-reviews/put")
api.add_resource(DeleteReviewResource, "/book-reviews/delete")


if __name__ == "__main__":
    app.run(debug=True)
