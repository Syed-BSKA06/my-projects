#!/usr/bin/env python3

COUNTRIES = {
    "afghanistan": {"capital": "Kabul", "largest_city": "Kabul"},
    "albania": {"capital": "Tirana", "largest_city": "Tirana"},
    "algeria": {"capital": "Algiers", "largest_city": "Algiers"},
    "angola": {"capital": "Luanda", "largest_city": "Luanda"},
    "argentina": {"capital": "Buenos Aires", "largest_city": "Buenos Aires"},
    "australia": {"capital": "Canberra", "largest_city": "Sydney"},
    "austria": {"capital": "Vienna", "largest_city": "Vienna"},
    "azerbaijan": {"capital": "Baku", "largest_city": "Baku"},
    "bahrain": {"capital": "Manama", "largest_city": "Manama"},
    "bangladesh": {"capital": "Dhaka", "largest_city": "Dhaka"},
    "belarus": {"capital": "Minsk", "largest_city": "Minsk"},
    "belgium": {"capital": "Brussels", "largest_city": "Brussels"},
    "bolivia": {"capital": "Sucre", "largest_city": "Santa Cruz de la Sierra"},
    "bosnia and herzegovina": {"capital": "Sarajevo", "largest_city": "Sarajevo"},
    "brazil": {"capital": "Brasília", "largest_city": "São Paulo"},
    "bulgaria": {"capital": "Sofia", "largest_city": "Sofia"},
    "cambodia": {"capital": "Phnom Penh", "largest_city": "Phnom Penh"},
    "cameroon": {"capital": "Yaoundé", "largest_city": "Douala"},
    "canada": {"capital": "Ottawa", "largest_city": "Toronto"},
    "chile": {"capital": "Santiago", "largest_city": "Santiago"},
    "china": {"capital": "Beijing", "largest_city": "Shanghai"},
    "colombia": {"capital": "Bogotá", "largest_city": "Bogotá"},
    "congo": {"capital": "Brazzaville", "largest_city": "Brazzaville"},
    "costa rica": {"capital": "San José", "largest_city": "San José"},
    "croatia": {"capital": "Zagreb", "largest_city": "Zagreb"},
    "cuba": {"capital": "Havana", "largest_city": "Havana"},
    "czech republic": {"capital": "Prague", "largest_city": "Prague"},
    "denmark": {"capital": "Copenhagen", "largest_city": "Copenhagen"},
    "dominican republic": {"capital": "Santo Domingo", "largest_city": "Santo Domingo"},
    "ecuador": {"capital": "Quito", "largest_city": "Guayaquil"},
    "egypt": {"capital": "Cairo", "largest_city": "Cairo"},
    "el salvador": {"capital": "San Salvador", "largest_city": "San Salvador"},
    "ethiopia": {"capital": "Addis Ababa", "largest_city": "Addis Ababa"},
    "finland": {"capital": "Helsinki", "largest_city": "Helsinki"},
    "france": {"capital": "Paris", "largest_city": "Paris"},
    "georgia": {"capital": "Tbilisi", "largest_city": "Tbilisi"},
    "germany": {"capital": "Berlin", "largest_city": "Berlin"},
    "ghana": {"capital": "Accra", "largest_city": "Accra"},
    "greece": {"capital": "Athens", "largest_city": "Athens"},
    "guatemala": {"capital": "Guatemala City", "largest_city": "Guatemala City"},
    "honduras": {"capital": "Tegucigalpa", "largest_city": "Tegucigalpa"},
    "hungary": {"capital": "Budapest", "largest_city": "Budapest"},
    "india": {"capital": "New Delhi", "largest_city": "Mumbai"},
    "indonesia": {"capital": "Jakarta", "largest_city": "Jakarta"},
    "iran": {"capital": "Tehran", "largest_city": "Tehran"},
    "iraq": {"capital": "Baghdad", "largest_city": "Baghdad"},
    "ireland": {"capital": "Dublin", "largest_city": "Dublin"},
    "israel": {"capital": "Jerusalem", "largest_city": "Jerusalem"},
    "italy": {"capital": "Rome", "largest_city": "Rome"},
    "ivory coast": {"capital": "Yamoussoukro", "largest_city": "Abidjan"},
    "jamaica": {"capital": "Kingston", "largest_city": "Kingston"},
    "japan": {"capital": "Tokyo", "largest_city": "Tokyo"},
    "jordan": {"capital": "Amman", "largest_city": "Amman"},
    "kazakhstan": {"capital": "Astana", "largest_city": "Almaty"},
    "kenya": {"capital": "Nairobi", "largest_city": "Nairobi"},
    "kuwait": {"capital": "Kuwait City", "largest_city": "Kuwait City"},
    "laos": {"capital": "Vientiane", "largest_city": "Vientiane"},
    "lebanon": {"capital": "Beirut", "largest_city": "Beirut"},
    "libya": {"capital": "Tripoli", "largest_city": "Tripoli"},
    "malaysia": {"capital": "Kuala Lumpur", "largest_city": "Kuala Lumpur"},
    "mali": {"capital": "Bamako", "largest_city": "Bamako"},
    "mexico": {"capital": "Mexico City", "largest_city": "Mexico City"},
    "morocco": {"capital": "Rabat", "largest_city": "Casablanca"},
    "mozambique": {"capital": "Maputo", "largest_city": "Maputo"},
    "myanmar": {"capital": "Naypyidaw", "largest_city": "Yangon"},
    "nepal": {"capital": "Kathmandu", "largest_city": "Kathmandu"},
    "netherlands": {"capital": "Amsterdam", "largest_city": "Amsterdam"},
    "new zealand": {"capital": "Wellington", "largest_city": "Auckland"},
    "nicaragua": {"capital": "Managua", "largest_city": "Managua"},
    "niger": {"capital": "Niamey", "largest_city": "Niamey"},
    "nigeria": {"capital": "Abuja", "largest_city": "Lagos"},
    "north korea": {"capital": "Pyongyang", "largest_city": "Pyongyang"},
    "norway": {"capital": "Oslo", "largest_city": "Oslo"},
    "oman": {"capital": "Muscat", "largest_city": "Muscat"},
    "pakistan": {"capital": "Islamabad", "largest_city": "Karachi"},
    "panama": {"capital": "Panama City", "largest_city": "Panama City"},
    "paraguay": {"capital": "Asunción", "largest_city": "Asunción"},
    "peru": {"capital": "Lima", "largest_city": "Lima"},
    "philippines": {"capital": "Manila", "largest_city": "Quezon City"},
    "poland": {"capital": "Warsaw", "largest_city": "Warsaw"},
    "portugal": {"capital": "Lisbon", "largest_city": "Lisbon"},
    "qatar": {"capital": "Doha", "largest_city": "Doha"},
    "romania": {"capital": "Bucharest", "largest_city": "Bucharest"},
    "russia": {"capital": "Moscow", "largest_city": "Moscow"},
    "saudi arabia": {"capital": "Riyadh", "largest_city": "Riyadh"},
    "senegal": {"capital": "Dakar", "largest_city": "Dakar"},
    "serbia": {"capital": "Belgrade", "largest_city": "Belgrade"},
    "singapore": {"capital": "Singapore", "largest_city": "Singapore"},
    "somalia": {"capital": "Mogadishu", "largest_city": "Mogadishu"},
    "south africa": {"capital": "Pretoria", "largest_city": "Johannesburg"},
    "south korea": {"capital": "Seoul", "largest_city": "Seoul"},
    "spain": {"capital": "Madrid", "largest_city": "Madrid"},
    "sri lanka": {"capital": "Sri Jayawardenepura Kotte", "largest_city": "Colombo"},
    "sudan": {"capital": "Khartoum", "largest_city": "Khartoum"},
    "sweden": {"capital": "Stockholm", "largest_city": "Stockholm"},
    "switzerland": {"capital": "Bern", "largest_city": "Zurich"},
    "syria": {"capital": "Damascus", "largest_city": "Aleppo"},
    "taiwan": {"capital": "Taipei", "largest_city": "New Taipei"},
    "tanzania": {"capital": "Dodoma", "largest_city": "Dar es Salaam"},
    "thailand": {"capital": "Bangkok", "largest_city": "Bangkok"},
    "tunisia": {"capital": "Tunis", "largest_city": "Tunis"},
    "turkey": {"capital": "Ankara", "largest_city": "Istanbul"},
    "turkmenistan": {"capital": "Ashgabat", "largest_city": "Ashgabat"},
    "uganda": {"capital": "Kampala", "largest_city": "Kampala"},
    "ukraine": {"capital": "Kyiv", "largest_city": "Kyiv"},
    "united arab emirates": {"capital": "Abu Dhabi", "largest_city": "Dubai"},
    "united kingdom": {"capital": "London", "largest_city": "London"},
    "united states": {"capital": "Washington, D.C.", "largest_city": "New York City"},
    "uruguay": {"capital": "Montevideo", "largest_city": "Montevideo"},
    "uzbekistan": {"capital": "Tashkent", "largest_city": "Tashkent"},
    "venezuela": {"capital": "Caracas", "largest_city": "Caracas"},
    "vietnam": {"capital": "Hanoi", "largest_city": "Ho Chi Minh City"},
    "yemen": {"capital": "Sana'a", "largest_city": "Sana'a"},
    "zambia": {"capital": "Lusaka", "largest_city": "Lusaka"},
    "zimbabwe": {"capital": "Harare", "largest_city": "Harare"},
}

# Aliases for common alternate names
ALIASES = {
    "usa": "united states",
    "us": "united states",
    "america": "united states",
    "uk": "united kingdom",
    "britain": "united kingdom",
    "great britain": "united kingdom",
    "england": "united kingdom",
    "uae": "united arab emirates",
    "south korea": "south korea",
    "drc": "congo",
    "czechia": "czech republic",
    "türkiye": "turkey",
    "côte d'ivoire": "ivory coast",
}


def lookup(country: str):
    key = country.strip().lower()
    key = ALIASES.get(key, key)
    return COUNTRIES.get(key)


def main():
    print("Country Info Lookup")
    print("Type a country name to get its capital and most populated city.")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        try:
            user_input = input("Country: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        info = lookup(user_input)
        if info:
            print(f"  Capital             : {info['capital']}")
            print(f"  Most Populated City : {info['largest_city']}\n")
        else:
            print(f"  '{user_input}' not found. Check spelling or try an alternate name.\n")


if __name__ == "__main__":
    main()
