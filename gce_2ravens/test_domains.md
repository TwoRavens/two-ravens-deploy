
```
import requests

domains = ['apricot.2ravens.org', 'black.2ravens.org', 'blue.2ravens.org', 'brown.2ravens.org', 'cyan.2ravens.org', 'green.2ravens.org', 'grey.2ravens.org', 'lavender.2ravens.org', 'lime.2ravens.org', 'magenta.2ravens.org', 'maroon.2ravens.org', 'mint.2ravens.org', 'navy.2ravens.org', 'olive.2ravens.org', 'orange.2ravens.org', 'pink.2ravens.org', 'purple.2ravens.org', 'red.2ravens.org', 'white.2ravens.org', 'yellow.2ravens.org']

for x in domains:
  print('try: ', x)
  r = requests.get('http://' + x)
  print(r.status_code)

```
