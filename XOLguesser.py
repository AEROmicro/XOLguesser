import random
import difflib
import time

print("Welcome to XOLguesser")
time.sleep(1)
print("Programmed and edited by AEROxol")
print("Version 0.1")
time.sleep(0.5)


# -------------------------
# STATS
# -------------------------
stats = {
    "played": 0,
    "wins": 0,
    "losses": 0
}

# -------------------------
# COUNTRY DATA
# 195 countries: 193 UN members + Vatican City and Palestine
# name, short name, continent, capital, region, population (approx, million), aliases
# -------------------------
COUNTRIES = [
    # Africa
    {"name":"Algeria","short":"Algeria","continent":"Africa","capital":"Algiers","region":"North Africa","population":45,"aliases":[]},
    {"name":"Angola","short":"Angola","continent":"Africa","capital":"Luanda","region":"Southern Africa","population":36,"aliases":[]},
    {"name":"Benin","short":"Benin","continent":"Africa","capital":"Porto Novo","region":"West Africa","population":13,"aliases":[]},
    {"name":"Botswana","short":"Botswana","continent":"Africa","capital":"Gaborone","region":"Southern Africa","population":2.6,"aliases":[]},
    {"name":"Burkina Faso","short":"Burkina Faso","continent":"Africa","capital":"Ouagadougou","region":"West Africa","population":21,"aliases":[]},
    {"name":"Burundi","short":"Burundi","continent":"Africa","capital":"Gitega","region":"East Africa","population":11,"aliases":[]},
    {"name":"Cameroon","short":"Cameroon","continent":"Africa","capital":"Yaounde","region":"Central Africa","population":27,"aliases":[]},
    {"name":"Cape Verde","short":"Cape Verde","continent":"Africa","capital":"Praia","region":"West Africa","population":0.5,"aliases":[]},
    {"name":"Central African Republic","short":"Central African Republic","continent":"Africa","capital":"Bangui","region":"Central Africa","population":5,"aliases":[]},
    {"name":"Chad","short":"Chad","continent":"Africa","capital":"NDjamena","region":"Central Africa","population":17,"aliases":["TD"]},
    {"name":"Comoros","short":"Comoros","continent":"Africa","capital":"Moroni","region":"West Africa","population":0.8,"aliases":["KM"]},
    {"name":"Democratic Republic of the Congo","short":"Democratic Republic of the Congo","continent":"Africa","capital":"Kinshasa","region":"Central Africa","population":96,"aliases":["DRC"]},
    {"name":"Republic of the Congo","short":"Republic of the Congo","continent":"Africa","capital":"Brazzaville","region":"Central Africa","population":6,"aliases":[]},
    {"name":"Djibouti","short":"Djibouti","continent":"Africa","capital":"Djibouti","region":"West Africa","population":1,"aliases":[]},
    {"name":"Egypt","short":"Egypt","continent":"Africa","capital":"Cairo","region":"North Africa","population":109,"aliases":[]},
    {"name":"Equatorial Guinea","short":"Equatorial Guinea","continent":"Africa","capital":"Malabo","region":"Central Africa","population":2,"aliases":[]},
    {"name":"Eritrea","short":"Eritrea","continent":"Africa","capital":"Asmara","region":"Central Africa","population":4,"aliases":[]},
    {"name":"Eswatini","short":"Eswatini","continent":"Africa","capital":"Lobamba","region":"Southern Africa","population":1,"aliases":[]},
    {"name":"Ethiopia","short":"Ethiopia","continent":"Africa","capital":"Addis Ababa","region":"East Africa","population":120,"aliases":[]},
    {"name":"Gabon","short":"Gabon","continent":"Africa","capital":"Libreville","region":"Central Africa","population":2,"aliases":[]},
    {"name":"The Gambia","short":"Gambia","continent":"Africa","capital":"Banjul","region":"West Africa","population":3,"aliases":["Gambia"]},
    {"name":"Ghana","short":"Ghana","continent":"Africa","capital":"Accra","region":"West Africa","population":33,"aliases":[]},
    {"name":"Guinea","short":"Guinea","continent":"Africa","capital":"Conakry","region":"West Africa","population":14,"aliases":[]},
    {"name":"Guinea-Bissau","short":"Guinea-Bissau","continent":"Africa","capital":"Bissau","region":"West Africa","population":2,"aliases":[]},
    {"name":"Ivory Coast","short":"Ivory Coast","continent":"Africa","capital":"Yamoussoukro","region":"West Africa","population":27,"aliases":[]},
    {"name":"Kenya","short":"Kenya","continent":"Africa","capital":"Nairobi","region":"East Africa","population":53,"aliases":[]},
    {"name":"Lesotho","short":"Lesotho","continent":"Africa","capital":"Maseru","region":"Southern Africa","population":2,"aliases":[]},
    {"name":"Liberia","short":"Liberia","continent":"Africa","capital":"Monrovia","region":"West Africa","population":5,"aliases":[]},
    {"name":"Libya","short":"Libya","continent":"Africa","capital":"Tripoli","region":"North Africa","population":7,"aliases":["LY"]},
    {"name":"Madagascar","short":"Madagascar","continent":"Africa","capital":"Antananarivo","region":"East Africa","population":26,"aliases":[]},
    {"name":"Malawi","short":"Malawi","continent":"Africa","capital":"Lilongwe","region":"East Africa","population":19,"aliases":[]},
    {"name":"Mali","short":"Mali","continent":"Africa","capital":"Bamako","region":"West Africa","population":20,"aliases":[]},
    {"name":"Mauritania","short":"Mauritania","continent":"Africa","capital":"Nouakchott","region":"West Africa","population":4,"aliases":[]},
    {"name":"Mauritius","short":"Mauritius","continent":"Africa","capital":"Port Louis","region":"East Africa","population":1.3,"aliases":[]},
    {"name":"Morocco","short":"Morocco","continent":"Africa","capital":"Rabat","region":"North Africa","population":36,"aliases":[]},
    {"name":"Mozambique","short":"Mozambique","continent":"Africa","capital":"Maputo","region":"East Africa","population":30,"aliases":[]},
    {"name":"Namibia","short":"Namibia","continent":"Africa","capital":"Windhoek","region":"Southern Africa","population":2.5,"aliases":[]},
    {"name":"Niger","short":"Niger","continent":"Africa","capital":"Niamey","region":"West Africa","population":24,"aliases":[]},
    {"name":"Nigeria","short":"Nigeria","continent":"Africa","capital":"Abuja","region":"West Africa","population":200,"aliases":[]},
    {"name":"Rwanda","short":"Rwanda","continent":"Africa","capital":"Kigali","region":"East Africa","population":12,"aliases":[]},
    {"name":"São Tomé and Príncipe","short":"São Tomé and Príncipe","continent":"Africa","capital":"São Tomé","region":"Central Africa","population":0.2,"aliases":["Sao Tome", "São Tomé"]},
    {"name":"Senegal","short":"Senegal","continent":"Africa","capital":"Dakar","region":"West Africa","population":16,"aliases":[]},
    {"name":"Seychelles","short":"Seychelles","continent":"Africa","capital":"Victoria","region":"East Africa","population":0.1,"aliases":[]},
    {"name":"Sierra Leone","short":"Sierra Leone","continent":"Africa","capital":"Freetown","region":"West Africa","population":8,"aliases":[]},
    {"name":"Somalia","short":"Somalia","continent":"Africa","capital":"Mogadishu","region":"East Africa","population":15,"aliases":[]},
    {"name":"South Africa","short":"South Africa","continent":"Africa","capital":"Pretoria","region":"Southern Africa","population":58,"aliases":[]},
    {"name":"South Sudan","short":"South Sudan","continent":"Africa","capital":"Juba","region":"East Africa","population":11,"aliases":[]},
    {"name":"Sudan","short":"Sudan","continent":"Africa","capital":"Khartoum","region":"North Africa","population":43,"aliases":[]},
    {"name":"Tanzania","short":"Tanzania","continent":"Africa","capital":"Dodoma","region":"East Africa","population":58,"aliases":[]},
    {"name":"Togo","short":"Togo","continent":"Africa","capital":"Lomé","region":"West Africa","population":8,"aliases":[]},
    {"name":"Tunisia","short":"Tunisia","continent":"Africa","capital":"Tunis","region":"North Africa","population":11,"aliases":[]},
    {"name":"Uganda","short":"Uganda","continent":"Africa","capital":"Kampala","region":"East Africa","population":45,"aliases":[]},
    {"name":"Zambia","short":"Zambia","continent":"Africa","capital":"Lusaka","region":"East Africa","population":18,"aliases":[]},
    {"name":"Zimbabwe","short":"Zimbabwe","continent":"Africa","capital":"Harare","region":"East Africa","population":14,"aliases":[]},

    # Asia
    {"name":"Afghanistan","short":"Afghanistan","continent":"Asia","capital":"Kabul","region":"Southern Asia","population":38,"aliases":[]},
    {"name":"Armenia","short":"Armenia","continent":"Asia","capital":"Yerevan","region":"Western Asia","population":3,"aliases":[]},
    {"name":"Azerbaijan","short":"Azerbaijan","continent":"Asia","capital":"Baku","region":"Western Asia","population":10,"aliases":[]},
    {"name":"Bahrain","short":"Bahrain","continent":"Asia","capital":"Manama","region":"Western Asia","population":1.7,"aliases":[]},
    {"name":"Bangladesh","short":"Bangladesh","continent":"Asia","capital":"Dhaka","region":"Southern Asia","population":165,"aliases":[]},
    {"name":"Bhutan","short":"Bhutan","continent":"Asia","capital":"Thimphu","region":"Southern Asia","population":0.8,"aliases":[]},
    {"name":"Brunei","short":"Brunei","continent":"Asia","capital":"Bandar Seri Begawan","region":"South-Eastern Asia","population":0.4,"aliases":[]},
    {"name":"Cambodia","short":"Cambodia","continent":"Asia","capital":"Phnom Penh","region":"South-Eastern Asia","population":16,"aliases":[]},
    {"name":"China","short":"China","continent":"Asia","capital":"Beijing","region":"Eastern Asia","population":1400,"aliases":[]},
    {"name":"Cyprus","short":"Cyprus","continent":"Asia","capital":"Nicosia","region":"Western Asia","population":1.2,"aliases":[]},
    {"name":"Georgia","short":"Georgia","continent":"Asia","capital":"Tbilisi","region":"Western Asia","population":4,"aliases":[]},
    {"name":"India","short":"India","continent":"Asia","capital":"New Delhi","region":"Southern Asia","population":1366,"aliases":[]},
    {"name":"Indonesia","short":"Indonesia","continent":"Asia","capital":"Jakarta","region":"South-Eastern Asia","population":273,"aliases":[]},
    {"name":"Iran","short":"Iran","continent":"Asia","capital":"Tehran","region":"Western Asia","population":81,"aliases":[]},
    {"name":"Iraq","short":"Iraq","continent":"Asia","capital":"Baghdad","region":"Western Asia","population":40,"aliases":[]},
    {"name":"Israel","short":"Israel","continent":"Asia","capital":"Jerusalem","region":"Western Asia","population":9,"aliases":[]},
    {"name":"Japan","short":"Japan","continent":"Asia","capital":"Tokyo","region":"Eastern Asia","population":126,"aliases":[]},
    {"name":"Jordan","short":"Jordan","continent":"Asia","capital":"Amman","region":"Western Asia","population":10,"aliases":[]},
    {"name":"Kazakhstan","short":"Kazakhstan","continent":"Asia","capital":"Nur-Sultan","region":"Central Asia","population":18,"aliases":[]},
    {"name":"Kuwait","short":"Kuwait","continent":"Asia","capital":"Kuwait City","region":"Western Asia","population":4,"aliases":[]},
    {"name":"Kyrgyzstan","short":"Kyrgyzstan","continent":"Asia","capital":"Bishkek","region":"Central Asia","population":6,"aliases":[]},
    {"name":"Laos","short":"Laos","continent":"Asia","capital":"Vientiane","region":"South-Eastern Asia","population":7,"aliases":[]},
    {"name":"Lebanon","short":"Lebanon","continent":"Asia","capital":"Beirut","region":"Western Asia","population":6,"aliases":[]},
    {"name":"Malaysia","short":"Malaysia","continent":"Asia","capital":"Kuala Lumpur","region":"South-Eastern Asia","population":32,"aliases":[]},
    {"name":"Maldives","short":"Maldives","continent":"Asia","capital":"Malé","region":"Southern Asia","population":0.5,"aliases":[]},
    {"name":"Mongolia","short":"Mongolia","continent":"Asia","capital":"Ulaanbaatar","region":"Eastern Asia","population":3,"aliases":[]},
    {"name":"Myanmar","short":"Myanmar","continent":"Asia","capital":"Naypyidaw","region":"South-Eastern Asia","population":54,"aliases":[]},
    {"name":"Nepal","short":"Nepal","continent":"Asia","capital":"Kathmandu","region":"Southern Asia","population":29,"aliases":[]},
    {"name":"North Korea","short":"North Korea","continent":"Asia","capital":"Pyongyang","region":"Eastern Asia","population":25,"aliases":["Democratic Peoples Republic of Korea"]},
    {"name":"Oman","short":"Oman","continent":"Asia","capital":"Muscat","region":"Western Asia","population":4.6,"aliases":[]},
    {"name":"Pakistan","short":"Pakistan","continent":"Asia","capital":"Islamabad","region":"Southern Asia","population":208,"aliases":[]},
    {"name":"Palestine","short":"Palestine","continent":"Asia","capital":"Jerusalem","region":"Western Asia","population":5,"aliases":[]},
    {"name":"Philippines","short":"Philippines","continent":"Asia","capital":"Manila","region":"South-Eastern Asia","population":108,"aliases":[]},
    {"name":"Qatar","short":"Qatar","continent":"Asia","capital":"Doha","region":"Western Asia","population":2.8,"aliases":[]},
    {"name":"Russia","short":"Russia","continent":"Asia","capital":"Moscow","region":"Eastern Europe/Asia","population":146,"aliases":[]},
    {"name":"Saudi Arabia","short":"Saudi Arabia","continent":"Asia","capital":"Riyadh","region":"Western Asia","population":34,"aliases":[]},
    {"name":"Singapore","short":"Singapore","continent":"Asia","capital":"Singapore","region":"South-Eastern Asia","population":5.7,"aliases":[]},
    {"name":"South Korea","short":"South Korea","continent":"Asia","capital":"Seoul","region":"Eastern Asia","population":51,"aliases":[]},
    {"name":"Sri Lanka","short":"Sri Lanka","continent":"Asia","capital":"Sri Jayawardenepura Kotte","region":"Southern Asia","population":21,"aliases":[]},
    {"name":"Syria","short":"Syria","continent":"Asia","capital":"Damascus","region":"Western Asia","population":17,"aliases":[]},
    {"name":"Taiwan","short":"Taiwan","continent":"Asia","capital":"Taipei","region":"Eastern Asia","population":23,"aliases":[]},
    {"name":"Tajikistan","short":"Tajikistan","continent":"Asia","capital":"Dushanbe","region":"Central Asia","population":9,"aliases":[]},
    {"name":"Thailand","short":"Thailand","continent":"Asia","capital":"Bangkok","region":"South-Eastern Asia","population":70,"aliases":[]},
    {"name":"Timor-Leste","short":"Timor-Leste","continent":"Asia","capital":"Dili","region":"South-Eastern Asia","population":1.3,"aliases":["East Timor"]},
    {"name":"Turkey","short":"Turkey","continent":"Asia","capital":"Ankara","region":"Western Asia","population":82,"aliases":[]},
    {"name":"Turkmenistan","short":"Turkmenistan","continent":"Asia","capital":"Ashgabat","region":"Central Asia","population":6,"aliases":[]},
    {"name":"United Arab Emirates","short":"UAE","continent":"Asia","capital":"Abu Dhabi","region":"Western Asia","population":9.1,"aliases":["UAE", "Emirates"]},
    {"name":"Uzbekistan","short":"Uzbekistan","continent":"Asia","capital":"Tashkent","region":"Central Asia","population":33,"aliases":[]},
    {"name":"Vietnam","short":"Vietnam","continent":"Asia","capital":"Hanoi","region":"South-Eastern Asia","population":96,"aliases":[]},
    {"name":"Yemen","short":"Yemen","continent":"Asia","capital":"Sana'a","region":"Western Asia","population":29,"aliases":[]},

    # Europe
    {"name":"Albania","short":"Albania","continent":"Europe","capital":"Tirana","region":"Southern Europe","population":3,"aliases":[]},
    {"name":"Andorra","short":"Andorra","continent":"Europe","capital":"Andorra la Vella","region":"Southern Europe","population":0.08,"aliases":[]},
    {"name":"Austria","short":"Austria","continent":"Europe","capital":"Vienna","region":"Central Europe","population":9,"aliases":[]},
    {"name":"Belarus","short":"Belarus","continent":"Europe","capital":"Minsk","region":"Eastern Europe","population":9,"aliases":[]},
    {"name":"Belgium","short":"Belgium","continent":"Europe","capital":"Brussels","region":"Western Europe","population":11,"aliases":[]},
    {"name":"Bosnia and Herzegovina","short":"Bosnia","continent":"Europe","capital":"Sarajevo","region":"South-Eastern Europe","population":3,"aliases":["Bosnia", "Herzegovina"]},
    {"name":"Bulgaria","short":"Bulgaria","continent":"Europe","capital":"Sofia","region":"Eastern Europe","population":7,"aliases":[]},
    {"name":"Croatia","short":"Croatia","continent":"Europe","capital":"Zagreb","region":"South-Eastern Europe","population":4,"aliases":[]},
    {"name":"Cyprus","short":"Cyprus","continent":"Europe","capital":"Nicosia","region":"Eastern Europe","population":1.2,"aliases":[]},
    {"name":"Czech Republic","short":"Czechia","continent":"Europe","capital":"Prague","region":"Central Europe","population":10,"aliases":["Czechia"]},
    {"name":"Denmark","short":"Denmark","continent":"Europe","capital":"Copenhagen","region":"Northern Europe","population":6,"aliases":[]},
    {"name":"Estonia","short":"Estonia","continent":"Europe","capital":"Tallinn","region":"Northern Europe","population":1.3,"aliases":[]},
    {"name":"Finland","short":"Finland","continent":"Europe","capital":"Helsinki","region":"Northern Europe","population":5.5,"aliases":[]},
    {"name":"France","short":"France","continent":"Europe","capital":"Paris","region":"Western Europe","population":67,"aliases":[]},
    {"name":"Germany","short":"Germany","continent":"Europe","capital":"Berlin","region":"Western Europe","population":83,"aliases":[]},
    {"name":"Greece","short":"Greece","continent":"Europe","capital":"Athens","region":"Southern Europe","population":11,"aliases":[]},
    {"name":"Hungary","short":"Hungary","continent":"Europe","capital":"Budapest","region":"Central Europe","population":10,"aliases":[]},
    {"name":"Iceland","short":"Iceland","continent":"Europe","capital":"Reykjavík","region":"Northern Europe","population":0.36,"aliases":[]},
    {"name":"Ireland","short":"Ireland","continent":"Europe","capital":"Dublin","region":"Northern Europe","population":4.9,"aliases":[]},
    {"name":"Italy","short":"Italy","continent":"Europe","capital":"Rome","region":"Southern Europe","population":60,"aliases":[]},
    {"name":"Latvia","short":"Latvia","continent":"Europe","capital":"Riga","region":"Northern Europe","population":1.9,"aliases":[]},
    {"name":"Liechtenstein","short":"Liechtenstein","continent":"Europe","capital":"Vaduz","region":"Western Europe","population":0.038,"aliases":[]},
    {"name":"Lithuania","short":"Lithuania","continent":"Europe","capital":"Vilnius","region":"Northern Europe","population":2.8,"aliases":[]},
    {"name":"Luxembourg","short":"Luxembourg","continent":"Europe","capital":"Luxembourg City","region":"Western Europe","population":0.6,"aliases":[]},
    {"name":"Malta","short":"Malta","continent":"Europe","capital":"Valletta","region":"Southern Europe","population":0.52,"aliases":[]},
    {"name":"Moldova","short":"Moldova","continent":"Europe","capital":"Chișinău","region":"Eastern Europe","population":3,"aliases":[]},
    {"name":"Monaco","short":"Monaco","continent":"Europe","capital":"Monaco","region":"Western Europe","population":0.04,"aliases":[]},
    {"name":"Montenegro","short":"Montenegro","continent":"Europe","capital":"Podgorica","region":"South-Eastern Europe","population":0.6,"aliases":[]},
    {"name":"Netherlands","short":"Netherlands","continent":"Europe","capital":"Amsterdam","region":"Western Europe","population":17,"aliases":[]},
    {"name":"North Macedonia","short":"North Macedonia","continent":"Europe","capital":"Skopje","region":"Southern Europe","population":2,"aliases":["Macedonia"]},
    {"name":"Norway","short":"Norway","continent":"Europe","capital":"Oslo","region":"Northern Europe","population":5.3,"aliases":[]},
    {"name":"Poland","short":"Poland","continent":"Europe","capital":"Warsaw","region":"Eastern Europe","population":38,"aliases":[]},
    {"name":"Portugal","short":"Portugal","continent":"Europe","capital":"Lisbon","region":"Southern Europe","population":10,"aliases":[]},
    {"name":"Romania","short":"Romania","continent":"Europe","capital":"Bucharest","region":"Eastern Europe","population":19,"aliases":[]},
    {"name":"San Marino","short":"San Marino","continent":"Europe","capital":"San Marino","region":"Southern Europe","population":0.03,"aliases":[]},
    {"name":"Serbia","short":"Serbia","continent":"Europe","capital":"Belgrade","region":"South-Eastern Europe","population":7,"aliases":[]},
    {"name":"Slovakia","short":"Slovakia","continent":"Europe","capital":"Bratislava","region":"Central Europe","population":5.4,"aliases":[]},
    {"name":"Slovenia","short":"Slovenia","continent":"Europe","capital":"Ljubljana","region":"South-Eastern Europe","population":2.1,"aliases":[]},
    {"name":"Spain","short":"Spain","continent":"Europe","capital":"Madrid","region":"Southern Europe","population":47,"aliases":[]},
    {"name":"Sweden","short":"Sweden","continent":"Europe","capital":"Stockholm","region":"Northern Europe","population":10,"aliases":[]},
    {"name":"Switzerland","short":"Switzerland","continent":"Europe","capital":"Bern","region":"Western Europe","population":8.5,"aliases":[]},
    {"name":"Ukraine","short":"Ukraine","continent":"Europe","capital":"Kyiv","region":"Eastern Europe","population":44,"aliases":[]},
    {"name":"United Kingdom","short":"UK","continent":"Europe","capital":"London","region":"Northern Europe","population":66,"aliases":["Britain", "Great Britain", "England"]},
    {"name":"Vatican City","short":"Vatican City","continent":"Europe","capital":"Vatican City","region":"Southern Europe","population":0.0008,"aliases":["Vatican"]},

    # North America
    {"name":"Antigua and Barbuda","short":"Antigua","continent":"North America","capital":"St. John's","region":"Caribbean","population":0.1,"aliases":["Antigua", "Barbuda"]},
    {"name":"Bahamas","short":"Bahamas","continent":"North America","capital":"Nassau","region":"Caribbean","population":0.4,"aliases":[]},
    {"name":"Barbados","short":"Barbados","continent":"North America","capital":"Bridgetown","region":"Caribbean","population":0.3,"aliases":[]},
    {"name":"Belize","short":"Belize","continent":"North America","capital":"Belmopan","region":"Central America","population":0.4,"aliases":[]},
    {"name":"Canada","short":"Canada","continent":"North America","capital":"Ottawa","region":"Northern America","population":37,"aliases":["CA", "CAN"]},
    {"name":"Costa Rica","short":"Costa Rica","continent":"North America","capital":"San José","region":"Central America","population":5,"aliases":[]},
    {"name":"Cuba","short":"Cuba","continent":"North America","capital":"Havana","region":"Caribbean","population":11,"aliases":[]},
    {"name":"Dominica","short":"Dominica","continent":"North America","capital":"Roseau","region":"Caribbean","population":0.07,"aliases":[]},
    {"name":"Dominican Republic","short":"Dominican Republic","continent":"North America","capital":"Santo Domingo","region":"Caribbean","population":11,"aliases":[]},
    {"name":"El Salvador","short":"El Salvador","continent":"North America","capital":"San Salvador","region":"Central America","population":6,"aliases":[]},
    {"name":"Grenada","short":"Grenada","continent":"North America","capital":"St. George's","region":"Caribbean","population":0.1,"aliases":[]},
    {"name":"Guatemala","short":"Guatemala","continent":"North America","capital":"Guatemala City","region":"Central America","population":17,"aliases":[]},
    {"name":"Haiti","short":"Haiti","continent":"North America","capital":"Port-au-Prince","region":"Caribbean","population":11,"aliases":[]},
    {"name":"Honduras","short":"Honduras","continent":"North America","capital":"Tegucigalpa","region":"Central America","population":10,"aliases":[]},
    {"name":"Jamaica","short":"Jamaica","continent":"North America","capital":"Kingston","region":"Caribbean","population":3,"aliases":[]},
    {"name":"Mexico","short":"Mexico","continent":"North America","capital":"Mexico City","region":"Central America","population":126,"aliases":[]},
    {"name":"Nicaragua","short":"Nicaragua","continent":"North America","capital":"Managua","region":"Central America","population":6,"aliases":[]},
    {"name":"Panama","short":"Panama","continent":"North America","capital":"Panama City","region":"Central America","population":4.3,"aliases":[]},
    {"name":"Saint Kitts and Nevis","short":"Saint Kitts and Nevis","continent":"North America","capital":"Basseterre","region":"Caribbean","population":0.05,"aliases":["Saint Kitts", "St. Kitts", "The Nevis"]},
    {"name":"Saint Lucia","short":"Saint Lucia","continent":"North America","capital":"Castries","region":"Caribbean","population":0.18,"aliases":["St. Lucia"]},
    {"name":"Saint Vincent and the Grenadines","short":"Saint Vincent","continent":"North America","capital":"Kingstown","region":"Caribbean","population":0.11,"aliases":["Saint Vincent", "Grenadines", "St. Vincent"]},
    {"name":"Trinidad and Tobago","short":"Trinidad and Tobago","continent":"North America","capital":"Port of Spain","region":"Caribbean","population":1.4,"aliases":["Trinidad", "Tobago"]},
    {"name":"United States","short":"USA","continent":"North America","capital":"Washington, D.C.","region":"Northern America","population":328,"aliases":["USA", "US", "U.S.", "America", "United States"]},

    # Oceania
    {"name":"Australia","short":"Australia","continent":"Oceania","capital":"Canberra","region":"Australia and New Zealand","population":25,"aliases":[]},
    {"name":"Fiji","short":"Fiji","continent":"Oceania","capital":"Suva","region":"Melanesia","population":0.9,"aliases":[]},
    {"name":"Kiribati","short":"Kiribati","continent":"Oceania","capital":"Tarawa","region":"Micronesia","population":0.1,"aliases":[]},
    {"name":"Marshall Islands","short":"Marshall Islands","continent":"Oceania","capital":"Majuro","region":"Micronesia","population":0.06,"aliases":[]},
    {"name":"Micronesia","short":"Micronesia","continent":"Oceania","capital":"Palikir","region":"Micronesia","population":0.1,"aliases":[]},
    {"name":"Nauru","short":"Nauru","continent":"Oceania","capital":"Yaren","region":"Micronesia","population":0.01,"aliases":[]},
    {"name":"New Zealand","short":"New Zealand","continent":"Oceania","capital":"Wellington","region":"Australia and New Zealand","population":4.8,"aliases":[]},
    {"name":"Palau","short":"Palau","continent":"Oceania","capital":"Ngerulmud","region":"Micronesia","population":0.02,"aliases":[]},
    {"name":"Papua New Guinea","short":"Papua New Guinea","continent":"Oceania","capital":"Port Moresby","region":"Melanesia","population":8.9,"aliases":[]},
    {"name":"Samoa","short":"Samoa","continent":"Oceania","capital":"Apia","region":"Polynesia","population":0.2,"aliases":[]},
    {"name":"Solomon Islands","short":"Solomon Islands","continent":"Oceania","capital":"Honiara","region":"Melanesia","population":0.6,"aliases":[]},
    {"name":"Tonga","short":"Tonga","continent":"Oceania","capital":"Nuku'alofa","region":"Polynesia","population":0.1,"aliases":[]},
    {"name":"Tuvalu","short":"Tuvalu","continent":"Oceania","capital":"Funafuti","region":"Polynesia","population":0.01,"aliases":[]},
    {"name":"Vanuatu","short":"Vanuatu","continent":"Oceania","capital":"Port Vila","region":"Melanesia","population":0.3,"aliases":[]}
]

# -------------------------
# HELPERS
# -------------------------
def normalize(text):
    return text.lower().strip()

def valid_inputs(country):
    """Return list of valid inputs including country name, short name, and aliases."""
    return [normalize(country["short"]), normalize(country["name"])] + [normalize(a) for a in country["aliases"]]

def spellcheck(guess, options, threshold=0.4):
    """Return the closest match if similarity exceeds threshold, more lenient."""
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

def hint_bank(country):
    """Generate hints about the country."""
    return [
        f"It is in {country['continent']}",
        f"It is in the region {country['region']}",
        f"The capital city is {country['capital']}",
        f"It has about {country['population']} million people",
        f"The name starts with {country['short'][0]}",
        f"The short name has {len(country['short'])} letters"
    ]

# -------------------------
# GAME FUNCTION
# -------------------------
def play(simulated_inputs=None):
    stats["played"] += 1

    print("\nChoose a continent")
    print("1 Africa")
    print("2 Asia")
    print("3 Europe")
    print("4 North America")
    print("5 South America")
    print("6 Oceania")
    print("7 All")

    if simulated_inputs is not None and simulated_inputs:
        choice = simulated_inputs.pop(0)
        print(f"Enter number: {choice}")
    else:
        try:
            choice = input("Enter number: ").strip()
        except OSError:
            choice = "7"
            print("Input not available. Defaulting to all continents.")

    continent_map = {
        "1": "Africa",
        "2": "Asia",
        "3": "Europe",
        "4": "North America",
        "5": "South America",
        "6": "Oceania"
    }

    # Filter countries by continent if applicable
    pool = COUNTRIES  # Your countries list should be assigned here
    if choice in continent_map:
        pool = [c for c in COUNTRIES if c["continent"] == continent_map[choice]]

    country = random.choice(pool)
    answers = valid_inputs(country)
    hints = hint_bank(country)
    random.shuffle(hints)
    hint_index = 0

    for attempt in range(1, 6):
        if simulated_inputs is not None and simulated_inputs:
            guess_input = simulated_inputs.pop(0)
            print(f"Guess {attempt}/5: {guess_input}")
        else:
            try:
                guess_input = input(f"Guess {attempt}/5: ")
            except OSError:
                guess_input = ""

        guess = normalize(guess_input)

        # Check for exact match
        if guess in answers:
            print("Correct")
            stats["wins"] += 1
            return

        # Check for close match with enhanced spellcheck
        suggestion = spellcheck(guess, answers, threshold=0.4)
        if suggestion:
            prompt = f"Did you mean {suggestion}? (y/n): "
            confirm = "n"
            if simulated_inputs is not None and simulated_inputs:
                confirm = simulated_inputs.pop(0)
                print(f"{prompt}{confirm}")
            else:
                try:
                    confirm = input(prompt).lower()
                except OSError:
                    confirm = "n"
                    print(f"{prompt}{confirm}")

            if confirm == "y":
                print("Correct")
                stats["wins"] += 1
                return

        print("Wrong guess. Try again.")
        if attempt >= 2 and hints and hint_index < len(hints):
            print("Hint:", hints[hint_index])
            hint_index += 1

    print("Out of guesses")
    print("Answer:", country["name"])
    stats["losses"] += 1

# -------------------------
# MAIN LOOP
# -------------------------
# main loop
simulated_inputs = None
while True:
    play(simulated_inputs=simulated_inputs)
    print("\nStats")
    print("Played:", stats["played"])
    print("Wins:", stats["wins"])
    print("Losses:", stats["losses"])

    if simulated_inputs is not None and simulated_inputs:
        again = simulated_inputs.pop(0)
        print(f"Play again? (y/n): {again}")
    else:
        try:
            again = input("\nPlay again? (y/n): ").lower()
        except OSError:
            again = "n"
            print("\nPlay again? (y/n): n")

    if again != "y":
        break