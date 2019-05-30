import time
from random import randint
from sendemail import SendEmail 

sender_email = 'pcaviator18@gmail.com'
receiver_email = 'pcaviator18+01@gmail.com'

password = input('Password: ')

subject = 'Happy Birthday! 🎂🎉🎈'
names = ['Leia', 'Cutie', 'Babe', 'Baby', 'Woman', 'Thot', 'Hoe']
emojis = ['😊', '💗', '💜', '🔥', '🍑', '🍆', '🌶️']

images = [
  'https://i.redd.it/un44882dvyj21.jpg', 
  'https://i.imgur.com/6VgM90g.jpg',
  'https://i.imgur.com/fcuRqwl.jpg', 
  'https://i.redd.it/fxqfz6w62v821.jpg', 
  'https://i.imgur.com/olvP9F4.jpg',
  'https://i.redd.it/tbnqzmcp4k411.jpg',
  'https://i.imgur.com/vaLYc.jpg',
  'https://i.redd.it/6azy3rjaopv01.jpg', 
  'https://i.imgur.com/aneCtPJ.jpg',
  'https://i.redd.it/jpqodmc83ia21.jpg',
  'https://i.imgur.com/zyZv7Ru.jpg',
  'https://i.imgur.com/z2WsIvI.jpg',
  'https://i.redd.it/q43v73nhbpn21.jpg',
  'https://i.imgur.com/u5xinP4.jpg',
  'https://i.redd.it/j7azr1mno8511.jpg',
  'https://i.imgur.com/pLoeg5w.jpg',
  'https://i.imgur.com/92nhSJ2.jpg',
  'https://i.imgur.com/y74Y9Ty.jpg',
  'https://i.imgur.com/QHdJy0Q.png',
  'https://i.redd.it/av9alv0xf0e11.jpg',
  'https://i.redd.it/q8fvn0cc4h411.jpg',
  'https://i.imgur.com/Je8Kuwm.jpg',
  'https://i.redd.it/uesiw1u8imtz.jpg',
  'https://i.redd.it/r7ugv0mlbupz.jpg',
  'https://i.imgur.com/ro3bnpL.jpg',
  'https://i.imgur.com/5TnG6eX.jpg',
  'https://i.imgur.com/gkCcExY.jpg',
  'https://i.imgur.com/weegEzi.jpg',
  'https://i.redd.it/3bvr3x6r9z011.jpg',
  'https://i.imgur.com/xgkC7h6.jpg',
  'https://i.imgur.com/ZwcT3OY.jpg',
  'https://i.redd.it/fssuxogzr5b11.jpg',
]

message = """\
<html>
  <body>
    <h3>Happy Birthday {name}!</h3><br>
    <p>
       Hope you're having a great day! Here's a little something for you:<br>
       <img src="{image}" alt="" style="max-width: 700px"/>
       <br>
       Love Joel! {emoji} 
    </p>
  </body>
</html>
"""

for i in range(0, len(images)):
      val = randint(0, 6)
      email = SendEmail(sender_email, receiver_email, password)
      email.send(subject, message.format(name=names[val], emoji=emojis[val], image=images[i]))
      time.sleep(900)
