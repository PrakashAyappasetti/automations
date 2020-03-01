import urllib
from urllib.request import urlopen

# ht = '163g1a0505'
# _id = '56736241'
# _at = '5912588'
# url = f'https://jntuaresults.ac.in/results/res.php?ht={ht}&id={_id}&accessToken={_at}'
url = 'https://jntuaresults.ac.in/results/res.php?ht=163g1a0505&id=56736241&accessToken=5912588,true'
resp = urlopen(url)
data = resp.read()
print(data)
