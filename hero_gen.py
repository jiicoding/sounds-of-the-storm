import os, sys

print("hero name: ", end='')
name = input()
print("skin name: ", end='')
skin = input()
print("# of files in hero dir: ", end='')
skin_num = input()

if name == skin:
  title = skin
else:
  title = skin + ' ' + name

if not os.path.isdir('VO/{}/{}'.format(name,skin)):
  print('Invalid path name')
  sys.exit()

if skin_num == '1':
  header = """<!DOCTYPE html>
  <html>
    <head>
      <title>{0}</title>
      <meta charset="utf-8">
      <link href="../styles/skin_heroes.css" rel="stylesheet" type="text/css">
      <link href='http://fonts.googleapis.com/css?family=Oswald:700' rel='stylesheet' type='text/css'>
    </head>
    <body>
      <div class="header">
        <h3 id="right"></h3>
        <h2>{0}</h2>
        <h3 id="left"><a href="../index.html">Main Menu</a></h3>
      </div>
      <img src="../images/{2}.jpg" class="icon" alt="{0}}"/>
      <br>
      <a href="DOWNLOAD_LINK_HERE" target='_blank' class="link">
        <div class="download">
          <h4>Download</h4>
        </div>
      </a>
      <br>""".format(title,title.lower())
elif skin_num == '2':
  alt_skins = os.listdir('VO/{}'.format(name))
  alt_skins.remove('.DS_Store')
  alt_skins.remove(skin)

  if skin == name:
    link = alt_skins[0]
    alt_skins[0] = alt_skins[0] + ' ' + name
  else:
    link = 'Default'

  header = """<!DOCTYPE html>
  <html>
    <head>
      <title>{0}</title>
      <meta charset="utf-8">
      <link href="../styles/skin_heroes.css" rel="stylesheet" type="text/css">
      <link href='http://fonts.googleapis.com/css?family=Oswald:700' rel='stylesheet' type='text/css'>
    </head>
    <body>
      <div class="header">
        <h3 id="right"><a href="{1}.html">{3}</a></h3>
        <h2>{0}</h2>
        <h3 id="left"><a href="../index.html">Main Menu</a></h3>
      </div>
      <img src="../images/{2}.jpg" class="icon" alt="{0}"/>
      <br>
      <a href="DOWNLOAD_LINK_HERE" target='_blank' class="link">
        <div class="download">
          <h4>Download</h4>
        </div>
      </a>
      <br>""".format(title,alt_skins[0],title.lower(),link)
else:
  alt_skins = os.listdir('VO/{}'.format(name))
  alt_skins.remove('.DS_Store')
  alt_skins.remove(skin)
  if skin == name:
    link1 = alt_skin[0]
    link2 = alt_skin[1]
  else:
    alt_skins.remove(name)
    link1 = 'Default'
    link2 = alt_skin[0]
  header ="""<!DOCTYPE html>
<html>
  <head>
    <title>{0}</title>
    <meta charset="utf-8">
    <link href="../styles/skin_heroes.css" rel="stylesheet" type="text/css">
    <link href='http://fonts.googleapis.com/css?family=Oswald:700' rel='stylesheet' type='text/css'>
  </head>
  <body>
    <div class="header">
      <h3 id="right"><a href="{1}.html">{1}</a></h3>
      <h2>{0}</h2>
      <h3 id="left"><a href="../index.html">Main Menu</a></h3>
    </div>
    <h3 id="right"><a href="{2}.html">{2}</a></h3>
    <p></p>
    <h1>
        <img src="../images/{3}.jpg" class="icon" alt="{0}"/>
    </h1>
    </br>
    <a href="DOWNLOAD_LINK_HERE" target='_blank' class="link">
      <div class="download">
        <h4>Download</h4>
      </div>
    </a>
    <br>""".format(title,link1,link2,title.lower())
hero_page= open("{}.html".format(title),"w")
hero_page.write(header)

counter = 0
for track in os.listdir('VO/{}/{}'.format(name,skin)):
  if track == '.DS_Store':
    continue
  start = track.index('_')+1
  t_name = track[start:len(track)-4]
  t_name = t_name.replace('_',' ')
  block = """
    <div class="track">
      <h4>{}</h4>
      <audio controls>
        <source src="../VO/{}/{}/{}" />
      </audio>
    </div>""".format(t_name,name,skin,track)
  hero_page.write(block)
  counter += 1

ph_count = 5 - (counter % 4)
ph = """
    <div class="placeholder"></div>"""
for i in range(ph_count):
  hero_page.write(ph)

closer ="""
      <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

        ga('create', 'UA-67473619-1', 'auto');
        ga('send', 'pageview');
      </script>
    </body>
  </html>"""
hero_page.write(closer)
hero_page.close()
