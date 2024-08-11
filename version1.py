# Sample data of movies
movies = [
    {"title": "The Matrix", "genre": "Action, Sci-Fi"},
    {"title": "Inception", "genre": "Action, Sci-Fi"},
    {"title": "Interstellar", "genre": "Adventure, Drama, Sci-Fi"},
    {"title": "The Dark Knight", "genre": "Action, Crime, Drama"},
    {"title": "Pulp Fiction", "genre": "Crime, Drama"},
    {"title": "The Godfather", "genre": "Crime, Drama"},
    {"title": "Schindler's List", "genre": "Biography, Drama, History"},
    {"title": "The Lord of the Rings: The Return of the King", "genre": "Action, Adventure, Drama"},
    {"title": "Forrest Gump", "genre": "Drama, Romance"},
    {"title": "The Shawshank Redemption", "genre": "Drama"}
]

def recommend_movies(selected_genre, n_recommendations=3):
    recommendations = []

    # Find movies matching the selected genre
    for movie in movies:
        if selected_genre.lower() in movie["genre"].lower():
            recommendations.append(movie["title"])

    # Limit the number of recommendations to the desired amount
    return recommendations[:n_recommendations]

def movie_recommendation_app():
    print("Welcome to the Movie Recommendation App!")
    print("Available genres: Action, Sci-Fi, Adventure, Drama, Crime, Biography, History, Romance")

    while True:
        genre = input("\nEnter a genre to get movie recommendations (or type 'exit' to quit): ")

        if genre.lower() == 'exit':
            print("Thank you for using the Movie Recommendation App!")
            break

        recommendations = recommend_movies(genre)

        if recommendations:
            print("\nWe recommend these movies:")
            for i, title in enumerate(recommendations, 1):
                print(f"{i}. {title}")
        else:
            print(f"Sorry, no movies found for the genre '{genre}'.")

if __name__ == "__main__":
    movie_recommendation_app()
