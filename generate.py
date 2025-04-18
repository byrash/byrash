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

#### I'm an Enterprise Architect.

- 🏢 I'm currently working at **A great company :)**
- 🌍 I'm mostly active within the **Leadership, Architecture & Dev Community**
- 💬 Ping me about **Architecture**, **Clean code**,  **Development**, **Design thinking**, **Leadership**
- 📫 Reach me: [shiv.byra@gmail.com](mailto:shiv.byra@gmail.com)
- ⚡️ Fun fact: I'm a huge fan of Multi Threading (All the things that happens only in Prod ) , Cyber Security & AI .

## Github Usage ~ Status 
![Shivaji's github stats](https://github-readme-stats.vercel.app/api?username=byrash&show_icons=true&hide_border=true&theme=dark&private=true)   

![Shivaji's profile views](https://komarev.com/ghpvc/?username=byrash&&style=flat-square")

## Language Usage ~ Status
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=byrash&layout=compact&theme=dark&show_icons=true&hide_border=true&private=true)

</p>
<h3 align="center">Have a nice day!</h3>
''')
f.close()
