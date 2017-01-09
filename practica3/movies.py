import csv
f = open('movie_metadata.csv')
csv_f = csv.reader(f)

#color,director_name,num_critic_for_reviews,duration,director_facebook_likes,actor_3_facebook_likes,actor_2_name,actor_1_facebook_likes,gross,genres,actor_1_name,movie_title,num_voted_users,cast_total_facebook_likes,actor_3_name,facenumber_in_poster,plot_keywords,movie_imdb_link,num_user_for_reviews,language,country,content_rating,budget,title_year,actor_2_facebook_likes,imdb_score,aspect_ratio,movie_facebook_likes
movie_color = 0
movie_bw    = 0
directors   = []
for row in csv_f:
    #print(row)
    color,director_name,num_critic_for_reviews,duration,director_facebook_likes,actor_3_facebook_likes,actor_2_name,actor_1_facebook_likes,gross,genres,actor_1_name,movie_title,num_voted_users,cast_total_facebook_likes,actor_3_name,facenumber_in_poster,plot_keywords,movie_imdb_link,num_user_for_reviews,language,country,content_rating,budget,title_year,actor_2_facebook_likes,imdb_score,aspect_ratio,movie_facebook_likes = row
    if color == 'Color':
        movie_color = movie_color + 1
    if color == ' Black and White':
        movie_bw    = movie_bw + 1
    if directors.has_key(director_name):
        directors[director_name]['movies_count'] = directors[director_name]['movies_count'] + 1
    else:
        directors[director_name] = {'movies_count': 1}

html_str = """
<table border=1>
     <tr>
       <th>Pregunta</th>
       <th>Respuesta</th>
     </tr>
     <indent>
       <tr>
         <td>Cuantas peliculas a 'color' y 'blanco y negro' hay en la lista?</td>
         <td> {} Peliculas a color y {} en Blanco y Negro</td>
       </tr>
       <tr>
         <td>Cuantas películas produjeron cada director?</td>
         <td>{}</td>
       </tr>
     </indent>
</table>
""".format(movie_color, movie_bw, directors)

Html_file= open("movies-report.html","w")
Html_file.write(html_str)
Html_file.close()

# print("{} movies Color".format(movie_color))
# print("{} movies Black and White".format(movie_bw))