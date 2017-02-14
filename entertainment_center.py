import fresh_tomatoes
import media

toy_story = media.Movie("Toy story", "A STORY OF A BOY AND HIS TOYS THAT COMES TO LIFE",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#toy_story is an instance of class Movie() imported by media file


#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A MARINE ON An ALIEN PLANET",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

everest = media.Movie("Everest","A JOURNEY TO MOUNT EVEREST",
                    "https://upload.wikimedia.org/wikipedia/en/2/28/Everest_poster.jpg",
                    "https://www.youtube.com/watch?v=5ZQVpPiOji0")
#everest.show_trailer()

school_of_rock = media.Movie("School of rock","USING ROCK MUSIC TO LEARN",
                            "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

midnight_in_paris = media.Movie("Midnight in paris", "GOING BACK IN TIME TO MEET AUTHORS",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger games","A REALLY REAL REALITY SHOW",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, everest, school_of_rock, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

#hunger_games.show_poster()
#print(media.Movie.VALID_RATINGS)

#print(media.Movie.__doc__) # doc returns the documentation in the class movie if any(""" ---- """)
#print(media.Movie.__name__)# name return class name
#print(media.Movie.__module__)#module returns the folder name


