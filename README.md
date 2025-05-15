# Scripts

Various simple scripts for Linux:

* `trackpoint` : set sensitivity, speed, drift time, and acceleration of ThinkPad TrackPoint
* `gateway` : network gateway IP address
* `ipaddr` : print IP address
* `externalip` : print external IP address (as seen from outside the NAT router)
* `diskusers` : print summary every ten seconds of processes using disk
* `filesbetween`: find files with modification times in a date range
* `oggalbum`: Tag a set of Ogg Vorbis files using an album description file
* `oggmakealbum`: Create an album description file from a set of Ogg Vorbis files
* `cdmakealbum`: Create an album description file from a CD
* `oggripalbum`: Rip a CD info a set of Ogg Vorbis files
* `redirect.cgi`: CGI script to allow censored URLs to be posted on Reddit and Twitter
* `mdump`: hexadecimal file dumper
* `cookies` : convert Firefox's cookies.sqlite format to Netscape cookies
* `firefox-dpms` : disable screensaver when Firefox plays sounds/videos
* `detab` - filter to changes tabs to spaces

## Ogg Vorbis scripts

There are four Ruby scripts here related to tagging and ripping Ogg Vorbis files.

### Tagging Ogg Vorbis files

The scripts `oggalbum` and `oggmakealbum` make it easier (for me, at least)
to edit the comment tags in Ogg Vorbis audio files.  I dislike using GUI tools for
this purpose, so these scripts use (or create) album description files, which
are plain text and easy to edit.  The scripts also support the tagging needed
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

Here is a sample album descriptor for a CD that has two works:

```
ALBUM=Piano Quartets CD 1 - Domus
DATE=1988
ARTIST=Domus
GENRE=Classical
TRACKTOTAL=8
COMPOSER=Johannes Brahms
GROUPING=Piano Quartet No. 1 in g minor
SUBTITLE=Opus 25
01 - No.1 G Minor Op.25 -I- Allegro.ogg=I. Allegro
02 - No.1 G Minor Op.25 -II- Intermezzo. Allegro (ma non troppo).ogg=II. Intermezzo
03 - No.1 G Minor Op.25 -III- Andante con moto.ogg=III. Andante
04 - No.1 G Minor Op.25 -IV- Rondo alla Zingarese. Presto.ogg=IV. Rondo alla Zingarese
GROUPING=Piano Quartet No. 3 in c minor
SUBTITLE=Opus 60
05 - No.3 C Minor Op.60 -I- Allegro non troppo.ogg=I. Allegro non troppo
06 - No.3 C Minor Op.60 -II- Scherzo. Allegro.ogg=II. Scherzo. Allegro
07 - No.3 C Minor Op.60 -III- Andante.ogg=III. Andante
08 - No.3 C Minor Op.60 -IV- Finale. Allegro comodo.ogg=IV. Finale. Allegro comodo
```
There are two types of lines in the album description:

* A track descriptor in the form `filename.ogg=title`
* A tag in the form TAG=VALUE

Tags do not need to be specified for each track; instead, all previously seen
tags are applied to the current track.  You only need to specify tags that
are going to change for the following tracks.  We can see that in the example
above, where there are two works, and the GROUPING and SUBTITLE tags are changed
just before the list of tracks for the second work.

To change the tags for a set of Ogg Vorbis files, use `oggalbum <albumfile>`
where `<albumfile>` is an album descriptor file, as shown above.
(I typically use the filename `album.txt` for album descriptors.)

To generate an album descriptor from a set of Ogg Vorbis files, use
`oggalbum file...`.  You can use wildcard filenames, but be aware that
that the sort order of the filenames may not be the same as the track
order.  To prevent this problem when ripping an album, make sure that the first
characters in the filename are the track number.  The ripping scripts
described below can help with this.

### Ripping Ogg Vorbis files

Use the scripts `cdmakealbum` and `oggripalbum` to rip a CD into Ogg Vorbis files.

First use `cdmakealbum` to create a first cut at an album descriptor file.
This script reads the CD in the `/dev/cdrom` device and queries two online music
databases (Gnudb and MusicBrainz) for album and track information.  It then
prints the equivalent album descriptors for all the discs found in these
databases.  This can result in multiple descriptors being printed, but this is useful
because these databases often have incorrect or missing information, and
you can edit the output to create a suitable album descriptor.

By default, `cdmakealbum` generates track listings in which the
filenames consists of the track number, followed by the track title,
and terminated with `.ogg`.  This scheme ensures that the filename
sort order will be the same as the track number sort order. Use the
`-f` option to change the way the filename is constructed.
You can also edit the resulting album descriptor manually
to use any naming convention you choose, perhaps to simplify
or shorten the filenames.

Once you have a good album descriptor in a file (which I typically
name `album.txt`), use the script `oggripalbum` to rip the CD tracks
into a set of Ogg Vorbis files.  The tags specified in the album
descriptor will be applied to the Ogg files.  You can check
this by running `oggmakealbum *.ogg` after the ripping is done;
the result should be identical with the album descriptor file.
