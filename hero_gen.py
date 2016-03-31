import os, sys

#User input
while True:
    #Enter hero name
    print('')
    print("Hero Name: ", end='')
    #Convert to titled form,
    name = input().lower().title()
    #Check name validity
    if not os.path.isdir('VO_Hero/{}'.format(name)):
        print('Invalid path name, try again')
    else:
        break

#Create array of available skins for selected hero
skins = os.listdir('VO_Hero/{}'.format(name.title()))

#Ignore .DS_Store
if '.DS_Store' in skins:
    skins.remove('.DS_Store')

if len(skins) == 1:
    s_num = 1

else:
    #Print list of available skins if there is more than one
    inc = 1
    print('Skins for {}:'.format(name))
    for skin in skins:
        print(str(inc) + ') ' + skin)
        inc += 1

    #Get skin selection input from user
    while True:
        print('Choose Skin Number: ', end='')
        s_num = int(input()) #s_num = skin selection number (1-...)
        #Verify validity selection
        if s_num in range(1, inc):
            break
        else:
            print('Invalid number, try again')

skin_file = skins[s_num-1] #skin_file = name of selected skin
skins.remove(skin_file) #Remove skin selection from 'skins' array
link_list = [] #instantiate list for alternate skin hyperlinks

#add alternate skins to link_list
for skin in skins:
    #Convert " 'Hero' - 'Skin' " to 'Skin'
    link_list.append(skin.split(' - ')[1])

#Set 'title' variable, used for tab, main display, and alt names
if 'Default' in skin_file:
    title = name #title = default name
else:
    title = skin_file[skin_file.index('-')+2:] + ' ' + name #title = skin name

#Write the initial lines of the html file
header = """<!DOCTYPE html>
<html>
  <head>
    <title>{0}</title>
    <meta charset="utf-8">
    <link href="../styles/skin_heroes.css" rel="stylesheet" type="text/css">
    <link href='http://fonts.googleapis.com/css?family=Oswald:700' rel='stylesheet' type='text/css'>
  </head>
  <body>
    <div class="col" align="left">
      <h3><a href="../index.html">Main Menu</a></h3>
    </div>
    <div class="col" align="center">
      <h2>{0}</h2>
      <img src="../images/{1}.jpg" alt="{0}"/><br>""".format(title,title.lower())

text = header

#Get old download link
dlFound = False
for heroFile in os.listdir('hero_pages/'):
    if heroFile != '.DS_Store':
        if skin_file in heroFile:
            #read heroFile
            readFile = open(os.getcwd()+'/'+'hero_pages'+'/'+skin_file+'.html')
            fileContent = readFile.readlines()
            for seg in fileContent:
                if 'mega.nz' in seg:
                    downloadURL = seg[seg.index('<a href="')+8:seg.index(" target=")]
                    dlFound = True
            break

#Generate html surrounding doanload link
if dlFound is True:
    dl = """
      <a href={} target='_blank' class="link">
        <div class="download">
          <h4>Download</h4>
        </div>
      </a>
    </div>""".format(downloadURL)
else:
    dl = """
      <a href=DOWNLOAD_LINK_HERE target='_blank' class="link">
        <div class="download">
          <h4>Download</h4>
        </div>
      </a>
    </div>"""
    print('')
    print("Missing download link for: '" + skin_file + "'")
text += dl

altSkinHeader = """
    <div class="col" align="right">
      <h3>"""
text += altSkinHeader

for i in range(0, len(skins)):
    altSkinBody = """
        <a href="{0}.html">{1}</a><br>""".format(skins[i],link_list[i])
    text += altSkinBody

altSkinCloser = """
      </h3>
    </div>
    """
text += altSkinCloser

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
    #add block to file input string
    text += block
    counter += 1
#calculate and write number of needed placeholders
ph_count = 5 - (counter % 4)
ph = """
    <div class="placeholder"></div>"""
for i in range(ph_count):
    text += ph

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
text += closer

#Create file for hero in hero_pages folder named skin_file
hero_page = open("hero_pages/{}.html".format(skin_file),"w")

#Write text to file
hero_page.write(text)

#close file
hero_page.close()
print('done')
