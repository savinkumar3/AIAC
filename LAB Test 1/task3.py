def get_movies_from_user():
    movies = []
    n = int(input("How many movies do you want to enter? "))
    for i in range(n):
        name = input(f"Enter the name of movie #{i+1}: ")
        genres = input(f"Enter the genres for '{name}' (comma separated): ")
        genre_list = [g.strip().lower() for g in genres.split(',')]
        movies.append({'name': name, 'genres': genre_list})
    return movies

def recommend_movies(movies, preferred_genre):
    preferred_genre = preferred_genre.strip().lower()
    recommended = []
    for movie in movies:
        if preferred_genre in movie['genres']:
            recommended.append(movie['name'])
    return recommended

def main():
    print("Welcome to the Movie Recommender!")
    movies = get_movies_from_user()
    preferred_genre = input("Enter your preferred genre: ")
    recommendations = recommend_movies(movies, preferred_genre)
    if recommendations:
        print("Recommended movies for you:")
        for movie in recommendations:
            print("-", movie)
    else:
        print("Sorry, no movies found for your preferred genre.")

if __name__ == "__main__":
    main()
