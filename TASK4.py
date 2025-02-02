# TASK-4 RECOMMENDATION SYSTEM

movies = {
    "Action": [
        "Mad Max: Fury Road", "John Wick", "The Dark Knight", 
        "Avengers: Endgame", "Gladiator", "Die Hard", "Terminator 2: Judgment Day"
    ],
    "Comedy": [
        "The Hangover", "Superbad", "Step Brothers", 
        "Groundhog Day", "Anchorman: The Legend of Ron Burgundy", "Dumb and Dumber", "Shaun of the Dead"
    ],
    "Drama": [
        "The Shawshank Redemption", "Forrest Gump", "The Pursuit of Happyness", 
        "The Godfather", "Schindler's List", "12 Angry Men", "A Beautiful Mind"
    ],
    "Sci-Fi": [
        "Inception", "Interstellar", "The Matrix", 
        "Blade Runner 2049", "Star Wars: A New Hope", "Jurassic Park", "E.T. the Extra-Terrestrial"
    ],
    "Horror": [
        "The Conjuring", "A Quiet Place", "It", 
        "Hereditary", "Get Out", "The Exorcist", "Halloween"
    ],
    "Romance": [
        "The Notebook", "Pride and Prejudice", "Titanic", 
        "La La Land", "Crazy Rich Asians", "A Star is Born", "Me Before You"
    ],
    "Adventure": [
        "The Lord of the Rings: The Fellowship of the Ring", "Pirates of the Caribbean: The Curse of the Black Pearl", 
        "Indiana Jones: Raiders of the Lost Ark", "Jumanji: Welcome to the Jungle", 
        "Avatar", "The Jungle Book", "The Hobbit: An Unexpected Journey"
    ]
}

def recommend_movies(user_genres):
    recommendations = []
    for genre in user_genres:
        if genre in movies:
            recommendations.extend(movies[genre])
    return recommendations

print("Welcome to the Movie Recommendation System!")
print("We have movies in the following genres: Action, Comedy, Drama, Sci-Fi, Horror, Romance, Adventure")

user_preferences = input("Enter your favorite genres (comma-separated): ").strip().split(",")

user_preferences = [genre.strip().capitalize() for genre in user_preferences]

recommended_movies = recommend_movies(user_preferences)

if recommended_movies:
    print("\nBased on your preferences, we recommend the following movies:")
    for movie in recommended_movies:
        print(f"- {movie}")
else:
    print("Sorry, we couldn't find any movies matching your preferences. Try different genres!")
