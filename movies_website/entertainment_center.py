# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes


pan = media.Movie('Pan',
		       	  '12-year-old orphan Peter is spirited away to the magical world of Neverland.',
                  'https://upload.wikimedia.org/wikipedia/en/5/50/Pan_2015_poster.jpg',
		          'https://www.youtube.com/watch?v=tjW1mKwNUSo',
		          'Directed by Joe Wright',
		          'With Levi Miller, Hugh Jackman, Garrett Hedlund, Rooney Mara',
		          'Rating; G')

martian = media.Movie('The Martian',
					  'During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew.',
                      'https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg',
		              'https://www.youtube.com/watch?v=ej3ioOneTy8',
		              'Directed by Ridley Scott',
		              'With Matt Damon, Jessica Chastain, Kristen Wiig, Kate Mara',
		              'Rating; PG-13')

matrix = media.Movie('The Matrix',
					 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers..',
                     'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
		   		     'https://www.youtube.com/watch?v=Q8g9zL-JL8E',
		   		     'Directed by The Wachowskis',
		   		     'Staring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, Joe Pantoliano',
		   		     'Rating; R')


xmen = media.Movie('The X Men: Apocalypse',
				   ' Apocalypse the most powerfull mutant of all comes to reclaim the world.',
                   'https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg',
		           'https://www.youtube.com/watch?v=bgQcilG-7as',
		           'Directed by Bryan Singer',
		           'Starring James McAvoy, Michael Fassbender, Jennifer Lawrence, Oscar Isaac, Nicholas Hoult, Rose Byrne, Tye Sheridan, Sophie Turner, Olivia Munn, Lucas Till',
		           'Rating; PG-13')


starwars = media.Movie('Star Wars: The Force Awakens',
					   'Apocalypse the most powerfull mutant of all comes to reclaim the world.',
                   	   'https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg',
					   'https://www.youtube.com/watch?v=sGbxmsDFVnE',
					   'Directed by J.J. Abrams',
					   'Starring Harrison Ford, Mark Hamill, Carrie Fisher, Adam Driver, Daisy Ridley, John Boyega, Oscar Isaac, Lupita Nyong, Andy Serkis, Domhnall Gleeson, Anthony Daniels, Peter Mayhew, Max von Sydow, Yayan Ruhian, Iko Uwais',
					   'Rating; PG-13')

tarzan = media.Movie('The Legend of Tarzan',
					 'Tarzan, having acclimated to life in London, is called back to his former home in the jungle to investigate the activities at a mining encampment.',
                     'https://upload.wikimedia.org/wikipedia/en/e/e5/The_Legend_of_Tarzan_poster.jpg',
		 		     'https://www.youtube.com/watch?v=Aj7ty6sViiU',
					 'Directed by David Yates',
					 'Starring  Alexander Skarsgard, Margot Robbie, Christoph Waltz',
					 'Rating; PG-13')






#print (toyStory.storyline)
#avatar.showTrailer()


movies = [pan, martian, matrix, xmen, starwars, tarzan]
fresh_tomatoes.open_movies_page(movies)
#print media.Movie.VALID_RATINGS
#print (media.Movie.__name__)
#print (media.Movie.__doc__)
#print (media.Movie.__bases__)