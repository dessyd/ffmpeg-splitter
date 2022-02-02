# use ffmpeg to split an mp3 according to a set list
from __future__ import print_function
import subprocess as sp

# NB: add -copy if from m4a -> m4a; else no -copy
setfile = './titles.set'
cdfile = './Modern Eon - Fiction Tales - full.m4a'
outdir = './tracks'
meta_src = 'https://www.youtube.com/watch?v=YnyrVst8HkQ'
do_copy = True
print('splitting \'%s\' according to sets in \'%s\' into directory \'%s\'' % (cdfile, setfile, outdir))

metas = {'artist':'Modern Eon', 'album':'Fiction Tales'}
metastring = ' '.join([ '-metadata %s="%s"' % (k,v) for k,v in metas.items()])

songs = []
with open(setfile) as f:
  for line in f:
    start, title = line.strip().split(' ', 1)
    songs.append((start, title))

print('read %d lines' % len(songs))

# set id3 tags ala http://jonhall.info/how_to/create_id3_tags_using_ffmpeg
cmds = []
for i in range(len(songs) - 1):
  cmd = (songs[i][0], songs[i+1][0], songs[i][1])
  cmds.append(cmd)

  run = 'ffmpeg -y -i \"%s\" -acodec %s -ss %s -to %s ' % (cdfile, 'copy' if do_copy else 'libfdk_aac -qscale:a 2', cmd[0], cmd[1])
  run += '%s -metadata title="%s" -metadata track="%d/%d" -metadata publisher="%s" ' % (metastring, cmd[2], i+1, len(songs) - 1, meta_src)
  run += '"%s/%02d %s.m4a"' % (outdir, i + 1, cmd[2])
  # print("\tcmd: %s" % run)
  sp.call(run, shell=True)
  #