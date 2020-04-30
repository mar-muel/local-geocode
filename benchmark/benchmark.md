# Comparison against geopy

This comparison shows how local-geocode and geopy predict user locations provided by Twitter users. 

Local-geocode agrees on the country-level in about 51% of the tested cases with geopy (n=50k). The below samples shows the top 150 disagreements between geopy and local-geocde.

## Main take-aways
* Local-geocde does better at imaginary names which don't exist or are abstract
* Geopy does usually better when states are given (e.g. London, ON vs. London UK), however geopy fails in the case of "CA" for California 
* An error rate of zero is tricky due to the many name collisions

|     | user.location                  | local-geocode   | geopy   |
|----:|:-------------------------------|:----------------|:--------|
|   0 | Hong Kong                      | hk              | cn      |
|   1 | Earth                          | nan             | us      |
|   2 | San Francisco, CA              | us              | ca      |
|   3 | Worldwide                      | nan             | gb      |
|   4 | Global                         | nan             | ca      |
|   5 | Planet Earth                   | nan             | in      |
|   6 | she/her                        | cn              | us      |
|   7 | Everywhere                     | nan             | ro      |
|   8 | Internet                       | nan             | ht      |
|   9 | 香港                             | hk              | cn      |
|  10 | World                          | nan             | nz      |
|  11 | Southern California            | us              | et      |
|  12 | 🇵🇭                             | nan             | nan     |
|  13 | Europe                         | nan             | de      |
|  14 | America                        | us              | nl      |
|  15 | Lagos                          | ng              | la      |
|  16 | Oakland, CA                    | us              | ca      |
|  17 | Jamaica                        | us              | jm      |
|  18 | Hell                           | nan             | us      |
|  19 | North West, England            | gb              | de      |
|  20 | South East, England            | gb              | se      |
|  21 | Long Beach, CA                 | us              | ca      |
|  22 | CA                             | us              | ca      |
|  23 |                                | nan             | nan     |
|  24 | earth                          | nan             | us      |
|  25 | Mars                           | nan             | fr      |
|  26 | Bay Area                       | pr              | us      |
|  27 | Here                           | nan             | ba      |
|  28 | Somewhere                      | nan             | fr      |
|  29 | Berkeley, CA                   | us              | ca      |
|  30 | Puerto Rico                    | pr              | us      |
|  31 | PA                             | us              | pa      |
|  32 | SoCal                          | nan             | br      |
|  33 | Africa                         | tn              | td      |
|  34 | New England                    | gb              | us      |
|  35 | U.S.A.                         | us              | eg      |
|  36 | hell                           | nan             | us      |
|  37 | PH                             | nan             | ph      |
|  38 | Hogwarts                       | nan             | ke      |
|  39 | Birmingham, AL                 | gb              | us      |
|  40 | DC                             | us              | co      |
|  41 | LA                             | us              | nan     |
|  42 | Earth                          | nan             | us      |
|  43 | Pacific Northwest              | bj              | us      |
|  44 | he/him                         | nan             | ng      |
|  45 | +62                            | nan             | fr      |
|  46 | Midwest                        | nan             | us      |
|  47 | MY                             | nan             | us      |
|  48 | Victoria, Australia            | ca              | au      |
|  49 | North America                  | us              | ca      |
|  50 | Jakarta Capital Region         | id              | ph      |
|  51 | DMV                            | nan             | us      |
|  52 | 🇲🇾                             | nan             | nan     |
|  53 | Neverland                      | nan             | us      |
|  54 | Alexandria, VA                 | eg              | us      |
|  55 | Nowhere                        | nan             | gb      |
|  56 | PNW                            | nan             | ir      |
|  57 | AZ                             | us              | az      |
|  58 | they/them                      | nan             | th      |
|  59 | Riverside, CA                  | us              | ca      |
|  60 | 🌎                              | nan             | nan     |
|  61 | Home                           | nan             | de      |
|  62 | London, Ontario                | gb              | ca      |
|  63 | everywhere                     | nan             | ro      |
|  64 | somewhere                      | nan             | fr      |
|  65 | Asia                           | ph              | ru      |
|  66 | 🇨🇦                             | nan             | nan     |
|  67 | Federal Capital Territory, Nig | ng              | nan     |
|  68 | 🇺🇸                             | nan             | nan     |
|  69 | Irvine, CA                     | us              | ca      |
|  70 | East Coast                     | nz              | sg      |
|  71 | Wakanda                        | nan             | ss      |
|  72 | SF Bay Area                    | pr              | us      |
|  73 | worldwide                      | nan             | do      |
|  74 | Islamabad                      | pk              | bd      |
|  75 | ph                             | nan             | ph      |
|  76 | The World                      | in              | nz      |
|  77 | .                              | nan             | nan     |
|  78 | Santa Barbara, CA              | us              | ca      |
|  79 | West Coast                     | au              | nz      |
|  80 | Santa Monica, CA               | us              | ca      |
|  81 | VA                             | us              | vn      |
|  82 | Universe                       | nan             | dk      |
|  83 | Antarctica                     | nan             | nan     |
|  84 | Heaven                         | nan             | gb      |
|  85 | Kuala Lumpur, Wilayah Persekut | my              | nan     |
|  86 | Wonderland                     | nan             | ph      |
|  87 | localhost                      | nan             | be      |
|  88 | Beverly Hills, CA              | us              | ca      |
|  89 | Vancouver, WA                  | ca              | us      |
|  90 | LDN                            | nan             | cz      |
|  91 | Silicon Valley                 | nan             | us      |
|  92 | 🌍                              | nan             | nan     |
|  93 | National Capital Region, Repub | ph              | nan     |
|  94 | ATL                            | us              | co      |
|  95 | Unknown                        | nan             | et      |
|  96 | here                           | nan             | ba      |
|  97 | Athens, GA                     | gr              | us      |
|  98 | Chicagoland                    | nan             | us      |
|  99 | 🌎🌍🌏                            | nan             | nan     |
| 100 | Around the world               | in              | ca      |
| 101 | nowhere                        | nan             | gb      |
| 102 | 🌏                              | nan             | nan     |
| 103 | Pasadena, CA                   | us              | ca      |
| 104 | Northern Virginia              | us              | au      |
| 105 | HTX                            | nan             | dk      |
| 106 | +65                            | nan             | fr      |
| 107 | Moon                           | nan             | ee      |
| 108 | bay area                       | pr              | us      |
| 109 | Jakarta Capital Region, Indone | id              | nan     |
| 110 | Namibia                        | nan             | na      |
| 111 | Oceanside, CA                  | us              | ca      |
| 112 | Naples, FL                     | it              | us      |
| 113 | stump of the Liberty Tree      | in              | nan     |
| 114 | European Union                 | us              | bg      |
| 115 | Yorkshire                      | gb              | us      |
| 116 | America                        | us              | nl      |
| 117 | MA                             | us              | it      |
| 118 | Columbia, SC                   | co              | us      |
| 119 | Newport Beach, CA              | us              | ca      |
| 120 | EARTH                          | nan             | us      |
| 121 | West Region, Singapore         | sg              | se      |
| 122 | home                           | nan             | de      |
| 123 | Space                          | nan             | au      |
| 124 | Santa Rosa, CA                 | ph              | ca      |
| 125 | Ontario, CA                    | us              | ca      |
| 126 | So Cal                         | nan             | au      |
| 127 | hong kong                      | hk              | cn      |
| 128 | +63                            | nan             | tw      |
| 129 | Stockton, CA                   | us              | ca      |
| 130 | 🏳️🌈                            | nan             | do      |
| 131 | Somewhere over the rainbow     | in              | nan     |
| 132 | Salem, OR                      | in              | us      |
| 133 | Malibu, CA                     | us              | ca      |
| 134 | Gotham City                    | nan             | us      |
| 135 | htx                            | nan             | dk      |
| 136 | Twitter                        | nan             | us      |
| 137 | She/her                        | cn              | us      |
| 138 | Winterfell                     | nan             | de      |
| 139 | lagos                          | ng              | la      |
| 140 | The Internet                   | in              | ht      |
| 141 | WORLDWIDE                      | nan             | gb      |
| 142 | Narnia                         | nan             | it      |
| 143 | International                  | nan             | cz      |
| 144 | Pluto                          | nan             | us      |
| 145 | NorCal                         | nan             | au      |
| 146 | Kuala Lumpur City, Kuala Lumpu | my              | nan     |
| 147 | Davis, CA                      | us              | ca      |
| 148 | Portland, ME                   | us              | mx      |
| 149 | she/they                       | cn              | ca      |
