import csv
import psycopg2
from nameparser import HumanName


# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="movies",
    user="hangman",
    password="hangman"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()
def main():
    # Define the CSV file path
    csv_file = "d:\my databases\movie_details_V1.csv"
    #try:
        # Open the CSV file and read its contents
    with open(csv_file,"r") as file:
        reader = csv.DictReader(file)
        # Iterate over each row in the CSV file
        for row in reader:
            print(row)
            movie = processRow(row)
            #Add movie to movie table
            movie_id = addMovie(movie)
            #Add company to company table
            for m_key, m_value in movie.items():
                
                if m_key in ('Production','Distribution'):
                    if not m_value == "":
                        c_List = m_value.split(",")
                        for c_value in c_List:
                            company_id = addCompany(c_value)
                            if company_id > 0:
                                ok = addMovieCompany(movie_id, company_id, m_key[0])
                                if not ok:
                                    print("Error inserting into s_mv_cmpny")
                else:
                    if m_key in ('Director', 'Writer', 'Screenplay', 'Story', 'Producer', 'Cast', 'Narration', 'Cinematography', 'Editor', 'Music_director'):
                        if not m_value == "":
                           a_List = m_value.split(",")
                           #Add profession if it does not exist
                           profession_id = addProfession(m_key)
                           for a_value in a_List:
                                # Add artists to artists table
                                a_value = a_value.strip()
                                artist_id = addArtist(a_value)
                                print(artist_id)
                                if movie_id > 0 and artist_id > 0 and profession_id > 0:
                                    #add to intersection table movie, artist and profession.
                                    apm_id = addAPM(movie_id, artist_id, profession_id)
                                    print(apm_id)
    """ except:
        print("error")
        #exit normally """

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    
def processRow(row):
    # Extract the required fields from the row
    movie = {}
    movie_artist = {}
    movie_company = {}
    boxOffice=''
    boxOffice = row["Box office"].split('(')[0]
    boxOffice = boxOffice.replace('est.','')
    movie['title'] = row["title"]
    movie['genre'] = 1
    movie['based'] = row["Based on"]
    movie['released'] = row["Release date"]
    movie['duration'] = row["Running time"]
    movie['country_code'] = 102
    movie['language'] = 'Hindi'
    movie['budget'] = row["Budget"]
    movie['box_office'] = boxOffice
    movie_artist['Director'] = row["Directed by"]
    movie_artist['Writer'] = row["Written by"]
    movie_artist['Screenplay'] = row["Screenplay by"]
    movie_artist['Based'] = row["Based on"]
    movie_artist['Story'] = row["Story by"]
    movie_artist['Producer'] = row["Produced by"]
    movie_artist['Cast'] = row["Starring"]
    movie_artist['Narration'] = row["Narrated by"]
    movie_artist['Cinematography'] = row["Cinematography"]
    movie_artist['Editor'] = row["Edited by"]
    movie_artist['Music_director'] = row["Music by"]
    movie.update(movie_artist)
    movie_company['Production'] = row["Productioncompany"]
    movie_company['Distribution'] = row["Distributed by"]
    movie.update(movie_company)
    return movie

def addMovie(movie):
    # find if the movie already exists, else proceed to add movie.
    table_movies = 'public."backendApp_s_movie"'
    title = movie['title']
    sql_findMovie = f"SELECT EXISTS (SELECT 1 FROM " + table_movies + " WHERE movie_title = %s)"
    movie_exists = cursor.execute(sql_findMovie, (title,))
    if (movie_exists):
        return movie_exists
    else:
        # Define the SQL query to insert the row into the movies table
        sql_movie = f"INSERT INTO {table_movies} (movie_title , movie_genre_id, movie_based, movie_released, movie_duration,movie_country_id,movie_language,movie_budget,movie_boxoffice)" \
            f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) returning id"

        # Execute the SQL query with the row data
        
        cursor.execute(sql_movie,(movie['title'], movie['genre'], movie['based'], movie['released'], movie['duration'], movie['country_code'], movie['language'], movie['budget'], movie['box_office']))
        movieID = cursor.fetchone()[0]
        if (not movieID > 0):
            print("Error adding movie")
        return (movieID)

def addCompany(company_name):
    table_company = 'public."backendApp_s_company"'
    
    sql_company = f" SELECT id FROM " + table_company + \
                      " WHERE company_name = %s"
    
    # Execute the SQL query with the row data
    company_id = cursor.execute(sql_company, (company_name,))
    if (not company_id):
        print("Company not found in company Table")
        # Define the SQL query to insert the row into the table
        sql_company = f"INSERT INTO {table_company} (company_name) " \
            f"VALUES (%s) returning id"
        # Execute the SQL query with the row data
        cursor.execute(sql_company, (company_name,))
        company_id = cursor.fetchone()[0]
        if not company_id > 0:
            print("Error inserting into company table")
    return company_id

def addMovieCompany(movie_id, company_id, company_role):
    table_mvcmpny = 'public."backendApp_s_mv_cmpny"'
   
    # Define the SQL query to insert the row into the table
    sql_mvcmpny = f"INSERT INTO {table_mvcmpny} (movie_id, company_id, company_role) " \
        f"VALUES (%s, %s, %s) returning id"
    # Execute the SQL query with the row data
    cursor.execute(sql_mvcmpny, (movie_id, company_id, company_role))
    mvCompany_id = cursor.fetchone()[0]
    return mvCompany_id


def addProfession(profession):
    table_prof = 'public."backendApp_s_profession"'

    sql_profession = f" SELECT id FROM " + table_prof + \
                        " WHERE profession_name = %s"
    # Execute the SQL query with the row data
    profession_id = cursor.execute(sql_profession,(profession,))
    if (not profession_id):
        # Define the SQL query to insert the row into the table
        sql_profession = f"INSERT INTO " + table_prof + \
                        " (profession_name) VALUES (%s) returning id"
        # Execute the SQL query with the row data
        cursor.execute(sql_profession, (profession,))
        profession_id = cursor.fetchone()[0]
    return profession_id

def addArtist(fullName):
    # Find if the artist exists, else add him to the artist table and establish his profession in the movie.
    table_artists = 'public."backendApp_s_artist"'
    dname = HumanName(fullName)
    d_surname = ''
    if len(d_surname) > 0:
        d_surname = dname.surname_list[len(dname.surname_list)-1]
    print(fullName,'surname', d_surname)

    sql_artists = f" SELECT id FROM {table_artists} \
                      WHERE artist_full_name = %s"
    # Execute the SQL query with the row data
    artist_id = cursor.execute(sql_artists,(fullName,))
    if (not artist_id):
        # Define the SQL query to insert the row into the table
        sql_artists = f"INSERT INTO {table_artists} (artist_full_name, artist_title, artist_first_name, artist_middle_name, artist_last_name, artist_suffix, artist_nickname, artist_surname,artist_gender, artist_citizenof_id) " \
            f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;"

        # Execute the SQL query with the row data
        cursor.execute(sql_artists, (fullName, dname.title,
                                     dname.first, dname.middle, dname.last, dname.suffix,
                                     dname.nickname, d_surname,
                                     'M', 102))
        artist_id = cursor.fetchone()[0]
        if not artist_id > 0:
            print("Error inserting into artist table")
    return artist_id

def addAPM(movie_id, artist_id, profession_id):
    table_apm = 'public."backendApp_s_mv_artst_prfssn"'
    sql_apm = f" INSERT INTO {table_apm} (movie_id, artist_id, profession_id) VALUES (%s, %s, %s) returning id"
    # Execute the SQL query with the row data
    cursor.execute(sql_apm,
                (movie_id, artist_id, profession_id,))
    apm_id = cursor.fetchone()[0]
    if not apm_id > 0:
        print("Error inserting into MOVIE_ARTIST_PROFESSION table")
    return apm_id

if __name__ == "__main__":
    main()
