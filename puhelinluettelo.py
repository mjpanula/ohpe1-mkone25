"""
Puhelinluettelo-algoritmi
=========================

Tämä skripti esittelee Harvardin CS50-kurssin ensimmäisellä luennolla esiteltyjä
hakualgoritmeja käyttäen puhelinluetteloa esimerkkinä.

Skripti demonstroi:
1. Lineaarinen haku (Linear Search)
2. Binäärihaku (Binary Search)

Algoritmit etsivät henkilön nimeä puhelinluettelosta ja palauttavat
vastaavan puhelinnumeron.
"""

import time


# ============================================================================
# ESIMERKKIDATA - Puhelinluettelo
# ============================================================================

# Järjestämätön puhelinluettelo (käytetään lineaarisessa haussa)
# Jokainen merkintä on sanakirja, jossa on nimi ja puhelinnumero
jarjestamaton_luettelo = [
    {"nimi": "Matti Meikäläinen", "numero": "040-1234567"},
    {"nimi": "Liisa Virtanen", "numero": "050-9876543"},
    {"nimi": "Pekka Korhonen", "numero": "045-5551234"},
    {"nimi": "Anna Nieminen", "numero": "044-7778889"},
    {"nimi": "Juho Mäkinen", "numero": "041-3334445"},
    {"nimi": "Sari Lehtonen", "numero": "050-2223334"},
    {"nimi": "Mikko Tuominen", "numero": "045-6667778"},
    {"nimi": "Kaisa Laine", "numero": "044-9990001"},
]

# Järjestetty puhelinluettelo (käytetään binäärihaussa)
# Nimet on järjestetty aakkosjärjestykseen, mikä on edellytys binäärihaulle
jarjestetty_luettelo = [
    {"nimi": "Anna Nieminen", "numero": "044-7778889"},
    {"nimi": "Juho Mäkinen", "numero": "041-3334445"},
    {"nimi": "Kaisa Laine", "numero": "044-9990001"},
    {"nimi": "Liisa Virtanen", "numero": "050-9876543"},
    {"nimi": "Matti Meikäläinen", "numero": "040-1234567"},
    {"nimi": "Mikko Tuominen", "numero": "045-6667778"},
    {"nimi": "Pekka Korhonen", "numero": "045-5551234"},
    {"nimi": "Sari Lehtonen", "numero": "050-2223334"},
]


# ============================================================================
# LINEAARINEN HAKU (Linear Search)
# ============================================================================

def lineaarinen_haku(luettelo, etsittava_nimi):
    """
    Lineaarinen haku käy läpi jokaisen elementin luettelossa yksi kerrallaan
    alusta loppuun, kunnes etsittävä löytyy tai koko luettelo on käyty läpi.
    
    Aikakompleksisuus: O(n)
    - Paras tapaus: O(1) - etsittävä on ensimmäisenä
    - Huonoin tapaus: O(n) - etsittävä on viimeisenä tai ei löydy
    - Keskimäärin: O(n/2) ≈ O(n)
    
    Parametrit:
        luettelo: Lista sanakirjoja, joissa on 'nimi' ja 'numero' avaimet
        etsittava_nimi: Etsittävän henkilön nimi (merkkijono)
    
    Palauttaa:
        Puhelinnumeron jos nimi löytyy, muuten None
    """
    
    # Alustetaan laskuri seuraamaan, montako vertailua tehdään
    vertailuja = 0
    
    # Käydään läpi jokainen henkilö luettelossa
    # enumerate() antaa meille sekä indeksin että henkilön tiedot
    for indeksi, henkilo in enumerate(luettelo):
        vertailuja += 1  # Kasvatetaan laskuria jokaisesta vertailusta
        
        # Tarkistetaan, onko tämän henkilön nimi se, mitä etsimme
        if henkilo["nimi"] == etsittava_nimi:
            # Löytyi! Tulostetaan tietoja hausta
            print(f"  ✓ Löytyi indeksistä {indeksi}")
            print(f"  ✓ Vertailuja tehty: {vertailuja}")
            
            # Palautetaan puhelinnumero
            return henkilo["numero"]
    
    # Jos tänne asti päästiin, nimeä ei löytynyt
    print(f"  ✗ Ei löytynyt")
    print(f"  ✗ Vertailuja tehty: {vertailuja}")
    return None


# ============================================================================
# BINÄÄRIHAKU (Binary Search)
# ============================================================================

def binaarihaku(luettelo, etsittava_nimi):
    """
    Binäärihaku on tehokkaampi hakualgoritmi, mutta vaatii että luettelo on
    järjestetty. Se jakaa haettavan alueen puoliksi joka kierroksella.
    
    Toimintaperiaate:
    1. Katso keskimmäinen alkio
    2. Jos se on etsittävä, olemme valmiita
    3. Jos etsittävä on pienempi, jatka vasemmasta puoliskosta
    4. Jos etsittävä on suurempi, jatka oikeasta puoliskosta
    5. Toista kunnes löytyy tai haku-alue loppuu
    
    Aikakompleksisuus: O(log n)
    - Paras tapaus: O(1) - etsittävä on keskellä
    - Huonoin tapaus: O(log n)
    - Esimerkki: 1000 alkiota vaatii maksimissaan ~10 vertailua
    
    Parametrit:
        luettelo: JÄRJESTETTY lista sanakirjoja ('nimi' ja 'numero')
        etsittava_nimi: Etsittävän henkilön nimi (merkkijono)
    
    Palauttaa:
        Puhelinnumeron jos nimi löytyy, muuten None
    """
    
    # Määritellään aluksi haku-alue: koko luettelo
    # 'vasen' on ensimmäinen indeksi, 'oikea' on viimeinen indeksi
    vasen = 0
    oikea = len(luettelo) - 1
    
    # Laskuri vertailujen määrälle
    vertailuja = 0
    
    # Toistetaan niin kauan kuin haku-alue ei ole tyhjä
    # (vasen <= oikea tarkoittaa että alueella on vielä alkioita)
    while vasen <= oikea:
        # Lasketaan keskimmäinen indeksi
        # Käytetään kaavaa (vasen + oikea) // 2
        # Huom: '//' on kokonaislukujakolasku Pythonissa
        keski = (vasen + oikea) // 2
        
        # Haetaan keskimmäisen alkion tiedot
        keskimmainen = luettelo[keski]
        vertailuja += 1
        
        # Tulostetaan debug-tietoa: mitä aluetta tutkitaan
        print(f"  → Tutkitaan indeksit {vasen}-{oikea}, keski: {keski} ({keskimmainen['nimi']})")
        
        # Verrataan keskimmäistä nimeä etsittävään
        if keskimmainen["nimi"] == etsittava_nimi:
            # Löytyi täsmälleen!
            print(f"  ✓ Löytyi indeksistä {keski}")
            print(f"  ✓ Vertailuja tehty: {vertailuja}")
            return keskimmainen["numero"]
        
        elif keskimmainen["nimi"] < etsittava_nimi:
            # Keskimmäinen nimi on aakkosjärjestyksessä ennen etsittävää
            # Joten etsittävä on oikealla puolella
            # Siirretään 'vasen' rajaa keskikohdan oikealle puolelle
            vasen = keski + 1
            print(f"  → '{keskimmainen['nimi']}' < '{etsittava_nimi}' - jatketaan oikealta")
        
        else:
            # Keskimmäinen nimi on aakkosjärjestyksessä etsittävän jälkeen
            # Joten etsittävä on vasemmalla puolella
            # Siirretään 'oikea' rajaa keskikohdan vasemmalle puolelle
            oikea = keski - 1
            print(f"  → '{keskimmainen['nimi']}' > '{etsittava_nimi}' - jatketaan vasemmalta")
    
    # Jos silmukasta poistuttiin, nimeä ei löytynyt
    print(f"  ✗ Ei löytynyt")
    print(f"  ✗ Vertailuja tehty: {vertailuja}")
    return None


# ============================================================================
# APUFUNKTIOT - Tulosten visualisointi
# ============================================================================

def tulosta_otsikko(otsikko):
    """
    Tulostaa muotoillun otsikon tekstille.
    Käytetään selkeyttämään ohjelman tulostetta.
    """
    print("\n" + "=" * 70)
    print(otsikko)
    print("=" * 70)


def tulosta_luettelo(luettelo, otsikko):
    """
    Tulostaa puhelinluettelon sisällön siististi muotoiltuna.
    
    Parametrit:
        luettelo: Tulostettava luettelo
        otsikko: Otsikko luettelolle
    """
    print(f"\n{otsikko}:")
    print("-" * 50)
    for i, henkilo in enumerate(luettelo):
        print(f"{i}: {henkilo['nimi']:.<30} {henkilo['numero']}")
    print("-" * 50)


def suorita_haku_ja_mittaa(haku_funktio, luettelo, nimi, algoritmin_nimi):
    """
    Suorittaa haun ja mittaa sen suoritusajan.
    
    Parametrit:
        haku_funktio: Käytettävä hakufunktio (lineaarinen_haku tai binaarihaku)
        luettelo: Puhelinluettelo josta haetaan
        nimi: Etsittävä nimi
        algoritmin_nimi: Algoritmin nimi tulostusta varten
    """
    print(f"\n🔍 Haetaan: '{nimi}' ({algoritmin_nimi})")
    print("-" * 50)
    
    # Mitataan suoritusaika
    # time.perf_counter() antaa tarkan ajan sekunteina
    aloitus = time.perf_counter()
    
    # Suoritetaan haku
    tulos = haku_funktio(luettelo, nimi)
    
    # Lasketaan kulunut aika
    lopetus = time.perf_counter()
    kulunut_aika = lopetus - aloitus
    
    # Tulostetaan tulos
    if tulos:
        print(f"  📞 Puhelinnumero: {tulos}")
    print(f"  ⏱️  Suoritusaika: {kulunut_aika:.6f} sekuntia")


# ============================================================================
# PÄÄOHJELMA - Demonstraatio
# ============================================================================

def main():
    """
    Pääfunktio joka demonstroi molempia hakualgoritmeja.
    
    Ohjelma:
    1. Näyttää järjestämättömän ja järjestetyn luettelon
    2. Suorittaa lineaarisia hakuja
    3. Suorittaa binäärihakuja
    4. Vertailee algoritmien tehokkuutta
    """
    
    # Tulostetaan tervetuloviesti
    tulosta_otsikko("PUHELINLUETTELO-ALGORITMI - CS50 Demonstraatio")
    
    print("\nTämä ohjelma demonstroi kahta eri hakualgoritmia:")
    print("1. Lineaarinen haku (Linear Search) - O(n)")
    print("2. Binäärihaku (Binary Search) - O(log n)")
    print("\nMolemmat algoritmit etsivät nimeä puhelinluettelosta.")
    
    # Näytetään luettelot
    tulosta_luettelo(jarjestamaton_luettelo, 
                     "Järjestämätön luettelo (lineaariseen hakuun)")
    tulosta_luettelo(jarjestetty_luettelo, 
                     "Järjestetty luettelo (binäärihakuun)")
    
    # ========================================================================
    # DEMONSTRAATIO 1: Lineaarinen haku
    # ========================================================================
    
    tulosta_otsikko("DEMONSTRAATIO 1: Lineaarinen haku")
    
    print("\nLineaarinen haku käy läpi jokaisen alkion järjestyksessä.")
    print("Se ei vaadi luettelon järjestämistä, mutta on hitaampi.")
    
    # Haku 1: Nimi löytyy alusta
    suorita_haku_ja_mittaa(lineaarinen_haku, jarjestamaton_luettelo, 
                          "Matti Meikäläinen", "Lineaarinen haku")
    
    # Haku 2: Nimi löytyy keskeltä
    suorita_haku_ja_mittaa(lineaarinen_haku, jarjestamaton_luettelo, 
                          "Pekka Korhonen", "Lineaarinen haku")
    
    # Haku 3: Nimi löytyy lopusta
    suorita_haku_ja_mittaa(lineaarinen_haku, jarjestamaton_luettelo, 
                          "Kaisa Laine", "Lineaarinen haku")
    
    # Haku 4: Nimeä ei löydy
    suorita_haku_ja_mittaa(lineaarinen_haku, jarjestamaton_luettelo, 
                          "Erkki Esimerkki", "Lineaarinen haku")
    
    # ========================================================================
    # DEMONSTRAATIO 2: Binäärihaku
    # ========================================================================
    
    tulosta_otsikko("DEMONSTRAATIO 2: Binäärihaku")
    
    print("\nBinäärihaku jakaa haettavan alueen puoliksi joka kierroksella.")
    print("Se vaatii järjestetyn luettelon, mutta on paljon nopeampi.")
    
    # Haku 1: Nimi keskellä
    suorita_haku_ja_mittaa(binaarihaku, jarjestetty_luettelo, 
                          "Liisa Virtanen", "Binäärihaku")
    
    # Haku 2: Nimi alussa
    suorita_haku_ja_mittaa(binaarihaku, jarjestetty_luettelo, 
                          "Anna Nieminen", "Binäärihaku")
    
    # Haku 3: Nimi lopussa
    suorita_haku_ja_mittaa(binaarihaku, jarjestetty_luettelo, 
                          "Sari Lehtonen", "Binäärihaku")
    
    # Haku 4: Nimeä ei löydy
    suorita_haku_ja_mittaa(binaarihaku, jarjestetty_luettelo, 
                          "Erkki Esimerkki", "Binäärihaku")
    
    # ========================================================================
    # YHTEENVETO
    # ========================================================================
    
    tulosta_otsikko("YHTEENVETO - Algoritmien vertailu")
    
    print("\n📊 LINEAARINEN HAKU (Linear Search)")
    print("   ✓ Edut:")
    print("     - Yksinkertainen toteuttaa")
    print("     - Toimii järjestämättömällä datalla")
    print("     - Hyvä pienille tietomäärille")
    print("   ✗ Haitat:")
    print("     - Hidas suurilla tietomäärillä")
    print("     - Aikakompleksisuus: O(n)")
    print("     - Pahimmassa tapauksessa käy läpi koko luettelon")
    
    print("\n📊 BINÄÄRIHAKU (Binary Search)")
    print("   ✓ Edut:")
    print("     - Erittäin nopea suurillakin tietomäärillä")
    print("     - Aikakompleksisuus: O(log n)")
    print("     - Esim. miljoona alkiota: ~20 vertailua riittää")
    print("   ✗ Haitat:")
    print("     - Vaatii järjestetyn datan")
    print("     - Järjestäminen vie aikaa O(n log n)")
    
    print("\n💡 KÄYTÄNNÖN OHJE:")
    print("   - Käytä lineaarista hakua kun:")
    print("     → Data on pieni (alle 100 alkiota)")
    print("     → Data on järjestämätön eikä sitä kannata järjestää")
    print("     → Haet vain kerran")
    print("\n   - Käytä binäärihakua kun:")
    print("     → Data on suuri (satoja, tuhansia tai miljoonia alkioita)")
    print("     → Data on jo järjestetty tai haet monta kertaa")
    print("     → Nopeus on kriittistä")
    
    print("\n" + "=" * 70)
    print("Demonstraatio päättyi!")
    print("=" * 70 + "\n")


# ============================================================================
# OHJELMAN KÄYNNISTYS
# ============================================================================

# Tämä lohko suoritetaan vain jos skripti ajetaan suoraan
# (ei suoriteta jos skripti tuodaan moduulina toiseen ohjelmaan)
if __name__ == "__main__":
    main()
