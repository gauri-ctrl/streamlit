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
    # Sample data for 50 movies
    movies = {
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
                # Add more Hollywood romantic movies here
            ],
            'Action': [
                {
                    'title': 'Mad Max: Fury Road',
                    'trailer': 'https://www.youtube.com/watch?v=hEJnMQG9ev8',
                    'cast': 'Tom Hardy, Charlize Theron',
                    'director': 'George Miller',
                    'release_date': '2015-05-15',
                    'budget': '$150 million',
                    'collection': '$375 million',
                    'verdict': 'High-octane action with stunning visuals.',
                    'rating': '8.1',
                    'review': 'A relentless, visually arresting action spectacle.',
                    'platform': 'Hulu'
                },
                # Add more Hollywood action movies here
            ],
            # Add more categories for Hollywood
        },
        'Bollywood': {
            'Drama': [
                {
                    'title': '3 Idiots',
                    'trailer': 'https://www.youtube.com/watch?v=K0eDlF6bG8c',
                    'cast': 'Aamir Khan, R. Madhavan',
                    'director': 'Rajkumar Hirani',
                    'release_date': '2009-12-25',
                    'budget': '$8 million',
                    'collection': '$85 million',
                    'verdict': 'A mix of comedy and drama with a strong message.',
                    'rating': '8.4',
                    'review': 'Heartwarming and thought-provoking.',
                    'platform': 'Netflix'
                },
                # Add more Bollywood drama movies here
            ],
            'Horror': [
                {
                    'title': 'Bhool Bhulaiyaa',
                    'trailer': 'https://www.youtube.com/watch?v=G7NDFY4s-ns',
                    'cast': 'Akshay Kumar, Vidya Balan',
                    'director': 'Priyadarshan',
                    'release_date': '2007-10-12',
                    'budget': '$2 million',
                    'collection': '$16 million',
                    'verdict': 'A unique blend of horror and comedy.',
                    'rating': '7.2',
                    'review': 'An entertaining and spooky experience.',
                    'platform': 'Amazon Prime Video'
                },
                # Add more Bollywood horror movies here
            ],
            # Add more categories for Bollywood
        },
        'Sandalwood': {
            'Adventure': [
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
                # Add more Sandalwood adventure movies here
            ],
            # Add more categories for Sandalwood
        },
        # Add more industries like Tollywood, Mollywood, Kollywood, Chinese film industry
    }

    categories = ['Romantic', 'Action', 'Comedy', 'Drama', 'Horror', 'Fantasy', 'Adventure', 'Science Fiction', 'Thriller', 'Crime', 'Mystery', 'War', 'Biopic']
    industries = ['Hollywood', 'Bollywood', 'Sandalwood', 'Tollywood', 'Mollywood', 'Kollywood', 'Chinese film industry']
    
    # Get user inputs for industry
    print("Select an industry:", ', '.join(industries))
    industry = input().capitalize()
    
    if industry not in industries:
        print("Invalid industry.")
        return
    
    # Get user inputs for category
    print("Select a movie type:", ', '.join(categories))
    category = input().capitalize()
    
    if category not in categories:
        print("Invalid category.")
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
