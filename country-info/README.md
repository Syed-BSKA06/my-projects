# Country Info Lookup

A simple Python CLI tool — type a country name and instantly get its **capital** and **most populated city**.

## Requirements

- Python 3.6+
- No external libraries needed

## Usage

```bash
python country_info.py
```

## Example

```
Country Info Lookup
Type a country name to get its capital and most populated city.
Type 'quit' or 'exit' to stop.

Country: India
  Capital             : New Delhi
  Most Populated City : Mumbai

Country: Australia
  Capital             : Canberra
  Most Populated City : Sydney

Country: USA
  Capital             : Washington, D.C.
  Most Populated City : New York City
```

## Supported Aliases

Common short names are supported:

| You type | Resolves to |
|---|---|
| USA / US / America | United States |
| UK / Britain / England | United Kingdom |
| UAE | United Arab Emirates |
| Czechia | Czech Republic |
| Türkiye | Turkey |

## Coverage

Includes 120+ countries. If a country isn't found, double-check the spelling or try an alternate name.
