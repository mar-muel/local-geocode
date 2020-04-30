# Comparison against geopy

This comparison shows how local-geocode and geopy predict user locations provided by Twitter users. 

Local-geocode agrees on the country-level in about 51% of the tested cases with geopy (n=50k). The below samples shows the top 150 disagreements between geopy and local-geocde.

## Main take-aways
* Local-geocde does better at imaginary names which don't exist or are abstract
* Geopy does usually better when states are given (e.g. London, ON vs. London UK), however geopy fails in the case of "CA" for California 
* An error rate of zero is tricky due to the many name collisions

|   # | user.location                                                                         | local-geocode   | geopy   |
|----:|:--------------------------------------------------------------------------------------|:----------------|:--------|
|   0 | Hong Kong                                                                             | hk              | cn      |
|   1 | Earth                                                                                 |                 | us      |
|   2 | San Francisco, CA                                                                     | us              | ca      |
|   3 | Worldwide                                                                             |                 | gb      |
|   4 | Global                                                                                |                 | ca      |
|   5 | Planet Earth                                                                          |                 | in      |
|   6 | she/her                                                                               | cn              | us      |
|   7 | Everywhere                                                                            |                 | ro      |
|   8 | San Francisco                                                                         | ph              | us      |
|   9 | Internet                                                                              |                 | ht      |
|  10 | 香港                                                                                    | hk              | cn      |
|  11 | World                                                                                 |                 | nz      |
|  12 | Southern California                                                                   | us              | et      |
|  13 | 🇵🇭                                                                                    |                 |         |
|  14 | Europe                                                                                |                 | de      |
|  15 | America                                                                               | us              | nl      |
|  16 | Lagos                                                                                 | ng              | la      |
|  17 | Oakland, CA                                                                           | us              | ca      |
|  18 | Hell                                                                                  |                 | us      |
|  19 | North West, England                                                                   | gb              | de      |
|  20 | South East, England                                                                   | gb              | se      |
|  21 | Long Beach, CA                                                                        | us              | ca      |
|  22 | CA                                                                                    | us              | ca      |
|  23 |                                                                                       |                 |         |
|  24 | earth                                                                                 |                 | us      |
|  25 | Mars                                                                                  |                 | fr      |
|  26 | Bay Area                                                                              | pr              | us      |
|  27 | Here                                                                                  |                 | ba      |
|  28 | Somewhere                                                                             |                 | fr      |
|  29 | Berkeley, CA                                                                          | us              | ca      |
|  30 | Puerto Rico                                                                           | pr              | us      |
|  31 | PA                                                                                    | us              | pa      |
|  32 | San Francisco Bay Area                                                                | pr              | us      |
|  33 | SoCal                                                                                 |                 | br      |
|  34 | Africa                                                                                | tn              | td      |
|  35 | New England                                                                           | gb              | us      |
|  36 | U.S.A.                                                                                | us              | eg      |
|  37 | hell                                                                                  |                 | us      |
|  38 | PH                                                                                    |                 | ph      |
|  39 | Hogwarts                                                                              |                 | ke      |
|  40 | DC                                                                                    | us              | co      |
|  41 | LA                                                                                    | us              |         |
|  42 | Earth                                                                                 |                 | us      |
|  43 | Pacific Northwest                                                                     | bj              | us      |
|  44 | he/him                                                                                |                 | ng      |
|  45 | +62                                                                                   |                 | fr      |
|  46 | Midwest                                                                               |                 | us      |
|  47 | MY                                                                                    |                 | us      |
|  48 | North America                                                                         | us              | ca      |
|  49 | Jakarta Capital Region                                                                | id              | ph      |
|  50 | Hyderabad                                                                             | pk              | in      |
|  51 | DMV                                                                                   |                 | us      |
|  52 | 🇲🇾                                                                                    |                 |         |
|  53 | Neverland                                                                             |                 | us      |
|  54 | Nowhere                                                                               |                 | gb      |
|  55 | PNW                                                                                   |                 | ir      |
|  56 | AZ                                                                                    | us              | az      |
|  57 | they/them                                                                             |                 | th      |
|  58 | Riverside, CA                                                                         | us              | ca      |
|  59 | 🌎                                                                                     |                 |         |
|  60 | Home                                                                                  |                 | de      |
|  61 | Ottawa                                                                                | us              | ca      |
|  62 | everywhere                                                                            |                 | ro      |
|  63 | somewhere                                                                             |                 | fr      |
|  64 | Asia                                                                                  | ph              | ru      |
|  65 | 🇨🇦                                                                                    |                 |         |
|  66 | Federal Capital Territory, Nig                                                        | ng              |         |
|  67 | 🇺🇸                                                                                    |                 |         |
|  68 | Irvine, CA                                                                            | us              | ca      |
|  69 | East Coast                                                                            | nz              | sg      |
|  70 | Wakanda                                                                               |                 | ss      |
|  71 | SF Bay Area                                                                           | pr              | us      |
|  72 | worldwide                                                                             |                 | do      |
|  73 | Islamabad                                                                             | pk              | bd      |
|  74 | ph                                                                                    |                 | ph      |
|  75 | The World                                                                             | in              | nz      |
|  76 | .                                                                                     |                 |         |
|  77 | Santa Barbara, CA                                                                     | us              | ca      |
|  78 | West Coast                                                                            | au              | nz      |
|  79 | Santa Monica, CA                                                                      | us              | ca      |
|  80 | VA                                                                                    | us              | vn      |
|  81 | Universe                                                                              |                 | dk      |
|  82 | Antarctica                                                                            |                 |         |
|  83 | Heaven                                                                                |                 | gb      |
|  84 | Kuala Lumpur, Wilayah Persekut                                                        | my              |         |
|  85 | Wonderland                                                                            |                 | ph      |
|  86 | localhost                                                                             |                 | be      |
|  87 | Beverly Hills, CA                                                                     | us              | ca      |
|  88 | LDN                                                                                   |                 | cz      |
|  89 | Silicon Valley                                                                        |                 | us      |
|  90 | 🌍                                                                                     |                 |         |
|  91 | National Capital Region, Repub                                                        | ph              |         |
|  92 | ATL                                                                                   | us              | co      |
|  93 | Unknown                                                                               |                 | et      |
|  94 | Victoria, British Columbia                                                            | au              | ca      |
|  95 | Bristol                                                                               | us              | gb      |
|  96 | here                                                                                  |                 | ba      |
|  97 | Manila City, National Capital                                                         | pg              | ph      |
|  98 | Chicagoland                                                                           |                 | us      |
|  99 | 🌎🌍🌏                                                                                   |                 |         |
| 100 | Around the world                                                                      | in              | ca      |
| 101 | nowhere                                                                               |                 | gb      |
| 102 | 🌏                                                                                     |                 |         |
| 103 | Pasadena, CA                                                                          | us              | ca      |
| 104 | Northern Virginia                                                                     | us              | au      |
| 105 | HTX                                                                                   |                 | dk      |
| 106 | +65                                                                                   |                 | fr      |
| 107 | Moon                                                                                  |                 | ee      |
| 108 | bay area                                                                              | pr              | us      |
| 109 | Jakarta Capital Region, Indone                                                        | id              |         |
| 110 | Namibia                                                                               |                 | na      |
| 111 | Oceanside, CA                                                                         | us              | ca      |
| 112 | stump of the Liberty Tree                                                             | in              |         |
| 113 | European Union                                                                        | us              | bg      |
| 114 | Yorkshire                                                                             | gb              | us      |
| 115 | America                                                                               | us              | nl      |
| 116 | MA                                                                                    | us              | it      |
| 117 | Columbia, SC                                                                          | co              | us      |
| 118 | Gold Coast, Queensland                                                                | gh              | au      |
| 119 | Newport Beach, CA                                                                     | us              | ca      |
| 120 | EARTH                                                                                 |                 | us      |
| 121 | West Region, Singapore                                                                | sg              | se      |
| 122 | home                                                                                  |                 | de      |
| 123 | Space                                                                                 |                 | au      |
| 124 | Santa Rosa, CA                                                                        | us              | ca      |
| 125 | Ontario, CA                                                                           | us              | ca      |
| 126 | So Cal                                                                                |                 | au      |
| 127 | hong kong                                                                             | hk              | cn      |
| 128 | +63                                                                                   |                 | tw      |
| 129 | Stockton, CA                                                                          | us              | ca      |
| 130 | 🏳️🌈                                                                                   |                 | do      |
| 131 | Somewhere over the rainbow                                                            | in              |         |
| 132 | Malibu, CA                                                                            | us              | ca      |
| 133 | Gotham City                                                                           |                 | us      |
| 134 | htx                                                                                   |                 | dk      |
| 135 | Twitter                                                                               |                 | us      |
| 136 | She/her                                                                               | cn              | us      |
| 137 | Winterfell                                                                            |                 | de      |
| 138 | lagos                                                                                 | ng              | la      |
| 139 | The Internet                                                                          | in              | ht      |
| 140 | WORLDWIDE                                                                             |                 | gb      |
| 141 | Narnia                                                                                |                 | it      |
| 142 | International                                                                         |                 | cz      |
| 143 | Pluto                                                                                 |                 | us      |
| 144 | NorCal                                                                                |                 | au      |
| 145 | Kuala Lumpur City, Kuala Lumpu                                                        | my              |         |
| 146 | Davis, CA                                                                             | us              | ca      |
| 147 | Portland, ME                                                                          | us              | mx      |
