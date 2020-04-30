# Comparison against geopy

This comparison shows how local-geocode and geopy predict user locations provided by Twitter users. 

Local-geocode agrees on the country-level in about 51% of the tested cases with geopy (n=50k). The below samples shows the top 1000 disagreements between geopy and local-geocde.

## Main take-aways
• Local-geocde does better at imaginary names which don't exist or are abstract
• Geopy does usually better when states are given (e.g. London, ON vs. London UK), however geopy fails in the case of "CA" for California 
• An error rate of zero is tricky due to the many name collisions


|     | user.location                                                                         | local-geocode   | geopy   |
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
| 148 | she/they                                                                              | cn              | ca      |
| 149 | Everywhere                                                                            |                 | ro      |
| 150 | TN                                                                                    | us              | tn      |
| 151 | EU                                                                                    |                 | fr      |
| 152 | East Region, Singapore                                                                | sg              | se      |
| 153 | San Antonio                                                                           | ph              | us      |
| 154 | influence.co/the_mudan                                                                | us              |         |
| 155 | online                                                                                |                 | fr      |
| 156 | she/her                                                                               | cn              | us      |
| 157 | Orange, CA                                                                            | us              | ca      |
| 158 | Santa Fe, NM                                                                          | ar              | us      |
| 159 | 127.0.0.1                                                                             |                 |         |
| 160 | GA                                                                                    | us              | ga      |
| 161 | Milky Way                                                                             | in              | sc      |
| 162 | Lost                                                                                  |                 | gb      |
| 163 | Torrance, CA                                                                          | us              | ca      |
| 164 | Global Citizen                                                                        |                 |         |
| 165 | Anywhere                                                                              |                 | mw      |
| 166 | Reality                                                                               |                 | gb      |
| 167 | WORLD                                                                                 |                 | nz      |
| 168 | Hong Kong                                                                             | hk              | cn      |
| 169 | KL                                                                                    |                 | in      |
| 170 | RVA                                                                                   |                 | cd      |
| 171 | The Moon                                                                              | in              | ee      |
| 172 | unknown                                                                               |                 | et      |
| 173 | South London                                                                          | in              | id      |
| 174 | planet earth                                                                          |                 | in      |
| 175 | Ventura, CA                                                                           | us              | ca      |
| 176 | U.S.A                                                                                 |                 | eg      |
| 177 | South Jersey                                                                          | in              | je      |
| 178 | She/Her                                                                               | cn              | us      |
| 179 | neverland                                                                             |                 | us      |
| 180 | Venus                                                                                 |                 | us      |
| 181 | +60                                                                                   |                 | fr      |
| 182 | HK                                                                                    |                 | cn      |
| 183 | The South                                                                             | in              | kr      |
| 184 | Long Island                                                                           | is              | ca      |
| 185 | world                                                                                 |                 | nz      |
| 186 | Planet Earth                                                                          |                 | in      |
| 187 | Makati City, National Capital                                                         | pg              | ph      |
| 188 | Parts Unknown                                                                         |                 | co      |
| 189 | The Universe                                                                          | in              | dk      |
| 190 | ♡                                                                                     |                 |         |
| 191 | Gotham                                                                                |                 | us      |
| 192 | Mother Earth                                                                          |                 | gb      |
| 193 | World Patriot, Costa Rica                                                             | cr              |         |
| 194 | World Wide                                                                            |                 | cn      |
| 195 | Pacific NW                                                                            |                 | us      |
| 196 | South                                                                                 | in              | kr      |
| 197 | Fremont, CA                                                                           | us              | ca      |
| 198 | somewhere over the rainbow                                                            | in              |         |
| 199 | #Twitmo for tweeting too much.                                                        | br              |         |
| 200 | Compton, CA                                                                           | us              | ca      |
| 201 | Pale Blue Dot                                                                         | mm              |         |
| 202 | Pa                                                                                    | us              | pa      |
| 203 | Chico, CA                                                                             | us              | ca      |
| 204 | Inglewood, CA                                                                         | us              | ca      |
| 205 | Online                                                                                |                 | fr      |
| 206 | Worldwide                                                                             |                 | gb      |
| 207 | Hollywood, CA                                                                         | us              | ca      |
| 208 | nairobi, eastafrica                                                                   | ke              |         |
| 209 | Global                                                                                |                 | ca      |
| 210 | Monterey, CA                                                                          | us              | ca      |
| 211 | Central Florida                                                                       | us              | ve      |
| 212 | mars                                                                                  |                 | fr      |
| 213 | bed                                                                                   |                 | sk      |
| 214 | Sunnyvale, CA                                                                         | us              | ca      |
| 215 | StocksLand 💵🛢                                                                         |                 |         |
| 216 | heaven                                                                                |                 | gb      |
| 217 | San Juan, Puerto Rico                                                                 | pr              | us      |
| 218 | global                                                                                |                 | ca      |
| 219 | Huwan                                                                                 |                 | cn      |
| 220 | Land of the Free                                                                      | in              | ge      |
| 221 | EXO PLANET                                                                            |                 |         |
| 222 | Limbo                                                                                 |                 | gn      |
| 223 | The Dystopian State of America                                                        | us              |         |
| 224 | lost                                                                                  |                 | gb      |
| 225 | 🇳🇬                                                                                    |                 |         |
| 226 | v.1.1                                                                                 |                 | uz      |
| 227 | EXO Planet                                                                            |                 |         |
| 228 | Fontana, CA                                                                           | us              | ca      |
| 229 | ...                                                                                   |                 |         |
| 230 | Asgard                                                                                |                 | no      |
| 231 | Corona, CA                                                                            | us              | ca      |
| 232 | Mountain View, CA                                                                     | us              | ca      |
| 233 | Left Coast                                                                            | tz              | us      |
| 234 | JDSupra.com                                                                           | it              |         |
| 235 | Outer Space                                                                           | be              | gb      |
| 236 | Citizen of the World                                                                  | in              | tt      |
| 237 | 🇸🇬                                                                                    |                 |         |
| 238 | He/Him                                                                                |                 | ng      |
| 239 | Richmond, CA                                                                          | us              | ca      |
| 240 | Behind you                                                                            |                 | us      |
| 241 | moon                                                                                  |                 | ee      |
| 242 | Monaco                                                                                | de              | mc      |
| 243 | Columbia, MO                                                                          | co              | us      |
| 244 | Lagos                                                                                 | ng              | la      |
| 245 | wonderland                                                                            |                 | ph      |
| 246 | WorldWide                                                                             |                 | gb      |
| 247 | IL                                                                                    | us              |         |
| 248 | World                                                                                 |                 | nz      |
| 249 | Gold Coast                                                                            | gh              | au      |
| 250 | Nowhere                                                                               |                 | gb      |
| 251 | Southern hemisphere                                                                   | lk              | ca      |
| 252 | ¯\_(ツ)_/¯                                                                             | jp              | fr      |
| 253 | 757                                                                                   |                 | ru      |
| 254 | #Genève #Geneva 🇨🇭 or #Japan                                                          | jp              | ch      |
| 255 | Utopia                                                                                |                 | us      |
| 256 | active locally globally                                                               |                 |         |
| 257 | Ciudad Autónoma de Buenos Aire                                                        | us              | ar      |
| 258 | Dreamville                                                                            |                 | ph      |
| 259 | West Coast  | North America                                                           | us              |         |
| 260 | Newcastle                                                                             | za              | gb      |
| 261 | Ground Zero                                                                           |                 | nz      |
| 262 | Central Region, Singapore                                                             | np              | sg      |
| 263 | 🇮🇳                                                                                    |                 |         |
| 264 | 🇬🇧                                                                                    |                 |         |
| 265 | North Region, Singapore                                                               | sg              | se      |
| 266 | hogwarts                                                                              |                 | ke      |
| 267 | 🇮🇩                                                                                    |                 |         |
| 268 | Anfield                                                                               |                 | us      |
| 269 | ?                                                                                     |                 |         |
| 270 | space                                                                                 |                 | au      |
| 271 | D(M)V                                                                                 |                 | vn      |
| 272 | 221B Baker Street                                                                     |                 | fr      |
| 273 | 🌙                                                                                     |                 |         |
| 274 | Hope World                                                                            |                 | us      |
| 275 | Walnut Creek, CA                                                                      | us              | ca      |
| 276 | AMERICA                                                                               | us              | nl      |
| 277 | Africa                                                                                | tn              | td      |
| 278 | Mars                                                                                  |                 | fr      |
| 279 | Napa, CA                                                                              | us              | ca      |
| 280 | Cayman Islands                                                                        | ky              |         |
| 281 | Konoha                                                                                |                 | mx      |
| 282 | The Void                                                                              | in              | fr      |
| 283 | Pacific Northwest                                                                     | bj              | us      |
| 284 | Waikiki                                                                               |                 | us      |
| 285 | North London                                                                          | fr              | al      |
| 286 | Uranus                                                                                |                 | se      |
| 287 | behind you                                                                            |                 | us      |
| 288 | Borneo                                                                                |                 | id      |
| 289 | Around                                                                                |                 | ua      |
| 290 | Global- Vegas + Silicon Valley                                                        | us              |         |
| 291 | Western Pennsylvania, Greater Pittsburgh Area, Midwest, USA                           | us              |         |
| 292 | South East Asia                                                                       | bw              | gb      |
| 293 | Cascadia                                                                              |                 | us      |
| 294 | -                                                                                     |                 |         |
| 295 | Seattle, WA, USA (mostly)                                                             | us              |         |
| 296 | European Union 🇪🇺                                                                     | us              | bg      |
| 297 | internet                                                                              |                 | ht      |
| 298 | Wilayah Persekutuan Kuala Lump                                                        | my              |         |
| 299 | Conservativeland, Orange Co CA                                                        | us              |         |
| 300 | Victoria, BC                                                                          | au              | ca      |
| 301 | North Wales                                                                           | gb              | us      |
| 302 | Hayward, CA                                                                           | us              | ca      |
| 303 | On the road                                                                           | ca              | au      |
| 304 | La La Land                                                                            | us              | ls      |
| 305 | Some-Where in Canada                                                                  | ca              |         |
| 306 | Northern CA                                                                           | us              | ca      |
| 307 | idk                                                                                   | in              | id      |
| 308 | Cloud 9                                                                               |                 | us      |
| 309 | Garden Grove, CA                                                                      | us              | ca      |
| 310 | Magic Shop                                                                            |                 | ru      |
| 311 | Bethlehem, PA                                                                         | us              | br      |
| 312 | Ginninderra Creek Canberra Oz                                                         | au              |         |
| 313 | twitter                                                                               |                 | us      |
| 314 | Guam                                                                                  | gu              | us      |
| 315 | fan account                                                                           | fr              |         |
| 316 | Kashmir                                                                               | in              | pk      |
| 317 | Oz                                                                                    |                 | fr      |
| 318 | Middle Earth                                                                          |                 | us      |
| 319 | Lost in the Minnesota North Woods                                                     | us              |         |
| 320 | Terra                                                                                 |                 | cy      |
| 321 | Central Texas                                                                         | us              | bo      |
| 322 | Hell                                                                                  |                 | us      |
| 323 | 🇿🇦                                                                                    |                 |         |
| 324 | Marikina City                                                                         |                 | ph      |
| 325 | UAE                                                                                   | ae              | ua      |
| 326 | 🌎 Carpe Diem!                                                                         |                 | fr      |
| 327 | ???                                                                                   |                 |         |
| 328 | Hogwarts                                                                              |                 | ke      |
| 329 | Omnipresent                                                                           |                 |         |
| 330 | ǝʌɐ uooɯʎǝuoɥ                                                                         |                 |         |
| 331 | United States Minor Outlying I                                                        | us              |         |
| 332 | Somewhere                                                                             |                 | fr      |
| 333 | Somewhere Out There                                                                   |                 |         |
| 334 | Ph                                                                                    |                 | ph      |
| 335 | exo planet                                                                            |                 |         |
| 336 | hyderabad                                                                             | pk              | in      |
| 337 | LAGOS                                                                                 | ng              | la      |
| 338 | I'm more American than you are 🇺🇸🇺🇸🇺🇸  "Surprised to hear this" = You're a damn liar. | no              |         |
| 339 | world wide                                                                            |                 | cn      |
| 340 | Surprise, AZ                                                                          | us              | az      |
| 341 | 🌐                                                                                     |                 |         |
| 342 | 🌈                                                                                     |                 |         |
| 343 | 🏴                                                                                     |                 |         |
| 344 | ElysiumTimeIn fr all on Earth                                                         | ca              |         |
| 345 |                                                                                       |                 |         |
| 346 | Jalisco/Texas & Global                                                                | us              |         |
| 347 | Southern California                                                                   | us              | et      |
| 348 | Witness Protection                                                                    |                 |         |
| 349 | The world                                                                             | in              | nz      |
| 350 | Classified                                                                            |                 | cn      |
| 351 | 134340                                                                                |                 | es      |
| 352 | New England                                                                           | gb              | us      |
| 353 | Yorkshire and The Humber, Engl                                                        | gb              |         |
| 354 | Knowhere                                                                              |                 | us      |
| 355 | Portland                                                                              | jm              | us      |
| 356 | Central Coast, New South Wales                                                        | au              |         |
| 357 | ilkley                                                                                |                 | gb      |
| 358 | no                                                                                    |                 | no      |
| 359 | Hong Kong, My Homeland                                                                | hk              |         |
| 360 | East Africa                                                                           | np              | ca      |
| 361 | anywhere                                                                              |                 | mw      |
| 362 | D[M]V                                                                                 |                 |         |
| 363 | Thinkstan                                                                             |                 |         |
| 364 | he/they                                                                               |                 | fr      |
| 365 | pluto                                                                                 |                 | us      |
| 366 | Europe                                                                                |                 | de      |
| 367 | San Jose                                                                              | cr              | us      |
| 368 | Bedford                                                                               | gb              | us      |
| 369 | 🇺🇸                                                                                    |                 |         |
| 370 | City of Angels                                                                        |                 | us      |
| 371 | Here and there                                                                        |                 | us      |
| 372 | Azania                                                                                |                 | tz      |
| 373 | South Wales                                                                           | gb              | us      |
| 374 | Frankfurt on the Main, Germany                                                        | de              |         |
| 375 | Earth.                                                                                |                 | us      |
| 376 | exoplanet                                                                             |                 | de      |
| 377 | Bikini Bottom                                                                         |                 | vn      |
| 378 | Headquartered in Beijing, PRC                                                         | cn              |         |
| 379 | Jersey Shore                                                                          | je              | us      |
| 380 | √α. в૯α૮ђ, √¡૨g¡ท¡α                                                                   |                 |         |
| 381 | south                                                                                 | in              | kr      |
| 382 | Southern California, U.S.                                                             | us              | et      |
| 383 | europe                                                                                |                 | de      |
| 384 | Southern CA                                                                           | us              | ca      |
| 385 | Astroworld                                                                            |                 | us      |
| 386 | my bed                                                                                |                 | de      |
| 387 | Vegas                                                                                 | us              | cu      |
| 388 | Purgatory                                                                             |                 | us      |
| 389 | Disneyland                                                                            |                 | us      |
| 390 | Saturn                                                                                |                 | de      |
| 391 | Behind You                                                                            |                 | us      |
| 392 | earth                                                                                 |                 | us      |
| 393 | Nationwide                                                                            |                 | gb      |
| 394 | Fact Based World                                                                      |                 |         |
| 395 | Mountains, Lake Almanor, CA                                                           | us              |         |
| 396 | Valhalla                                                                              |                 | us      |
| 397 | 🇪🇺                                                                                    |                 |         |
| 398 | Fairfield, CA                                                                         | us              | ca      |
| 399 | San Junipero                                                                          | ml              | us      |
| 400 | North East                                                                            | in              | us      |
| 401 | 🇲🇽                                                                                    |                 |         |
| 402 | Thailand - Madagascar - Egypt                                                         | eg              |         |
| 403 | Dreamland                                                                             |                 | gb      |
| 404 | Bay Area                                                                              | pr              | us      |
| 405 | Earth, I think...                                                                     |                 |         |
| 406 | Roseville, CA                                                                         | us              | ca      |
| 407 | World Citizen                                                                         |                 | tt      |
| 408 | Westeros                                                                              |                 | de      |
| 409 | GREAT STATE OF GEORGIA / ATL                                                          | us              |         |
| 410 | universe                                                                              |                 | dk      |
| 411 | EVERYWHERE                                                                            |                 | ro      |
| 412 | magic shop                                                                            |                 | ru      |
| 413 | ☁️                                                                                    |                 | do      |
| 414 | Northern Ireland, United Kingd                                                        | gb              |         |
| 415 | KCMO                                                                                  |                 | us      |
| 416 | dmv                                                                                   |                 | us      |
| 417 | Atlantis                                                                              | za              | us      |
| 418 | West London                                                                           | in              | gb      |
| 419 | Abu Dhabi, United Arab Emirate                                                        | ae              |         |
| 420 | Isle of Man                                                                           | im              | gb      |
| 421 | Here, there, everywhere                                                               |                 |         |
| 422 | Bed                                                                                   |                 | sk      |
| 423 | 地球                                                                                    |                 | cn      |
| 424 | Milky Way Galaxy                                                                      | in              | us      |
| 425 | Lancaster, CA                                                                         | us              | ca      |
| 426 | Az                                                                                    | us              | az      |
| 427 | 🌌                                                                                     |                 |         |
| 428 | Chandigarh, IN                                                                        | us              | in      |
| 429 | Nunya                                                                                 |                 | pe      |
| 430 | Merseyside                                                                            |                 | gb      |
| 431 | CO                                                                                    | us              | co      |
| 432 | Middle of Nowhere                                                                     |                 | ca      |
| 433 | Tatooine...                                                                           |                 | us      |
| 434 | MAGA Country                                                                          |                 | es      |
| 435 | Clown World                                                                           |                 |         |
| 436 | Cagayan De Oro City, Northern                                                         | gh              | ph      |
| 437 | Home in MI & Kissimmee, FL                                                            | us              |         |
| 438 | san francisco                                                                         | ph              | us      |
| 439 | Planet earth                                                                          |                 | in      |
| 440 | Texas Hill Country                                                                    | us              | ve      |
| 441 | Tampa Bay                                                                             | pr              | us      |
| 442 | Kowloon City District                                                                 | hk              | cn      |
| 443 | New Zealand  paper.li/JUDENZ                                                          | nz              |         |
| 444 | AFRICA                                                                                | tn              | td      |
| 445 | Florida,uSA,Kingdom of Hungary                                                        | us              |         |
| 446 | somewhere                                                                             |                 | fr      |
| 447 | Nirvana                                                                               |                 | us      |
| 448 | A Pale Blue Dot                                                                       | mm              |         |
| 449 | SATX                                                                                  |                 |         |
| 450 | #DV #CSA  #Daniel_Morgan                                                              |                 |         |
| 451 | Alameda, CA                                                                           | us              | ca      |
| 452 | Greta City,   Land Of Moral Hazard, Elbonia                                           |                 |         |
| 453 | Mandaluyong City, National Cap                                                        | ph              |         |
| 454 | Nemo me impune lacessit                                                               | us              |         |
| 455 | Merica                                                                                |                 | lr      |
| 456 | Shithole, USA                                                                         | us              |         |
| 457 | atl                                                                                   | us              | co      |
| 458 | Laguna Beach, CA                                                                      | us              | ca      |
| 459 | Somewhere on earth                                                                    | ca              |         |
| 460 | Zion                                                                                  | il              | us      |
| 461 | ✈️                                                                                    |                 | do      |
| 462 | TPA and SF                                                                            | us              |         |
| 463 | Just out of Sorts                                                                     |                 |         |
| 464 | The North                                                                             | fr              | no      |
| 465 | 风下之乡、沙巴 - North Borneo . Sabah                                                        | my              |         |
| 466 | Midgard                                                                               |                 | gb      |
| 467 | 🇭🇰                                                                                    |                 |         |
| 468 | H-Town                                                                                |                 | lr      |
| 469 | Federal Capital Territory                                                             | ng              | au      |
| 470 | the moon                                                                              | in              | ee      |
| 471 | ca                                                                                    | us              | ca      |
| 472 | az                                                                                    | us              | az      |
| 473 | multifandom                                                                           |                 |         |
| 474 | Indy                                                                                  | in              | ca      |
| 475 | Cyberspace                                                                            |                 | ng      |
| 476 | European Union                                                                        | us              | bg      |
| 477 | Here & There                                                                          |                 | us      |
| 478 | outer space                                                                           | be              | gb      |
| 479 | West Midlands                                                                         | in              | gb      |
| 480 | Flyover Country                                                                       |                 | in      |
| 481 | midwest                                                                               |                 | us      |
| 482 | DC Metro Area                                                                         | us              | ph      |
| 483 | North-East Region, Singapore                                                          | sg              | se      |
| 484 | Somewhere on Earth                                                                    | ca              |         |
| 485 | 19                                                                                    |                 | fr      |
| 486 | CA Conservative turned TEXAN! Gov. Greg Abbott is the best! #MAGA                     | us              |         |
| 487 | West Coast, Best Coast 😎🌴                                                             | au              | nz      |
| 488 | Downey, CA                                                                            | us              | ca      |
| 489 | ASIA                                                                                  | ph              | ru      |
| 490 | Location                                                                              |                 | us      |
| 491 | everywhere                                                                            |                 | ro      |
| 492 | 7th ring of Hades pa.                                                                 | us              |         |
| 493 | Midwest                                                                               |                 | us      |
| 494 | Tokyo Japan                                                                           | jp              | ru      |
| 495 | Western Hemisphere                                                                    | lk              | us      |
| 496 | Plymouth                                                                              | us              | gb      |
| 497 | Broomtar’s Ohio USA                                                                   | us              |         |
| 498 | Commerce, CA                                                                          | us              | ca      |
| 499 | the void                                                                              | in              | fr      |
| 500 | Sunny Southern California                                                             | us              |         |
| 501 | State of Confusion                                                                    |                 | us      |
| 502 | The Heartland                                                                         | in              | us      |
| 503 | South East Asia                                                                       | bw              | gb      |
| 504 | Pasig City, National Capital R                                                        | pg              |         |
| 505 | ask why?                                                                              | ci              |         |
| 506 | USA, London, Asia.                                                                    | us              |         |
| 507 | TOTAL U.S. GOV'T OBLITERATION                                                         | us              |         |
| 508 | Wealth Building Newsletter                                                            |                 |         |
| 509 | Ultima Thule                                                                          |                 | us      |
| 510 | A bunker in middle America                                                            | us              |         |
| 511 | Here and There                                                                        |                 | us      |
| 512 | Banana Republic                                                                       |                 | us      |
| 513 | Undisclosed                                                                           |                 |         |
| 514 | Valenzuela City                                                                       |                 | es      |
| 515 | ÜT: 48.195723,-122.119899                                                             |                 |         |
| 516 | The Yard                                                                              | in              | us      |
| 517 | Canberra, Australian Capital T                                                        | ar              | au      |
| 518 | Nomad                                                                                 |                 | us      |
| 519 | Santa Maria, CA                                                                       | us              | ca      |
| 520 | They/Them                                                                             |                 | th      |
| 521 | Turtle Island                                                                         | is              | us      |
| 522 | Europa                                                                                |                 | de      |
| 523 | San Francisco                                                                         | ph              | us      |
| 524 | HongKong                                                                              | hk              | cn      |
| 525 | your heart                                                                            |                 | us      |
| 526 | ID                                                                                    | us              | id      |
| 527 | planet Earth                                                                          |                 | in      |
| 528 | Minas Tirith                                                                          | br              | gb      |
| 529 | Andromeda                                                                             |                 | cz      |
| 530 | SF Bay Area, CA                                                                       | us              |         |
| 531 | North Jersey                                                                          | fr              | je      |
| 532 | Suffolk                                                                               | us              | gb      |
| 533 | DTX                                                                                   |                 | in      |
| 534 | STL                                                                                   | us              | nz      |
| 535 | left coast                                                                            | tz              | us      |
| 536 | 🏔HighRockyNews RT for planet)                                                         | br              |         |
| 537 | LA, CA                                                                                | us              | ca      |
| 538 | KY & Southern California                                                              | us              |         |
| 539 | N'importe où                                                                          |                 | fr      |
| 540 | Conway, AR                                                                            | us              | ar      |
| 541 | The Earth                                                                             | in              | us      |
| 542 | IN                                                                                    | us              | in      |
| 543 | Victoria BC                                                                           | au              | ca      |
| 544 | The 3rd planet called Terra                                                           | in              |         |
| 545 | Neptune                                                                               |                 | us      |
| 546 | City of Tagum, Davao Region                                                           | ph              |         |
| 547 | PH 🇵🇭                                                                                 |                 | ph      |
| 548 | HONG KONG                                                                             | hk              | cn      |
| 549 | Western New York                                                                      | us              | sl      |
| 550 | 🇵🇭                                                                                    |                 |         |
| 551 | God's Country                                                                         |                 | us      |
| 552 | ゆっくりまったりの通り道 鍵垢さんは一言お声がけ下さい。                                                          |                 |         |
| 553 | Southeast                                                                             | bj              | se      |
| 554 | the world                                                                             | in              | nz      |
| 555 | Macau                                                                                 | mo              | cn      |
| 556 | 305                                                                                   |                 | fi      |
| 557 | Hawthorne, CA                                                                         | us              | ca      |
| 558 | Trumpland                                                                             |                 |         |
| 559 | BLIИK IN YOUR AREA                                                                    | us              |         |
| 560 | L.A.                                                                                  | us              | de      |
| 561 | Truth & Transparency                                                                  |                 |         |
| 562 | In your heart                                                                         | us              |         |
| 563 | 18                                                                                    |                 | fr      |
| 564 | Ampang, Wilayah Persekutuan Ku                                                        | my              |         |
| 565 | The World.                                                                            | in              | nz      |
| 566 | Vishakhapatnam, India                                                                 | in              |         |
| 567 | 🌎 ❤️️ เt ๏г lєคשє เt 💫👽                                                               |                 |         |
| 568 | Bay area                                                                              | pr              | us      |
| 569 | ldn                                                                                   |                 | cz      |
| 570 | Wherever,France mostly                                                                | fr              |         |
| 571 | mother earth                                                                          |                 | gb      |
| 572 | hope world                                                                            |                 | us      |
| 573 | Carson, CA                                                                            | us              | ca      |
| 574 | Puerto Rico                                                                           | pr              | us      |
| 575 | 301                                                                                   |                 | fi      |
| 576 | Columbia, MD                                                                          | co              | us      |
| 577 | Elsewhere                                                                             |                 | us      |
| 578 | iPhone: 0.000000,0.000000                                                             |                 |         |
| 579 | Somewhere out there                                                                   |                 |         |
| 580 | North Pole                                                                            | pl              |         |
| 581 | Present                                                                               |                 | za      |
| 582 | DM04                                                                                  |                 |         |
| 583 | The Milky Way                                                                         | in              | sc      |
| 584 | waterdeep city                                                                        |                 |         |
| 585 | Parallel Universe                                                                     |                 | us      |
| 586 | Alternate Universe                                                                    |                 | us      |
| 587 | Somewhere Over The Rainbow                                                            | in              |         |
| 588 | sg                                                                                    |                 | sg      |
| 589 | City of Sacraments CA                                                                 | us              |         |
| 590 | Sin City                                                                              | mx              | gb      |
| 591 | The Real World                                                                        | in              | gb      |
| 592 | Woodland, CA                                                                          | us              | ca      |
| 593 | Gold Coast, Australia                                                                 | gh              | au      |
| 594 | WNY                                                                                   |                 | sa      |
| 595 | Mordor                                                                                |                 | gb      |
| 596 | Hidden Leaf Village                                                                   |                 | us      |
| 597 | she / her                                                                             | cn              | us      |
| 598 | Martinique                                                                            | mq              | fr      |
| 599 | Vododara, India                                                                       | in              |         |
| 600 | Shadowbannia                                                                          |                 |         |
| 601 | North East Tasmania                                                                   | in              | au      |
| 602 | The Palm of God's Right Hand                                                          | in              |         |
| 603 | bahay                                                                                 |                 | ph      |
| 604 | disintegrating nation                                                                 |                 |         |
| 605 | Appalachian Mtns, TN                                                                  | us              |         |
| 606 | In your head                                                                          | us              | au      |
| 607 | SG                                                                                    |                 | sg      |
| 608 | Southern Maine                                                                        | lk              | us      |
| 609 | The Eastern Oregon outback                                                            | ke              | us      |
| 610 | Qualicum Beach                                                                        |                 | ca      |
| 611 | ✨                                                                                     |                 |         |
| 612 | 3rd Rock from the Sun                                                                 | in              | us      |
| 613 | Hyrule                                                                                |                 | gg      |
| 614 | L-1485                                                                                |                 | us      |
| 615 | Windhoek, Namibia                                                                     |                 | na      |
| 616 | Guadeloupe                                                                            | gp              | fr      |
| 617 | Danville, CA                                                                          | us              | ca      |
| 618 | Laguna Beach, Ca                                                                      | us              | ca      |
| 619 | Tatooine                                                                              |                 | us      |
| 620 | in your heart                                                                         | us              |         |
| 621 | C-137                                                                                 |                 | mx      |
| 622 | in bed                                                                                | us              | th      |
| 623 | North                                                                                 | fr              | no      |
| 624 | JHB                                                                                   | in              | za      |
| 625 | Dallas Texas                                                                          | us              | br      |
| 626 | Perry, Birmingham, Gaia                                                               | gb              |         |
| 627 | islamabad                                                                             | pk              | bd      |
| 628 | Asia Pacific                                                                          | ph              | us      |
| 629 | CA                                                                                    | us              | ca      |
| 630 | Heaven                                                                                |                 | gb      |
| 631 | IE                                                                                    |                 | ie      |
| 632 | No border.                                                                            |                 | us      |
| 633 | The Matrix                                                                            | in              | de      |
| 634 | Bali                                                                                  | id              | fr      |
| 635 | Wurundjeri Land                                                                       |                 |         |
| 636 | Camden Town, London                                                                   | us              | gb      |
| 637 | Gallifrey                                                                             |                 | gb      |
| 638 | purgatory                                                                             |                 | us      |
| 639 | America 🇺🇸                                                                            | us              | nl      |
| 640 | Pacific Shores (PST)                                                                  |                 |         |
| 641 | Earth 1                                                                               |                 | cz      |
| 642 | The Sunshine State                                                                    | us              | au      |
| 643 | Puget Sound                                                                           |                 | us      |
| 644 | NZ                                                                                    |                 | nz      |
| 645 | land of bubbles & speculators                                                         |                 |         |
| 646 | +254                                                                                  |                 | fi      |
| 647 | multi                                                                                 |                 | ec      |
| 648 | BUROKLOTARIJE                                                                         |                 |         |
| 649 | dtx                                                                                   |                 | in      |
| 650 | Chester                                                                               | us              | gb      |
| 651 | EXOPLANET                                                                             |                 | de      |
| 652 | PNW                                                                                   |                 | ir      |
| 653 | 🇦🇺                                                                                    |                 |         |
| 654 | anywhere but here                                                                     | cd              |         |
| 655 | here and there                                                                        |                 | us      |
| 656 | Stamford Bridge                                                                       | us              | gb      |
| 657 | PHL                                                                                   | th              | us      |
| 658 | Open to Expat Extraction Roles                                                        | us              |         |
| 659 | INA                                                                                   | jp              | de      |
| 660 | 🇯🇲                                                                                    |                 |         |
| 661 | 地獄                                                                                    |                 | jp      |
| 662 | 3rd rock from the sun                                                                 | in              | us      |
| 663 | #ImpeachTrump                                                                         |                 |         |
| 664 | Sint Pancras, Langedijk                                                               | pk              | nl      |
| 665 | sleeping                                                                              |                 | be      |
| 666 | KC                                                                                    |                 | fk      |
| 667 | I'm with Elvis - everywhere                                                           |                 |         |
| 668 | Del Mar, CA                                                                           | us              | ca      |
| 669 | Finding A Middle Ground Planet                                                        |                 |         |
| 670 | В путинской России пропаганда - лучшая игра.                                          | us              |         |
| 671 | #DemCastTX#DenCastCA#DemCastAZ                                                        |                 |         |
| 672 | The “Very Large Person State”                                                         | in              |         |
| 673 | Blighty                                                                               |                 | au      |
| 674 | East Yorkshire                                                                        | gb              | us      |
| 675 | honeymoon ave                                                                         |                 | us      |
| 676 | Earth, Solar System                                                                   |                 |         |
| 677 | 202                                                                                   |                 | fi      |
| 678 | somewhere on earth                                                                    | ca              |         |
| 679 | San Antonio Texas                                                                     | us              | mx      |
| 680 | Boston area                                                                           | us              | ph      |
| 681 | Ca                                                                                    | us              | ca      |
| 682 | hell                                                                                  |                 | us      |
| 683 | North Pole, AK                                                                        | pl              | us      |
| 684 | World WIde                                                                            |                 | cn      |
| 685 | Planet earth                                                                          |                 | in      |
| 686 | 🇨🇦🇺🇸                                                                                  |                 |         |
| 687 | Twin Cities                                                                           |                 | us      |
| 688 | Gen. Santos City, Soccsksargen                                                        | ph              |         |
| 689 | Bethlehem, Pa.                                                                        | us              | br      |
| 690 | Western NY                                                                            | us              | fr      |
| 691 | Santiago                                                                              | cl              | cr      |
| 692 | www.facebook.com                                                                      | it              | np      |
| 693 | Kekistan                                                                              |                 |         |
| 694 | Text RESIST to 50409                                                                  |                 |         |
| 695 | Hobbiton, Shire                                                                       |                 |         |
| 696 | warnsomegraphicphotosbadnews                                                          |                 |         |
| 697 | None                                                                                  |                 | it      |
| 698 | Matthew 24:4-31 Kjv                                                                   |                 |         |
| 699 | 163 Fountain St, Branson, MO                                                          | us              |         |
| 700 | Stranger than Dystopia                                                                | in              |         |
| 701 | DE                                                                                    | us              | de      |
| 702 | Valueinvesting                                                                        |                 |         |
| 703 | YYZ                                                                                   |                 | ca      |
| 704 | Vancouver Island                                                                      | is              | ca      |
| 705 | venus                                                                                 |                 | us      |
| 706 | she/her/hers                                                                          | cn              |         |
| 707 | If I'm not there, I'm here.                                                           | us              |         |
| 708 | secret                                                                                |                 | us      |
| 709 | South East London                                                                     | bw              | gb      |
| 710 | Echoes divinity tidal surge code 3.14                                                 |                 |         |
| 711 | yes                                                                                   | ir              | de      |
| 712 | Westlake Village, CA                                                                  | us              | ca      |
| 713 | Htx                                                                                   |                 | dk      |
| 714 | Chicago area                                                                          | us              | ph      |
| 715 | NL                                                                                    | ca              | nl      |
| 716 | Anytown, USA                                                                          | us              |         |
| 717 | Global citizen                                                                        |                 |         |
| 718 | +233                                                                                  |                 | fi      |
| 719 | milky way galaxy                                                                      | in              | us      |
| 720 | all over the place                                                                    | in              | au      |
| 721 | भारतवर्ष                                                                              | in              |         |
| 722 | WWG1WGA                                                                               |                 |         |
| 723 | Holland, MI                                                                           | nl              | us      |
| 724 | Riyadh, Kingdom of Saudi Arabi                                                        | sa              |         |
| 725 | Appalachia                                                                            |                 | us      |
| 726 | Margaritaville                                                                        |                 | us      |
| 727 | Blue Dot In Corrupted TN                                                              | us              |         |
| 728 | Galaxy                                                                                |                 | us      |
| 729 | الرياض, المملكة العربية السعود                                                        | sa              |         |
| 730 | Mana aje boleh                                                                        |                 |         |
| 731 | 919                                                                                   |                 | no      |
| 732 | NY , Luxembourg , Tunisia                                                             | us              |         |
| 733 | ❤️                                                                                    |                 | iq      |
| 734 | Rocky Mountains                                                                       |                 | us      |
| 735 | South China Sea                                                                       | cn              |         |
| 736 | The Midwest                                                                           | in              | us      |
| 737 | ur mom                                                                                |                 |         |
| 738 | satx                                                                                  |                 |         |
| 739 | International Website                                                                 |                 | fi      |
| 740 | GTA                                                                                   |                 | us      |
| 741 | Ministry of Magic, London                                                             | gb              |         |
| 742 | RT's Are FYI Purposes Only                                                            | pr              |         |
| 743 | The Great State of Texas                                                              | us              |         |
| 744 | Caloocan City, National Capita                                                        | ph              |         |
| 745 | Citizen of The World                                                                  | in              | tt      |
| 746 | Middle of nowhere                                                                     |                 | ca      |
| 747 | North Idaho                                                                           | fr              | us      |
| 748 | He/him                                                                                |                 | ng      |
| 749 | U                                                                                     |                 | it      |
| 750 | Ohio (Great Lakes area) USA                                                           | us              |         |
| 751 | Your Face                                                                             |                 | fi      |
| 752 | Kota Baharu, Kelantan                                                                 | my              |         |
| 753 | Azeroth                                                                               |                 |         |
| 754 | LV                                                                                    |                 | lv      |
| 755 | Living in a world of fools                                                            | us              |         |
| 756 | OT7                                                                                   |                 | de      |
| 757 | Middle East                                                                           | np              | us      |
| 758 | Tweets are my own and not representative of my employer                               | pr              |         |
| 759 | Right Here                                                                            |                 | us      |
| 760 | planet Earth                                                                          |                 | in      |
| 761 | Earth, Sol System.                                                                    | in              |         |
| 762 | 956                                                                                   |                 | kr      |
| 763 | All over the world                                                                    | in              | nl      |
| 764 | Long Island                                                                           | is              | ca      |
| 765 | No                                                                                    |                 | no      |
| 766 | Libs’ Nightmares                                                                      |                 |         |
| 767 | 614                                                                                   |                 | fi      |
| 768 | Living Blue in NC                                                                     | us              |         |
| 769 | South East England                                                                    | gb              | se      |
| 770 | 510                                                                                   |                 | dk      |
| 771 | vegas                                                                                 | us              | cu      |
| 772 | ma Pesije                                                                             | us              | be      |
| 773 | East coast                                                                            | nz              | sg      |
| 774 | he/him/his                                                                            |                 | fj      |
| 775 | Frozen borderland of the north                                                        | fr              |         |
| 776 | 50.984736,-114.080062                                                                 |                 | ca      |
| 777 | Somewhere Out There in WI                                                             | us              |         |
| 778 | 🇬🇭                                                                                    |                 |         |
| 779 | right here                                                                            |                 | us      |
| 780 | Right here                                                                            |                 | us      |
| 781 | East Bay, CA                                                                          | us              | ca      |
| 782 | Pasadena CA                                                                           | us              | ca      |
| 783 | New Jersey, mostly                                                                    | us              |         |
| 784 | Genesis                                                                               |                 | us      |
| 785 | Wan Chai District, Hong Kong                                                          | hk              | cn      |
| 786 | Commiefornia                                                                          |                 |         |
| 787 | Home                                                                                  |                 | de      |
| 788 | Right behind you                                                                      |                 | it      |
| 789 | under your bed                                                                        |                 |         |
| 790 | Konohagakure                                                                          |                 |         |
| 791 | Sunshine State                                                                        | us              | au      |
| 792 | #Narnia.!                                                                             |                 | it      |
| 793 | Vista, CA                                                                             | us              | ca      |
| 794 | Rio Grand Valley, NM                                                                  | br              |         |
| 795 | #nofixedaddress                                                                       |                 |         |
| 796 | The Left Coast                                                                        | in              | us      |
| 797 | ᛏᛉ                                                                                    |                 | af      |
| 798 | Nope                                                                                  |                 | tg      |
| 799 | The Bunker                                                                            | in              | us      |
| 800 | 大阪, JPN, 地球                                                                           | jp              |         |
| 801 | The Shire                                                                             | in              | mz      |
| 802 | Deep South                                                                            | in              | us      |
| 803 | 🇵🇷                                                                                    |                 |         |
| 804 | caratland                                                                             |                 |         |
| 805 | in your head                                                                          | us              | au      |
| 806 | Richmond Olympic Oval                                                                 | us              | ca      |
| 807 | 716                                                                                   |                 | tw      |
| 808 | Earth, Milky Way Galaxy                                                               | in              |         |
| 809 | Ldn                                                                                   |                 | cz      |
| 810 | Cosmos                                                                                |                 | br      |
| 811 | The Upside Down                                                                       | in              | ca      |
| 812 | Tou                                                                                   |                 | in      |
| 813 | I'm right here ...                                                                    |                 | se      |
| 814 | 🍌Republic, by 🍌 Republicans                                                           |                 |         |
| 815 | Chicago burbs                                                                         | us              |         |
| 816 | Seattle Munich Bangalore Seoul                                                        | kr              |         |
| 817 | ot7                                                                                   |                 | de      |
| 818 | in your mind                                                                          | us              | in      |
| 819 | wakanda                                                                               |                 | ss      |
| 820 | World Wide Web                                                                        |                 |         |
| 821 | Metro Detroit                                                                         | us              | ph      |
| 822 | Right behind you :)                                                                   |                 | it      |
| 823 | NoVa                                                                                  |                 | hu      |
| 824 | cloud 9                                                                               |                 | us      |
| 825 | Central Perk                                                                          | ke              | sg      |
| 826 | Manila City, National Capital                                                         | pg              | ph      |
| 827 | Alamo, CA                                                                             | us              | ca      |
| 828 | Northeast                                                                             | bj              | us      |
| 829 | El Monte, CA                                                                          | us              | pt      |
| 830 | SultanMeraki.com                                                                      | it              |         |
| 831 | Colorado & Santa Fe                                                                   | us              | br      |
| 832 | Да здесь я, и не надейтесь                                                            | ro              |         |
| 833 | Africa.                                                                               | tn              | td      |
| 834 | Hamilton Hill, Perth (WA)                                                             | us              | au      |
| 835 | The Beach                                                                             | in              | ca      |
| 836 | San Juan, PR                                                                          | ar              | br      |
| 837 | @URAnonymous1                                                                         |                 |         |
| 838 | Central California                                                                    | us              | br      |
| 839 | U.S.A.                                                                                | us              | eg      |
| 840 | north                                                                                 | fr              | no      |
| 841 | Pandemic                                                                              |                 | nz      |
| 842 | Glendale, CA                                                                          | us              | ca      |
| 843 | Straya                                                                                |                 |         |
| 844 | The Wild West                                                                         | in              | au      |
| 845 | Whidbey Island                                                                        | is              | us      |
| 846 | Loading...                                                                            |                 | au      |
| 847 | Coming for your stuff                                                                 | br              |         |
| 848 | The Resistance                                                                        | in              | fr      |
| 849 | Cornelia Street                                                                       |                 | us      |
| 850 | The Burrow                                                                            | in              | gb      |
| 851 | www                                                                                   |                 | gb      |
| 852 | 🇰🇪                                                                                    |                 |         |
| 853 | Pearl of the Orient                                                                   | in              | ph      |
| 854 | Southwest                                                                             | bf              | us      |
| 855 | dc                                                                                    | us              | co      |
| 856 | Stolen Land                                                                           |                 | au      |
| 857 | Belgian Hub                                                                           |                 | za      |
| 858 | China Grove, NC                                                                       | cn              | us      |
| 859 | The Vancouver Model #CullenIsComing                                                   | in              |         |
| 860 | None of your business                                                                 |                 |         |
| 861 | Pa.                                                                                   | us              | pa      |
| 862 | #WesternMassVoter                                                                     |                 |         |
| 863 | eileenlovercheck,webster, tx                                                          | us              |         |
| 864 | Now                                                                                   |                 | se      |
| 865 | 19qmFVMQw4PqMXXJXPYYjrmW1Y8Dge4HDP                                                    |                 |         |
| 866 | Preston                                                                               | us              | gb      |
| 867 | 💜                                                                                     |                 |         |
| 868 | Casterly Rock                                                                         | us              | vn      |
| 869 | Mysore  and  BERLIN                                                                   | in              |         |
| 870 | Global.                                                                               |                 | ca      |
| 871 | Flyover country                                                                       |                 | in      |
| 872 | Deep in the heart of Texas                                                            | us              |         |
| 873 | III% Everywhere                                                                       | ye              | ro      |
| 874 | Claremont, CA                                                                         | us              | ca      |
| 875 | South African Nomad                                                                   | in              |         |
| 876 | Republic of Namjoon                                                                   |                 |         |
| 877 | Carolina, Puerto Rico                                                                 | pr              | us      |
| 878 | MidWest                                                                               |                 | us      |
| 879 | IIUM                                                                                  |                 | my      |
| 880 | My house                                                                              |                 | id      |
| 881 | The eye of the Universe                                                               | in              |         |
| 882 | Motilal Oswal Financial                                                               |                 |         |
| 883 | 🇵🇰                                                                                    |                 |         |
| 884 | LA                                                                                    | us              |         |
| 885 | Universe                                                                              |                 | dk      |
| 886 | South Asia                                                                            | in              | ar      |
| 887 | DM(V)                                                                                 |                 | it      |
| 888 | Wet Market                                                                            | us              | ph      |
| 889 | France, USA, UK                                                                       | us              |         |
| 890 | Lothian                                                                               |                 | us      |
| 891 | Too close for comfort.                                                                | br              |         |
| 892 | Blue dot in Texas                                                                     | us              |         |
| 893 | Stretford End                                                                         | in              | gb      |
| 894 | +234                                                                                  |                 | nl      |
| 895 | NW                                                                                    |                 | no      |
| 896 | 20                                                                                    |                 | tr      |
| 897 | 🦋                                                                                     |                 |         |
| 898 | Western hemisphere                                                                    | lk              | us      |
| 899 | NotWithPsychosRunningAsylum                                                           |                 |         |
| 900 | Caribbean                                                                             |                 | ht      |
| 901 | Cyberjaya                                                                             |                 | my      |
| 902 | Wash,D.C.                                                                             | us              | bo      |
| 903 | Jamaica- Trinidad &Tobago                                                             | jm              | tt      |
| 904 | Windhoek                                                                              |                 | na      |
| 905 | Traveling                                                                             |                 | id      |
| 906 | River Avon                                                                            |                 | gb      |
| 907 | The West                                                                              | in              | ke      |
| 908 | The moon                                                                              | in              | ee      |
| 909 | 🌊                                                                                     |                 |         |
| 910 | Angus                                                                                 | gb              | fr      |
| 911 | Aruba                                                                                 | aw              | nl      |
| 912 | United State                                                                          |                 | us      |
| 913 | Concord, CA                                                                           | us              | ca      |
| 914 | 방탄소년단                                                                                 |                 |         |
| 915 | HELL                                                                                  |                 | us      |
| 916 | 210                                                                                   |                 | si      |
| 917 | Texas & I don't do TrueTwit😜                                                          | us              |         |
| 918 | St. John's                                                                            | ag              | ca      |
| 919 | Pre 97 Hong Kong ➡ 🇺🇸                                                                 | hk              | cn      |
| 920 | (she/her)                                                                             | cn              | us      |
| 921 | N.E. Florida & FL Keys                                                                | us              |         |
| 922 | The Bay                                                                               | in              | fr      |
| 923 | Red State                                                                             |                 | gb      |
| 924 | Laniakea Supercluster                                                                 |                 |         |
| 925 | Neverland                                                                             |                 | us      |
| 926 | Richmond, London                                                                      | us              | gb      |
| 927 | Kiama                                                                                 |                 | au      |
| 928 | South West                                                                            | in              | us      |
| 929 | WA for the moment.                                                                    | us              |         |
| 930 | your moms house                                                                       |                 | us      |
| 931 | OC                                                                                    |                 | tl      |
| 932 | Dark side of the moon                                                                 | in              | us      |
| 933 | Hong Kong-Beijing-Singapore                                                           | cn              |         |
| 934 | New Orleans, La./Austin, Tx.                                                          | us              |         |
| 935 | milky way                                                                             | in              | sc      |
| 936 | Lasgidi                                                                               |                 |         |
| 937 | Durham                                                                                | ca              | us      |
| 938 | 17                                                                                    |                 | fr      |
| 939 | Worldwide 🌏                                                                           |                 | gb      |
| 940 | The America's.                                                                        | us              | pe      |
| 941 | Live from Vancouver, BC 🇨🇦                                                            | ca              |         |
| 942 | Valhalla, Maui & Geneva                                                               | ch              |         |
| 943 | Yooperland                                                                            |                 |         |
| 944 | In Your Mind                                                                          | us              | in      |
| 945 | Curmudgeon Cove, Australia                                                            | au              |         |
| 946 | UNIVERSE                                                                              |                 | dk      |
| 947 | world citizen                                                                         |                 | tt      |
| 948 | Hamilton                                                                              | us              | ca      |
| 949 | Somewhere in the Good old USA!                                                        | us              |         |
| 950 | Planeta Tierra                                                                        |                 | mx      |
| 951 | Multiverse                                                                            |                 | gb      |
| 952 | WORLDWIDE                                                                             |                 | gb      |
| 953 | Earth 🌎                                                                               |                 | us      |
| 954 | Halifax                                                                               | us              | ca      |
| 955 | Marikina City, National Capita                                                        |                 |         |
| 956 | The Future                                                                            | in              | us      |
| 957 | my house                                                                              |                 | id      |
| 958 | UPLB                                                                                  |                 | ph      |
| 959 | Western US/ The Drones know                                                           | us              |         |
| 960 | Great state of Texas                                                                  | us              |         |
| 961 | Kano                                                                                  | ng              | fr      |
| 962 | Pallet Town                                                                           |                 | my      |
| 963 | he/him                                                                                |                 | ng      |
| 964 | 704                                                                                   |                 | by      |
| 965 | Hong Kong / India / UK                                                                | in              |         |
| 966 | mi casa                                                                               | us              | iq      |
| 967 | Idk                                                                                   | in              | id      |
| 968 | Paranaque City, National Capit                                                        |                 |         |
| 969 | Iowa, yes Iowa. Turn it blue.                                                         | us              |         |
| 970 | Ohlone Land                                                                           |                 |         |
| 971 | LinkedIn:                                                                             |                 | in      |
| 972 | Southeast Asia                                                                        | bj              | gb      |
| 973 | Everywhere.                                                                           |                 | ro      |
| 974 | Florida and Arizona, U.S.A.                                                           | us              |         |
| 975 | #TheResistance                                                                        |                 |         |
| 976 | winterfell                                                                            |                 | de      |
| 977 | bristol                                                                               | us              | gb      |
| 978 | GLOBAL                                                                                |                 | ca      |
| 979 | Venice, CA                                                                            | us              | ca      |
| 980 | Camp Nou                                                                              | nc              | es      |
| 981 | GRrrrrrr Bad Dawg                                                                     |                 |         |
| 982 | Eastern Time Zone                                                                     | ke              | au      |
| 983 | The DMV                                                                               | in              | us      |
| 984 | Home: the tropics                                                                     | in              | ph      |
| 985 | Northern Hemisphere                                                                   | gh              |         |
| 986 | #DeportTxIllegalAliens🇨🇱👊                                                             |                 |         |
| 987 | Valenzuela City, National Capi                                                        |                 |         |
| 988 | altrove                                                                               |                 | au      |
| 989 | where people dream of justice                                                         |                 |         |
| 990 | #Trumpville                                                                           |                 |         |
| 991 | Yes                                                                                   | ir              | de      |
| 992 | Krypton                                                                               |                 | us      |
| 993 | New Jerseyan in the PNW.                                                              | us              |         |
| 994 | saturn                                                                                |                 | de      |
| 995 | Atl                                                                                   | us              | co      |
| 996 | Fly Over States                                                                       |                 | us      |
| 997 | Auckland Central, Auckland                                                            | ke              | nz      |
| 998 | North of Nowhere                                                                      | fr              | us      |
| 999 | under these bitches skin                                                              |                 |         |
