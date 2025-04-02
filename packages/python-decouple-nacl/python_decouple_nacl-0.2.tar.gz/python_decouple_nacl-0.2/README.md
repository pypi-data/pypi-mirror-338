# python-decouple-nacl

Asymmetrisesti salattujen asetuksien tuki `python-decouple`-paketissa.

Täydentää `python-decouple`-paketin määrittelemää `Config`-luokkaa siten, että
- kuvioon `!{...}` täsmäävät merkkijonot asetuksen arvossa tunnistetaan salatuiksi merkkijonoiksi
- aaltosulkeiden sisältö tulkitaan Base-64-koodattuna tavujonona
- tavujono puretaan selväkieliseksi yksityisellä avaimella
- kuvio korvataan tällä selväkielisellä tekstillä ennen mahdollisten `cast`- ja `default`-parametrien soveltamista.


## Avaimet

Yksityinen avain poimitaan `DECOUPLE_NACL_SK`-asetusavaimella samasta `AutoConfig`- tai `Config`-oliosta kuin purettavat asetukset.
- avaimia voi olla useita pilkulla erotettuna
- kunkin avaimen arvo tulkitaan Base-64-koodattuna tavujonona

Mikäli myös julkinen avain on annettu asetusavaimella `DECOUPLE_NACL_PK`, tulkitaan tämäkin Base-64-tavujonona ja validoidaan yhdessä yksityisen avaimen kanssa.

Mikäli yksityisiä avaimia on asetettu useita, on julkisen avaimen asetus pakollinen: käytettävä yksityinen avain valitaan tämän perusteella.


## Asennus

Paketti:
```bash
pip install python-decouple-nacl
```

Tuonti (kuten `python-decouple`-paketissa):
```python
from decouple_nacl import config, ...

config(...)
```

Huomaa, että `import`-käsky tekee tarvittavat muutokset `python-decouple`-paketin
toteuttamiin luokkiin ja funktioihin; tarvittaessa voidaan tehdä pelkkä tyhjä tuonti:
```python
import decouple_nacl
```


## Käyttöönotto


### Avainpari

```python
from decouple_nacl_tyokalut import luo_avainpari
luo_avainpari()  # Tulostaa yksityisen ja julkisen avaimen.

# TAI:

from nacl.public import PrivateKey
sk = PrivateKey.generate()
pk = pk.public_key

# Tallennetaan yksityinen avain omaan (suojattuun) .env-tiedostoonsa:
with open('/(1)/.env', 'w') as kahva:
  kahva.write(
    f'DECOUPLE_NACL_SK={base64.b64encode(sk.encode()).decode()}\n'
  )

# Tallennetaan julkinen avain erilliseen, julkisesti (git) hallinnoituun
# .env-tiedostoonsa:
with open('/(2)/.env', 'w') as kahva:
  kahva.write(
    f'DECOUPLE_NACL_PK={base64.b64encode(pk.encode()).decode()}\n'
  )
```

### Salatut parametrit

Tulostetaan tarvittavat asetusparametrit salatussa muodossa.
Tuloste viedään sellaisenaan julkiseen .env-tiedostoon.
```python
from decouple_nacl_tyokalut import salaa_data
salaa_data('...')  # sulkujen sisään DECOUPLE_NACL_PK-parametrin sisältö
```

Esimerkki tulostiedostoista:
```env
# /(1)/.env
DECOUPLE_NACL_SK=/CRP06uxYokIqZeTrnFkRxBhGMmipige8h+etn/qz2c=


# /(2)/.env
DECOUPLE_NACL_PK=Iuhvvgo3J4bKxDo+jMeT/J6ELzOW6+H8qElWxqJj0xc=
SALAISUUS=!{hHUNiQieNxzIhYC8Pk2qgbT3w4hMdEAUMp9tx39gwkTp0vUuql83hl9//KCqXDnDDZA=}
```

Komento uusien parametrien lisäämiseksi .env-tiedostoon:
```bash
$ python -c '__import__("decouple_nacl_tyokalut").salaa_data("'$( sed -En 's/DECOUPLE_NACL_PK=//p' projekti/.env )'")' <<EOF >>> projekti/.env
AVAIN = arvo
AVAIN2 = arvo2
...
EOF
$
```


## Käyttö

Käyttäjälle parametrien salaaminen ei näy. Käyttö tavanomaisesti decouplen
työkaluilla:
```python
from decouple import AutoConfig

CONFIG = AutoConfig(...)
assert CONFIG('SALAISUUS', cast=int) == '42'
```
