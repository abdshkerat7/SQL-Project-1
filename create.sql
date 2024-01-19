create table Films(
  filmId primary key,
  index varchar,
  actors varchar,
  film varchar,
  year_of_release varchar,
  directors varchar,
  authors varchar,
  studio varchar,
  genres varchar,
  movie_time varchar,
  imdb_rating varchar,
  imdb_votes varchar,
  content_rating varchar,
);


create table was_awarded(
  oscar_year primary key,
  filmId primary key,
  award varchar
);


create table oscar_cermony(
  oscar_year primary key
);











