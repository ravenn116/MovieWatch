# MovieWatch Requirements

## 1. Customer Statement of Requirements

 MovieWatch is a web-based application designed for people who want a simple and organized way to manage their movie watchlists. This application will allow users to add, filter, search, delete, view, and manage movies while also keeping track of whether each movie has been watched or needs to be watched. MovieWatch will help in providing users with an easy-to-use interface and database for storing movie information. The goal of this application is to help provide a centralized and convenient location for avid movie watchers to keep track of their films.

## 2. Requirements Specification

### Functional Requirements

1. Let users add movies to their watchlist
2. Let users enter movie information such as title, genre, and release year
3. Let users view all movies they stored in their watchlist
4. Let users update information for any existing movie
5. Let users delete any movie from their watchlist
6. Let users search for their movies using the title or genre
7. Let users filter movies based on genre or viewing status
8. Let users label a movie as "Watched" or "Want to Watch"
9. Store movie information in a database
10. Retrieve any saved movie information from the database when users access their watchlist

### Non-Functional Requirements 

1. Respond to user actions within a reasonable amount of time
2. Maintain accurate movie information when records are deleted, updated, or added
3. Store movie details reliably in the database
4. Prevent unauthorized users from modifying or deleting any stored movie information
5. Be accessible through a standard web browser such as Chrome
6. Be designed to handle increasing numbers of movie records without impacting usability 

## 3. Data and Storage Blueprint

### Data Input

MovieWatch will use manual entry as the primary method of data input. Users will enter movie information through forms provided by the application's user interface. The information entered by the users will include the movie title, genre, release year, and viewing status. Users will also be able to update any existing movie information or remove movies from their watchlist. After the user submits the information, the application will process the input and store the movie record within the database. 

### Database or Storage

MovieWatch will use a MySQL relational database to manage and store movie information. MySQL will be used since it can organize data into structured tables and support operations like inserting, updating, and deleting records. Using this database system will allow MovieWatch to maintain movie information and details even after the application is closed and provide dependable access to all stored records.  

The primary movie table will contain fields like a unique movie ID and viewing status. The movie ID will be used to distinctly identify each movie record. The title, genre, and release year will store basic information about each of the movies, while the viewing status will indicate whether the movie is "Watched" or "Want to Watch." The application will connect to the MySQL database through the Python and Flask backend so that information can be properly stored and retrieved whenever needed.

## 4. Agile Product Backlog

1. As a user, I want to add movies to my watchlist so that I can keep track of movies I want to watch
2. As a user, I want to enter information such as movie title, genre,  and release year so that I can keep detailed information about each movie
3. As a user, I want to view all movies in my watchlist so that I can easily see the movies that are saved
4. As a user, I want to update information for an existing movie so that I can change or correct its information as needed
5. As a user, I want to delete movies from my watchlist so that I can remove movies I no longer want to watch
6. As a user, I want to search for movies by genre or title so that I can quickly find a specific movie in my watchlist
7. As a user, I want to filter movies by genre or viewing status so that I can find and organize movies based on my preferences 
8. As a user, I want to label movies as "Watched" or "Want to Watch" so that I can keep track of my viewing progress
9. As a user, I want my movie information to be stored in a database so that my watchlist information is available and saved when I return to the application
10. As a user, I want my saved movie information to be retrieved from the database when I access my watchlist so that I can view my previously saved movies 
    
