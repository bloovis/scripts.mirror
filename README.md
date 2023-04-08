# Scripts

Various simple scripts for Linux:

* `trackpoint` : set sensitivity, speed, drift time, and acceleration of ThinkPad TrackPoint
* `gateway` : network gateway IP address
* `ipaddr` : print IP address
* `externalip` : print external IP address (as seen from outside the NAT router)
* `diskusers` : print summary every ten seconds of processes using disk
* `filesbetween`: find files with modification times in a date range
* `oggalbum`: Tag a set of ogg files using an album description file
* `oggmakealbum`: Create an album description file from a set of ogg files
* `redirect.cgi`: CGI script to allow censored URLs to be posted on Reddit and Twitter

## Ogg scripts

I wrote the two Ruby scripts, `oggalbum` and `oggmakealbum`, to make it easier
to edit the comment tags in ogg audio files.  I dislike using GUI tools for
this purpose, so my scripts use (or create) album description files, which
are plain text and easy to edit.  My scripts also support the tagging I needed
for classical music, which differs from pop music in these ways:

* the performer and composer are not usually the same
* a single album might have several works
* a single album might have several performers

These requirements are met with the use of the following tags, which
are recognized by the [Classical Music Tagger](https://gitlab.com/AndreasK/classical-music-tagger)
app for Android:

* `GROUPING`: the name of a work, which may be composed of several tracks
* `SUBTITLE`: the subtitle of the work's name
* `ARTIST`: the performer
* `COMPOSER`: the composer

Here is a sample album description for a CD that has two works:

```
GENRE=Classical
DATE=1988
ALBUM=Piano Quartets CD 1 - Domus
ARTIST=Domus
SUBTITLE=Opus 25
COMPOSER=Johannes Brahms
TRACKTOTAL=8
GROUPING=Piano Quartet No. 1 in g minor
ogg/01 - No.1 G Minor Op.25 -I- Allegro.ogg=I. Allegro
ogg/02 - No.1 G Minor Op.25 -II- Intermezzo. Allegro (ma non troppo).ogg=II. Intermezzo
ogg/03 - No.1 G Minor Op.25 -III- Andante con moto.ogg=III. Andante
ogg/04 - No.1 G Minor Op.25 -IV- Rondo alla Zingarese. Presto.ogg=IV. Rondo alla Zingarese
GROUPING=Piano Quartet No. 3 in c minor
SUBTITLE=Opus 60
ogg/05 - No.3 C Minor Op.60 -I- Allegro non troppo.ogg=I. Allegro non troppo
ogg/06 - No.3 C Minor Op.60 -II- Scherzo. Allegro.ogg=II. Scherzo. Allegro
ogg/07 - No.3 C Minor Op.60 -III- Andante.ogg=III. Andante
ogg/08 - No.3 C Minor Op.60 -IV- Finale. Allegro comodo.ogg=IV. Finale. Allegro comodo
```

There are two types of lines in the album description:

* A track descriptor in the form `filename.ogg=title`
* A tag in the form TAG=VALUE

Tags do not need to be specified for each track; instead, all previously seen
tags are applied to the current track.  You only need to specify tags that
are going to change for the following tracks.  We can see that in the example
above, where there are two works, and the GROUPING and SUBTITLE tags are changed
just before the list of tracks for the second work.
