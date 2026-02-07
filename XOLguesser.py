import random
import difflib
import time

# XOLguesser

# Developed by AEROforge
# Supervised and Founded by AEROxol
# Programming and Debugging by AEROxol

# Licensed under GNU General Public License v3.0 (GPLv3)
# Anyone redistributing or modifying this code must retain this notice.

# Copyright (C) 2026 AEROforge (AEROxol)
# Licensed under GNU GPLv3
# Trademark: XOLguesser is a brand of AEROforge


#Version 0.1: Release
#Version 0.2: Minor bug fixes; revorked menu options
#Version 0.3: Removed continent selection; added clearner menu format
#Version 0.4: Added territories, US states, and Candain provinces
#Version 0.5: Added ASCII art banner, added new options
#Version 0.6: Added new territories
#Version 0.7: State abriviatons added; New territories and aliases
#Version 0.8: Expanded aliase support for Oceania, North America, and Europe
#Version 0.9: Added South America; laid framework for captials guessing feature
#Version 1.0: Offical Release; basic bugs fixed
#Version 1.1: Added new territories; expanded aliases to other continents
#Version 1.2: Altered menu format; now two menus
#Version 1.3: Reverted menu back to old format
#Version 1.4: Complete capital option
#Version 1.5: Fixed capital menu to prevent repeating over again
#Version 1.6: Altered minor wording of promts
#Version 1.7: Finalized the completion of the capital option
#Version 1.8: Added state abrviations in upercase
#Version 1.9: Added state abrviations in lowercase and lowercase charater support where needed
#Version 2.0: Edited ASCII art to fit better and added loading screen
#Version 2.1: Started to add state capitals guessing game
#Verison 2.2: Added new hints for state captials
#Verison 2.3: Completed state capitals for general use
#Verison 2.4: Bug testing/fixing
#Verison 2.5: Fixed double asking if you want to play again bug
#Verison 2.6: Added year founded hint and removed region hint
#Version 2.7: Added new aliais and short names for select countries
#Verison 2.8: Fixed indentation issues and syntax errors relating to quitting the game
#Verison 2.9: Improved game quitting mechaninc
#Verison 3.0: Added new game mode; guess country based on capital
#Verison 3.1: Fixed bug where guess country based on capital would only play once then exit and not be playable again
#Verison 3.2: Added partial state capitals to guess the state game mode
#Verison 3.3: Finished guess the state based on the capital mode
#Verison 3.4: Added new menu

# ASCII Art
art = ("|---------------------------------------------------------------------------------------------------------|\n|                                                                                                         |\n|    /$$   /$$  /$$$$$$  /$$                                         Desgined and Programmed by AEROxol   |\n|   | $$  / $$ /$$__  $$| $$                                                                              |\n|   |  $$/ $$/| $$  \ $$| $$        /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$  /$$$$$$   /$$$$$$    |\n|    \  $$$$/ | $$  | $$| $$       /$$__  $$| $$  | $$ /$$__  $$ /$$_____//$$_____/ /$$__  $$ /$$__  $$   |\n|     >$$  $$ | $$  | $$| $$      | $$  \ $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$ | $$$$$$$$| $$  \__/   |\n|    /$$/\  $$| $$  | $$| $$      | $$  | $$| $$  | $$| $$_____/ \____  $$\____  $$| $$_____/| $$         |\n|   | $$  \ $$|  $$$$$$/| $$$$$$$$|  $$$$$$$|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/|  $$$$$$$| $$         |\n|   |__/  |__/ \______/ |________/ \____  $$ \______/  \_______/|_______/|_______/  \_______/|__/         |\n|                                  /$$  \ $$                                                              |\n|                                 |  $$$$$$/                                                              |\n|                                  \______/                                                 Version 3.4   |\n|                                                                                                         |\n|---------------------------------------------------------------------------------------------------------|")


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Starting XOLguesser...\n")
time.sleep(1)
print(art)
print("\n")

time.sleep(1)

# -------------------------
# STATS
# -------------------------
stats = {
    "played": 0,
    "wins": 0,
    "losses": 0
}

# -------------------------
# Countries, Territories, Dependencies, States, Provinces
# Includes states and providences
# -------------------------

COUNTRIES = [
    # Africa
    {"name":"Algeria","short":"Algeria","continent":"Africa","capital":"Algiers","region":"North Africa","population":45,"aliases":[], "territory":False, "un_member":True},
    {"name":"Angola","short":"Angola","continent":"Africa","capital":"Luandaon","region":"Southern Africa","population":36,"aliases":[], "territory":False, "un_member":True},
    {"name":"Benin","short":"Benin","continent":"Africa","capital":"Porto Novo","region":"West Africa","population":13,"aliases":[], "territory":False, "un_member":True},
    {"name":"Botswana","short":"Botswana","continent":"Africa","capital":"Gaborone","region":"Southern Africa","population":2.6,"aliases":[], "territory":False, "un_member":True},
    {"name":"Burkina Faso","short":"Burkina Faso","continent":"Africa","capital":"Ouagadougou","region":"West Africa","population":21,"aliases":[], "territory":False, "un_member":True},
    {"name":"Burundi","short":"Burundi","continent":"Africa","capital":"Gitega","region":"East Africa","population":11,"aliases":[], "territory":False, "un_member":True},
    {"name":"Cameroon","short":"Cameroon","continent":"Africa","capital":"Yaounde","region":"Central Africa","population":27,"aliases":[], "territory":False, "un_member":True},
    {"name":"Cape Verde","short":"Cape Verde","continent":"Africa","capital":"Praia","region":"West Africa","population":0.5,"aliases":[], "territory":False, "un_member":True},
    {"name":"Central African Republic","short":"Cemonitorntral African Republic","continent":"Africa","capital":"Bangui","region":"Central Africa","population":5,"aliases":[], "territory":False, "un_member":True},
    {"name":"Chad","short":"Chad","continent":"Africa","capital":"NDjamena","region":"Central Africa","population":17,"aliases":["TD"], "territory":False, "un_member":True},
    {"name":"Comoros","short":"Comoros","continent":"Africa","capital":"Moroni","region":"West Africa","population":0.8,"aliases":["KM"], "territory":False, "un_member":True},
    {"name":"Democratic Republic of the Congo","short":"Democratic Republic of the Congo","continent":"Africa","capital":"Kinshasa","region":"Central Africa","population":96,"aliases":["DRC"], "territory":False, "un_member":True},
    {"name":"Republic of the Congo","short":"Republic of the Congo","continent":"Africa","capital":"Brazzaville","region":"Central Africa","population":6,"aliases":[], "territory":False, "un_member":True},
    {"name":"Djibouti","short":"Djibouti","continent":"Africa","capital":"Djibouti","region":"West Africa","population":1,"aliases":[], "territory":False, "un_member":True},
    {"name":"Egypt","short":"Egypt","continent":"Africa","capital":"Cairo","region":"North Africa","population":109,"aliases":[], "territory":False, "un_member":True},
    {"name":"Equatorial Guinea","short":"Equatorial Guinea","continent":"Africa","capital":"Malabo","region":"Central Africa","population":2,"aliases":[], "territory":False, "un_member":True},
    {"name":"Eritrea","short":"Eritrea","continent":"Africa","capital":"Asmara","region":"Central Africa","population":4,"aliases":[], "territory":False, "un_member":True},
    {"name":"Eswatini","short":"Eswatini","continent":"Africa","capital":"Lobamba","region":"Southern Africa","population":1,"aliases":[], "territory":False, "un_member":True},
    {"name":"Ethiopia","short":"Ethiopia","continent":"Africa","capital":"Addis Ababa","region":"East Africa","population":120,"aliases":[], "territory":False, "un_member":True},
    {"name":"Gabon","short":"Gabon","continent":"Africa","capital":"Libreville","region":"Central Africa","population":2,"aliases":[], "territory":False, "un_member":True},
    {"name":"The Gambia","short":"Gambia","continent":"Africa","capital":"Banjul","region":"West Africa","population":3,"aliases":["Gambia"], "territory":False, "un_member":True},
    {"name":"Ghana","short":"Ghana","continent":"Africa","capital":"Accra","region":"West Africa","population":33,"aliases":[], "territory":False, "un_member":True},
    {"name":"Guinea","short":"Guinea","continent":"Africa","capital":"Conakry","region":"West Africa","population":14,"aliases":[], "territory":False, "un_member":True},
    {"name":"Guinea-Bissau","short":"Guinea-Bissau","continent":"Africa","capital":"Bissau","region":"West Africa","population":2,"aliases":[], "territory":False, "un_member":True},
    {"name":"Ivory Coast","short":"Ivory Coast","continent":"Africa","capital":"Yamoussoukro","region":"West Africa","population":27,"aliases":[], "territory":False, "un_member":True},
    {"name":"Kenya","short":"Kenya","continent":"Africa","capital":"Nairobi","region":"East Africa","population":53,"aliases":[], "territory":False, "un_member":True},
    {"name":"Lesotho","short":"Lesotho","continent":"Africa","capital":"Maseru","region":"Southern Africa","population":2,"aliases":[], "territory":False, "un_member":True},
    {"name":"Liberia","short":"Liberia","continent":"Africa","capital":"Monrovia","region":"West Africa","population":5,"aliases":[], "territory":False, "un_member":True},
    {"name":"Libya","short":"Libya","continent":"Africa","capital":"Tripoli","region":"North Africa","population":7,"aliases":["LY"], "territory":False, "un_member":True},
    {"name":"Madagascar","short":"Madagascar","continent":"Africa","capital":"Antananarivo","region":"East Africa","population":26,"aliases":[], "territory":False, "un_member":True},
    {"name":"Malawi","short":"Malawi","continent":"Africa","capital":"Lilongwe","region":"East Africa","population":19,"aliases":[], "territory":False, "un_member":True},
    {"name":"Mali","short":"Mali","continent":"Africa","capital":"Bamako","region":"West Africa","population":20,"aliases":[], "territory":False, "un_member":True},
    {"name":"Mauritania","short":"Mauritania","continent":"Africa","capital":"Nouakchott","region":"West Africa","population":4,"aliases":[], "territory":False, "un_member":True},
    {"name":"Mauritius","short":"Mauritius","continent":"Africa","capital":"Port Louis","region":"East Africa","population":1.3,"aliases":[], "territory":False, "un_member":True},
    {"name":"Morocco","short":"Morocco","continent":"Africa","capital":"Rabat","region":"North Africa","population":36,"aliases":[], "territory":False, "un_member":True},
    {"name":"Mozambique","short":"Mozambique","continent":"Africa","capital":"Maputo","region":"East Africa","population":30,"aliases":[], "territory":False, "un_member":True},
    {"name":"Namibia","short":"Namibia","continent":"Africa","capital":"Windhoek","region":"Southern Africa","population":2.5,"aliases":[], "territory":False, "un_member":True},
    {"name":"Niger","short":"Niger","continent":"Africa","capital":"Niamey","region":"West Africa","population":24,"aliases":[], "territory":False, "un_member":True},
    {"name":"Nigeria","short":"Nigeria","continent":"Africa","capital":"Abuja","region":"West Africa","population":200,"aliases":[], "territory":False, "un_member":True},
    {"name":"Rwanda","short":"Rwanda","continent":"Africa","capital":"Kigali","region":"East Africa","population":12,"aliases":[], "territory":False, "un_member":True},
    {"name":"São Tomé and Príncipe","short":"São Tomé and Príncipe","continent":"Africa","capital":"São Tomé","region":"Central Africa","population":0.2,"aliases":["Sao Tome", "São Tomé"], "territory":False, "un_member":False},
    {"name":"Senegal","short":"Senegal","continent":"Africa","capital":"Dakar","region":"West Africa","population":16,"aliases":[], "territory":False, "un_member":True},
    {"name":"Seychelles","short":"Seychelles","continent":"Africa","capital":"Victoria","region":"East Africa","population":0.1,"aliases":[], "territory":False, "un_member":True},
    {"name":"Sierra Leone","short":"Sierra Leone","continent":"Africa","capital":"Freetown","region":"West Africa","population":8,"aliases":[], "territory":False, "un_member":True},
    {"name":"Somalia","short":"Somalia","continent":"Africa","capital":"Mogadishu","region":"East Africa","population":15,"aliases":[], "territory":False, "un_member":True},
    {"name":"South Africa","short":"South Africa","continent":"Africa","capital":"Pretoria","region": "Southern Africa", "population":63, "aliases" :[], "territory":False, "un_member":True},
    {"name":"South Sudan","short":"South Sudan","continent":"Africa","capital":"Juba","region":"East Africa","population":11,"aliases":[], "territory":False, "un_member":True},
    {"name":"Sudan","short":"Sudan","continent":"Africa","capital":"Khartoum","region":"North Africa","population":43,"aliases":[], "territory":False, "un_member":True},
    {"name":"Tanzania","short":"Tanzania","continent":"Africa","capital":"Dodoma","region":"East Africa","population":58,"aliases":[], "territory":False, "un_member":True},
    {"name":"Togo","short":"Togo","continent":"Africa","capital":"Lomé","region":"West Africa","population":8,"aliases":[], "territory":False, "un_member":True},
    {"name":"Tunisia","short":"Tunisia","continent":"Africa","capital":"Tunis","region":"North Africa","population":11,"aliases":[], "territory":False, "un_member":True},
    {"name":"Uganda","short":"Uganda","continent":"Africa","capital":"Kampala","region":"East Africa","population":45,"aliases":[], "territory":False, "un_member":True},
    {"name":"Zambia","short":"Zambia","continent":"Africa","capital":"Lusaka","region":"East Africa","population":18,"aliases":[], "territory":False, "un_member":True},
    {"name":"Zimbabwe","short":"Zimbabwe","continent":"Africa","capital":"Harare","region":"East Africa","population":14,"aliases":[], "territory":False, "un_member":True},

    # Asia
    {"name":"Afghanistan","short":"Afghanistan","continent":"Asia","capital":"Kabul","region":"Southern Asia","population":38,"aliases":[], "territory":False, "un_member":True},
    {"name":"Armenia","short":"Armenia","continent":"Asia","capital":"Yerevan","region":"Western Asia","population":3,"aliases":[], "territory":False, "un_member":True},
    {"name":"Azerbaijan","short":"Azerbaijan","continent":"Asia","capital":"Baku","region":"Western Asia","population":10,"aliases":[], "territory":False, "un_member":True},
    {"name":"Bahrain","short":"Bahrain","continent":"Asia","capital":"Manama","region":"Western Asia","population":1.7,"aliases":[], "territory":False, "un_member":True},
    {"name":"Bangladesh","short":"Bangladesh","continent":"Asia","capital":"Dhaka","region":"Southern Asia","population":165,"aliases":[], "territory":False, "un_member":True},
    {"name":"Bhutan","short":"Bhutan","continent":"Asia","capital":"Thimphu","region":"Southern Asia","population":0.8,"aliases":[], "territory":False, "un_member":True},
    {"name":"Brunei","short":"Brunei","continent":"Asia","capital":"Bandar Seri Begawan","region":"South-Eastern Asia","population":0.4,"aliases":[], "territory":False, "un_member":True},
    {"name":"Cambodia","short":"Cambodia","continent":"Asia","capital":"Phnom Penh","region":"South-Eastern Asia","population":16,"aliases":[], "territory":False, "un_member":True},
    {"name":"China","short":"China","continent":"Asia","capital":"Beijing","region":"Eastern Asia","population":1400,"aliases":[], "territory":False, "un_member":True},
    {"name":"Cyprus","short":"Cyprus","continent":"Asia","capital":"Nicosia","region":"Western Asia","population":1.2,"aliases":[], "territory":False, "un_member":True},
    {"name":"Georgia","short":"Georgia","continent":"Asia","capital":"Tbilisi","region":"Western Asia","population":4,"aliases":[], "territory":False, "un_member":True},
    {"name":"India","short":"India","continent":"Asia","capital":"New Delhi","region":"Southern Asia","population":1366,"aliases":[], "territory":False, "un_member":True},
    {"name":"Indonesia","short":"Indonesia","continent":"Asia","capital":"Jakarta","region":"South-Eastern Asia","population":273,"aliases":[], "territory":False, "un_member":True},
    {"name":"Iran","short":"Iran","continent":"Asia","capital":"Tehran","region":"Western Asia","population":81,"aliases":[], "territory":False, "un_member":True},
    {"name":"Iraq","short":"Iraq","continent":"Asia","capital":"Baghdad","region":"Western Asia","population":40,"aliases":[], "territory":False, "un_member":True},
    {"name":"Israel","short":"Israel","continent":"Asia","capital":"Jerusalem","region":"Western Asia","population":9,"aliases":[], "territory":False, "un_member":True},
    {"name":"Japan","short":"Japan","continent":"Asia","capital":"Tokyo","region":"Eastern Asia","population":126,"aliases":[], "territory":False, "un_member":True},
    {"name":"Jordan","short":"Jordan","continent":"Asia","capital":"Amman","region":"Western Asia","population":10,"aliases":[], "territory":False, "un_member":True},
    {"name":"Kazakhstan","short":"Kazakhstan","continent":"Asia","capital":"Nur-Sultan","region":"Central Asia","population":18,"aliases":[], "territory":False, "un_member":True},
    {"name":"Kuwait","short":"Kuwait","continent":"Asia","capital":"Kuwait City","region":"Western Asia","population":4,"aliases":[], "territory":False, "un_member":True},
    {"name":"Kyrgyzstan","short":"Kyrgyzstan","continent":"Asia","capital":"Bishkek","region":"Central Asia","population":6,"aliases":[], "territory":False, "un_member":True},
    {"name":"Laos","short":"Laos","continent":"Asia","capital":"Vientiane","region":"South-Eastern Asia","population":7,"aliases":[], "territory":False, "un_member":True},
    {"name":"Lebanon","short":"Lebanon","continent":"Asia","capital":"Beirut","region":"Western Asia","population":6,"aliases":[], "territory":False, "un_member":True},
    {"name":"Malaysia","short":"Malaysia","continent":"Asia","capital":"Kuala Lumpur","region":"South-Eastern Asia","population":32,"aliases":[], "territory":False, "un_member":True},
    {"name":"Maldives","short":"Maldives","continent":"Asia","capital":"Malé","region":"Southern Asia","population":0.5,"aliases":[], "territory":False, "un_member":True},
    {"name":"Mongolia","short":"Mongolia","continent":"Asia","capital":"Ulaanbaatar","region":"Eastern Asia","population":3,"aliases":[], "territory":False, "un_member":True},
    {"name":"Myanmar","short":"Myanmar","continent":"Asia","capital":"Naypyidaw","region":"South-Eastern Asia","population":54,"aliases":[], "territory":False, "un_member":True},
    {"name":"Nepal","short":"Nepal","continent":"Asia","capital":"Kathmandu","region":"Southern Asia","population":29,"aliases":[], "territory":False, "un_member":True},
    {"name":"North Korea","short":"North Korea","continent":"Asia","capital":"Pyongyang","region":"Eastern Asia","population":25,"aliases":["Democratic Peoples Republic of Korea"], "territory":False, "un_member":True},
    {"name":"Oman","short":"Oman","continent":"Asia","capital":"Muscat","region":"Western Asia","population":4.6,"aliases":[], "territory":False, "un_member":True},
    {"name":"Pakistan","short":"Pakistan","continent":"Asia","capital":"Islamabad","region":"Southern Asia","population":208,"aliases":[], "territory":False, "un_member":True},
    {"name":"Palestine","short":"Palestine","continent":"Asia","capital":"Jerusalem","region":"Western Asia","population":5,"aliases":[], "territory":False, "un_member":False},
    {"name":"Philippines","short":"Philippines","continent":"Asia","capital":"Manila","region":"South-Eastern Asia","population":108,"aliases":[], "territory":False, "un_member":True},
    {"name":"Qatar","short":"Qatar","continent":"Asia","capital":"Doha","region":"Western Asia","population":2.8,"aliases":[], "territory":False, "un_member":True},
    {"name":"Russia","short":"Russia","continent":"Asia","capital":"Moscow","region":"Eastern Europe/Asia","population":146,"aliases":[], "territory":False, "un_member":True},
    {"name":"Saudi Arabia","short":"Saudi Arabia","continent":"Asia","capital":"Riyadh","region":"Western Asia","population":34,"aliases":[], "territory":False, "un_member":True},
    {"name":"Singapore","short":"Singapore","continent":"Asia","capital":"Singapore","region":"South-Eastern Asia","population":5.7,"aliases":[], "territory":False, "un_member":True},
    {"name":"South Korea","short":"South Korea","continent":"Asia","capital":"Seoul","region":"Eastern Asia","population":51,"aliases":[], "territory":False, "un_member":True},
    {"name":"Sri Lanka","short":"Sri Lanka","continent":"Asia","capital":"Sri Jayawardenepura Kotte","region":"Southern Asia","population":21,"aliases":[], "territory":False, "un_member":True},
    {"name":"Syria","short":"Syria","continent":"Asia","capital":"Damascus","region":"Western Asia","population":17,"aliases":[], "territory":False, "un_member":True},
    {"name":"Taiwan","short":"Taiwan","continent":"Asia","capital":"Taipei","region":"Eastern Asia","population":23,"aliases":[], "territory":False, "un_member":False},
    {"name":"Tajikistan","short":"Tajikistan","continent":"Asia","capital":"Dushanbe","region":"Central Asia","population":9,"aliases":[], "territory":False, "un_member":True},
    {"name":"Thailand","short":"Thailand","continent":"Asia","capital":"Bangkok","region":"South-Eastern Asia","population":70,"aliases":[], "territory":False, "un_member":True},
    {"name":"Timor-Leste","short":"Timor-Leste","continent":"Asia","capital":"Dili","region":"South-Eastern Asia","population":1.3,"aliases":["East Timor"], "territory":False, "un_member":False},
    {"name":"Turkey","short":"Turkey","continent":"Asia","capital":"Ankara","region":"Western Asia","population":82,"aliases":[], "territory":False, "un_member":True},
    {"name":"Turkmenistan","short":"Turkmenistan","continent":"Asia","capital":"Ashgabat","region":"Central Asia","population":6,"aliases":[], "territory":False, "un_member":True},
    {"name":"United Arab Emirates","short":"UAE","continent":"Asia","capital":"Abu Dhabi","region":"Western Asia","population":9.1,"aliases":["UAE", "Emirates"], "territory":False, "un_member":True},
    {"name":"Uzbekistan","short":"Uzbekistan","continent":"Asia","capital":"Tashkent","region":"Central Asia","population":33,"aliases":[], "territory":False, "un_member":True},
    {"name":"Vietnam","short":"Vietnam","continent":"Asia","capital":"Hanoi","region":"South-Eastern Asia","population":96,"aliases":[], "territory":False, "un_member":True},
    {"name":"Yemen","short":"Yemen","continent":"Asia","capital":"Sana'a","region":"Western Asia","population":29,"aliases":[], "territory":False, "un_member":True},

    # Europe
    {"name":"Albania","short":"Albania","continent":"Europe","capital":"Tirana","region":"Southern Europe","population":3,"aliases":[], "territory":False, "un_member":True},
    {"name":"Andorra","short":"Andorra","continent":"Europe","capital":"Andorra la Vella","region":"Southern Europe","population":0.08,"aliases":[], "territory":False, "un_member":True},
    {"name":"Austria","short":"Austria","continent":"Europe","capital":"Vienna","region":"Central Europe","population":9,"aliases":[], "territory":False, "un_member":True},
    {"name":"Belarus","short":"Belarus","continent":"Europe","capital":"Minsk","region":"Eastern Europe","population":9,"aliases":[], "territory":False, "un_member":True},
    {"name":"Belgium","short":"Belgium","continent":"Europe","capital":"Brussels","region":"Western Europe","population":11,"aliases":[], "territory":False, "un_member":True},
    {"name":"Bosnia and Herzegovina","short":"Bosnia","continent":"Europe","capital":"Sarajevo","region":"South-Eastern Europe","population":3,"aliases":["Bosnia", "Herzegovina"], "territory":False, "un_member":True},
    {"name":"Bulgaria","short":"Bulgaria","continent":"Europe","capital":"Sofia","region":"Eastern Europe","population":7,"aliases":[], "territory":False, "un_member":True},
    {"name":"Croatia","short":"Croatia","continent":"Europe","capital":"Zagreb","region":"South-Eastern Europe","population":4,"aliases":[], "territory":False, "un_member":True},
    {"name":"Cyprus","short":"Cyprus","continent":"Europe","capital":"Nicosia","region":"Eastern Europe","population":1.2,"aliases":[], "territory":False, "un_member":True},
    {"name":"Czech Republic","short":"Czechia","continent":"Europe","capital":"Prague","region":"Central Europe","population":10,"aliases":["Czechia"], "territory":False, "un_member":True},
    {"name":"Denmark","short":"Denmark","continent":"Europe","capital":"Copenhagen","region":"Northern Europe","population":6,"aliases":[], "territory":False, "un_member":True},
    {"name":"Estonia","short":"Estonia","continent":"Europe","capital":"Tallinn","region":"Northern Europe","population":1.3,"aliases":[], "territory":False, "un_member":True},
    {"name":"Finland","short":"Finland","continent":"Europe","capital":"Helsinki","region":"Northern Europe","population":5.5,"aliases":[], "territory":False, "un_member":True},
    {"name":"France","short":"France","continent":"Europe","capital":"Paris","region":"Western Europe","population":67,"aliases":[], "territory":False, "un_member":True},
    {"name":"Germany","short":"Germany","continent":"Europe","capital":"Berlin","region":"Western Europe","population":83,"aliases":[], "territory":False, "un_member":True},
    {"name":"Greece","short":"Greece","continent":"Europe","capital":"Athens","region":"Southern Europe","population":11,"aliases":[], "territory":False, "un_member":True},
    {"name":"Hungary","short":"Hungary","continent":"Europe","capital":"Budapest","region":"Central Europe","population":10,"aliases":[], "territory":False, "un_member":True},
    {"name":"Iceland","short":"Iceland","continent":"Europe","capital":"Reykjavík","region":"Northern Europe","population":0.36,"aliases":[], "territory":False, "un_member":True},
    {"name":"Ireland","short":"Ireland","continent":"Europe","capital":"Dublin","region":"Northern Europe","population":4.9,"aliases":[], "territory":False, "un_member":True},
    {"name":"Italy","short":"Italy","continent":"Europe","capital":"Rome","region":"Southern Europe","population":60,"aliases":[], "territory":False, "un_member":True},
    {"name":"Latvia","short":"Latvia","continent":"Europe","capital":"Riga","region":"Northern Europe","population":1.9,"aliases":[], "territory":False, "un_member":True},
    {"name":"Liechtenstein","short":"Liechtenstein","continent":"Europe","capital":"Vaduz","region":"Western Europe","population":0.038,"aliases":[], "territory":False, "un_member":True},
    {"name":"Lithuania","short":"Lithuania","continent":"Europe","capital":"Vilnius","region":"Northern Europe","population":2.8,"aliases":[], "territory":False, "un_member":True},
    {"name":"Luxembourg","short":"Luxembourg","continent":"Europe","capital":"Luxembourg City","region":"Western Europe","population":0.6,"aliases":[], "territory":False, "un_member":True},
    {"name":"Malta","short":"Malta","continent":"Europe","capital":"Valletta","region":"Southern Europe","population":0.52,"aliases":[], "territory":False, "un_member":True},
    {"name":"Moldova","short":"Moldova","continent":"Europe","capital":"Chișinău","region":"Eastern Europe","population":3,"aliases":[], "territory":False, "un_member":True},
    {"name":"Monaco","short":"Monaco","continent":"Europe","capital":"Monaco","region":"Western Europe","population":0.04,"aliases":[], "territory":False, "un_member":True},
    {"name":"Montenegro","short":"Montenegro","continent":"Europe","capital":"Podgorica","region":"South-Eastern Europe","population":0.6,"aliases":[], "territory":False, "un_member":True},
    {"name":"Netherlands","short":"Netherlands","continent":"Europe","capital":"Amsterdam","region":"Western Europe","population":17,"aliases":[], "territory":False, "un_member":True},
    {"name":"North Macedonia","short":"North Macedonia","continent":"Europe","capital":"Skopje","region":"Southern Europe","population":2,"aliases":["Macedonia"], "territory":False, "un_member":True},
    {"name":"Norway","short":"Norway","continent":"Europe","capital":"Oslo","region":"Northern Europe","population":5.3,"aliases":[], "territory":False, "un_member":True},
    {"name":"Poland","short":"Poland","continent":"Europe","capital":"Warsaw","region":"Eastern Europe","population":38,"aliases":[], "territory":False, "un_member":True},
    {"name":"Portugal","short":"Portugal","continent":"Europe","capital":"Lisbon","region":"Southern Europe","population":10,"aliases":[], "territory":False, "un_member":True},
    {"name":"Romania","short":"Romania","continent":"Europe","capital":"Bucharest","region":"Eastern Europe","population":19,"aliases":[], "territory":False, "un_member":True},
    {"name":"San Marino","short":"San Marino","continent":"Europe","capital":"San Marino","region":"Southern Europe","population":0.03,"aliases":[], "territory":False, "un_member":True},
    {"name":"Serbia","short":"Serbia","continent":"Europe","capital":"Belgrade","region":"South-Eastern Europe","population":7,"aliases":[], "territory":False, "un_member":True},
    {"name":"Slovakia","short":"Slovakia","continent":"Europe","capital":"Bratislava","region":"Central Europe","population":5.4,"aliases":[], "territory":False, "un_member":True},
    {"name":"Slovenia","short":"Slovenia","continent":"Europe","capital":"Ljubljana","region":"South-Eastern Europe","population":2.1,"aliases":[], "territory":False, "un_member":True},
    {"name":"Spain","short":"Spain","continent":"Europe","capital":"Madrid","region":"Southern Europe","population":47,"aliases":[], "territory":False, "un_member":True},
    {"name":"Sweden","short":"Sweden","continent":"Europe","capital":"Stockholm","region":"Northern Europe","population":10,"aliases":[], "territory":False, "un_member":True},
    {"name":"Switzerland","short":"Switzerland","continent":"Europe","capital":"Bern","region":"Western Europe","population":8.5,"aliases":[], "territory":False, "un_member":True},
    {"name":"Ukraine","short":"Ukraine","continent":"Europe","capital":"Kyiv","region":"Eastern Europe","population":44,"aliases":[], "territory":False, "un_member":True},
    {"name":"United Kingdom","short":"UK","continent":"Europe","capital":"London","region":"Northern Europe","population":66,"aliases":["Britain", "Great Britain", "England"], "territory":False, "un_member":True},
    {"name":"Vatican City","short":"Vatican City","continent":"Europe","capital":"Vatican City","region":"Southern Europe","population":0.0008,"aliases":["Vatican"], "territory":False, "un_member":True},

    # North America
    {"name":"Antigua and Barbuda","short":"Antigua","continent":"North America","capital":"St. John's","region":"Caribbean","population":0.1,"aliases":["Antigua", "Barbuda"], "territory":False, "un_member":True},
    {"name":"Bahamas","short":"Bahamas","continent":"North America","capital":"Nassau","region":"Caribbean","population":0.4,"aliases":[], "territory":False, "un_member":True},
    {"name":"Barbados","short":"Barbados","continent":"North America","capital":"Bridgetown","region":"Caribbean","population":0.3,"aliases":[], "territory":False, "un_member":True},
    {"name":"Belize","short":"Belize","continent":"North America","capital":"Belmopan","region":"Central America","population":0.4,"aliases":[], "territory":False, "un_member":True},
    {"name":"Canada","short":"Canada","continent":"North America","capital":"Ottawa","region":"Northern America","population":37,"aliases":["CA", "CAN"], "territory":False, "un_member":True},
    {"name":"Costa Rica","short":"Costa Rica","continent":"North America","capital":"San José","region":"Central America","population":5,"aliases":[], "territory":False, "un_member":True},
    {"name":"Cuba","short":"Cuba","continent":"North America","capital":"Havana","region":"Caribbean","population":11,"aliases":[], "territory":False, "un_member":True},
    {"name":"Dominica","short":"Dominica","continent":"North America","capital":"Roseau","region":"Caribbean","population":0.07,"aliases":[], "territory":False, "un_member":True},
    {"name":"Dominican Republic","short":"Dominican Republic","continent":"North America","capital":"Santo Domingo","region":"Caribbean","population":11,"aliases":["Dominican"], "territory":False, "un_member":True},
    {"name":"El Salvador","short":"El Salvador","continent":"North America","capital":"San Salvador","region":"Central America","population":6,"aliases":[], "territory":False, "un_member":True},
    {"name":"Grenada","short":"Grenada","continent":"North America","capital":"St. George's","region":"Caribbean","population":0.1,"aliases":[], "territory":False, "un_member":True},
    {"name":"Guatemala","short":"Guatemala","continent":"North America","capital":"Guatemala City","region":"Central America","population":17,"aliases":[], "territory":False, "un_member":True},
    {"name":"Haiti","short":"Haiti","continent":"North America","capital":"Port-au-Prince","region":"Caribbean","population":11,"aliases":[], "territory":False, "un_member":True},
    {"name":"Honduras","short":"Honduras","continent":"North America","capital":"Tegucigalpa","region":"Central America","population":10,"aliases":[], "territory":False, "un_member":True},
    {"name":"Jamaica","short":"Jamaica","continent":"North America","capital":"Kingston","region":"Caribbean","population":3,"aliases":[], "territory":False, "un_member":True},
    {"name":"Mexico","short":"Mexico","continent":"North America","capital":"Mexico City","region":"Central America","population":126,"aliases":[], "territory":False, "un_member":True},
    {"name":"Nicaragua","short":"Nicaragua","continent":"North America","capital":"Managua","region":"Central America","population":6,"aliases":[], "territory":False, "un_member":True},
    {"name":"Panama","short":"Panama","continent":"North America","capital":"Panama City","region":"Central America","population":4.3,"aliases":[], "territory":False, "un_member":True},
    {"name":"Saint Kitts and Nevis","short":"Saint Kitts and Nevis","continent":"North America","capital":"Basseterre","region":"Caribbean","population":0.05,"aliases":["Saint Kitts", "St. Kitts", "The Nevis"], "territory":False, "un_member":True},
    {"name":"Saint Lucia","short":"Saint Lucia","continent":"North America","capital":"Castries","region":"Caribbean","population":0.18,"aliases":["St. Lucia"], "territory":False, "un_member":True},
    {"name":"Saint Vincent and the Grenadines","short":"Saint Vincent","continent":"North America","capital":"Kingstown","region":"Caribbean","population":0.11,"aliases":["Saint Vincent", "Grenadines", "St. Vincent"], "territory":False, "un_member":True},
    {"name":"Trinidad and Tobago","short":"Trinidad and Tobago","continent":"North America","capital":"Port of Spain","region":"Caribbean","population":1.4,"aliases":["Trinidad", "Tobago"], "territory":False, "un_member":True},
    {"name":"United States","short":"USA","continent":"North America","capital":"Washington, D.C.","region":"Northern America","population":328,"aliases":["USA", "US", "U.S.", "America", "United States"], "territory":False, "un_member":True},

    # Oceania
    {"name":"Australia","short":"Australia","continent":"Oceania","capital":"Canberra","region":"Australia and New Zealand","population":25,"aliases":[], "territory":False, "un_member":True},
    {"name":"Fiji","short":"Fiji","continent":"Oceania","capital":"Suva","region":"Melanesia","population":0.9,"aliases":[], "territory":False, "un_member":True},
    {"name":"Kiribati","short":"Kiribati","continent":"Oceania","capital":"Tarawa","region":"Micronesia","population":0.1,"aliases":[], "territory":False, "un_member":True},
    {"name":"Marshall Islands","short":"Marshall Islands","continent":"Oceania","capital":"Majuro","region":"Micronesia","population":0.06,"aliases":[], "territory":False, "un_member":True},
    {"name":"Micronesia","short":"Micronesia","continent":"Oceania","capital":"Palikir","region":"Micronesia","population":0.1,"aliases":[], "territory":False, "un_member":True},
    {"name":"Nauru","short":"Nauru","continent":"Oceania","capital":"Yaren","region":"Micronesia","population":0.01,"aliases":[], "territory":False, "un_member":True},
    {"name":"New Zealand","short":"New Zealand","continent":"Oceania","capital":"Wellington","region":"Australia and New Zealand","population":4.8,"aliases":[], "territory":False, "un_member":True},
    {"name":"Palau","short":"Palau","continent":"Oceania","capital":"Ngerulmud","region":"Micronesia","population":0.02,"aliases":[], "territory":False, "un_member":True},
    {"name":"Papua New Guinea","short":"Papua New Guinea","continent":"Oceania","capital":"Port Moresby","region":"Melanesia","population":8.9,"aliases":["Papua", "New Guinea"], "territory":False, "un_member":True},
    {"name":"Samoa","short":"Samoa","continent":"Oceania","capital":"Apia","region":"Polynesia","population":0.2,"aliases":[], "territory":False, "un_member":True},
    {"name":"Solomon Islands","short":"Solomon Islands","continent":"Oceania","capital":"Honiara","region":"Melanesia","population":0.6,"aliases":["Solomon"], "territory":False, "un_member":True},
    {"name":"Tonga","short":"Tonga","continent":"Oceania","capital":"Nuku'alofa","region":"Polynesia","population":0.1,"aliases":[], "territory":False, "un_member":True},
    {"name":"Tuvalu","short":"Tuvalu","continent":"Oceania","capital":"Funafuti","region":"Polynesia","population":0.01,"aliases":[], "territory":False, "un_member":True},
    {"name":"Vanuatu","short":"Vanuatu","continent":"Oceania","capital":"Port Vila","region":"Melanesia","population":0.3,"aliases":[], "territory":False, "un_member":True},

    # South America
    {"name":"Argentina","short":"Argentina","continent":"South America","capital":"Buenos Aires","region":"South America","population":45,"aliases":[], "territory":False, "un_member":True},
    {"name":"Bolivia","short":"Bolivia","continent":"South America","capital":"La Paz","region":"South America","population":12,"aliases":[], "territory":False, "un_member":True},
    {"name":"Brazil","short":"Brazil","continent":"South America","capital":"Brasília","region":"South America","population":214,"aliases":[], "territory":False, "un_member":True},
    {"name":"Chile","short":"Chile","continent":"South America","capital":"Santiago","region":"South America","population":19,"aliases":[], "territory":False, "un_member":True},
    {"name":"Colombia","short":"Colombia","continent":"South America","capital":"Bogotá","region":"South America","population":51.5,"aliases":[], "territory":False, "un_member":True},
    {"name":"Ecuador","short":"Ecuador","continent":"South America","capital":"Quito","region":"South America","population":18,"aliases":[], "territory":False, "un_member":True},
    {"name":"Guyana","short":"Guyana","continent":"South America","capital":"Gerogetown","region":"South America","population":0.8,"aliases":[], "territory":False, "un_member":True},
    {"name":"Paraguay","short":"Paraguay","continent":"South America","capital":"Asunción","region":"South America","population":7,"aliases":[], "territory":False, "un_member":True},
    {"name":"Peru","short":"Peru","continent":"South America","capital":"Lima","region":"South America","population":34,"aliases":["Papua", "New Guinea"], "territory":False, "un_member":True},
    {"name":"Suriname","short":"Suriname","continent":"South America","capital":"Paramaribo","region":"South America","population":0.6,"aliases":[], "territory":False, "un_member":True},
    {"name":"Uruguay","short":"Uruguay","continent":"South America","capital":"Montevideo","region":"South America","population":3.5,"aliases":["Solomon"], "territory":False, "un_member":True},
    {"name":"Venezuela","short":"Venezuela","continent":"South America","capital":"Caracas","region":"South America","population":28,"aliases":[], "territory":False, "un_member":True},

]

# US States
# Land of the Free home of the Brave

US_STATES = [
    {"name":"Alabama","short":"AL","continent":"North America","region":"USA State","population":4.9,"aliases":["Alabama", "AL", "al"], "state":True, "un_member":False},
    {"name":"Alaska","short":"AK","continent":"North America","region":"USA State","population":0.7,"aliases":["Alaska", "AK", "ak"], "state":True, "un_member":False},
    {"name":"Arizona","short":"AZ","continent":"North America","region":"USA State","population":7.3,"aliases":["Arizona", "AZ", "az"], "state":True, "un_member":False},
    {"name":"Arkansas","short":"AR","continent":"North America","region":"USA State","population":3,"aliases":["Arkansas", "AR", "ar"], "state":True, "un_member":False},
    {"name":"California","short":"CA","continent":"North America","region":"USA State","population":39,"aliases":["California", "CA", "ca"], "state":True, "un_member":False},
    {"name":"Colorado","short":"CO","continent":"North America","region":"USA State","population":5.8,"aliases":["Colorado", "CO", "co"], "state":True, "un_member":False},
    {"name":"Connecticut","short":"CT","continent":"North America","region":"USA State","population":3.6,"aliases":["Connecticut", "CT", "ct"], "state":True, "un_member":False},
    {"name":"Delaware","short":"DE","continent":"North America","region":"USA State","population":1,"aliases":["Delaware", "DE", "de"], "state":True, "un_member":False},
    {"name":"Florida","short":"FL","continent":"North America","region":"USA State","population":21,"aliases":["Florida", "FL", "fl"], "state":True, "un_member":False},
    {"name":"Georgia","short":"GA","continent":"North America","region":"USA State","population":10.7,"aliases":["Georgia", "GA", "ga"], "state":True, "un_member":False},
    {"name":"Hawaii","short":"HI","continent":"North America","region":"USA State","population":1.4,"aliases":["Hawaii", "HI", "hi"], "state":True, "un_member":False},
    {"name":"Idaho","short":"ID","continent":"North America","region":"USA State","population":1.8,"aliases":["Idaho", "ID", "id"], "state":True, "un_member":False},
    {"name":"Illinois","short":"IL","continent":"North America","region":"USA State","population":12.6,"aliases":["Illinois", "IL", "il"], "state":True, "un_member":False},
    {"name":"Indiana","short":"IN","continent":"North America","region":"USA State","population":6.7,"aliases":["Indiana", "IN", "in"], "state":True, "un_member":False},
    {"name":"Iowa","short":"IA","continent":"North America","region":"USA State","population":3.2,"aliases":["Iowa", "IA", "ia"], "state":True, "un_member":False},
    {"name":"Kansas","short":"KS","continent":"North America","region":"USA State","population":2.9,"aliases":["Kansas", "KS", "ks"], "state":True, "un_member":False},
    {"name":"Kentucky","short":"KY","continent":"North America","region":"USA State","population":4.4,"aliases":["Kentucky", "KY", "ky"], "state":True, "un_member":False},
    {"name":"Louisiana","short":"LA","continent":"North America","region":"USA State","population":4.6,"aliases":["Louisiana", "LA", "la"], "state":True, "un_member":False},
    {"name":"Maine","short":"ME","continent":"North America","region":"USA State","population":1.3,"aliases":["Maine", "ME", "me"], "state":True, "un_member":False},
    {"name":"Maryland","short":"MD","continent":"North America","region":"USA State","population":6,"aliases":["Maryland", "MD", "md"], "state":True, "un_member":False},
    {"name":"Massachusetts","short":"MA","continent":"North America","region":"USA State","population":6.9,"aliases":["Massachusetts", "MA", "ma"], "state":True, "un_member":False},
    {"name":"Michigan","short":"MI","continent":"North America","region":"USA State","population":9.9,"aliases":["Michigan", "MI", "mi"], "state":True, "un_member":False},
    {"name":"Minnesota","short":"MN","continent":"North America","region":"USA State","population":5.6,"aliases":["Minnesota", "MN", "mn"], "state":True, "un_member":False},
    {"name":"Mississippi","short":"MS","continent":"North America","region":"USA State","population":3,"aliases":["Mississippi", "MI", "mi"], "state":True, "un_member":False},
    {"name":"Missouri","short":"MO","continent":"North America","region":"USA State","population":6.1,"aliases":["Missouri", "MO", "mo"], "state":True, "un_member":False},
    {"name":"Montana","short":"MT","continent":"North America","region":"USA State","population":1.1,"aliases":["Montana", "MT", "mt"], "state":True, "un_member":False},
    {"name":"Nebraska","short":"NE","continent":"North America","region":"USA State","population":1.9,"aliases":["Nebraska", "NE", "ne"], "state":True, "un_member":False},
    {"name":"Nevada","short":"NV","continent":"North America","region":"USA State","population":3,"aliases":["Nevada", "NV", "nv"], "state":True, "un_member":False},
    {"name":"New Hampshire","short":"NH","continent":"North America","region":"USA State","population":1.4,"aliases":["New Hampshire", "NH", "nh"], "state":True, "un_member":False},
    {"name":"New Jersey","short":"NJ","continent":"North America","region":"USA State","population":8.9,"aliases":["New Jersey", "NJ", "nj"], "state":True, "un_member":False},
    {"name":"New Mexico","short":"NM","continent":"North America","region":"USA State","population":2.1,"aliases":["New Mexico", "NM", "nm"], "state":True, "un_member":False},
    {"name":"New York","short":"NY","continent":"North America","region":"USA State","population":19.8,"aliases":["New York", "NY", "ny"], "state":True, "un_member":False},
    {"name":"North Carolina","short":"NC","continent":"North America","region":"USA State","population":10.4,"aliases":["North Carolina", "NC", "nc"], "state":True, "un_member":False},
    {"name":"North Dakota","short":"ND","continent":"North America","region":"USA State","population":0.76,"aliases":["North Dakota", "ND", "nd"], "state":True, "un_member":False},
    {"name":"Ohio","short":"OH","continent":"North America","region":"USA State","population":11.7,"aliases":["Ohio", "OH", "oh"], "state":True, "un_member":False},
    {"name":"Oklahoma","short":"OK","continent":"North America","region":"USA State","population":3.9,"aliases":["Oklahoma", "OK", "ok"], "state":True, "un_member":False},
    {"name":"Oregon","short":"OR","continent":"North America","region":"USA State","population":4.2,"aliases":["Oregon", "OR", "or"], "state":True, "un_member":False},
    {"name":"Pennsylvania","short":"PA","continent":"North America","region":"USA State","population":12.8,"aliases":["Pennsylvania", "PA", "pa"], "state":True, "un_member":False},
    {"name":"Rhode Island","short":"RI","continent":"North America","region":"USA State","population":1.06,"aliases":["Rhode Island", "RI", "ri"], "state":True, "un_member":False},
    {"name":"South Carolina","short":"SC","continent":"North America","region":"USA State","population":5.1,"aliases":["South Carolina", "SC", "sc"], "state":True, "un_member":False},
    {"name":"South Dakota","short":"SD","continent":"North America","region":"USA State","population":0.88,"aliases":["South Dakota", "SD", "sd"], "state":True, "un_member":False},
    {"name":"Tennessee","short":"TN","continent":"North America","region":"USA State","population":6.8,"aliases":["Tennessee", "TN", "tn"], "state":True, "un_member":False},
    {"name":"Texas","short":"TX","continent":"North America","region":"USA State","population":29,"aliases":["Texas", "TX", "tx"], "state":True, "un_member":False},
    {"name":"Utah","short":"UT","continent":"North America","region":"USA State","population":3.2,"aliases":["Utah", "UT", "ut"], "state":True, "un_member":False},
    {"name":"Vermont","short":"VT","continent":"North America","region":"USA State","population":0.6,"aliases":["Vermont", "VT", "vt"], "state":True, "un_member":False},
    {"name":"Virginia","short":"VA","continent":"North America","region":"USA State","population":8.5,"aliases":["Virginia", "VA", "va"], "state":True, "un_member":False},
    {"name":"Washington","short":"WA","continent":"North America","region":"USA State","population":7.6,"aliases":["Washington", "WA", "wa"], "state":True, "un_member":False},
    {"name":"West Virginia","short":"WV","continent":"North America","region":"USA State","population":1.8,"aliases":["West Virginia", "WV", "wv"], "state":True, "un_member":False},
    {"name":"Wisconsin","short":"WI","continent":"North America","region":"USA State","population":5.8,"aliases":["Wisconsin", "WI", "wi"], "state":True, "un_member":False},
    {"name":"Wyoming","short":"WY","continent":"North America","region":"USA State","population":0.58,"aliases":["Wyoming", "WY", "wy"], "state":True, "un_member":False},
]

US_STATESCAP = [
    {"name":"Alabama","short":"AL","yearfounded":"1846","capital":"Montgomery","population":0.2, "statecap":True, "un_member":False},
    {"name":"Alaska","short":"AK","yearfounded":"1906","capital":"Juneau","population":0.03, "statecap":True, "un_member":False},
    {"name":"Arizona","short":"AZ","yearfounded":"1889","capital":"Phoenix","population":1.6, "statecap":True, "un_member":False},
    {"name":"Arkansas","short":"AR","yearfounded":"1821","capital":"Little Rock","population":0.2, "statecap":True, "un_member":False},
    {"name":"California","short":"CA","yearfounded":"1854","capital":"Sacramento","population":0.5, "statecap":True, "un_member":False},
    {"name":"Colorado","short":"CO","yearfounded":"1867","capital":"Denver","population":0.7, "statecap":True, "un_member":False},
    {"name":"Connecticut","short":"CT","yearfounded":"1875","capital":"Hartford","population":0.2, "statecap":True, "un_member":False},
    {"name":"Delaware","short":"DE","yearfounded":"1777","capital":"Dover","population":0.03, "statecap":True, "un_member":False},
    {"name":"Florida","short":"FL","yearfounded":"1824","capital":"Tallahassee","population":0.2, "statecap":True, "un_member":False},
    {"name":"Georgia","short":"GA","yearfounded":"1868","capital":"Atlanta","population":0.5, "statecap":True, "un_member":False},
    {"name":"Hawaii","short":"HI","yearfounded":"1845","capital":"Honolulu","population":0.35, "statecap":True, "un_member":False},
    {"name":"Idaho","short":"ID","yearfounded":"1865","capital":"Boise","population":0.2, "statecap":True, "un_member":False},
    {"name":"Illinois","short":"IL","yearfounded":"1837","capital":"Springfield","population":0.1, "statecap":True, "un_member":False},
    {"name":"Indiana","short":"IN","yearfounded":"1825","capital":"Indianapolis","population":0.9, "statecap":True, "un_member":False},
    {"name":"Iowa","short":"IA","yearfounded":"1857","capital":"Des Moines","population":0.2, "statecap":True, "un_member":False},
    {"name":"Kansas","short":"KS","yearfounded":"1856","capital":"Topeka","population":0.1, "statecap":True, "un_member":False},
    {"name":"Kentucky","short":"KY","yearfounded":"1792","capital":"Frankfort","population":0.07, "statecap":True, "un_member":False},
    {"name":"Louisiana","short":"LA","yearfounded":"1880","capital":"Baton Rouge","population":0.2, "statecap":True, "un_member":False},
    {"name":"Maine","short":"ME","yearfounded":"1832","capital":"Augusta","population":0.01, "statecap":True, "un_member":False},
    {"name":"Maryland","short":"MD","yearfounded":"1694","capital":"Annapolis","population":0.04, "statecap":True, "un_member":False},
    {"name":"Massachusetts","short":"MA","yearfounded":"1630","capital":"Boston","population":0.67, "statecap":True, "un_member":False},
    {"name":"Michigan","short":"MI","yearfounded":"1847","capital":"Lansing","population":0.1, "statecap":True, "un_member":False},
    {"name":"Minnesota","short":"MN","yearfounded":"1849","capital":"Saint Paul","population":0.3, "statecap":True, "un_member":False},
    {"name":"Mississippi","short":"MS","yearfounded":"1864","capital":"Jackson","population":0.15, "statecap":True, "un_member":False},
    {"name":"Missouri","short":"MO","yearfounded":"1826","capital":"Jefferson City","population":0.4, "statecap":True, "un_member":False},
    {"name":"Montana","short":"MT","yearfounded":"1875","capital":"Helena","population":0.03, "statecap":True, "un_member":False},
    {"name":"Nebraska","short":"NE","yearfounded":"1867","capital":"Lincoln","population":0.3, "statecap":True, "un_member":False},
    {"name":"Nevada","short":"NV","yearfounded":"1861","capital":"Carson City","population":0.05, "statecap":True, "un_member":False},
    {"name":"New Hampshire","short":"NH","yearfounded":"1808","capital":"Concord","population":0.04, "statecap":True, "un_member":False},
    {"name":"New Jersey","short":"NJ","yearfounded":"1784","capital":"Trenton","population":0.1, "statecap":True, "un_member":False},
    {"name":"New Mexico","short":"NM","yearfounded":"1610","capital":"Santa Fe","population":0.1, "statecap":True, "un_member":False},
    {"name":"New York","short":"NY","yearfounded":"1797","capital":"Albany","population":0.1, "statecap":True, "un_member":False},
    {"name":"North Carolina","short":"NC","yearfounded":"1792","capital":"Raleigh","population":1.4, "statecap":True, "un_member":False},
    {"name":"North Dakota","short":"ND","yearfounded":"1883","capital":"Bismarck","population":0.07, "statecap":True, "un_member":False},
    {"name":"Ohio","short":"OH","yearfounded":"1816","capital":"Columbus","population":0.1, "statecap":True, "un_member":False},
    {"name":"Oklahoma","short":"OK","yearfounded":"1910","capital":"Oklahoma City","population":0.7, "statecap":True, "un_member":False},
    {"name":"Oregon","short":"OR","yearfounded":"1855","capital":"Salem","population":0.2, "statecap":True, "un_member":False},
    {"name":"Pennsylvania","short":"PA","yearfounded":"1812","capital":"Harrisburg","population":0.05, "statecap":True, "un_member":False},
    {"name":"Rhode Island","short":"RI","yearfounded":"1900","capital":"Providence","population":0.2, "statecap":True, "un_member":False},
    {"name":"South Carolina","short":"SC","yearfounded":"1786","capital":"Columbia","population":0.1, "statecap":True, "un_member":False},
    {"name":"South Dakota","short":"SD","yearfounded":"1889","capital":"Pierre","population":0.01, "statecap":True, "un_member":False},
    {"name":"Tennessee","short":"TN","yearfounded":"1826","capital":"Nashville","population":0.7, "statecap":True, "un_member":False},
    {"name":"Texas","short":"TX","yearfounded":"1801","capital":"Austin","population":1, "statecap":True, "un_member":False},
    {"name":"Utah","short":"UT","yearfounded":"1858","capital":"Salt Lake City","population":0.2, "statecap":True, "un_member":False},
    {"name":"Vermont","short":"VT","yearfounded":"1805","capital":"Montpelier","population":0.008, "statecap":True, "un_member":False},
    {"name":"Virginia","short":"VA","yearfounded":"1780","capital":"Richmond","population":0.2, "statecap":True, "un_member":False},
    {"name":"Washington","short":"WA","yearfounded":"1853","capital":"Olympia","population":0.05, "statecap":True, "un_member":False},
    {"name":"West Virginia","short":"WV","yearfounded":"1885","capital":"Charleston","population":0.05, "statecap":True, "un_member":False},
    {"name":"Wisconsin","short":"WI","yearfounded":"1838","capital":"Madison","population":0.27, "statecap":True, "un_member":False},
    {"name":"Wyoming","short":"WY","yearfounded":"1869","capital":"Cheyenne","population":0.06, "statecap":True, "un_member":False},




]

# Canadian Provinces
# Oh
CAN_PROVINCES = [
    # Provinces
    {"name": "Alberta", "short": "AB", "region": "Canada", "population": 4.4, "aliases": ["Alberta"], "province": True, "un_member": False},
    {"name": "British Columbia", "short": "BC", "region": "Canada", "population": 5.1, "aliases": ["British Columbia"], "province": True, "un_member": False},
    {"name": "Manitoba", "short": "MB", "region": "Canada", "population": 1.4, "aliases": ["Manitoba"], "province": True, "un_member": False},
    {"name": "New Brunswick", "short": "NB", "region": "Canada", "population": 0.78, "aliases": ["New Brunswick", "Brunswick"], "province": True, "un_member": False},
    {"name": "Newfoundland and Labrador", "short": "NL", "region": "Canada", "population": 0.52, "aliases": ["Newfoundland" "Labrador"], "province": True, "un_member": False},
    {"name": "Nova Scotia", "short": "NS", "region": "Canada", "population": 0.97, "aliases": ["Nova Scotia"], "province": True, "un_member": False},
    {"name": "Ontario", "short": "ON", "region": "Canada", "population": 14, "aliases": ["Ontario"], "province": True, "un_member": False},
    {"name": "Prince Edward Island", "short": "PE", "region": "Canada", "population": 0.16, "aliases": ["PE", "Prince Edward"], "province": True, "un_member": False},
    {"name": "Quebec", "short": "QC", "region": "Canada", "population": 8.4, "aliases": ["Quebec"], "province": True, "un_member": False},
    {"name": "Saskatchewan", "short": "SK", "region": "Canada", "population": 1.2, "aliases": ["Saskatchewan"], "province": True, "un_member": False},
    # Territories marked as provinces
    {"name": "Northwest Territories", "short": "NT", "region": "Canada", "population": 0.045, "aliases": ["Northwest Territories"], "province": True, "un_member": False},
    {"name": "Nunavut", "short": "NU", "region": "Canada", "population": 0.036, "aliases": ["Nunavut"], "province": True, "un_member": False},
    {"name": "Yukon", "short": "YT", "region": "Canada", "population": 0.045, "aliases": ["Yukon"], "province": True, "un_member": False},

]

TERRITORIES = [
    # Chinese territories
    {"name": "Hong Kong", "short": "HK", "country": "China", "continent": "Asia", "region": "Eastern Asia", "population": 7.5, "aliases": ["Hong Kong"], "territory": True},
    {"name": "Macau", "short": "MO", "country": "China", "continent": "Asia", "region": "Eastern Asia", "population": 0.7, "aliases": ["Macau"], "territory": True},

    # New Zealand territories
    {"name": "Niue", "short": "NU", "country": "New Zealand", "continent": "Oceania", "region": "Australia and New Zealand", "population": 0.006, "aliases": ["Niue"], "territory": True},
    {"name": "Tokelau", "short": "TK", "country": "New Zealand", "continent": "Oceania", "region": "Australia and New Zealand", "population": 0.0014, "aliases": ["Tokelau"], "territory": True},
    {"name": "Cook Islands", "short": "CK", "country": "New Zealand", "continent": "Oceania", "region": "Australia and New Zealand", "population": 0.015, "aliases": ["Cook Islands"], "territory": True},

    #Australian territories
    {"name": "Cocos (Keeling) Islands", "short": "CC", "country": "Australia", "continent": "Oceania", "region": "Australia and New Zealand", "population": 0.014, "aliases": ["Cocos Islands", "Keeling Islands"], "territory": True},
    {"name": "Christmas Island", "short": "CX", "country": "Australia", "continent": "Oceania", "region": "Australia and New Zealand", "population": 0.002, "aliases": ["Christmas Island"], "territory": True},

    # Norwegian territories
    {"name": "Svalbard", "short": "SJ", "country": "Norway", "continent": "Europe", "region": "Northern Europe", "population": 0.0029, "aliases": ["Svalbard"], "territory": True},
    {"name": "Bouvet Island", "short": "BV", "country": "Norway", "continent": "Antarctica", "region": "Southern Ocean", "population": 0, "aliases": ["Bouvet Island", "Bouvet"], "territory": True},

    # US territories
    {"name": "American Samoa", "short": "AS", "country": "United States", "continent": "Oceania", "region": "Polynesia", "population": 0.055, "aliases": ["American Samoa"], "territory": True},
    {"name": "Guam", "short": "GU", "country": "United States", "continent": "Oceania", "region": "Micronesia", "population": 0.17, "aliases": ["Guam"], "territory": True},
    {"name": "Northern Mariana Islands", "short": "MP", "country": "United States", "continent": "Oceania", "region": "Micronesia", "population": 0.055, "aliases": ["Northern Mariana Islands", "Mariana Islands", "Northern Mariana"], "territory": True},
    {"name": "US Virgin Islands", "short": "VI", "country": "United States", "continent": "North America", "region": "Caribbean", "population": 0.106, "aliases": ["U.S. Virgin Islands", "USVI"], "territory": True},
    {"name": "Puerto Rico", "short": "PR", "country": "United States", "continent": "North America", "region": "Caribbean", "population": 3.2, "aliases": ["Puerto Rico"], "territory": True},

    # French Territories
    {"name": "French Southern and Antarctic Lands", "short": "TF", "country": "France", "continent": "Antarctica", "region": "Antarctica", "population": 0.19, "aliases": ["French Southern Lands", "French Antartic"], "territory": True},
    {"name": "Saint Pierre and Miquelon", "short": "PM", "country": "France", "continent": "North America", "region": "North America", "population": 0.6, "aliases": ["Saint Pierre Miquelon"], "territory": True},
    {"name": "French Guiana", "short": "GF", "country": "France", "continent": "South America", "region": "South America", "population": 0.3, "aliases": ["French Guiana"], "territory": True},

    # Finish territories
    {"name": "Åland Islands", "short": "AX", "country": "Finland", "continent": "Europe", "region": "Northern Europe", "population": 0.03, "aliases": ["Åland", "Aland", "Aland Islands"], "territory": True},

    # British territories
    {"name": "Jersey", "short": "JE", "country": "United Kingdom", "continent": "Europe", "region": "Northern Europe", "population": 0.1, "aliases": ["Jersey"], "territory": True},
    {"name": "Guernsey", "short": "GG", "country": "United Kingdom", "continent": "Europe", "region": "Northern Europe", "population": 0.07, "aliases": ["Guernsey"], "territory": True},
    {"name": "British Virgin Islands", "short": "VG", "country": "United Kingdom", "continent": "North America", "region": "Caribbean", "population": 0.03, "aliases": ["British Virgin Islands", "British VI"], "territory": True},
    {"name": "Falkland Islands", "short": "FK", "country": "United Kingdom", "continent": "South America", "region": "South America", "population": 0.03, "aliases": ["Falkland Islands", "Isla Malvinas"], "territory": True},
    {"name": "Akrotiri and Dhekelia", "short": "UK", "country": "United Kingdom", "continent": "Europe", "region": "Southern Europe", "population": 0.01, "aliases": ["Akrotiri Dhekelia", "Akrotiri", "Dhekelia"], "territory": True},

    # Danish territories
    {"name": "Faroe Islands", "short": "FO", "country": "Denmark", "continent": "Europe", "region": "Northern Europe", "population": 0.052, "aliases": ["Faroe Islands"], "territory": True},
    {"name": "Greenland", "short": "GL", "country": "Denmark", "continent": "North America", "region": "North America", "population": 0.56, "aliases": ["Greenland"], "territory": True},

]
# ----------------- Utility functions -----------------

def normalize(s):
    if isinstance(s, str):
        return s.lower().strip()
    return ""

def init_all_options():
    global ALL_COUNTRY_NAMES
    ALL_COUNTRY_NAMES = [normalize(c["name"]) for c in COUNTRIES]
    ALL_COUNTRY_NAMES += [normalize(c["short"]) for c in COUNTRIES]
    ALL_COUNTRY_NAMES += [normalize(c["capital"]) for c in COUNTRIES]
    for c in COUNTRIES:
        for a in c.get("aliases", []):
            ALL_COUNTRY_NAMES.append(normalize(a))
    # US states
    ALL_COUNTRY_NAMES += [normalize(s["name"]) for s in US_STATES]
    # Canadian provinces
    for p in CAN_PROVINCES:
        ALL_COUNTRY_NAMES.append(normalize(p["name"]))
        for a in p.get("aliases", []):
            ALL_COUNTRY_NAMES.append(normalize(a))
    # Territories
    for t in TERRITORIES:
        ALL_COUNTRY_NAMES.append(normalize(t["name"]))
        for a in t.get("aliases", []):
            ALL_COUNTRY_NAMES.append(normalize(a))
    # Capital names
    for c in COUNTRIES:
        ALL_COUNTRY_NAMES.append(normalize(c["name"]))
        ALL_COUNTRY_NAMES.append(normalize(c["capital"]))
    # State capitals
    for c in US_STATESCAP:
        ALL_COUNTRY_NAMES.append(normalize(c["name"]))
        ALL_COUNTRY_NAMES.append(normalize(c["capital"]))

init_all_options()

def get_continent_of_name(name):
    name = normalize(name)
    for c in COUNTRIES + US_STATES + CAN_PROVINCES + TERRITORIES:
        if normalize(c["name"]) == name:
            return c.get("continent")
        if "aliases" in c:
            for a in c["aliases"]:
                if normalize(a) == name:
                    return c.get("continent")
    return None

def get_pool_by_option(option):
    if option == "1":
        return COUNTRIES + TERRITORIES
    elif option == "2":
        return COUNTRIES
    elif option == "3":
        return TERRITORIES
    elif option == "4":
        return US_STATES
    elif option == "5":
        return CAN_PROVINCES
    elif option == ["6", "8"]:
        return []  # No special pool for capitals here
    elif option == "9":
        return US_STATESCAP
    else:
        return COUNTRIES

def spellcheck(guess, options, threshold=0.85):
    best_match = None
    best_ratio = 0


    for option in options:
        ratio = difflib.SequenceMatcher(None, guess, option).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = option
    if best_ratio >= threshold:
        return best_match
    return None

def get_continent_of_name(name):
    """
    Return the continent for a given name by searching all data.
    """
    name = normalize(name)
    for c in COUNTRIES + US_STATES + CAN_PROVINCES + TERRITORIES:
        if normalize(c["name"]) == name:
            return c.get("continent")
        if "aliases" in c:
            for a in c["aliases"]:
                if normalize(a) == name:
                    return c.get("continent")
    return None

def provide_continent_hint(guess_name, answer_continent):
    """
    Give a hint comparing the guessed continent with the answer's continent.
    """
    guess_continent = get_continent_of_name(guess_name)
    if guess_continent is None:
        return "Your guess doesn't match anything in the database."
    elif guess_continent == answer_continent:
        return "You're in the right continent!"
    else:
        return f"Your guess is in {guess_continent}, but it is in a different continent."

def hint_bank(entity):
    """
    Generate hints based on entity type.
    """
    hints = []

    # US State
    if entity.get("state", False):
        population = entity.get("population", "unknown")
        hints.append(f"This is a US state with about {population} million people.")
        hints.append(f"Its name has {len(entity['name'])} letters.")
        hints.append(f"The name starts with '{entity['name'][0]}'.")
        if "yearfounded" in entity:
            hints.append(f"It was founded in {entity['yearfounded']}.")

    # Canadian Province
    elif entity.get("province", False):
        population = entity.get("population", "unknown")
        hints.append(f"This is a Canadian province with about {population} million people.")
        hints.append(f"Its name has {len(entity['name'])} letters.")
        hints.append(f"The name starts with '{entity['name'][0]}'.")
        if "region" in entity:
            hints.append(f"Region: {entity['region']}.")

    # Territory or Dependency
    elif entity.get("territory", False):
        country_name = entity.get("country", "Unknown")
        region = entity.get("region", "Unknown")
        continent = entity.get("continent", "Unknown")
        population = entity.get("population", "unknown")
        hints.append(f"This territory is part of {country_name}.")
        hints.append(f"Located in {region} within {continent}.")
        hints.append(f"Population: {population} million.")

    # Capital city
    elif entity.get("capital", False):
        country_name = entity.get("name", "Unknown")
        region = entity.get("region", "Unknown")
        continent = entity.get("continent", "Unknown")
        population = entity.get("population", "unknown")
        if mode == ("7"):
            hints.append(f"The capital has a population of {entity['population']}.")
            hints.append(f"This capital was made the state capital in {entity['yearfounded']}.")
            hints.append(f"Its name has {len(entity['capital'])} letters.")
        elif mode == ("6"):
            hints.append(f"This is the capital of {country_name}.")
            hints.append(f"Located in {region} on {continent}.")
            hints.append(f"Its name has {len(entity['capital'])} letters.")
        elif mode == ("8"):
            hints.append(f"Located in {region} on {continent}.")
            hints.append(f"The country has a population of {entity['population']}.")
            hints.append(f"Its name has {len(entity['capital'])} letters.")

    # General info for countries
    else:
        continent = entity.get("continent", "Unknown")
        region = entity.get("region", "Unknown")
        name_len = len(entity["name"])
        population = entity.get("population", "unknown")
        capital = entity.get("capital", "N/A")
        hints.append(f"It is in {continent}.")
        hints.append(f"Region: {region}.")
        hints.append(f"The capital city is {capital}.")
        hints.append(f"Population: {population} million.")
        hints.append(f"Name has {name_len} letters.")
        hints.append(f"Name starts with '{entity['name'][0]}'.")

    return hints

# ----------------- Main game functions -----------------

def play_full_game():
    global stats
    stats["played"] += 1

    pool = get_pool_by_option(mode)
    country = random.choice(pool)
    answers = [normalize(c) for c in [country["name"]]]
    answer_continent = country.get("continent", "Unknown")
    hints = []

    hints += hint_bank(country)
    random.shuffle(hints)
    hint_index = 0

    print("Guess the name of the country/state/province/territory:")

    for attempt in range(1, 6):
        guess_input = input(f"Attempt {attempt}/5: ")
        guess = normalize(guess_input)

        if guess in answers:
            print("Correct!")
            stats["wins"] += 1
            return

        combined_options = ALL_COUNTRY_NAMES + [normalize(t["name"]) for t in TERRITORIES]
        suggestion = spellcheck(guess, combined_options, threshold=0.85)

        if suggestion:
            confirm = input(f"Did you mean {suggestion}? (y/n): ").lower()
            if confirm == "y":
                if normalize(suggestion) in answers:
                    print("Correct!")
                    stats["wins"] += 1
                    return
                else:
                    print("No, that's not correct.")
                    def provide_continent_hint(guess_name, answer_continent):
                        guess_continent = get_continent_of_name(guess_name)
                        if guess_continent is None:
                            print("Your guess doesn't match anything in the database")
                        elif guess_continent == answer_continent:
                            return "You're in the right continent!"
                        else:
                            return f"Your guess is in {guess_continent}, but it is in a diffrent continent."
        if attempt >= 2 and hints and hint_index < len(hints):
            print("Hint:", hints[hint_index])
            hint_index += 1

    # Show clues after attempts
    answer = answers[0]
    answer_obj = next((c for c in COUNTRIES + US_STATES + CAN_PROVINCES + TERRITORIES if normalize(c["name"]) == answer), None)
    if answer_obj:
        population = answer_obj.get("population", "unknown")
        first_letter = answer_obj["name"][0]
        length = len(answer_obj["name"])
        continent = answer_obj.get("continent", "unknown")
        print(f"No more guesses. The answer was {answer_obj['name']}")

# Also the reverse of the guess capital capital -> country and country -> capital
def play_guess_capital():

    global stats
    stats["played"] += 1
    country = random.choice(COUNTRIES)
    answers = [normalize(country["capital"])]
    answer_continent = country.get("continent", "Unknown")
    hints = []

    hints += hint_bank(country)
    random.shuffle(hints)
    hint_index = 0


    print(f"Guess the capital of {country['name']}:")

    for attempt in range(1, 6):
        guess_input = input(f"Attempt {attempt}/5: ")
        guess = normalize(guess_input)

        if guess in answers:
            print("Correct!")
            stats["wins"] += 1
            return

        print(provide_continent_hint(guess, answer_continent))
        suggestion = spellcheck(guess, ALL_COUNTRY_NAMES, threshold=0.85)
        if suggestion:
            confirm = input(f"Did you mean {suggestion}? (y/n): ").lower()
            if confirm == "y":
                if normalize(suggestion) in answers:
                    print("Correct!")
                    stats["wins"] += 1
                    return
                else:
                    print("No, that's not correct.")

        if attempt >= 2 and hints and hint_index < len(hints):
            print("Hint:", hints[hint_index])
            hint_index += 1

    # Show info after attempts
    answer = answers[0]
    answer_obj = next((c for c in COUNTRIES if normalize(c["capital"]) == answer), None)
    if answer_obj:
        population = answer_obj.get("population", "unknown")
        first_letter = answer_obj["name"][0]
        length = len(answer_obj["name"])
        continent = answer_obj.get("continent", "unknown")
        print("No more guesses.")

#-----------------reverse capitals--------------

def play_guess_capitalreverse():

    global stats
    stats["played"] += 1
    country = random.choice(COUNTRIES)
    answers = [normalize(country["name"])]
    answer_continent = country.get("continent", "Unknown")
    hints = []

    hints += hint_bank(country)
    random.shuffle(hints)
    hint_index = 0


    print(f"Guess what country has the capital of {country['capital']}:")

    for attempt in range(1, 6):
        guess_input = input(f"Attempt {attempt}/5: ")
        guess = normalize(guess_input)

        if guess in answers:
            print("Correct!")
            stats["wins"] += 1
            return

        print(provide_continent_hint(guess, answer_continent))
        suggestion = spellcheck(guess, ALL_COUNTRY_NAMES, threshold=0.85)
        if suggestion:
            confirm = input(f"Did you mean {suggestion}? (y/n): ").lower()
            if confirm == "y":
                if normalize(suggestion) in answers:
                    print("Correct!")
                    stats["wins"] += 1
                    return
                else:
                    print("No, that's not correct.")

        if attempt >= 2 and hints and hint_index < len(hints):
            print("Hint:", hints[hint_index])
            hint_index += 1

    # Show info after attempts
    answer = answers[0]
    answer_obj = next((c for c in COUNTRIES if normalize(c["name"]) == answer), None)
    if answer_obj:
        population = answer_obj.get("population", "unknown")
        first_letter = answer_obj["name"][0]
        length = len(answer_obj["name"])
        continent = answer_obj.get("continent", "unknown")
        print("No more guesses.")


#-------------State Capitals--------------------

def play_guess_statecapital():

    global stats
    stats["played"] += 1
    country = random.choice(US_STATESCAP)
    answers = [normalize(country["capital"])]
    answer_continent = country.get("continent", "Unknown")
    hints = []

    hints += hint_bank(country)
    random.shuffle(hints)
    hint_index = 0

    print(f"Guess the state capital of {country['name']}:")

    for attempt in range(1, 6):
        guess_input = input(f"Attempt {attempt}/5: ")
        guess = normalize(guess_input)

        if guess in answers:
            print("Correct!")
            stats["wins"] += 1
            return

        print(provide_continent_hint(guess, answer_continent))
        suggestion = spellcheck(guess, ALL_COUNTRY_NAMES, threshold=0.85)
        if suggestion:
            confirm = input(f"Did you mean {suggestion}? (y/n): ").lower()
            if confirm == "y":
                if normalize(suggestion) in answers:
                    print("Correct!")
                    stats["wins"] += 1
                    return
                else:
                    print("No, that's not correct.")

        if attempt >= 2 and hints and hint_index < len(hints):
            print("Hint:", hints[hint_index])
            hint_index += 1

    # Show info after attempts
    answer = answers[0]
    answer_obj = next((c for c in US_STATESCAP if normalize(c["capital"]) == answer), None)
    if answer_obj:
        population = answer_obj.get("population", "unknown")
        first_letter = answer_obj["name"][0]
        length = len(answer_obj["name"])
        continent = answer_obj.get("continent", "unknown")
        print("No more guesses.")

#---------------------State Capitals reverse--------------

def play_guess_statecapitalreverse():

    global stats
    stats["played"] += 1
    country = random.choice(US_STATESCAP)
    answers = [normalize(country["name"])]
    answer_continent = country.get("continent", "Unknown")
    hints = []

    hints += hint_bank(country)
    random.shuffle(hints)
    hint_index = 0

    print(f"Guess what state has the capital of {country['capital']}:")

    for attempt in range(1, 6):
        guess_input = input(f"Attempt {attempt}/5: ")
        guess = normalize(guess_input)

        if guess in answers:
            print("Correct!")
            stats["wins"] += 1
            return

        print(provide_continent_hint(guess, answer_continent))
        suggestion = spellcheck(guess, ALL_COUNTRY_NAMES, threshold=0.85)
        if suggestion:
            confirm = input(f"Did you mean {suggestion}? (y/n): ").lower()
            if confirm == "y":
                if normalize(suggestion) in answers:
                    print("Correct!")
                    stats["wins"] += 1
                    return
                else:
                    print("No, that's not correct.")

        if attempt >= 2 and hints and hint_index < len(hints):
            print("Hint:", hints[hint_index])
            hint_index += 1

    # Show info after attempts
    answer = answers[0]
    answer_obj = next((c for c in US_STATESCAP if normalize(c["capital"]) == answer), None)
    if answer_obj:
        population = answer_obj.get("population", "unknown")
        first_letter = answer_obj["name"][0]
        length = len(answer_obj["name"])
        continent = answer_obj.get("continent", "unknown")
        print("No more guesses.")

#-----------------speedrun----------------
def play_timedcountry_namingthrity(duration_seconds=30):
    global stats
    stats["played"] += 1
    print(f"\nYou have {duration_seconds} seconds to name as many countries as possible!\n")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!")
    start_time = time.time()
    guessed_countries = set()
    total_countries = len([c for c in COUNTRIES])  # Total countries in dataset

    while True:
        elapsed = time.time() - start_time
        remaining = duration_seconds - elapsed
        if remaining <= 0:
            break
        print(f"\nTime remaining: {int(remaining)} seconds")
        guess_input = input("Enter country name: ")
        guess = normalize(guess_input)

        # Check if guess matches any country or alias
        found = False
        for country in COUNTRIES:
            names = [normalize(country["name"]), normalize(country["short"]), normalize(country["capital"])]
            if guess in names:
                if country["name"] not in guessed_countries:
                    guessed_countries.add(country["name"])
                    print(f"Correct! {country['name']} added.")
                else:
                    print(f"You already guessed {country['name']}.")
                found = True
                break
        if not found:
            print("Incorrect or already guessed.")

    print(f"\nTime's up! You named {len(guessed_countries)} countries.")
    print(f"Total countries in database: {total_countries}")
    print("Your guessed countries:")
    for c in guessed_countries:
        print(c)

def play_timedcountry_namingsixty(duration_seconds=60):
    global stats
    stats["played"] += 1
    print(f"\nYou have {duration_seconds} seconds to name as many countries as possible!\n")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!")
    start_time = time.time()
    guessed_countries = set()
    total_countries = len([c for c in COUNTRIES])  # Total countries in dataset

    while True:
        elapsed = time.time() - start_time
        remaining = duration_seconds - elapsed
        if remaining <= 0:
            break
        print(f"\nTime remaining: {int(remaining)} seconds")
        guess_input = input("Enter country name: ")
        guess = normalize(guess_input)

        # Check if guess matches any country or alias
        found = False
        for country in COUNTRIES:
            names = [normalize(country["name"]), normalize(country["short"]), normalize(country["capital"])]
            if guess in names:
                if country["name"] not in guessed_countries:
                    guessed_countries.add(country["name"])
                    print(f"Correct! {country['name']} added.")
                else:
                    print(f"You already guessed {country['name']}.")
                found = True
                break
        if not found:
            print("Incorrect or already guessed.")

    print(f"\nTime's up! You named {len(guessed_countries)} countries.")
    print(f"Total countries in database: {total_countries}")
    print("Your guessed countries:")
    for c in guessed_countries:
        print(c)











# ----------------- Main loop -----------------
if __name__ == "__main__":
    stats = {"played": 0, "wins": 0}
    while True:
        def main_menu():
            print("\n--- Main Menu ---")
            print("1. Countries/Territories")
            print("2. Countries")
            print("3. Territories")
            print("4. US States")
            print("5. Canadian Provinces")
            print("6. Guess the Capital")
            print("7. State Capitals")
            print("8. Guess the Country from the Capital")
            print("9. Guess the State from the Capital")
            print("10. More Modes")
            return input("Select an option (1-10): ")

        def main_menu_cont():
            print("\n--- Main Menu (Continued) ---")
            print("11. Speedrun (30s)")
            print("12. Speedrun (60s)")
            print("13. Go Back")
            return input("Select an option (11-13): ")

        while True:
            mode = main_menu()
            if mode == "10":
                # Continue to additional modes
                mode = main_menu_cont()
            elif mode == "13":
                # Go back to main menu
                continue

            # Now handle the selected mode
            if mode in ["1", "2", "3", "4", "5"]:
                # Modes that play full game
                print("\nLoading...")
                time.sleep(1)
                play_full_game()
            elif mode == "6":
                # Guess capital
                print("\nLoading...")
                time.sleep(1)
                play_guess_capital()
            elif mode == "7":
                # State capitals
                print("\nLoading...")
                time.sleep(1)
                play_guess_statecapital()
            elif mode == "8":
                # Guess country from capital
                print("\nLoading...")
                time.sleep(1)
                play_guess_capitalreverse()
            elif mode == "9":
                # Guess the state from the capital
                print("\nLoading...")
                time.sleep(1)
                play_guess_statecapitalreverse()
            elif mode == "11":
                print("\nLoading...")
                time.sleep(1)
                play_timedcountry_namingthrity()
            elif mode == "12":
                print("\nLoading...")
                time.sleep(1)
                play_timedcountry_namingsixtey()
            else:
                print("Invalid option. Please choose again.")
                continue

            # Show stats after each game
            print(f"\nStats: Played: {stats['played']}, Wins: {stats['wins']}")
            again = input("Play again? (y/n): ").lower()
            if again != "y":
                print("\nThanks for playing!")
                print("Licensed under GNU GPLv3.")
                print("Copyright (C) 2026 AEROforge")
                break
        # End of the inner while loop, restart main menu or exit
        break

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Thanks for playing!")
    print("Licensed under GNU GPLv3.")
    print("Copyright (C) 2026 AEROforge")
