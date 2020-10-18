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

Viime kerran palautteista:
Mietin klassisen naiivin äänestysjärjestelmän ongelmaa jonkun aikaa ja päädyin siihen lopputulokseen, että on parempi antaa yhden käyttäjän antaa samalle ravintolalle monta arviota, koska mielipide voi tietenkin ajan kanssa muuttua. Ehkä paras ratkaisu olisi arvioinnin rajoittaminen esimerkiksi yhteen viikossa?
Arvostelut tosiaan pitäisi laittaa luettavaksi suoraan etusivulta ennen kirjautumista, se pääsi unohtumaan mutta tuskin tuottaa hirveitä vaikeuksia.
Loput kommentit on otettu huomioon ja hoidettu, vaikka käyttäjätiedon käyttö on edelleen hieman hakusessa admin-oikeuden kannalta.
-----------------------------------------------------------------------------------------------------------------------------------------------------
Loppupalautus:

Sovelluksen testaamisen pitäisi olla melko yksinkertaista. Valitettavasti sekä occupation että admin user kentät ovat vieläkin hyödyttömiä, mutta niihin täytyy silti valita jotain, että käyttäjä luodaan tietokantaan. En löytänyt tapaa vahvistaa käyttäjän admin-asetusta, ja en ehtinyt saada recommendations-tietokantaa toimimaan halutulla tavalla muiden ongelmien takia. 
Ajatuksena oli, että jokaisen ravintolan kohdalla lukisi sen suosituin käyttäjäkunta, ja sen lisäksi ehkä vielä suositusten kokonaismäärä ja sivun yläosassa kunkin käyttäjäkunnan (occupation) suosimat ravintolat. Arvostelut ja kommentointi kuitenkin toimivat halutulla tavalla, ja sivuston navigointi on parantunut suurest aiempiin versioihin verrattuna. Sivuston tyyli on melko yksitoikkoinen, käytin bootstrappia ja sen päälle hieman omia muutoksia, mutta
halusin enimmäkseen keskittyä sovelluksen toiminnallisuuteen, joka silti jäi kesken. Leijonanosa sovellukseen käytetystä ajasta meni noin viiden saman ongelman selvittämiseen mikä nyt jälkeenpäin näkyy toiminnallisuuksien puutteissa, ja niistäkin onnistuin selvittämään vain osan. Kurssi oli kuitenkin äärimmäisen opettavainen ja ongelmista huolimatta tuntui siltä, että sain 
jotain konkreettista ja mahdollisesti hyödyllistä tehtyä.
Harmittaa vain se tunne, että sovelluksesta olisi melko helpolla saanut paljon mallikkaamman.

----------
(Deadlinen jälkeen kirjoitettu osa)
Haluan kuitenkin jatkaa sovelluksen kehittämistä loppuun ihan harjoituksen vuoksi ja toivon, että se ei haittaa arvostelua. Githubista kai saa deadlinea edeltävän version, mikäli olen ehtinyt päivittää sovellusta ennen sen arvostelua.
PS. pahoittelut rumasta ulkoasusta, cornsilk käy vanhaksi äkkiä