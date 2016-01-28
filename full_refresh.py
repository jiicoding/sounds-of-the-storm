import os, sys


for name in os.listdir('VO_Hero'):
    if name == '.DS_Store':
        continue
    if '.DS_Store' in os.listdir('VO_Hero/'+name):
        os.remove('VO_Hero/'+name+'/.DS_Store')
        skins = os.listdir('VO_Hero/' + name)
        inc = len(skins)-1
    else:
        skins = os.listdir('VO_Hero/' + name)
        inc = len(skins)

    print(name)
    for skin in os.listdir('VO_Hero/' + name):
        print(skin)
        print(inc)
        skins = os.listdir('VO_Hero/' + name)
        print(skins)
        if skin != '.DS_Store':
            inc = len(skins)

            skin_file = skin #skin_file = name of selected skin
            print(skin_file)
            skins.remove(skin_file) #Remove skin selection from 'skins' array
            link_list = [] #instantiate list for alternate skin hyperlinks

            #add alternate skins to link_list
            for i in skins:
                #Convert " 'Hero' - 'Skin' " to 'Skin'
                link_list.append(i.split(' - ')[1])

            #Set 'title' variable, used for tab, main display, and alt names
            if 'Default' in skin_file:
                title = name #title = default name
            else:
                title = skin_file[skin_file.index('-')+2:] + ' ' + name #title = skin name

            #There's three header possibilities
            #1) No alternate skins
            #2) 1 alternate skin
            #3) 2 alternate skins

            #1) No alternate skins
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
            #2) 1 alternate skin
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
            #3) 2 alternate skins
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

            #Create file for hero in hero_pages folder named skin_file
            hero_page = open("hero_pages/{}.html".format(skin_file),"w")
            #Write header to file
            hero_page.write(header)

            #Generate mp3 body
            counter = 0
            #loop through each mp3 file in skin folder
            for track in os.listdir('VO_Hero/{}/{}'.format(name,skin_file)):
              #ex. track = 'AnubarakCybarakBase_AI_Attack00.mp3'
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
    <source src="../VO_Hero/{}/{}/{}" />
  </audio>
</div>""".format(t_name,name,skin_file,track)
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
