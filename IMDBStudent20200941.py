#!/usr/bin/python3

genre = []
genre2 = []

with open('movie.dat') as file:
  movie = file.read().splitlines()
  for i in movie:
    genre.append(i.split('::')[2])
  for i in genre:
    genre2.append(i.split('|')
  f = open('movie.txt', 'wt')
  f.write("Animation %d\n" % genre2.count('Animation'))
  f.write("Children's %d\n" % genre2.count('Children's'))
  f.write("Comedy %d\n" % genre2.count('Comedy'))
  f.write("Adventure %d\n" % genre2.count('Adventure'))
  f.write("Fantasy %d\n" % genre2.count('Fantasy'))
  f.write("Romance %d\n" % genre2.count('Romance'))
  f.write("Drama %d\n" % genre2.count('Drama'))
  f.write("Crime %d\n" % genre2.count('Crime'))
  f.write("Thriller %d\n" % genre2.count('Thriller'))
  f.write("Action %d\n" % genre2.count('Action'))
  f.write("Horror %d\n" % genre2.count('Horror'))
  f.write("Documentary %d\n" % genre2.count('Documentary'))
