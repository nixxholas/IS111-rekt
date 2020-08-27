import display_lyrics

lyricFile = str.splitlines(open("Lyrics.txt").read())
display_lyrics.traverse_lines_v2(lyricFile)