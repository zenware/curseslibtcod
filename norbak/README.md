# The Fires of Norbak

version: 0.3

Changelog:
v0.3 (current):
 - added shop & currency
v0.2:
 - added weapons & armor.
 - fixed the runaway feature, so now when you unsuccessfully run away, you take the turn's damage as normal.
 
imports: curses (windows-curses on Windows), random, time, playsound

"Norbak.py" is the source, "/dist/Norbak" is an executable for MacOS only.

Space is the select key, rather than enter. Curses doesn't work well with the enter key, for some reason. The only exception to this is when you are inputing your name, here enter will work.
