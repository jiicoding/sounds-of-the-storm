import os, sys

while True:
    print("Hero Name: ", end='')
    name = input().lower().title()
    if not os.path.isdir('VO/{}'.format(name)):
        print('Invalid path name, try again')
    else:
        break
skins = os.listdir('VO/{}'.format(name.title()))
if '.DS_Store' in skins:
    skins.remove('.DS_Store')
inc = 1
print('Skins for {}:'.format(name))
for skin in skins:
    print(str(inc) + ') ' + skin)
    inc += 1

while True:
    print('Choose Skin Number: ', end='')
    s_num = int(input())
    if s_num in range(1, inc):
        break
    else:
        print('Invalid number, try again')

skin_file = skins[s_num-1] #filename of skin
skins.remove(skin_file)
link_list = []
for skin in skins:
    link_list.append(skin.split(' - ')[1])
if 'Default' in skin_file:
    title = name
else:
    title = skin_file[skin_file.index('-')+2:] + ' ' + name #how skin is referred to on screen

inc = inc - 1
if inc == 1:
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
      <img src="../images/{1}.jpg" class="icon" alt="{0}"/>
      <br>
      <a href="DOWNLOAD_LINK_HERE" target='_blank' class="link">
        <div class="download">
          <h4>Download</h4>
        </div>
      </a>
      <br>""".format(title,title.lower())
elif inc == 2:
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
      <br>""".format(title,skins[0],title.lower(),link_list[0])
else:
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
      <h3 id="right"><a href="{1}.html">{2}</a></h3>
      <h2>{0}</h2>
      <h3 id="left"><a href="../index.html">Main Menu</a></h3>
    </div>
    <h3 id="right"><a href="{3}.html">{4}</a></h3>
    <p></p>
    <h1>
        <img src="../images/{5}.jpg" class="icon" alt="{0}"/>
    </h1>
    </br>
    <a href="DOWNLOAD_LINK_HERE" target='_blank' class="link">
      <div class="download">
        <h4>Download</h4>
      </div>
    </a>
    <br>""".format(title,skins[0],link_list[0],skins[1],link_list[1],title.lower())
hero_page= open("{}.html".format(skin_file),"w")
hero_page.write(header)

counter = 0
for track in os.listdir('VO/{}/{}'.format(name,skin_file)):
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
    </div>""".format(t_name,name,skin_file,track)
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
