import requests
import json
import random

f = open("./README.md", "w")
pokemon_id = random.randint(1, 151)
res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
result = json.loads(res.text)
f.write(f'''
<p align="center">
<img src="{result['sprites']['front_default']}" width="150" height="150">

### Hello {{ You }} 👋

#### I'm a Senior Solution Designer / Architect working in Australia.

- 🏢 I'm currently working at **A great company :)**
- ⚙️ I use daily: `AWS`,  `Java`,  `Go lang`,  `React`, `Angular`,  `Python` &  `Few more ...`
- 🌍 I'm mostly active within the **Dev Community**
- 💅 Designed: @pestphp, [NorthMeetsSouth.audio](https://www.northmeetssouth.audio), [ThenPing.me](https://thenping.me), [HappydDev.fm](https://www.happydev.fm), etc…
- 💬 Ping me about **Architecture**, **Clean code**,  **Development**, **Design thinking**
- 📫 Reach me: [mailto:shivaji.byrapaneni@gmail.com](shivaji.byrapaneni@gmail.com)
- ⚡️ Fun fact: I'm a huge fan of Multi Threading (All the things that happens only in Prod ) & Security Concepts.
</p>
<h3 align="center">Have a nice day!</h3>
''')
f.close()
