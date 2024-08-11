'Hollywood': {
        'Romantic': [
            {
                'title': 'The Notebook',
                'trailer': 'https://www.youtube.com/watch?v=FCb6FhHDTHc',
                'cast': 'Ryan Gosling, Rachel McAdams',
                'director': 'Nick Cassavetes',
                'release_date': '2004-06-25',
                'budget': '$29 million',
                'collection': '$115 million',
                'verdict': 'Emotional and timeless love story.',
                'rating': '8.0',
                'review': 'A deeply moving romance that remains iconic.',
                'platform': 'HBO Max'
            },
            # Add more movies here
        ],
        # Add more categories here
    },
    'Bollywood': {
        'Action': [
            {
                'title': 'Dhoom 2',
                'trailer': 'https://www.youtube.com/watch?v=4FWqf3kqzJ4',
                'cast': 'Hrithik Roshan, Aishwarya Rai',
                'director': 'Sanjay Gadhvi',
                'release_date': '2006-11-24',
                'budget': '$10 million',
                'collection': '$25 million',
                'verdict': 'Stylish and entertaining.',
                'rating': '6.2',
                'review': 'A fun-filled action-packed movie with high entertainment value.',
                'platform': 'Disney+ Hotstar'
            },
            # Add more movies here
        ],
        # Add more categories here
    },
    # Add more industries here
    # Example of other industries
    'Sandalwood': {
        'Drama': [
            {
                'title': 'KGF Chapter 1',
                'trailer': 'https://www.youtube.com/watch?v=5A2-G7CkHT8',
                'cast': 'Yash, Srinidhi Shetty',
                'director': 'Prashanth Neel',
                'release_date': '2018-12-21',
                'budget': '$14 million',
                'collection': '$70 million',
                'verdict': 'A gripping tale with high-octane action sequences.',
                'rating': '8.2',
                'review': 'A blockbuster hit with great performances and high production values.',
                'platform': 'Amazon Prime Video'
            },
            # Add more movies here
        ],
        # Add more categories here
    },
    # Repeat for other industries and categories
}

def display_movie_details(movie):
    print(f"Title: {movie['title']}")
    print(f"Trailer: {movie['trailer']}")
    print(f"Cast: {movie['cast']}")
    print(f"Director: {movie['director']}")
    print(f"Release Date: {movie['release_date']}")
    print(f"Budget: {movie['budget']}")
    print(f"Collection: {movie['collection']}")
    print(f"Verdict: {movie['verdict']}")
    print(f"IMDb Rating: {movie['rating']}")
    print(f"Public Review: {movie['review']}")
    print(f"Available on: {movie['platform']}")
    print()

def main():
    print("Welcome to the Movie Information System!")
    
    categories = ['Romantic', 'Action', 'Comedy', 'Drama', 'Horror', 'Fantasy', 'Adventure', 'Science Fiction', 'Thriller', 'Crime', 'Mystery', 'War', 'Biopic']
    industries = ['Hollywood', 'Bollywood', 'Sandalwood', 'Tollywood', 'Mollywood', 'Kollywood', 'Chinese film industry']
    
    # Get user inputs for category
    print("Select a category:", ', '.join(categories))
    category = input().capitalize()
    
    if category not in categories:
        print("Invalid category.")
        return
    
    # Get user inputs for industry
    print("Select an industry:", ', '.join(industries))
    industry = input().capitalize()
    
    if industry not in industries:
        print("Invalid industry.")
        return
    
    # Display movies based on user inputs
    if industry in movies and category in movies[industry]:
        print(f"Movies in {industry} - {category} category:")
        for i, movie in enumerate(movies[industry][category], start=1):
            print(f"{i}. {movie['title']}")
        
        # Select a movie
        try:
            choice = int(input("Enter the number of the movie you want to view details for: "))
            selected_movie = movies[industry][category][choice - 1]
            display_movie_details(selected_movie)
        except (IndexError, ValueError):
            print("Invalid selection.")
    else:
        print("No movies found for the selected criteria.")

if __name__ == "__main__":
    main()
