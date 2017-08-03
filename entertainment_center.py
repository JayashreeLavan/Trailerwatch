import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys!",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

now_you_see_me = media.Movie("Now You see me",
                             "A Story of a boy and his toys!",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=KYz2wyBy3kc")

movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)
#print(toy_story.storyline)
#toy_story.show_trailer()
