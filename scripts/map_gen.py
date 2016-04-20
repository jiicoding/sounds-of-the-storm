import os, sys


voBGPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'vo/vo_bg/'))
bgPagesPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'pages/bg_pages/'))

#User input
while True:
    #Enter map name
    print("(case sensitive)")
    print("Battleground Name: ", end='')
    #set battleground name
    bg = input()
    #set directory and hero_page name
    bg_dir = 'Map - ' + bg
    #Check direcotry validity
    if not os.path.isdir(voBGPath + '/{}'.format(bg_dir)):
        print('Invalid path name, try again')
    else:
        break

#set image name
img = 'bg_' + bg.lower().replace(' ','-') + '.jpg'

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
      <img src="../../images/{1}" class="bg_icon" alt="{0}"/><br>
      <a href="DOWNLOAD_LINK_HERE" target='_blank' class="link">
        <div id="bgdownload">
          <h4>Download</h4>
        </div>
      </a>
    </div>
    <div class="col" align="right">
      <h3 id='skinParent' align='left'>
      </h3>
    </div>
    <br>""".format(bg, img)

#Create file for hero in hero_pages folder named skin_file
hero_page = open(bgPagesPath + "/{}.html".format(bg_dir),"w")
#Write header to file
hero_page.write(header)

#Generate mp3 body
counter = 0
#loop through each mp3 file in skin folder
for track in os.listdir(voBGPath + '/{}'.format(bg_dir)):
  #ex. track = '0_CreepVO_Necromancer_261.mp3'
  #ignore '.DS_Store'
  if track == '.DS_Store':
    continue

  start = track.index('_')+1 #ex. start = index of first letter after first '_',
                             #hopefully starting at the action name
  t_name = track[start:len(track)-4] #t_name = action name without .mp3
                                     #ex. t_name = 'AI_Attack00'
  t_name = t_name.replace('_',' ') #t_name = action name without '_'
                                   #ex. 'AI Attack00'
  #html audio block
  block = """
    <div class="track">
      <h4>{}</h4>
      <audio controls>
        <source src="../../vo/vo_bg/{}/{}" />
      </audio>
    </div>""".format(t_name,bg_dir,track)
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
