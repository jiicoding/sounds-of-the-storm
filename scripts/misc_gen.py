import os, sys


voPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'vo/vo_misc/'))
PagesPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'pages/misc_pages/'))

#set image name
img = 'misc_goatmen.png'
title = 'misc_GoatMen'

#set header
header = """<!DOCTYPE html>
<html>
  <head>
    <title>{0}</title>
    <meta charset="utf-8">
    <link href="../../css/skin_heroes.css" rel="stylesheet" type="text/css">
    <link href='http://fonts.googleapis.com/css?family=Oswald:700' rel='stylesheet' type='text/css'>
  </head>
  <body>
    <div class="col" align="left">
      <h3><a href="../../index.html" id="menu">Main Menu</a></h3>
    </div>
    <div class="col" align="center">
      <h2>{0}</h2>
      <img src="../../images/{1}" class="misc_icon" alt="{0}"/><br>
      <a href="DOWNLOAD_LINK_HERE" target='_blank' class="link">
        <div id="miscdownload">
          <h4>Download</h4>
        </div>
      </a>
    </div>
    <div class="col" align="right">
      <h3 id='skinParent' align='left'>
      </h3>
    </div>
    <br>""".format(title, img)


#Create file for hero in hero_pages folder named skin_file
hero_page = open(PagesPath + "/{}.html".format(title),"w")
#Write header to file
hero_page.write(header)

#Generate mp3 body
counter = 0
#loop through each mp3 file in skin folder
for track in os.listdir(voPath + '/{}'.format(title)):
  #ex. track = '0_CreepVO_Necromancer_261.mp3'
  #ignore '.DS_Store'
  if track == '.DS_Store':
    continue

  #html audio block
  block = """
    <div class="track">
      <h4>{1}</h4>
      <audio controls>
        <source src="../../vo/vo_misc/{0}/{1}" />
      </audio>
    </div>""".format(title,track)
  #write block to file
  hero_page.write(block)
  counter += 1
#calculate and write number of needed placeholders
ph_count = 5 - (counter % 4)
ph = """
    <div class="placeholder"></div>"""
for i in range(ph_count):
  hero_page.write(ph)

#Write google analytics code and closing tags
closer ="""
    <script src='../../js/jquery-1.12.2.min.js'></script>
    <script src='../../js/heroScript.js'></script>
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
#close file
hero_page.close()
