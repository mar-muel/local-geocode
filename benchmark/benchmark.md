# Comparison against geopy

This comparison shows how local-geocode and geopy predict user locations provided by Twitter users. 

Local-geocode agrees on the country-level in about 51% of the tested cases with geopy (n=50k). The below samples shows the top 150 disagreements between geopy and local-geocde.

## Main take-aways
* Local-geocde seems to do better overall, but this would need to be quantitatively assessed by human annotation.
* Imaginary names are not predicted, whereas geopy tries to predict something in all cases
* Local-geocode supports country codes for semi-autonomous countries (e.g. Hong Kong)
* Geopy does sometimes a better job when states are given (e.g. London, ON vs. London UK). However, geopy fails consistently in the case of "CA" for California 
* An error rate of zero is tricky due to the many name collisions

|     | user.location                  | local-geocode   | geopy   |
|----:|:-------------------------------|:----------------|:--------|
|   0 | Hong Kong                      | hk              | cn      |
|   1 | Earth                          |                 | us      |
|   2 | San Francisco, CA              | us              | ca      |
|   3 | Worldwide                      |                 | gb      |
|   4 | Global                         |                 | ca      |
|   5 | Planet Earth                   |                 | in      |
|   6 | she/her                        | cn              | us      |
|   7 | Everywhere                     |                 | ro      |
|   8 | Internet                       |                 | ht      |
|   9 | 香港                             | hk              | cn      |
|  10 | World                          |                 | nz      |
|  11 | Southern California            | us              | et      |
|  12 | 🇵🇭                             |                 |         |
|  13 | Europe                         |                 | de      |
|  14 | America                        | us              | nl      |
|  15 | Lagos                          | ng              | la      |
|  16 | Oakland, CA                    | us              | ca      |
|  17 | Jamaica                        | us              | jm      |
|  18 | Hell                           |                 | us      |
|  19 | North West, England            | gb              | de      |
|  20 | South East, England            | gb              | se      |
|  21 | Long Beach, CA                 | us              | ca      |
|  22 | CA                             | us              | ca      |
|  23 |                                |                 |         |
|  24 | earth                          |                 | us      |
|  25 | Mars                           |                 | fr      |
|  26 | Bay Area                       | pr              | us      |
|  27 | Here                           |                 | ba      |
|  28 | Somewhere                      |                 | fr      |
|  29 | Berkeley, CA                   | us              | ca      |
|  30 | Puerto Rico                    | pr              | us      |
|  31 | PA                             | us              | pa      |
|  32 | SoCal                          |                 | br      |
|  33 | Africa                         | tn              | td      |
|  34 | New England                    | gb              | us      |
|  35 | U.S.A.                         | us              | eg      |
|  36 | hell                           |                 | us      |
|  37 | PH                             |                 | ph      |
|  38 | Hogwarts                       |                 | ke      |
|  39 | Birmingham, AL                 | gb              | us      |
|  40 | DC                             | us              | co      |
|  41 | LA                             | us              |         |
|  42 | Earth                          |                 | us      |
|  43 | Pacific Northwest              | bj              | us      |
|  44 | he/him                         |                 | ng      |
|  45 | +62                            |                 | fr      |
|  46 | Midwest                        |                 | us      |
|  47 | MY                             |                 | us      |
|  48 | Victoria, Australia            | ca              | au      |
|  49 | North America                  | us              | ca      |
|  50 | Jakarta Capital Region         | id              | ph      |
|  51 | DMV                            |                 | us      |
|  52 | 🇲🇾                             |                 |         |
|  53 | Neverland                      |                 | us      |
|  54 | Alexandria, VA                 | eg              | us      |
|  55 | Nowhere                        |                 | gb      |
|  56 | PNW                            |                 | ir      |
|  57 | AZ                             | us              | az      |
|  58 | they/them                      |                 | th      |
|  59 | Riverside, CA                  | us              | ca      |
|  60 | 🌎                              |                 |         |
|  61 | Home                           |                 | de      |
|  62 | London, Ontario                | gb              | ca      |
|  63 | everywhere                     |                 | ro      |
|  64 | somewhere                      |                 | fr      |
|  65 | Asia                           | ph              | ru      |
|  66 | 🇨🇦                             |                 |         |
|  67 | Federal Capital Territory, Nig | ng              |         |
|  68 | 🇺🇸                             |                 |         |
|  69 | Irvine, CA                     | us              | ca      |
|  70 | East Coast                     | nz              | sg      |
|  71 | Wakanda                        |                 | ss      |
|  72 | SF Bay Area                    | pr              | us      |
|  73 | worldwide                      |                 | do      |
|  74 | Islamabad                      | pk              | bd      |
|  75 | ph                             |                 | ph      |
|  76 | The World                      | in              | nz      |
|  77 | .                              |                 |         |
|  78 | Santa Barbara, CA              | us              | ca      |
|  79 | West Coast                     | au              | nz      |
|  80 | Santa Monica, CA               | us              | ca      |
|  81 | VA                             | us              | vn      |
|  82 | Universe                       |                 | dk      |
|  83 | Antarctica                     |                 |         |
|  84 | Heaven                         |                 | gb      |
|  85 | Kuala Lumpur, Wilayah Persekut | my              |         |
|  86 | Wonderland                     |                 | ph      |
|  87 | localhost                      |                 | be      |
|  88 | Beverly Hills, CA              | us              | ca      |
|  89 | Vancouver, WA                  | ca              | us      |
|  90 | LDN                            |                 | cz      |
|  91 | Silicon Valley                 |                 | us      |
|  92 | 🌍                              |                 |         |
|  93 | National Capital Region, Repub | ph              |         |
|  94 | ATL                            | us              | co      |
|  95 | Unknown                        |                 | et      |
|  96 | here                           |                 | ba      |
|  97 | Athens, GA                     | gr              | us      |
|  98 | Chicagoland                    |                 | us      |
|  99 | 🌎🌍🌏                            |                 |         |
| 100 | Around the world               | in              | ca      |
| 101 | nowhere                        |                 | gb      |
| 102 | 🌏                              |                 |         |
| 103 | Pasadena, CA                   | us              | ca      |
| 104 | Northern Virginia              | us              | au      |
| 105 | HTX                            |                 | dk      |
| 106 | +65                            |                 | fr      |
| 107 | Moon                           |                 | ee      |
| 108 | bay area                       | pr              | us      |
| 109 | Jakarta Capital Region, Indone | id              |         |
| 110 | Namibia                        |                 | na      |
| 111 | Oceanside, CA                  | us              | ca      |
| 112 | Naples, FL                     | it              | us      |
| 113 | stump of the Liberty Tree      | in              |         |
| 114 | European Union                 | us              | bg      |
| 115 | Yorkshire                      | gb              | us      |
| 116 | America                        | us              | nl      |
| 117 | MA                             | us              | it      |
| 118 | Columbia, SC                   | co              | us      |
| 119 | Newport Beach, CA              | us              | ca      |
| 120 | EARTH                          |                 | us      |
| 121 | West Region, Singapore         | sg              | se      |
| 122 | home                           |                 | de      |
| 123 | Space                          |                 | au      |
| 124 | Santa Rosa, CA                 | ph              | ca      |
| 125 | Ontario, CA                    | us              | ca      |
| 126 | So Cal                         |                 | au      |
| 127 | hong kong                      | hk              | cn      |
| 128 | +63                            |                 | tw      |
| 129 | Stockton, CA                   | us              | ca      |
| 130 | 🏳️🌈                            |                 | do      |
| 131 | Somewhere over the rainbow     | in              |         |
| 132 | Salem, OR                      | in              | us      |
| 133 | Malibu, CA                     | us              | ca      |
| 134 | Gotham City                    |                 | us      |
| 135 | htx                            |                 | dk      |
| 136 | Twitter                        |                 | us      |
| 137 | She/her                        | cn              | us      |
| 138 | Winterfell                     |                 | de      |
| 139 | lagos                          | ng              | la      |
| 140 | The Internet                   | in              | ht      |
| 141 | WORLDWIDE                      |                 | gb      |
| 142 | Narnia                         |                 | it      |
| 143 | International                  |                 | cz      |
| 144 | Pluto                          |                 | us      |
| 145 | NorCal                         |                 | au      |
| 146 | Kuala Lumpur City, Kuala Lumpu | my              |         |
| 147 | Davis, CA                      | us              | ca      |
| 148 | Portland, ME                   | us              | mx      |
| 149 | she/they                       | cn              | ca      |

