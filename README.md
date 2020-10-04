# Vallilan-lounasravintolat
Repo tietokantasovellus-kurssille
heroku:https://lounasravintolat.herokuapp.com/

Tavoitteena on tehdä sovellus suurin piirtein materiaalin kolmannen esimerkin mallin mukaisesti.  Valitsin aiheen, koska asun alle kilometrin päästä noin kymmenestä eri lounasravintolasta, joten aiheesta on kokemusta.
Sovelluksen pohjana tulee olemaan ravintola-arviot, mutta haluaisin lisätä jotain omaa tai ainutlaatuista esimerkin kohtien lisäksi. Päätin aiheen vasta hyvin myöhään joten en ole hirveästi perusideaa pidemmälle vielä miettinyt.
Toivottavasti olen päättänyt sovelluksen hienosäädöistä toiseen palautukseen mennessä saadakseni ohjaajien palautteen.
Haluaisin myös varmistuksen siitä, että ravintoloiden oikeiden nimien käyttäminen on sallittua ja/tai toivottua.

Muutamia ideoita sovelluksen mahdollisille lisätoiminnoille olisivat ravintoloiden omistajien kommentit, ravintoloiden käyttäjien työpaikat ja mahdollisesti ravintolan suosittelupalvelu (ehkä muiden käyttäjien historiaan perustuva, voi olla liian työläs). Kaikki kommentit ja työpaikat olisivat tietenkin keksittyjä.
Jos tuntuu tarpeelliselta, voin myös ottaa lounasravintoloita muualta kuin Vallilasta, tai vain keksiä uusia.

---------------------------------------------------------------------------------------------------------
Palautus 2:

Sovelluksessa on nyt ensin (täysin hyödytön) kirjautuminen ja sitten sivu, jossa voi lisätä uusia ravintoloita arvioitavaksi ja antaa niille 4 omaa arviointikriteeriä, mikä mahdollistaa saman ravintolan arvioimisen monella eri tavalla (esim. ruoan laatu ja ravintolan mukavuus voidaan arvioida nyt erikseen sen sijaan, että ravintolalla olisi vain yksi arvio).
Samalta sivulta voi myös tietenkin itse osallistua arviointiin ja katsoa aikaisemmat tulokset. Olen yrittänyt kääntää sovellusta englanniksi mutta jotain taisi vielä olla kääntämättä. Myönnän suoraan että nyt palautuksen hetkellä en ole vielä saanut sovellusta toimimaan herokuun, mutta tämä on työn alla ja toivottavasti valmis maanantaiaamuna.
Sovelluksen testauksen pitäisi olla hyvin itseselitteistä, kirjaudu vain sisään millä tahansa tunnuksilla ja kokeile eri funktioita (lisääminen/arviointi/arviointien katsominen).

------------------------------------------------------------------------------------------------------------
Palautus 3:

Suurin osa halutuista ominaisuuksista on valmiita, mutta ylitsepääsemättömiä ongelmia on tullut muutamassa kohdassa. Halusin tehdä admin-käyttäjiä, jotka saisivat poistaa ravintoloita, mutta admin-oikeuden varmistus ei ole vielä onnistunut. 
Tämän lisäksi kommenttien jättäminen ei jostain syystä onnistu, koska sovellus ei löydä poll_id:tä oikean kyselyn löytämiseksi vaikka se on annettu hidden inputilla aivan kuten answer-metodissa. Tämän kanssa olen edelleen melko pihalla, joten vinkit olisivat tervetulleita.
Sovelluksesta puuttuu vielä kokonaan kyselyiden järjestäminen esimerkiksi aakkosjärjestykseen tai arvioiden mukaan, ja sen lisäksi haluan vielä lisätä toiminnallisuuden joka katsoo arvioijien "occupation"-kenttää ja sen perusteella osaa suositella (kehnosti mutta kuitenkin) ravintolaa.
Muutamia linkkejä puuttuu myös, esimerkiksi home-sivulta ei pääse kirjautumaan ulos, mutta näiden tekeminen ei tuota vaikeuksia.
Sovellus on paljon enemmän vaiheessa kuin toivoisin, mutta uskon että saan loput tehtyä kunhan pääsen mainituista ongelmista yli.