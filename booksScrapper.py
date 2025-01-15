from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup
from random import choice, randint, shuffle

app = Flask(__name__)

base_url = "https://books.toscrape.com/"
all_books = []


# Function to get the books from a page
def get_books_from_page(page_url):
    res = requests.get(f"{base_url}{page_url}")
    soup = BeautifulSoup(res.text, "html.parser")

    # Find all books on the page
    books = soup.find_all(class_="product_pod")
    page_books = []

    for book in books:
        title = book.find("h3").find("a")["title"]

        # Get the rating for the book (class="star-rating")
        rating_tag = book.find("p", class_="star-rating")
        if rating_tag:
            rating = rating_tag["class"][1]  # This gives us a class like "One", "Two", "Three", etc.
            page_books.append({"title": title, "rating": rating})

    return page_books


# Route to display the quiz page
@app.route('/')
def index():
    page_number = randint(1, 50)  # Random page
    page_url = f"catalogue/page-{page_number}.html"
    books_on_page = get_books_from_page(page_url)

    if books_on_page:
        book = choice(books_on_page)
        # Define possible star ratings
        rating_options = ["One", "Two", "Three", "Four", "Five"]

        # Add the correct rating to options
        options = [book["rating"]]

        # Add 3 random ratings to the options
        while len(options) < 4:
            random_rating = choice(rating_options)
            if random_rating not in options:
                options.append(random_rating)

        shuffle(options)  # Shuffle the options to randomize the positions

        return render_template('Quiz/quiz.html', book=book, options=options)
    else:
        return render_template('Quiz/error.html')


# Route to handle the quiz answer submission
@app.route('/submit', methods=['POST'])
def submit():
    selected_option = request.form['option']
    book_title = request.form['book_title']
    book_rating = request.form['book_rating']

    # Check if the user selected the correct rating
    if selected_option == book_rating:
        result = "Congratulations! You got it right!"
    else:
        result = f"Sorry, the correct rating is {book_rating} stars."

    return render_template('Quiz/result.html', result=result, book_title=book_title)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
