from pydantic import BaseModel, Field
from typing import List, Optional, Union, Any
from enum import Enum, IntEnum

# All extracted Enums

class Type(Enum):
    _3 = 3


class Interval(Enum):
    _0 = 0
    _1 = 1
    _2 = 2
    _3 = 3


class Language(Enum):
    en = 'en'
    fr = 'fr'
    de = 'de'


class Holiday_fixed_credit(Enum):
    _0 = 0
    _1 = 1


class Preset(Enum):
    EMPTY = ''


class Timezone(Enum):
    Africa_Abidjan = 'Africa/Abidjan'
    Africa_Accra = 'Africa/Accra'
    Africa_Addis_Ababa = 'Africa/Addis_Ababa'
    Africa_Algiers = 'Africa/Algiers'
    Africa_Asmara = 'Africa/Asmara'
    Africa_Bamako = 'Africa/Bamako'
    Africa_Bangui = 'Africa/Bangui'
    Africa_Banjul = 'Africa/Banjul'
    Africa_Bissau = 'Africa/Bissau'
    Africa_Blantyre = 'Africa/Blantyre'
    Africa_Brazzaville = 'Africa/Brazzaville'
    Africa_Bujumbura = 'Africa/Bujumbura'
    Africa_Cairo = 'Africa/Cairo'
    Africa_Casablanca = 'Africa/Casablanca'
    Africa_Ceuta = 'Africa/Ceuta'
    Africa_Conakry = 'Africa/Conakry'
    Africa_Dakar = 'Africa/Dakar'
    Africa_Dar_es_Salaam = 'Africa/Dar_es_Salaam'
    Africa_Djibouti = 'Africa/Djibouti'
    Africa_Douala = 'Africa/Douala'
    Africa_El_Aaiun = 'Africa/El_Aaiun'
    Africa_Freetown = 'Africa/Freetown'
    Africa_Gaborone = 'Africa/Gaborone'
    Africa_Harare = 'Africa/Harare'
    Africa_Johannesburg = 'Africa/Johannesburg'
    Africa_Juba = 'Africa/Juba'
    Africa_Kampala = 'Africa/Kampala'
    Africa_Khartoum = 'Africa/Khartoum'
    Africa_Kigali = 'Africa/Kigali'
    Africa_Kinshasa = 'Africa/Kinshasa'
    Africa_Lagos = 'Africa/Lagos'
    Africa_Libreville = 'Africa/Libreville'
    Africa_Lome = 'Africa/Lome'
    Africa_Luanda = 'Africa/Luanda'
    Africa_Lubumbashi = 'Africa/Lubumbashi'
    Africa_Lusaka = 'Africa/Lusaka'
    Africa_Malabo = 'Africa/Malabo'
    Africa_Maputo = 'Africa/Maputo'
    Africa_Maseru = 'Africa/Maseru'
    Africa_Mbabane = 'Africa/Mbabane'
    Africa_Mogadishu = 'Africa/Mogadishu'
    Africa_Monrovia = 'Africa/Monrovia'
    Africa_Nairobi = 'Africa/Nairobi'
    Africa_Ndjamena = 'Africa/Ndjamena'
    Africa_Niamey = 'Africa/Niamey'
    Africa_Nouakchott = 'Africa/Nouakchott'
    Africa_Ouagadougou = 'Africa/Ouagadougou'
    Africa_Porto_Novo = 'Africa/Porto-Novo'
    Africa_Tripoli = 'Africa/Tripoli'
    Africa_Tunis = 'Africa/Tunis'
    Africa_Windhoek = 'Africa/Windhoek'
    America_Adak = 'America/Adak'
    America_Anchorage = 'America/Anchorage'
    America_Anguilla = 'America/Anguilla'
    America_Antigua = 'America/Antigua'
    America_Araguaina = 'America/Araguaina'
    America_Argentina_Buenos_Aires = 'America/Argentina/Buenos_Aires'
    America_Argentina_Catamarca = 'America/Argentina/Catamarca'
    America_Argentina_Cordoba = 'America/Argentina/Cordoba'
    America_Argentina_Jujuy = 'America/Argentina/Jujuy'
    America_Argentina_La_Rioja = 'America/Argentina/La_Rioja'
    America_Argentina_Mendoza = 'America/Argentina/Mendoza'
    America_Argentina_Rio_Gallegos = 'America/Argentina/Rio_Gallegos'
    America_Argentina_Salta = 'America/Argentina/Salta'
    America_Argentina_San_Juan = 'America/Argentina/San_Juan'
    America_Argentina_San_Luis = 'America/Argentina/San_Luis'
    America_Argentina_Tucuman = 'America/Argentina/Tucuman'
    America_Argentina_Ushuaia = 'America/Argentina/Ushuaia'
    America_Aruba = 'America/Aruba'
    America_Asuncion = 'America/Asuncion'
    America_Atikokan = 'America/Atikokan'
    America_Bahia = 'America/Bahia'
    America_Bahia_Banderas = 'America/Bahia_Banderas'
    America_Barbados = 'America/Barbados'
    America_Belem = 'America/Belem'
    America_Belize = 'America/Belize'
    America_Blanc_Sablon = 'America/Blanc-Sablon'
    America_Boa_Vista = 'America/Boa_Vista'
    America_Bogota = 'America/Bogota'
    America_Boise = 'America/Boise'
    America_Cambridge_Bay = 'America/Cambridge_Bay'
    America_Campo_Grande = 'America/Campo_Grande'
    America_Cancun = 'America/Cancun'
    America_Caracas = 'America/Caracas'
    America_Cayenne = 'America/Cayenne'
    America_Cayman = 'America/Cayman'
    America_Chicago = 'America/Chicago'
    America_Chihuahua = 'America/Chihuahua'
    America_Costa_Rica = 'America/Costa_Rica'
    America_Creston = 'America/Creston'
    America_Cuiaba = 'America/Cuiaba'
    America_Curacao = 'America/Curacao'
    America_Danmarkshavn = 'America/Danmarkshavn'
    America_Dawson = 'America/Dawson'
    America_Dawson_Creek = 'America/Dawson_Creek'
    America_Denver = 'America/Denver'
    America_Detroit = 'America/Detroit'
    America_Dominica = 'America/Dominica'
    America_Edmonton = 'America/Edmonton'
    America_Eirunepe = 'America/Eirunepe'
    America_El_Salvador = 'America/El_Salvador'
    America_Fort_Nelson = 'America/Fort_Nelson'
    America_Fortaleza = 'America/Fortaleza'
    America_Glace_Bay = 'America/Glace_Bay'
    America_Goose_Bay = 'America/Goose_Bay'
    America_Grand_Turk = 'America/Grand_Turk'
    America_Grenada = 'America/Grenada'
    America_Guadeloupe = 'America/Guadeloupe'
    America_Guatemala = 'America/Guatemala'
    America_Guayaquil = 'America/Guayaquil'
    America_Guyana = 'America/Guyana'
    America_Halifax = 'America/Halifax'
    America_Havana = 'America/Havana'
    America_Hermosillo = 'America/Hermosillo'
    America_Indiana_Indianapolis = 'America/Indiana/Indianapolis'
    America_Indiana_Knox = 'America/Indiana/Knox'
    America_Indiana_Marengo = 'America/Indiana/Marengo'
    America_Indiana_Petersburg = 'America/Indiana/Petersburg'
    America_Indiana_Tell_City = 'America/Indiana/Tell_City'
    America_Indiana_Vevay = 'America/Indiana/Vevay'
    America_Indiana_Vincennes = 'America/Indiana/Vincennes'
    America_Indiana_Winamac = 'America/Indiana/Winamac'
    America_Inuvik = 'America/Inuvik'
    America_Iqaluit = 'America/Iqaluit'
    America_Jamaica = 'America/Jamaica'
    America_Juneau = 'America/Juneau'
    America_Kentucky_Louisville = 'America/Kentucky/Louisville'
    America_Kentucky_Monticello = 'America/Kentucky/Monticello'
    America_Kralendijk = 'America/Kralendijk'
    America_La_Paz = 'America/La_Paz'
    America_Lima = 'America/Lima'
    America_Los_Angeles = 'America/Los_Angeles'
    America_Lower_Princes = 'America/Lower_Princes'
    America_Maceio = 'America/Maceio'
    America_Managua = 'America/Managua'
    America_Manaus = 'America/Manaus'
    America_Marigot = 'America/Marigot'
    America_Martinique = 'America/Martinique'
    America_Matamoros = 'America/Matamoros'
    America_Mazatlan = 'America/Mazatlan'
    America_Menominee = 'America/Menominee'
    America_Merida = 'America/Merida'
    America_Mexico_City = 'America/Mexico_City'
    America_Miquelon = 'America/Miquelon'
    America_Moncton = 'America/Moncton'
    America_Monterrey = 'America/Monterrey'
    America_Montevideo = 'America/Montevideo'
    America_Montserrat = 'America/Montserrat'
    America_Nassau = 'America/Nassau'
    America_New_York = 'America/New_York'
    America_Nome = 'America/Nome'
    America_Noronha = 'America/Noronha'
    America_North_Dakota_Beulah = 'America/North_Dakota/Beulah'
    America_North_Dakota_Center = 'America/North_Dakota/Center'
    America_North_Dakota_New_Salem = 'America/North_Dakota/New_Salem'
    America_Ojinaga = 'America/Ojinaga'
    America_Panama = 'America/Panama'
    America_Paramaribo = 'America/Paramaribo'
    America_Phoenix = 'America/Phoenix'
    America_Port_au_Prince = 'America/Port-au-Prince'
    America_Port_of_Spain = 'America/Port_of_Spain'
    America_Porto_Velho = 'America/Porto_Velho'
    America_Puerto_Rico = 'America/Puerto_Rico'
    America_Punta_Arenas = 'America/Punta_Arenas'
    America_Rankin_Inlet = 'America/Rankin_Inlet'
    America_Recife = 'America/Recife'
    America_Regina = 'America/Regina'
    America_Resolute = 'America/Resolute'
    America_Rio_Branco = 'America/Rio_Branco'
    America_Santarem = 'America/Santarem'
    America_Santiago = 'America/Santiago'
    America_Santo_Domingo = 'America/Santo_Domingo'
    America_Sao_Paulo = 'America/Sao_Paulo'
    America_Scoresbysund = 'America/Scoresbysund'
    America_Sitka = 'America/Sitka'
    America_St_Barthelemy = 'America/St_Barthelemy'
    America_St_Johns = 'America/St_Johns'
    America_St_Kitts = 'America/St_Kitts'
    America_St_Lucia = 'America/St_Lucia'
    America_St_Thomas = 'America/St_Thomas'
    America_St_Vincent = 'America/St_Vincent'
    America_Swift_Current = 'America/Swift_Current'
    America_Tegucigalpa = 'America/Tegucigalpa'
    America_Thule = 'America/Thule'
    America_Tijuana = 'America/Tijuana'
    America_Toronto = 'America/Toronto'
    America_Tortola = 'America/Tortola'
    America_Vancouver = 'America/Vancouver'
    America_Whitehorse = 'America/Whitehorse'
    America_Winnipeg = 'America/Winnipeg'
    America_Yakutat = 'America/Yakutat'
    Antarctica_Davis = 'Antarctica/Davis'
    Antarctica_DumontDUrville = 'Antarctica/DumontDUrville'
    Antarctica_Macquarie = 'Antarctica/Macquarie'
    Antarctica_Mawson = 'Antarctica/Mawson'
    Antarctica_McMurdo = 'Antarctica/McMurdo'
    Antarctica_Palmer = 'Antarctica/Palmer'
    Antarctica_Rothera = 'Antarctica/Rothera'
    Antarctica_Syowa = 'Antarctica/Syowa'
    Arctic_Longyearbyen = 'Arctic/Longyearbyen'
    Asia_Aden = 'Asia/Aden'
    Asia_Almaty = 'Asia/Almaty'
    Asia_Amman = 'Asia/Amman'
    Asia_Anadyr = 'Asia/Anadyr'
    Asia_Aqtau = 'Asia/Aqtau'
    Asia_Aqtobe = 'Asia/Aqtobe'
    Asia_Ashgabat = 'Asia/Ashgabat'
    Asia_Atyrau = 'Asia/Atyrau'
    Asia_Baghdad = 'Asia/Baghdad'
    Asia_Bahrain = 'Asia/Bahrain'
    Asia_Baku = 'Asia/Baku'
    Asia_Bangkok = 'Asia/Bangkok'
    Asia_Barnaul = 'Asia/Barnaul'
    Asia_Beirut = 'Asia/Beirut'
    Asia_Bishkek = 'Asia/Bishkek'
    Asia_Brunei = 'Asia/Brunei'
    Asia_Chita = 'Asia/Chita'
    Asia_Colombo = 'Asia/Colombo'
    Asia_Damascus = 'Asia/Damascus'
    Asia_Dhaka = 'Asia/Dhaka'
    Asia_Dili = 'Asia/Dili'
    Asia_Dubai = 'Asia/Dubai'
    Asia_Dushanbe = 'Asia/Dushanbe'
    Asia_Gaza = 'Asia/Gaza'
    Asia_Hebron = 'Asia/Hebron'
    Asia_Ho_Chi_Minh = 'Asia/Ho_Chi_Minh'
    Asia_Hong_Kong = 'Asia/Hong_Kong'
    Asia_Hovd = 'Asia/Hovd'
    Asia_Irkutsk = 'Asia/Irkutsk'
    Asia_Jakarta = 'Asia/Jakarta'
    Asia_Jayapura = 'Asia/Jayapura'
    Asia_Jerusalem = 'Asia/Jerusalem'
    Asia_Kabul = 'Asia/Kabul'
    Asia_Kamchatka = 'Asia/Kamchatka'
    Asia_Karachi = 'Asia/Karachi'
    Asia_Kathmandu = 'Asia/Kathmandu'
    Asia_Khandyga = 'Asia/Khandyga'
    Asia_Kolkata = 'Asia/Kolkata'
    Asia_Krasnoyarsk = 'Asia/Krasnoyarsk'
    Asia_Kuala_Lumpur = 'Asia/Kuala_Lumpur'
    Asia_Kuching = 'Asia/Kuching'
    Asia_Kuwait = 'Asia/Kuwait'
    Asia_Macau = 'Asia/Macau'
    Asia_Magadan = 'Asia/Magadan'
    Asia_Makassar = 'Asia/Makassar'
    Asia_Manila = 'Asia/Manila'
    Asia_Muscat = 'Asia/Muscat'
    Asia_Nicosia = 'Asia/Nicosia'
    Asia_Novokuznetsk = 'Asia/Novokuznetsk'
    Asia_Novosibirsk = 'Asia/Novosibirsk'
    Asia_Omsk = 'Asia/Omsk'
    Asia_Oral = 'Asia/Oral'
    Asia_Phnom_Penh = 'Asia/Phnom_Penh'
    Asia_Pontianak = 'Asia/Pontianak'
    Asia_Pyongyang = 'Asia/Pyongyang'
    Asia_Qatar = 'Asia/Qatar'
    Asia_Qostanay = 'Asia/Qostanay'
    Asia_Riyadh = 'Asia/Riyadh'
    Asia_Sakhalin = 'Asia/Sakhalin'
    Asia_Samarkand = 'Asia/Samarkand'
    Asia_Seoul = 'Asia/Seoul'
    Asia_Shanghai = 'Asia/Shanghai'
    Asia_Singapore = 'Asia/Singapore'
    Asia_Srednekolymsk = 'Asia/Srednekolymsk'
    Asia_Taipei = 'Asia/Taipei'
    Asia_Tashkent = 'Asia/Tashkent'
    Asia_Tbilisi = 'Asia/Tbilisi'
    Asia_Tehran = 'Asia/Tehran'
    Asia_Thimphu = 'Asia/Thimphu'
    Asia_Tokyo = 'Asia/Tokyo'
    Asia_Tomsk = 'Asia/Tomsk'
    Asia_Ulaanbaatar = 'Asia/Ulaanbaatar'
    Asia_Urumqi = 'Asia/Urumqi'
    Asia_Ust_Nera = 'Asia/Ust-Nera'
    Asia_Vientiane = 'Asia/Vientiane'
    Asia_Vladivostok = 'Asia/Vladivostok'
    Asia_Yakutsk = 'Asia/Yakutsk'
    Asia_Yangon = 'Asia/Yangon'
    Asia_Yekaterinburg = 'Asia/Yekaterinburg'
    Asia_Yerevan = 'Asia/Yerevan'
    Atlantic_Azores = 'Atlantic/Azores'
    Atlantic_Bermuda = 'Atlantic/Bermuda'
    Atlantic_Canary = 'Atlantic/Canary'
    Atlantic_Cape_Verde = 'Atlantic/Cape_Verde'
    Atlantic_Faroe = 'Atlantic/Faroe'
    Atlantic_Madeira = 'Atlantic/Madeira'
    Atlantic_Reykjavik = 'Atlantic/Reykjavik'
    Atlantic_South_Georgia = 'Atlantic/South_Georgia'
    Atlantic_St_Helena = 'Atlantic/St_Helena'
    Atlantic_Stanley = 'Atlantic/Stanley'
    Australia_Adelaide = 'Australia/Adelaide'
    Australia_Brisbane = 'Australia/Brisbane'
    Australia_Broken_Hill = 'Australia/Broken_Hill'
    Australia_Darwin = 'Australia/Darwin'
    Australia_Eucla = 'Australia/Eucla'
    Australia_Hobart = 'Australia/Hobart'
    Australia_Lindeman = 'Australia/Lindeman'
    Australia_Lord_Howe = 'Australia/Lord_Howe'
    Australia_Melbourne = 'Australia/Melbourne'
    Australia_Perth = 'Australia/Perth'
    Australia_Sydney = 'Australia/Sydney'
    Europe_Amsterdam = 'Europe/Amsterdam'
    Europe_Andorra = 'Europe/Andorra'
    Europe_Astrakhan = 'Europe/Astrakhan'
    Europe_Athens = 'Europe/Athens'
    Europe_Belgrade = 'Europe/Belgrade'
    Europe_Berlin = 'Europe/Berlin'
    Europe_Bratislava = 'Europe/Bratislava'
    Europe_Brussels = 'Europe/Brussels'
    Europe_Bucharest = 'Europe/Bucharest'
    Europe_Budapest = 'Europe/Budapest'
    Europe_Busingen = 'Europe/Busingen'
    Europe_Chisinau = 'Europe/Chisinau'
    Europe_Copenhagen = 'Europe/Copenhagen'
    Europe_Dublin = 'Europe/Dublin'
    Europe_Gibraltar = 'Europe/Gibraltar'
    Europe_Guernsey = 'Europe/Guernsey'
    Europe_Helsinki = 'Europe/Helsinki'
    Europe_Isle_of_Man = 'Europe/Isle_of_Man'
    Europe_Istanbul = 'Europe/Istanbul'
    Europe_Jersey = 'Europe/Jersey'
    Europe_Kaliningrad = 'Europe/Kaliningrad'
    Europe_Kirov = 'Europe/Kirov'
    Europe_Kyiv = 'Europe/Kyiv'
    Europe_Lisbon = 'Europe/Lisbon'
    Europe_Ljubljana = 'Europe/Ljubljana'
    Europe_London = 'Europe/London'
    Europe_Luxembourg = 'Europe/Luxembourg'
    Europe_Madrid = 'Europe/Madrid'
    Europe_Malta = 'Europe/Malta'
    Europe_Mariehamn = 'Europe/Mariehamn'
    Europe_Minsk = 'Europe/Minsk'
    Europe_Monaco = 'Europe/Monaco'
    Europe_Moscow = 'Europe/Moscow'
    Europe_Oslo = 'Europe/Oslo'
    Europe_Paris = 'Europe/Paris'
    Europe_Podgorica = 'Europe/Podgorica'
    Europe_Prague = 'Europe/Prague'
    Europe_Riga = 'Europe/Riga'
    Europe_Rome = 'Europe/Rome'
    Europe_Samara = 'Europe/Samara'
    Europe_San_Marino = 'Europe/San_Marino'
    Europe_Sarajevo = 'Europe/Sarajevo'
    Europe_Saratov = 'Europe/Saratov'
    Europe_Simferopol = 'Europe/Simferopol'
    Europe_Skopje = 'Europe/Skopje'
    Europe_Sofia = 'Europe/Sofia'
    Europe_Stockholm = 'Europe/Stockholm'
    Europe_Tallinn = 'Europe/Tallinn'
    Europe_Tirane = 'Europe/Tirane'
    Europe_Ulyanovsk = 'Europe/Ulyanovsk'
    Europe_Vaduz = 'Europe/Vaduz'
    Europe_Vatican = 'Europe/Vatican'
    Europe_Vienna = 'Europe/Vienna'
    Europe_Vilnius = 'Europe/Vilnius'
    Europe_Volgograd = 'Europe/Volgograd'
    Europe_Warsaw = 'Europe/Warsaw'
    Europe_Zagreb = 'Europe/Zagreb'
    Europe_Zurich = 'Europe/Zurich'
    Indian_Antananarivo = 'Indian/Antananarivo'
    Indian_Chagos = 'Indian/Chagos'
    Indian_Christmas = 'Indian/Christmas'
    Indian_Cocos = 'Indian/Cocos'
    Indian_Comoro = 'Indian/Comoro'
    Indian_Kerguelen = 'Indian/Kerguelen'
    Indian_Mahe = 'Indian/Mahe'
    Indian_Maldives = 'Indian/Maldives'
    Indian_Mauritius = 'Indian/Mauritius'
    Indian_Mayotte = 'Indian/Mayotte'
    Indian_Reunion = 'Indian/Reunion'
    Pacific_Apia = 'Pacific/Apia'
    Pacific_Auckland = 'Pacific/Auckland'
    Pacific_Bougainville = 'Pacific/Bougainville'
    Pacific_Chatham = 'Pacific/Chatham'
    Pacific_Chuuk = 'Pacific/Chuuk'
    Pacific_Easter = 'Pacific/Easter'
    Pacific_Efate = 'Pacific/Efate'
    Pacific_Fakaofo = 'Pacific/Fakaofo'
    Pacific_Fiji = 'Pacific/Fiji'
    Pacific_Funafuti = 'Pacific/Funafuti'
    Pacific_Galapagos = 'Pacific/Galapagos'
    Pacific_Gambier = 'Pacific/Gambier'
    Pacific_Guadalcanal = 'Pacific/Guadalcanal'
    Pacific_Guam = 'Pacific/Guam'
    Pacific_Honolulu = 'Pacific/Honolulu'
    Pacific_Kiritimati = 'Pacific/Kiritimati'
    Pacific_Kosrae = 'Pacific/Kosrae'
    Pacific_Kwajalein = 'Pacific/Kwajalein'
    Pacific_Majuro = 'Pacific/Majuro'
    Pacific_Marquesas = 'Pacific/Marquesas'
    Pacific_Midway = 'Pacific/Midway'
    Pacific_Nauru = 'Pacific/Nauru'
    Pacific_Niue = 'Pacific/Niue'
    Pacific_Norfolk = 'Pacific/Norfolk'
    Pacific_Noumea = 'Pacific/Noumea'
    Pacific_Pago_Pago = 'Pacific/Pago_Pago'
    Pacific_Palau = 'Pacific/Palau'
    Pacific_Pitcairn = 'Pacific/Pitcairn'
    Pacific_Pohnpei = 'Pacific/Pohnpei'
    Pacific_Port_Moresby = 'Pacific/Port_Moresby'
    Pacific_Rarotonga = 'Pacific/Rarotonga'
    Pacific_Saipan = 'Pacific/Saipan'
    Pacific_Tahiti = 'Pacific/Tahiti'
    Pacific_Tarawa = 'Pacific/Tarawa'
    Pacific_Tongatapu = 'Pacific/Tongatapu'
    Pacific_Wake = 'Pacific/Wake'
    Pacific_Wallis = 'Pacific/Wallis'
    UTC = 'UTC'


# All referenced schemas as Pydantic models

CollidingabsencesItem = int

Collidingabsences = List[CollidingabsencesItem]

class AbsenceCollision(BaseModel):
    collidingAbsences: Collidingabsences

AbsenceType = int

Type = List[AbsenceType]

class AbsenceCollisionError(BaseModel):
    type: Optional[Type] = Field(None, example='AbsenceCollision')
    message: Optional[Union[str, None]] = Field(None, example='An error occurred, please try again.')
    path: Optional[Union[str, None]] = None
    details: Optional[AbsenceCollision] = None

Id = int

Users_id = int

Date_since = str

Date_until = str

Count_days = float

DayAbsenceType = int

AbsenceStatus = int

class AbsenceDayAbsenceV4(BaseModel):
    id: Id
    users_id: Users_id
    date_since: Date_since
    date_until: Date_until
    type: Optional[DayAbsenceType] = Field(None, description="Only with access rights for absence administration or in case of own absences")
    status: AbsenceStatus
    note: Optional[Union[str, None]] = Field(None, description="Only with access rights for absence administration or in case of own absences")
    public_note: Optional[Union[str, None]]
    sick_note: Optional[Union[bool, None]] = Field(None, description="Only with access rights for absence administration or in case of own absences. Only for types 4 (SickSelf) and 5 (SickChild). Null in case of other absences.")
    count_days: Count_days = Field(None, description="Null in case of overtime reduction.")
    count_hours: Optional[Any] = Field(None, description="Only with access rights for absence administration or in case of own absences. Null in case of other absences.")
    date_enquired: Optional[Union[str, None]] = Field(None, description="Only with access rights for absence administration or in case of own absences")
    date_approved: Optional[Union[str, None]] = Field(None, description="Only with access rights for absence administration or in case of own absences")
    approved_by: Optional[Union[int, None]] = Field(None, description="Only with access rights for absence administration or in case of own absences")

class AbsenceHasToBeDeclinedError(BaseModel):
    type: Optional[Type] = Field(None, example='AbsenceHasToBeDeclined')
    message: Optional[Union[str, None]] = Field(None, example='The absence has to be declined first.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Count_hours = float

HourAbsenceType = int

class AbsenceHourAbsenceV4(BaseModel):
    id: Id
    users_id: Users_id
    date_since: Date_since
    date_until: Date_until
    type: Optional[HourAbsenceType] = Field(None, description="Only with access rights for absence administration or in case of own absences")
    status: AbsenceStatus
    note: Optional[Union[str, None]] = Field(None, description="Only with access rights for absence administration or in case of own absences")
    public_note: Optional[Union[str, None]]
    sick_note: Optional[Union[bool, None]] = Field(None, description="Only with access rights for absence administration or in case of own absences. Only for types 4 (SickSelf) and 5 (SickChild). Null in case of other absences.")
    count_days: Count_days = Field(None, description="Null in case of overtime reduction.")
    count_hours: Optional[Count_hours] = Field(None, description="Only with access rights for absence administration or in case of own absences. Null in case of other absences.")
    date_enquired: Optional[Union[str, None]] = Field(None, description="Only with access rights for absence administration or in case of own absences")
    date_approved: Optional[Union[str, None]] = Field(None, description="Only with access rights for absence administration or in case of own absences")
    approved_by: Optional[Union[int, None]] = Field(None, description="Only with access rights for absence administration or in case of own absences")

AbsenceScope = str

AbsenceV4 = Union[AbsenceHourAbsenceV4, AbsenceDayAbsenceV4]

Name = str

Users_idsItem = int

Users_ids = List[Any]

Company_default = bool

class AccessGroupV2(BaseModel):
    id: Id = Field(None, example=10)
    name: Name = Field(None, example='Marketing')
    users_ids: Optional[Users_ids] = Field(None, description="IDs of the access group members", example=[1])
    has_elevated_access: Optional[Union[bool, None]] = Field(None, description="The access group contains elevated access. `null` in case of disabled project times module.")
    has_master_data_access: Optional[Union[bool, None]] = Field(None, description="The access group contains master data access (customers, projects, services). `null` in case of disabled project times module.")
    company_default: Company_default = Field(None, description="The access group is one of the company default access groups.")

AccessType = str

ApiAccessGroupsServicesGeneralV2_AccessTypeForPut = str

ApiAccessGroupsServicesV2_AccessTypeForPut = str

AccessValue = int

ApiAccessGroupsProjectsV2_AccessValueForPut = int

ApiAccessGroupsServicesV2_AccessValueForPut = int

Weekly_max = float

Interval_max = float

Add_to_worktime = bool

Daily_max = float

class WorkTimeRegulationV3(BaseModel):
    id: Id = Field(None, example=10)
    name: Optional[Name] = Field(None, description="Only visible for owners or workers with elevated access `manage_users_work_time_settings`", example='Germany')
    add_to_worktime: Add_to_worktime = Field(None, example=False)
    daily_max: Daily_max = Field(None, example=10)
    weekly_max: Weekly_max = Field(None, example=60)
    interval_max: Interval_max = Field(None, example=6)

Worktime_regulation = Union[WorkTimeRegulationV3, Any]

Support_pin = str

Email = str

Timezone = str

Can_generally_see_absences = bool

Active = bool

Role = str

Timeformat_12h = bool

Absence_managers_idItem = int

Absence_managers_id = List[Absence_managers_idItem]

Can_generally_manage_absences = bool

Default_holidays_count = bool

Default_target_hours = bool

WorkTimeEditLockDay = int

Work_time_edit_lock_days = Union[WorkTimeEditLockDay, Any]

Language = str

Can_add_customers = bool

EditLockDay = int

Edit_lock_dyn = Union[EditLockDay, Any]

WageType = int

Wage_type = Union[WageType, Any]

class UserV1(BaseModel):
    id: Id
    name: Optional[Union[str, None]]
    number: Optional[Union[str, None]] = None
    email: Optional[Email] = None
    role: Optional[Role] = None
    active: Active
    timeformat_12h: Timeformat_12h
    weekstart_monday: Optional[Union[bool, None]]
    weekend_friday: Optional[Union[bool, None]]
    language: Language
    timezone: Timezone
    wage_type: Optional[Wage_type] = None
    can_generally_see_absences: Optional[Can_generally_see_absences] = None
    can_generally_manage_absences: Optional[Can_generally_manage_absences] = None
    can_add_customers: Optional[Can_add_customers] = None
    worktime_regulation_id: Optional[Union[int, None]] = None
    teams_id: Optional[Union[int, None]]
    initials: Optional[Union[str, None]]
    nonbusinessgroups_id: Optional[Union[int, None]]
    boss: Optional[Union[int, None]] = None
    absence_managers_id: Optional[Absence_managers_id] = None
    default_holidays_count: Optional[Default_holidays_count] = None
    default_target_hours: Optional[Default_target_hours] = None
    edit_lock: Optional[Union[str, None]] = None
    edit_lock_dyn: Optional[Edit_lock_dyn] = None
    edit_lock_sync: Optional[Union[bool, None]] = None
    work_time_edit_lock_days: Optional[Work_time_edit_lock_days] = None
    creator: Optional[Union[int, None]] = None
    support_pin: Optional[Support_pin] = None

Allow_entry_overlaps = bool

Compensate_month_default = float

Holidays_count_default = float

Module_work_time = bool

Compensate_day_default = float

Onboarding_complete = bool

Force_linked_entry_times = bool

Module_absence = bool

Module_target_hours = bool

Allow_entries_text_multiline = bool

Wednesday = float

Friday = float

Sunday = float

Saturday = float

Monday = float

Tuesday = float

Thursday = float

class CompanyTargetHoursDefaultNodeV1(BaseModel):
    monday: Monday
    tuesday: Tuesday
    wednesday: Wednesday
    thursday: Thursday
    friday: Friday
    saturday: Saturday
    sunday: Sunday

Worktime_force_breaks = int

Allow_entries_for_customers = bool

Module_user_reports = bool

Timezone_default = str

Module_userreports = bool

Module_project_times = bool

Module_targethours = bool

Module_entries_texts = bool

Absence_reduces_target_hours = bool

class CompanyV1(BaseModel):
    id: Id
    name: Name
    timezone_default: Timezone_default
    currency: Optional[Union[str, None]]
    allow_entries_text_multiline: Allow_entries_text_multiline
    allow_entries_for_customers: Allow_entries_for_customers
    allow_entry_overlaps: Allow_entry_overlaps
    force_linked_entry_times: Force_linked_entry_times
    default_customers_id: Optional[Union[int, None]]
    default_services_id: Optional[Union[int, None]]
    module_absence: Module_absence
    module_work_time: Module_work_time
    module_targethours: Module_targethours
    module_target_hours: Module_target_hours
    module_userreports: Module_userreports
    module_user_reports: Module_user_reports
    module_project_times: Module_project_times
    module_entries_texts: Module_entries_texts
    nonbusiness_group_default: Optional[Union[int, None]]
    onboarding_complete: Onboarding_complete
    worktime_regulation_default: Optional[Union[int, None]]
    worktime_evaluate_regulations_since: Optional[Union[str, None]]
    worktime_force_breaks: Worktime_force_breaks
    holidays_count_default: Holidays_count_default
    absence_reduces_target_hours: Absence_reduces_target_hours
    compensate_day_default: Compensate_day_default
    compensate_month_default: Compensate_month_default
    target_hours_default: CompanyTargetHoursDefaultNodeV1

class AggregatesUsersMeV2(BaseModel):
    user: UserV1
    company: CompanyV1
    worktime_regulation: Worktime_regulation

Allowedvalues = List[Any]

class AllowedValues(BaseModel):
    allowedValues: Allowedvalues

class AllSubprojectsMustBeCompletedError(BaseModel):
    type: Optional[Type] = Field(None, example='AllSubprojectsMustBeCompleted')
    message: Optional[Union[str, None]] = Field(None, example='All subprojects must be completed before the parent project can be completed.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class ApiAbsencesV4Errors_ErrorModel(BaseModel):
    pass

class ApiAbsencesV4Errors(BaseModel):
    error: ApiAbsencesV4Errors_ErrorModel

class ApiAccessGroupsCustomersGeneralV2Errors_ErrorModel(BaseModel):
    pass

class ApiAccessGroupsCustomersGeneralV2Errors(BaseModel):
    error: ApiAccessGroupsCustomersGeneralV2Errors_ErrorModel

class ApiAccessGroupsServicesGeneralV2Errors_ErrorModel(BaseModel):
    pass

class ApiAccessGroupsServicesGeneralV2Errors(BaseModel):
    error: ApiAccessGroupsServicesGeneralV2Errors_ErrorModel

class ApiAccessGroupsV2Errors_ErrorModel(BaseModel):
    pass

class ApiAccessGroupsV2Errors(BaseModel):
    error: ApiAccessGroupsV2Errors_ErrorModel

class ApiCustomersV3Errors_ErrorModel(BaseModel):
    pass

class ApiCustomersV3Errors(BaseModel):
    error: ApiCustomersV3Errors_ErrorModel

Message = str

class ApiErrors(BaseModel):
    type: Optional[Type] = Field(None, description="Unique identifier of the error", example='General')
    message: Optional[Message] = Field(None, description="Textual error description", example='The requested resource could not be found.')
    details: Optional[Union[Any, None]] = Field(None, description="Additional error details if necessary", example=None)
    path: Optional[Union[str, None]] = None

class ApiHolidaysCarryV3Errors_ErrorModel(BaseModel):
    pass

class ApiHolidaysCarryV3Errors(BaseModel):
    error: ApiHolidaysCarryV3Errors_ErrorModel

class ApiHolidaysQuotaV2Errors_ErrorModel(BaseModel):
    pass

class ApiHolidaysQuotaV2Errors(BaseModel):
    error: ApiHolidaysQuotaV2Errors_ErrorModel

class ApiLumpSumServicesV4Errors_ErrorModel(BaseModel):
    pass

class ApiLumpSumServicesV4Errors(BaseModel):
    error: ApiLumpSumServicesV4Errors_ErrorModel

class ApiNonbusinessDaysV2Errors_ErrorModel(BaseModel):
    pass

class ApiNonbusinessDaysV2Errors(BaseModel):
    error: ApiNonbusinessDaysV2Errors_ErrorModel

class ApiNonbusinessGroupsV2Errors_ErrorModel(BaseModel):
    pass

class ApiNonbusinessGroupsV2Errors(BaseModel):
    error: ApiNonbusinessGroupsV2Errors_ErrorModel

class ApiOvertimeCarryV3Errors_ErrorModel(BaseModel):
    pass

class ApiOvertimeCarryV3Errors(BaseModel):
    error: ApiOvertimeCarryV3Errors_ErrorModel

class ApiOvertimeReductionsV3Errors_ErrorModel(BaseModel):
    pass

class ApiOvertimeReductionsV3Errors(BaseModel):
    error: ApiOvertimeReductionsV3Errors_ErrorModel

class ApiProjectsV4Errors_ErrorModel(BaseModel):
    pass

class ApiProjectsV4Errors(BaseModel):
    error: ApiProjectsV4Errors_ErrorModel

class ApiServicesV4Errors_ErrorModel(BaseModel):
    pass

class ApiServicesV4Errors(BaseModel):
    error: ApiServicesV4Errors_ErrorModel

class ApiSubprojectsV3Errors_ErrorModel(BaseModel):
    pass

class ApiSubprojectsV3Errors(BaseModel):
    error: ApiSubprojectsV3Errors_ErrorModel

class ApiTeamsV3Errors_ErrorModel(BaseModel):
    pass

class ApiTeamsV3Errors(BaseModel):
    error: ApiTeamsV3Errors_ErrorModel

class ApiUsersNonbusinessGroupsV3Errors_ErrorModel(BaseModel):
    pass

class ApiUsersNonbusinessGroupsV3Errors(BaseModel):
    error: ApiUsersNonbusinessGroupsV3Errors_ErrorModel

class ApiUsersV3Errors_ErrorModel(BaseModel):
    pass

class ApiUsersV3Errors(BaseModel):
    error: ApiUsersV3Errors_ErrorModel

class ArchiveCompanyDefaultIsNotAllowedError(BaseModel):
    type: Optional[Type] = Field(None, example='ArchiveCompanyDefaultIsNotAllowed')
    message: Optional[Union[str, None]] = Field(None, example='It is not allowed to archive an item which is company default.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

BillableDistinct = int

Billable = Union[BillableDistinct, Any]

class BilledCanOnlyBeSetWithHourBudgetError(BaseModel):
    type: Optional[Type] = Field(None, example='BilledCanOnlyBeSetWithHourBudget')
    message: Optional[Union[str, None]] = Field(None, example='Field can only be set for projects with hours as budget. Otherwise it is determined automatically based on the billed amount.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class BilledMoneyCanOnlyBeSetWithHardBudgetError(BaseModel):
    type: Optional[Type] = Field(None, example='BilledMoneyCanOnlyBeSetWithHardBudget')
    message: Optional[Union[str, None]] = Field(None, example="The project does not have a hard budget so that the billed amount can't be set. You have to set the single entries to billed.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Elevated_access_dependenciesItem = str

Elevated_access_dependencies = List[Elevated_access_dependenciesItem]

Access_name = str

class BlockingAccessDependencies(BaseModel):
    access_name: Access_name = Field(None, description="The access you were trying to remove", example='see_absences')
    elevated_access_dependencies: Optional[Elevated_access_dependencies] = Field(None, description="Elevated access dependencies that are blocking", example=['see_work_time', 'manage_work_time'])

class BlockingAccessDependenciesError(BaseModel):
    type: Optional[Type] = Field(None, example='BlockingAccessDependencies')
    message: Optional[Union[str, None]] = Field(None, example='Blocking dependencies need to be removed beforehand.')
    path: Optional[Union[str, None]] = None
    details: Optional[BlockingAccessDependencies] = None

class BossCannotBeArchivedError(BaseModel):
    type: Optional[Type] = Field(None, example='BossCannotBeArchived')
    message: Optional[Union[str, None]] = Field(None, example='Users who are bosses or team leaders cannot be archived.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Hard = bool

From_subprojects = bool

Thresholds = int

Notification_thresholds = List[Thresholds]

Monetary = bool

class SubprojectBudgetV3(BaseModel):
    monetary: Monetary
    hard: Hard
    from_subprojects: From_subprojects
    amount: Optional[Union[float, None]]
    notification_thresholds: Notification_thresholds

Budget = Union[SubprojectBudgetV3, Any]

class BudgetIsRequiredForRetainerProjectError(BaseModel):
    type: Optional[Type] = Field(None, example='BudgetIsRequiredForRetainerProject')
    message: Optional[Union[str, None]] = Field(None, example='Budget is required for retainer projects.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

BudgetOption = str

BudgetSource = int

Min = float

Max = float

Inclusive = bool

class NotBetween(BaseModel):
    min: Min = Field(None, example=0)
    max: Max = Field(None, example=10000)
    inclusive: Inclusive = Field(None, description="Are the minimum and maximum values allowed", example=True)

class BudgetTotalBelowSubprojectBudgetSumError(BaseModel):
    type: Optional[Type] = Field(None, example='BudgetTotalBelowSubprojectBudgetSum')
    message: Optional[Union[str, None]] = Field(None, example='The project budget may not fall below the total budget of all subprojects.')
    path: Optional[Union[str, None]] = None
    details: Optional[NotBetween] = None

Budget_is_hours = bool

class BudgetTotalErrorDetails(BaseModel):
    max: Max = Field(None, example=10000)
    budget_is_hours: Budget_is_hours = Field(None, example=True)

class BudgetTotalError(BaseModel):
    type: Optional[Type] = Field(None, example='BudgetTotal')
    message: Optional[Union[str, None]] = Field(None, example='The total budget of all subprojects may not exceed the project budget.')
    path: Optional[Union[str, None]] = None
    details: Optional[BudgetTotalErrorDetails] = None

class BudgetTotalExceedsAbsoluteMaximumError(BaseModel):
    type: Optional[Type] = Field(None, example='BudgetTotalExceedsAbsoluteMaximum')
    message: Optional[Union[str, None]] = Field(None, example='The total budget of all subprojects may not exceed the threshold of 99999999.')
    path: Optional[Union[str, None]] = None
    details: Optional[NotBetween] = None

class CannotChangeBudgetCommitmentBecauseOfCompletedSubprojectsError(BaseModel):
    type: Optional[Type] = Field(None, example='CannotChangeBudgetCommitmentBecauseOfCompletedSubprojects')
    message: Optional[Union[str, None]] = Field(None, example='You cannot change the budget commitment as long as there are completed subprojects.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class CannotChangeBudgetSourceBecauseOfSubprojectsError(BaseModel):
    type: Optional[Type] = Field(None, example='BudgetSourceIsNotChangedFromIntervalWhenSubprojectsExist')
    message: Optional[Union[str, None]] = Field(None, example='You cannot change the budget source of interval projects as long as there are subprojects.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class CannotChangeBudgetSourceForBilledIntervalProjectsError(BaseModel):
    type: Optional[Type] = Field(None, example='CannotChangeBudgetSourceForBilledIntervalProjectsError')
    message: Optional[Union[str, None]] = Field(None, example='You cannot change the budget type to interval for projects that have (partially) billed entries.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class CannotChangeBudgetTypeBecauseOfSubprojectsError(BaseModel):
    type: Optional[Type] = Field(None, example='CannotChangeBudgetTypeBecauseOfSubprojects')
    message: Optional[Union[str, None]] = Field(None, example='You cannot change the budget type (hard / should-be value and money / time) as long as there are subprojects.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class CannotManageAbsencesOfUserError(BaseModel):
    type: Optional[Type] = Field(None, description="Fehler, wenn Rechte fehlen, um die Abwesenheiten eines Users zu verwalten", example='CannotManageAbsencesOfUser')
    message: Optional[Union[str, None]] = Field(None, example='An error occurred, please try again.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class CannotModifyDemoDataError(BaseModel):
    type: Optional[Type] = Field(None, example='CannotModifyDemoData')
    message: Optional[Union[str, None]] = Field(None, example='You must not edit demo data.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class CannotRemoveBudgetBecauseOfSubprojectBudgetsError(BaseModel):
    type: Optional[Type] = Field(None, example='CannotRemoveBudgetBecauseOfSubprojectBudgets')
    message: Optional[Union[str, None]] = Field(None, example='You cannot remove the budget as long as there are subprojects with budgets.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

ChangeRequestIntervalType = int

ChangeRequestStatus = int

Time_insert = str

Users_name = str

Clocked = bool

Time_last_change = str

Time_since = str

Services_name = str

Customers_id = int

Time_last_change_work_time = str

Hourly_rate = float

Test_data = bool

Customers_name = str

Revenue = float

Clocked_offline = bool

class EntryV2Time(BaseModel):
    id: Id = Field(None, example=10)
    customers_id: Customers_id = Field(None, example=10)
    projects_id: Optional[Union[int, None]]
    subprojects_id: Optional[Union[int, None]]
    users_id: Users_id
    billable: Billable
    texts_id: Optional[Union[int, None]]
    text: Optional[Union[str, None]] = Field(None, description="Only if enhanced_list=true")
    time_since: Time_since = Field(None, example='2023-02-28T00:00:00Z')
    time_until: Optional[Union[str, None]] = Field(None, example='2023-02-28T00:00:00Z')
    time_insert: Time_insert = Field(None, example='2023-02-28Z00:00:00Z')
    time_last_change: Time_last_change = Field(None, example='2023-02-28T00:00:00Z')
    test_data: Test_data
    customers_name: Optional[Customers_name] = Field(None, description="Only if enhanced_list=true", example='Hotel Bergblick')
    projects_name: Optional[Union[str, None]] = Field(None, description="Only if enhanced_list=true", example='Publicity campaign')
    subprojects_name: Optional[Union[str, None]] = Field(None, description="Only if enhanced_list=true", example='Social media ads')
    users_name: Optional[Users_name] = Field(None, description="Only if enhanced_list=true", example='Max Mustermann')
    revenue: Optional[Revenue] = Field(None, description="Only with necessary access rights and if enhanced_list=true", example=999.9)
    type: Type = Field(None, description="Entry type: 1 = time, 2 = lump sum service, 3 = lump sum value.")
    services_id: Optional[Union[int, None]]
    duration: Optional[Union[int, None]]
    time_last_change_work_time: Time_last_change_work_time = Field(None, example='2023-02-28T00:00:00Z')
    time_clocked_since: Optional[Union[str, None]] = Field(None, example='2023-02-28T00:00:00Z')
    clocked: Clocked
    clocked_offline: Clocked_offline
    hourly_rate: Optional[Hourly_rate] = Field(None, description="Only with necessary access rights and if enhanced_list=true", example=99.99)
    services_name: Optional[Services_name] = Field(None, description="Only if enhanced_list=true", example='SEO service')

Lumpsum = float

class EntryV2LumpsumValue(BaseModel):
    id: Id = Field(None, example=10)
    customers_id: Customers_id = Field(None, example=10)
    projects_id: Optional[Union[int, None]]
    subprojects_id: Optional[Union[int, None]]
    users_id: Users_id
    billable: Billable
    texts_id: Optional[Union[int, None]]
    text: Optional[Union[str, None]] = Field(None, description="Only if enhanced_list=true")
    time_since: Time_since = Field(None, example='2023-02-28T00:00:00Z')
    time_until: Optional[Union[str, None]] = Field(None, example='2023-02-28T00:00:00Z')
    time_insert: Time_insert = Field(None, example='2023-02-28Z00:00:00Z')
    time_last_change: Time_last_change = Field(None, example='2023-02-28T00:00:00Z')
    test_data: Test_data
    customers_name: Optional[Customers_name] = Field(None, description="Only if enhanced_list=true", example='Hotel Bergblick')
    projects_name: Optional[Union[str, None]] = Field(None, description="Only if enhanced_list=true", example='Publicity campaign')
    subprojects_name: Optional[Union[str, None]] = Field(None, description="Only if enhanced_list=true", example='Social media ads')
    users_name: Optional[Users_name] = Field(None, description="Only if enhanced_list=true", example='Max Mustermann')
    revenue: Optional[Revenue] = Field(None, description="Only with necessary access rights and if enhanced_list=true", example=999.9)
    type: Type = Field(None, description="Entry type: 1 = time, 2 = lump sum value, 3 = lump sum service.")
    services_id: Optional[Union[int, None]]
    lumpsum: Lumpsum = Field(None, example=99.99)
    services_name: Optional[Services_name] = Field(None, description="Only if enhanced_list=true", example='SEO service')

Lumpsum_services_price = float

Lumpsum_services_amount = float

class EntryV2LumpsumService(BaseModel):
    id: Id = Field(None, example=10)
    customers_id: Customers_id = Field(None, example=10)
    projects_id: Optional[Union[int, None]]
    subprojects_id: Optional[Union[int, None]]
    users_id: Users_id
    billable: Billable
    texts_id: Optional[Union[int, None]]
    text: Optional[Union[str, None]] = Field(None, description="Only if enhanced_list=true")
    time_since: Time_since = Field(None, example='2023-02-28T00:00:00Z')
    time_until: Optional[Union[str, None]] = Field(None, example='2023-02-28T00:00:00Z')
    time_insert: Time_insert = Field(None, example='2023-02-28Z00:00:00Z')
    time_last_change: Time_last_change = Field(None, example='2023-02-28T00:00:00Z')
    test_data: Test_data
    customers_name: Optional[Customers_name] = Field(None, description="Only if enhanced_list=true", example='Hotel Bergblick')
    projects_name: Optional[Union[str, None]] = Field(None, description="Only if enhanced_list=true", example='Publicity campaign')
    subprojects_name: Optional[Union[str, None]] = Field(None, description="Only if enhanced_list=true", example='Social media ads')
    users_name: Optional[Users_name] = Field(None, description="Only if enhanced_list=true", example='Max Mustermann')
    revenue: Optional[Revenue] = Field(None, description="Only with necessary access rights and if enhanced_list=true", example=999.9)
    type: Type = Field(None, description="Entry type: 1 = time, 2 = lump sum service, 3 = lump sum value.")
    services_name: Optional[Services_name] = Field(None, description="Only if enhanced_list=true", example='SEO service')
    lumpsum_services_id: Optional[Union[int, None]]
    lumpsum_services_amount: Lumpsum_services_amount = Field(None, example=99.99)
    lumpsum_services_price: Optional[Lumpsum_services_price] = Field(None, description="Only if enhanced_list=true", example=99.99)

EntryV2 = Union[EntryV2Time, EntryV2LumpsumValue, EntryV2LumpsumService]

ClockStartStopV2_RunningModel = Union[EntryV2, Any]

ClockStartStopV2_StoppedModel = Union[EntryV2, Any]

Current_time = str

Stopped_has_been_truncated = bool

Additional_message = str

class ClockStartStopV2(BaseModel):
    running: ClockStartStopV2_RunningModel
    stopped: ClockStartStopV2_StoppedModel
    current_time: Current_time = Field(None, example='2023-02-28T00:00:00Z')
    stopped_has_been_truncated: Stopped_has_been_truncated
    additional_message: Optional[Additional_message] = None

ClockV2_RunningModel = Union[EntryV2, Any]

ClockV2_StoppedModel = Union[EntryV2, Any]

class ClockV2(BaseModel):
    running: ClockV2_RunningModel
    stopped: ClockV2_StoppedModel
    current_time: Current_time = Field(None, example='2023-02-28T00:00:00Z')

class CompletionIsForbiddenBySubprojectBudgetError(BaseModel):
    type: Optional[Type] = Field(None, example='CompletionIsForbiddenBySubprojectBudget')
    message: Optional[Union[str, None]] = Field(None, example="Project-completion is forbidden as the subprojects's budget sum does not match the project's budget.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class CompletionIsForbiddenBySubprojectCompletionError(BaseModel):
    type: Optional[Type] = Field(None, example='CompletionIsForbiddenBySubprojectCompletion')
    message: Optional[Union[str, None]] = Field(None, example='Project-completion is forbidden as subprojects are completed partly.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Inactive = int

class CustomerCountProjectsV3(BaseModel):
    customers_id: Customers_id = Field(None, example=10)
    active: Active = Field(None, example=504)
    inactive: Inactive = Field(None, example=27)

class custom_access_v2(BaseModel):
    pass

Billable_default = bool

CustomerColor = int

class CustomerV3(BaseModel):
    id: Id = Field(None, example=10)
    name: Name = Field(None, example='Hotel Bergblick')
    number: Optional[Union[str, None]] = Field(None, description="Freely selectable number for the customer", example='10')
    color: CustomerColor
    active: Active
    billable_default: Billable_default
    note: Optional[Union[str, None]] = Field(None, description="Only visible for owners or workers with elevated access `manage_customers_and_projects`", example='This customer is important for us')
    bill_service_id: Optional[Union[str, None]] = Field(None, description="Only visible for owners or workers with elevated access `manage_customers_and_projects` and if a billing application with customers support is linked up", example='1234')
    test_data: Test_data

Hasaccess = bool

class UsersAccessServiceRestrictedAccessV2(BaseModel):
    id: Id
    hasAccess: Hasaccess

AddSub = List[UsersAccessServiceRestrictedAccessV2]

Add = Union[AddSub, AddSub]

general_access_v2 = bool

Report = Union[general_access_v2, custom_access_v2]

Edit = Union[general_access_v2, custom_access_v2]

class customer_projects_access_v2(BaseModel):
    add: Optional[Add] = Field(None, example=True)
    report: Optional[Report] = Field(None, example={'123': True, '456': True})
    edit: Optional[Edit] = Field(None, example={'123': True, '456': {'projects': {'789': True}}})

CustomerProjectScope = str

class DeleteCompanyDefaultIsNotAllowedError(BaseModel):
    type: Optional[Type] = Field(None, example='DeleteCompanyDefaultIsNotAllowed')
    message: Optional[Union[str, None]] = Field(None, example='It is not allowed to delete a resource which is company default.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class DuplicateEntryForUserAndYearError(BaseModel):
    type: Optional[Type] = Field(None, example='DuplicateEntryForUserAndYear')
    message: Optional[Union[str, None]] = Field(None, example='A resource has already been defined for this user and year.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

ClockDurationV2_RunningModel = Union[EntryV2, Any]

Overlapping = bool

class Overlapping_correction(BaseModel):
    overlapping: Overlapping = Field(None, example=True)
    overlapping_free_time_since: Optional[Union[str, None]] = Field(None, example='2023-02-28T00:00:00Z')
    truncate_previous_entry: Optional[Union[int, None]] = Field(None, example=1)

class ClockDurationV2(BaseModel):
    updated: EntryV2
    running: ClockDurationV2_RunningModel
    overlapping_correction: Optional[Overlapping_correction]
    current_time: Current_time = Field(None, example='2023-02-28T00:00:00Z')

ResourcesItem = str

Resources = List[ResourcesItem]

class Resource(BaseModel):
    resources: Resources = Field(None, description="One or more affected resources", example=['customers', 'users'])

class EmailNotAvailableError(BaseModel):
    type: Optional[Type] = Field(None, example='EmailNotAvailable')
    message: Optional[Union[str, None]] = Field(None, example='Email is not available.')
    path: Optional[Union[str, None]] = None
    details: Optional[Resource] = None

Value = str

class EmptyError(BaseModel):
    type: Optional[Type] = Field(None, example='Empty')
    message: Optional[Union[str, None]] = Field(None, example='Value is required and cannot be empty.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class EndBeforeStartError(BaseModel):
    type: Optional[Type] = Field(None, example='EndBeforeStart')
    message: Optional[Union[str, None]] = Field(None, example='An error occurred, please try again.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Label = str

class entriesText_v3(BaseModel):
    id: Id = Field(None, example=10)
    label: Label = Field(None, example='test')
    value: Value = Field(None, example='test')

Confirm_key = str

Affected_entries = int

class EntryGroupConfirmUpdateV2(BaseModel):
    confirm_key: Confirm_key
    affected_entries: Affected_entries

class EntryGroupNoRestrictionV2(BaseModel):
    pass

class EntryGroupRestrictionV2(BaseModel):
    users_id: Optional[Union[int, None]]
    teams_id: Optional[Union[int, None]]
    customers_id: Optional[Union[int, None]]
    projects_id: Optional[Union[int, None]]
    subprojects_id: Optional[Union[int, None]]
    services_id: Optional[Union[int, None]]
    lumpsum_services_id: Optional[Union[int, None]]
    billable: Billable
    entriesTexts_id: Optional[Union[int, None]]
    budget_type: Optional[Union[str, None]]

Success = bool

Edited_entries = int

class EntryGroupUpdateV2(BaseModel):
    success: Success
    edited_entries: Edited_entries

Group = str

Duration = int

Restrictions = Union[EntryGroupNoRestrictionV2, EntryGroupRestrictionV2, Any]

Has_budget_revenues_billed = bool

Has_budget_revenues_not_billed = bool

Has_non_budget_revenues_billed = bool

Has_non_budget_revenues_not_billed = bool

Budget_used = bool

Hourly_rate_is_equal_and_has_no_lumpsums = bool

Grouped_by = str

Grouping = str

class EntryGroupV2(BaseModel):
    group: Group = Field(None, description="Identifier of the current group")
    name: Name = Field(None, description="Textual description of the current group")
    duration: Duration = Field(None, description="Duration of all time entries of the group")
    restrictions: Restrictions = Field(None, description="Restrictions that apply to the current group, except for the current grouped_by and time restrictions")
    revenue: Revenue = Field(None, description="Revenue of all time entries in the group (only if necessary employee rights for the group)")
    has_budget_revenues_billed: Has_budget_revenues_billed = Field(None, description="Does the group have at least one time entry that uses the hard project budget and has already been billed? (only if necessary employee rights for the group)")
    has_budget_revenues_not_billed: Has_budget_revenues_not_billed = Field(None, description="Does the group have at least one time entry that uses a hard project budget and has not yet been billed? (Only if necessary employee rights for the group)")
    has_non_budget_revenues_billed: Has_non_budget_revenues_billed = Field(None, description="Does the group have at least one time entry that does not use a hard project budget and has already been billed? (Only if the necessary employee rights are assigned to the group)")
    has_non_budget_revenues_not_billed: Has_non_budget_revenues_not_billed = Field(None, description="Does the group have at least one time entry that does not use a hard project budget and has not yet been billed? (Only if necessary employee rights for the group)")
    budget_used: Budget_used = Field(None, description="Was a fixed project budget used for at least one time entry? (Only if necessary employee rights for the group)")
    hourly_rate: Optional[Union[float, None]] = Field(None, description="Average hourly rate for the group (only if necessary employee rights for the group)")
    hourly_rate_is_equal_and_has_no_lumpsums: Hourly_rate_is_equal_and_has_no_lumpsums = Field(None, description="Is the hourly rate the same for all billable entries and does the group have no flat-rate entries? In this case, revenue can be calculated as follows: revenue = hourly_rate * duration. This is particularly useful for creating invoice items. (Only if the necessary employee rights for the group are available)")
    sub_groups: Optional[Union[Any, None]] = Field(None, description="If multiple grouping criteria have been specified, the next level can be found here.")
    grouped_by: Grouped_by = Field(None, description="Grouping criterion of the current grouping level")

EntryTextMode = str

Expected_valuesItem = str

Expected_values = List[Expected_valuesItem]

class ExpectedValues(BaseModel):
    expected_values: Expected_values = Field(None, description="One or more expected values", example=['string', 'integer'])

FieldsItem = str

Fields = List[FieldsItem]

class FieldsShouldBeEmptyError(BaseModel):
    type: Optional[Type] = Field(None, example='FieldsShouldBeEmpty')
    message: Optional[Union[str, None]] = Field(None, example='According to your other information, the following fields should be empty: type, status.')
    path: Optional[Union[str, None]] = None
    details: Optional[Fields] = None

class ForbiddenChangeToCustomAccessError(BaseModel):
    type: Optional[Type] = Field(None, example='ForbiddenChangeToCustomAccess')
    message: Optional[Union[str, None]] = Field(None, example='Change to selected access is only possible from yes.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class ForbiddenError(BaseModel):
    type: Optional[Type] = Field(None, example='Forbidden')
    message: Optional[Union[str, None]] = Field(None, example='Access denied.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class ForbiddenValueError(BaseModel):
    type: Optional[Type] = Field(None, example='ForbiddenValue')
    message: Optional[Union[str, None]] = Field(None, example='An error occurred, please try again.')
    path: Optional[Union[str, None]] = None
    details: Optional[AllowedValues] = None

Errors = List[ApiErrors]

class GeneralErrors(BaseModel):
    errors: Errors

class HalfDayAbsenceTooLongError(BaseModel):
    type: Optional[Type] = Field(None, example='HalfDayAbsenceTooLong')
    message: Optional[Union[str, None]] = Field(None, example='Absences of half a day may not extend over several days.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class HasToBeActiveError(BaseModel):
    type: Optional[Type] = Field(None, example='HasToBeActive')
    message: Optional[Union[str, None]] = Field(None, example='The resource must be active.')
    path: Optional[Union[str, None]] = None
    details: Optional[Resource] = None

class HasToBeInactiveError(BaseModel):
    type: Optional[Type] = Field(None, example='HasToBeInactive')
    message: Optional[Union[str, None]] = Field(None, example='The resource must be inactive.')
    path: Optional[Union[str, None]] = None
    details: Optional[Resource] = None

YearItem = int

Year = List[YearItem]

Count = float

class HolidaysCarryV3(BaseModel):
    id: Id = Field(None, example=10)
    users_id: Users_id
    year: Year
    count: Count = Field(None, example=5.5)
    note: Optional[Union[str, None]] = Field(None, example='Saved for spring vacation')

Year_since = int

class HolidaysQuotumV2(BaseModel):
    id: Id = Field(None, example=10)
    users_id: Users_id = Field(None, example=20)
    year_since: Year_since = Field(None, example='2023')
    year_until: Optional[Union[int, None]] = Field(None, example='2024')
    count: Count = Field(None, example=3.5)
    note: Optional[Union[str, None]] = Field(None, example='Carryover from previous year')

class IllegalChangeForCompletedProjectError(BaseModel):
    type: Optional[Type] = Field(None, example='IllegalChangeForCompletedProject')
    message: Optional[Union[str, None]] = Field(None, example="The project has already been completed. The budget and deadline can't be changed.")
    path: Optional[Union[str, None]] = None
    details: Optional[Fields] = None

class IntervalBudgetRequiresRetainerPlanError(BaseModel):
    type: Optional[Type] = Field(None, example='IntervalBudgetRequiresRetainerPlan')
    message: Optional[Union[str, None]] = Field(None, example='Interval budgets feature is not available in your current plan.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class IntervalChangeIsForbiddenForIntervalProjectsWithSubprojectsError(BaseModel):
    type: Optional[Type] = Field(None, example='IntervalChangeIsForbiddenForIntervalProjectsWithSubprojects')
    message: Optional[Union[str, None]] = Field(None, example='Changing the interval is forbidden for interval projects with existing subprojects.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class InvalidCombinationError(BaseModel):
    type: Optional[Type] = Field(None, example='InvalidCombination')
    message: Optional[Union[str, None]] = Field(None, example='The combination of the provided data is invalid.')
    path: Optional[Union[str, None]] = None
    details: Optional[Fields] = None

class InvalidDateError(BaseModel):
    type: Optional[Type] = Field(None, example='InvalidDate')
    message: Optional[Union[str, None]] = Field(None, example='The given value is not an actual date.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class IsDefaultHolidaysCountError(BaseModel):
    type: Optional[Type] = Field(None, example='IsDefaultHolidaysCount')
    message: Optional[Union[str, None]] = Field(None, example='It is not allowed to delete a holidays quota which is user default.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Price = float

class LumpSumServiceV4(BaseModel):
    id: Id = Field(None, example=10)
    name: Name = Field(None, example='Travel costs')
    price: Price = Field(None, description="Price per unit", example=80.25)
    unit: Optional[Union[str, None]] = Field(None, example='km')
    active: Active = Field(None, example=True)
    number: Optional[Union[str, None]] = Field(None, description="Lump sum service number", example='Travel-123')
    note: Optional[Union[str, None]] = Field(None, description="Only visible for owners or workers with elevated access `manage_services`", example='Travel costs for the trip to the customer')

class MaxUsersOfPlanTypeReachedError(BaseModel):
    type: Optional[Type] = Field(None, example='MaxUsersOfPlanTypeReached')
    message: Optional[Union[str, None]] = Field(None, example='You have reached the maximum number of co-workers included in your subscription. Please upgrade your plan in the payment section.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class MaxUsersReachedError(BaseModel):
    type: Optional[Type] = Field(None, example='MaxUsersReached')
    message: Optional[Union[str, None]] = Field(None, example='You have reached the maximum number of co-workers included in your subscription. Please update your subscription in the payment section.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

MenuIcon = str

class MissingManageUsersAccessError(BaseModel):
    type: Optional[Type] = Field(None, example='MissingManageUsersAccess')
    message: Optional[Union[str, None]] = Field(None, example='You are not allowed to edit or delete access groups with elevated access.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Access_groups_idsItem = int

Access_groups_ids = List[Access_groups_idsItem]

class MissingManageUsersAccessForAssigningAccessGroup(BaseModel):
    access_groups_ids: Access_groups_ids = Field(None, description="The access groups with elevated access")

class MissingManageUsersAccessForAssigningAccessGroupError(BaseModel):
    type: Optional[Type] = Field(None, example='MissingManageUsersAccessForAssigningAccessGroup')
    message: Optional[Union[str, None]] = Field(None, example='You are not allowed to assign groups with elevated access to users.')
    path: Optional[Union[str, None]] = None
    details: Optional[MissingManageUsersAccessForAssigningAccessGroup] = None

class MissingManageUsersAccessForRemovingAccessGroup(BaseModel):
    access_groups_ids: Access_groups_ids = Field(None, description="The access groups with elevated access")

class MissingManageUsersAccessForRemovingAccessGroupError(BaseModel):
    type: Optional[Type] = Field(None, example='MissingManageUsersAccessForRemovingAccessGroup')
    message: Optional[Union[str, None]] = Field(None, example='You are not allowed to remove groups with elevated access from users.')
    path: Optional[Union[str, None]] = None
    details: Optional[MissingManageUsersAccessForRemovingAccessGroup] = None

NonbusinessDayType = str

Nonbusiness_group_id = int

Half_day = bool

Surcharge_special = bool

Special_id = int

Evaluated_date = str

Day = str

Month = int

class NonbusinessDayV2(BaseModel):
    id: Id = Field(None, example=10)
    nonbusiness_group_id: Nonbusiness_group_id = Field(None, example=504)
    type: NonbusinessDayType
    name: Name = Field(None, example='Tag der deutschen Einheit')
    half_day: Half_day = Field(None, example=True)
    surcharge_special: Surcharge_special = Field(None, example=True)
    special_id: Optional[Special_id] = Field(None, example=64)
    evaluated_date: Evaluated_date = Field(None, description="Default: CurrentYear", example='2021-10-03')
    day: Optional[Day] = Field(None, description="only for types DISTINCT_ONCE and DISTINCT_RECURRING", example=3)
    month: Optional[Month] = Field(None, description="only for types DISTINCT_ONCE and DISTINCT_RECURRING", example=10)
    year: Optional[Year] = Field(None, description="only for type DISTINCT_ONCE", example=2021)

Nonbusiness = float

class NonbusinessGroupV2(BaseModel):
    id: Id = Field(None, example=10)
    name: Name = Field(None, example='Nonbusiness days in NRW')
    company_default: Company_default = Field(None, example=False)

class NotBetweenError(BaseModel):
    type: Optional[Type] = Field(None, example='NotBetween')
    message: Optional[Union[str, None]] = Field(None, example='An error occurred, please try again.')
    path: Optional[Union[str, None]] = None
    details: Optional[NotBetween] = None

class OnlyOwnerCanDeleteOwnerError(BaseModel):
    type: Optional[Type] = Field(None, example='OnlyOwnerCanDeleteOwner')
    message: Optional[Union[str, None]] = Field(None, example='Only Owner can delete owner.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Hours = float

class OvertimeCarryV3(BaseModel):
    id: Id = Field(None, example=10)
    users_id: Users_id
    year: Year = Field(None, example=2024)
    hours: Hours = Field(None, example=5.5)
    note: Optional[Union[str, None]] = Field(None, example='Saved for spring')

Date = str

Added_at = str

Added_by_users_id = int

class OvertimeReductionV3(BaseModel):
    id: Id = Field(None, example=10)
    users_id: Users_id
    date: Date = Field(None, example='2023-02-28')
    hours: Hours = Field(None, example=5.5)
    note: Optional[Union[str, None]] = Field(None, example='Visiting authorities')
    added_at: Added_at = Field(None, example='2023-02-28')
    added_by_users_id: Added_by_users_id = Field(None, example=10)

class ProjectCompletionAnyRunningEntriesError(BaseModel):
    type: Optional[Type] = Field(None, example='ProjectCompletionAnyRunningEntries')
    message: Optional[Union[str, None]] = Field(None, example="The project can't be set to completed. A co-worker is currently tracking time with the clock.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class ProjectCompletionNoBillableEntriesError(BaseModel):
    type: Optional[Type] = Field(None, example='ProjectCompletionNoBillableEntries')
    message: Optional[Union[str, None]] = Field(None, example="The project can't be set to completed. At least one billable entry is required.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class ProjectCompletionRunningEntriesError(BaseModel):
    type: Optional[Type] = Field(None, example='ProjectCompletionRunningEntries')
    message: Optional[Union[str, None]] = Field(None, example="The project can't be set to completed. A co-worker is currently tracking billable time with the clock.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class ProjectCompletionTooManyLumpSumsError(BaseModel):
    type: Optional[Type] = Field(None, example='ProjectCompletionTooManyLumpSums')
    message: Optional[Union[str, None]] = Field(None, example="The project can't be set to completed. The sum of billable lump sums must not exceed the budget.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class ProjectDeadlineIsNotBeforeProjectStartError(BaseModel):
    type: Optional[Type] = Field(None, example='ProjectDeadlineIsNotBeforeProjectStart')
    message: Optional[Union[str, None]] = Field(None, example='Deadline must be after or equal to start date.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class ProjectIsCompletedError(BaseModel):
    type: Optional[Type] = Field(None, example='ProjectIsCompleted')
    message: Optional[Union[str, None]] = Field(None, example='The project is completed.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class ProjectPeriodCollidesWithSubprojectPeriodsError(BaseModel):
    type: Optional[Type] = Field(None, example='ProjectPeriodCollidesWithSubprojectPeriods')
    message: Optional[Union[str, None]] = Field(None, example='The project period collides with one or more subproject periods.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class ProjectPeriodMustContainAllEntryStartsError(BaseModel):
    type: Optional[Type] = Field(None, example='ProjectPeriodMustContainAllEntryStarts')
    message: Optional[Union[str, None]] = Field(None, example='Project period must contain all entry dates.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Projects_id = int

Projects_name = str

class ProjectReportsV3(BaseModel):
    customers_id: Customers_id = Field(None, example=10)
    customers_name: Customers_name = Field(None, example='Hotel Bergblick')
    customers_number: Optional[Union[str, None]] = Field(None, description="Freely selectable number for the customer", example=10)
    projects_id: Projects_id = Field(None, example=10)
    projects_name: Projects_name = Field(None, example='Werbekampagne')
    projects_number: Optional[Union[str, None]] = Field(None, description="Freely selectable number for the project", example=10)

class ProjectsReportProjectReportItemV4(BaseModel):
    customers_id: Customers_id
    customers_name: Customers_name
    customers_number: Optional[Union[str, None]]
    projects_id: Projects_id
    projects_name: Projects_name
    projects_number: Optional[Union[str, None]]

Subprojects_id = int

Subprojects_name = str

class ProjectsReportRetainerSubprojectReportItemV4(BaseModel):
    customers_id: Customers_id
    customers_name: Customers_name
    customers_number: Optional[Union[str, None]]
    projects_id: Projects_id
    projects_name: Projects_name
    projects_number: Optional[Union[str, None]]
    subprojects_id: Subprojects_id
    subprojects_name: Subprojects_name
    subprojects_number: Optional[Union[str, None]]

ProjectsReportReportItemV4 = Union[ProjectsReportProjectReportItemV4, ProjectsReportRetainerSubprojectReportItemV4]

Completed = bool

Count_subprojects = int

class ProjectV4(BaseModel):
    id: Id = Field(None, example=10)
    customers_id: Customers_id
    name: Name = Field(None, example='Publicity campaign')
    number: Optional[Union[str, None]] = Field(None, example='10')
    active: Active
    billable_default: Billable_default
    note: Optional[Union[str, None]] = Field(None, description="Only with necessary access rights", example='This project is important for us')
    billed_money: Optional[Union[float, None]] = Field(None, description="Only with necessary access rights")
    billed_completely: Optional[Union[bool, None]] = Field(None, description="Only with necessary access rights")
    completed: Completed
    completed_at: Optional[Union[str, None]] = Field(None, example='2023-02-28T12:00:00Z')
    revenue_factor: Optional[Union[float, None]] = Field(None, description="Only with necessary access rights.\n`null` for a project with hard budget that hasn't been completed yet.\nFor a project with hard budget which has been completed with a budget usage of 400%, the factor is `0.25`.\n`1` for projects without budget or with soft budget.")
    test_data: Test_data
    count_subprojects: Count_subprojects = Field(None, description="Number of subprojects", example=5)
    deadline: Optional[Union[str, None]] = Field(None, example='2023-02-28')
    start_date: Optional[Union[str, None]] = Field(None, description="Date when the project becomes available for time tracking", example='2023-01-01')
    budget: Optional[Budget] = None
    bill_service_id: Optional[Union[str, None]] = Field(None, example='1234')

Customer_idsItem = int

Customer_ids = List[Customer_idsItem]

Project_idsItem = int

Project_ids = List[Project_idsItem]

Service_idsItem = int

Service_ids = List[Service_idsItem]

User_idsItem = int

User_ids = List[User_idsItem]

class RateV3(BaseModel):
    id: Id = Field(None, example=10)
    customer_ids: Customer_ids = Field(None, example=[1, 2, 3, 4, 5])
    project_ids: Project_ids = Field(None, example=[1, 2, 3, 4, 5])
    service_ids: Service_ids = Field(None, example=[1, 2, 3, 4, 5])
    user_ids: User_ids = Field(None, example=[1, 2, 3, 4, 5])
    hourly_rate: Hourly_rate = Field(None, example=99.99)
    test_data: Test_data = Field(None, example=False)
    children: Children = Field(None, example=[])

Children = List[RateV3]

Apikey = str

Addcustomers = bool

class SettingAccessV1(BaseModel):
    addCustomers: Addcustomers

Currency = str

Weekstart_monday = bool

Weekend_friday = bool

Allowentriestextmultiline = bool

Example = float

Format = str

class SettingPriceFormatV1(BaseModel):
    example: Example
    format: Format

Currency_symbol = str

class SettingV1(BaseModel):
    name: Name
    email: Email
    role: Role
    access: SettingAccessV1
    price_format: SettingPriceFormatV1
    timeformat_12h: Timeformat_12h
    weekstart_monday: Weekstart_monday
    weekend_friday: Weekend_friday
    language: Language
    currency: Currency
    currency_symbol: Currency_symbol
    timezone: Timezone
    support_pin: Support_pin
    allowEntriesTextMultiline: Allowentriestextmultiline

class RegisterV1(BaseModel):
    success: Success
    user: SettingV1
    apikey: Apikey
    first_login_key: Optional[Union[str, None]]

class RelationsPreventDeletionError(BaseModel):
    type: Optional[Type] = Field(None, example='RelationsPreventDeletion')
    message: Optional[Union[str, None]] = Field(None, example='Resource can not be deleted, there are existing relations. Please delete the related resources first.')
    path: Optional[Union[str, None]] = None
    details: Optional[Resource] = None

class RequiresBudgetError(BaseModel):
    type: Optional[Type] = Field(None, example='RequiresBudget')
    message: Optional[Union[str, None]] = Field(None, example='A budget is required when budget type is hard.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class ResourceConflictFoundError(BaseModel):
    type: Optional[Type] = Field(None, example='ResourceConflictFound')
    message: Optional[Union[str, None]] = Field(None, example='There is already a service with this name.')
    path: Optional[Union[str, None]] = None
    details: Optional[Resource] = None

class ResourceNotFoundError(BaseModel):
    type: Optional[Type] = Field(None, example='ResourceNotFound')
    message: Optional[Union[str, None]] = Field(None, example='The requested resource could not be found.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Inactive_idsItem = int

Inactive_ids = List[Inactive_idsItem]

class ResourcesInactive(BaseModel):
    inactive_ids: Inactive_ids = Field(None, description="One or more ids of inactive resources", example=[99999])

class ResourcesInactiveError(BaseModel):
    type: Optional[Type] = Field(None, example='ResourcesInactive')
    message: Optional[Union[str, None]] = Field(None, example='The requested resources are inactive.')
    path: Optional[Union[str, None]] = None
    details: Optional[ResourcesInactive] = None

Not_found_idsItem = int

Not_found_ids = List[Not_found_idsItem]

class ResourcesNotFound(BaseModel):
    not_found_ids: Not_found_ids = Field(None, description="One or more ids of missing resources", example=[99999])

class ResourcesNotFoundError(BaseModel):
    type: Optional[Type] = Field(None, example='ResourcesNotFound')
    message: Optional[Union[str, None]] = Field(None, example='The requested resources could not be found.')
    path: Optional[Union[str, None]] = None
    details: Optional[ResourcesNotFound] = None

class RunningEntriesPreventArchivingError(BaseModel):
    type: Optional[Type] = Field(None, example='RunningEntriesPreventArchiving')
    message: Optional[Union[str, None]] = Field(None, example='Resource can not be archived, there are running entries. Please stop those entries first.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class RunningEntriesPreventDeletionError(BaseModel):
    type: Optional[Type] = Field(None, example='RunningEntriesPreventDeletion')
    message: Optional[Union[str, None]] = Field(None, example='Resource can not be deleted, there are running entries. Please stop and delete those entries first.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class services_access_v2(BaseModel):
    add: Optional[Add] = Field(None, example={'123': True, '456': True})

ServiceScope = str

class ServiceV4(BaseModel):
    id: Id = Field(None, example=10)
    name: Name = Field(None, example='Repair')
    number: Optional[Union[str, None]] = Field(None, example='SRV-123')
    active: Active
    note: Optional[Union[str, None]] = Field(None, description="Only visible for owners or workers with elevated access `manage_services`", example='Repair cost for the customer')
    bill_service_id: Optional[Union[str, None]] = Field(None, description="Only visible for owners or workers with elevated access `manage_services` and if a billing application with services support is linked up", example='1234')

class ShouldNotHaveBudgetError(BaseModel):
    type: Optional[Type] = Field(None, example='ShouldNotHaveBudget')
    message: Optional[Union[str, None]] = Field(None, example='This subproject cannot have a budget, as it belongs to a project without budget.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Code = int

class SimpleErrors(BaseModel):
    code: Code = Field(None, description="HTTP status code")
    message: Message = Field(None, description="An error occurred")
    fields: Optional[Fields] = Field(None, description="Affected fields")

class SimpleErrorResponses(BaseModel):
    error: Optional[SimpleErrors] = Field(None, description="Service zum Auslesen des OpenApi-Attributs für das Multi-Error-Format")

ApiProjectsReportsV3_SortForIndex = str

ApiProjectsReportsV4_SortForIndex = str

ApiUsersV3_SortForIndex = str

SortIdName = str

SortIdNameActive = str

class SsoPreventsDeactivationError(BaseModel):
    type: Optional[Type] = Field(None, example='SsoPreventsDeactivation')
    message: Optional[Union[str, None]] = Field(None, example="This user account can't be deactivated because it is the main account of an add-on linkup.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class StatusIsForbiddenError(BaseModel):
    type: Optional[Type] = Field(None, example='StatusIsForbidden')
    message: Optional[Union[str, None]] = Field(None, example='The provided status is not available in this constellation.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectBudgetCommitmentNotEditableForBudgetSourceError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectBudgetCommitmentNotEditableForBudgetSource')
    message: Optional[Union[str, None]] = Field(None, example='Budget strictness cannot be edited for this budget source configuration.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectBudgetModificationIsProhibitedBecauseItIsCompletedError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectBudgetModificationIsProhibitedBecauseItIsCompleted')
    message: Optional[Union[str, None]] = Field(None, example='You cannot edit subproject budget data because the subproject is already completed.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectBudgetModificationIsProhibitedBecauseProjectIsCompletedError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectBudgetModificationIsProhibitedBecauseProjectIsCompleted')
    message: Optional[Union[str, None]] = Field(None, example='You cannot edit subproject budget data because the main project is already completed.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectBudgetTypeNotEditableForBudgetSourceError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectBudgetTypeNotEditableForBudgetSource')
    message: Optional[Union[str, None]] = Field(None, example='Budget type cannot be edited for this budget source configuration.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectCompletionAnyRunningEntriesError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectCompletionAnyRunningEntries')
    message: Optional[Union[str, None]] = Field(None, example="The subproject can't be set to completed. A co-worker is currently tracking time with the clock.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectCompletionNoBillableEntriesError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectCompletionNoBillableEntries')
    message: Optional[Union[str, None]] = Field(None, example="The subproject can't be set to completed. At least one billable entry is required.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectCompletionRunningEntriesError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectCompletionRunningEntries')
    message: Optional[Union[str, None]] = Field(None, example="The subproject can't be set to completed. A co-worker is currently tracking billable time with the clock.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectCompletionTooManyLumpSumsError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectCompletionTooManyLumpSums')
    message: Optional[Union[str, None]] = Field(None, example="The subproject can't be set to completed. The sum of billable lump sums must not exceed the budget.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectCompletionWithHardBudgetIsProhibitedForCompletedProjectsError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectCompletionWithHardBudgetIsProhibitedForCompletedProjects')
    message: Optional[Union[str, None]] = Field(None, example='You cannot complete a subproject with a hard budget because the project is completed.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectCreationWithBudgetIsProhibitedError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectCreationWithBudgetIsProhibited')
    message: Optional[Union[str, None]] = Field(None, example='You cannot create a subproject with a budget because it is already completed.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectDeadlineIsNotBeforeSubprojectStartError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectDeadlineIsNotBeforeSubprojectStart')
    message: Optional[Union[str, None]] = Field(None, example='Deadline must be after or equal to start date.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectIsCompletedError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectIsCompleted')
    message: Optional[Union[str, None]] = Field(None, example='The subproject is completed.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectPeriodIsNotWithinProjectsPeriodError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectPeriodIsNotWithinProjectsPeriod')
    message: Optional[Union[str, None]] = Field(None, example="The subproject's start date and deadline must be within the project's start date and deadline period.")
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectPeriodMustContainAllEntryStartsError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectPeriodMustContainAllEntryStarts')
    message: Optional[Union[str, None]] = Field(None, example='Project period must contain all entry dates.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class SubprojectsCanNotBeSetToBilledError(BaseModel):
    type: Optional[Type] = Field(None, example='SubprojectCanNotBeSetToBilled')
    message: Optional[Union[str, None]] = Field(None, example='Subprojects can not be set to billed (except interval subprojects). Please set the parent project to billed.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Billed = bool

class SubprojectV3(BaseModel):
    id: Id
    projects_id: Projects_id
    name: Name
    note: Optional[Union[str, None]] = None
    number: Optional[Union[str, None]]
    budget: Optional[Budget] = None
    billed: Billed
    billed_money: Optional[Union[float, None]]
    billed_completely: Optional[Union[bool, None]]
    billable_default: Billable_default
    completed: Completed
    completed_at: Optional[Union[str, None]]
    revenue_factor: Optional[Union[float, None]] = None
    start_date: Optional[Union[str, None]]
    deadline: Optional[Union[str, None]]
    bill_service_id: Optional[Union[str, None]] = None

TargetHourType = str

Absence_fixed_credit = bool

Compensation_daily = float

Compensation_monthly = float

Workday_monday = bool

Workday_tuesday = bool

Workday_wednesday = bool

Workday_thursday = bool

Workday_friday = bool

Workday_saturday = bool

Workday_sunday = bool

Monthly_target = float

class TargetHourV1(BaseModel):
    id: Id = Field(None, example=10)
    users_id: Users_id = Field(None, example=10)
    surcharge_models_id: Optional[Union[int, None]] = Field(None, example=10)
    type: TargetHourType
    date_since: Date_since = Field(None, example='2023-02-28')
    date_until: Optional[Union[str, None]] = Field(None, example='2023-03-03')
    test_data: Test_data
    monday: Optional[Monday] = Field(None, example=8.5)
    tuesday: Optional[Tuesday] = Field(None, example=8.5)
    wednesday: Optional[Wednesday] = Field(None, example=8.5)
    thursday: Optional[Thursday] = Field(None, example=8.5)
    friday: Optional[Friday] = Field(None, example=8.5)
    saturday: Optional[Saturday] = Field(None, example=8.5)
    sunday: Optional[Sunday] = Field(None, example=8.5)
    absence_fixed_credit: Optional[Absence_fixed_credit] = Field(None, description="true if credited absence hours are applied against the average target hours, false if credited absence hours match the target hours of the specific day", example=True)
    compensation_daily: Optional[Compensation_daily] = Field(None, example=30.5)
    compensation_monthly: Optional[Compensation_monthly] = Field(None, example=0.5)
    workday_monday: Optional[Workday_monday] = Field(None, example=True)
    workday_tuesday: Optional[Workday_tuesday] = Field(None, example=True)
    workday_wednesday: Optional[Workday_wednesday] = Field(None, example=True)
    workday_thursday: Optional[Workday_thursday] = Field(None, example=True)
    workday_friday: Optional[Workday_friday] = Field(None, example=True)
    workday_saturday: Optional[Workday_saturday] = Field(None, example=True)
    workday_sunday: Optional[Workday_sunday] = Field(None, example=True)
    monthly_target: Optional[Monthly_target] = Field(None, example=172.5)

class TeamV3(BaseModel):
    id: Id = Field(None, example=10)
    name: Name = Field(None, example='Marketing')
    leader: Optional[Union[int, None]] = Field(None, example=103)

class UnexpectedValueError(BaseModel):
    type: Optional[Type] = Field(None, example='UnexpectedValue')
    message: Optional[Union[str, None]] = Field(None, example='Only these values are expected: string')
    path: Optional[Union[str, None]] = None
    details: Optional[ExpectedValues] = None

Until = str

class UntilBeforeSinceIsForbiddenError(BaseModel):
    type: Optional[Type] = Field(None, example='UntilBeforeSinceIsForbidden')
    message: Optional[Union[str, None]] = Field(None, example='Until date must be after or equal to the since date.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class UntilMustBeInSameYearError(BaseModel):
    type: Optional[Type] = Field(None, example='UntilMustBeInSameYear')
    message: Optional[Union[str, None]] = Field(None, example='The "until" date must be in the same year as the "since" date.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Initials = str

Default_work_time_regulation = bool

Future_coworker = bool

Edit_lock = Union[EditLockDay, Any]

Budget_notifications = bool

class UserV3(BaseModel):
    id: Id = Field(None, example=10)
    name: Name
    weekstart_monday: Weekstart_monday = Field(None, description="If false, the week starts on Sunday")
    weekend_friday: Weekend_friday = Field(None, description="If false, the weekend is Saturday and Sunday")
    active: Active
    timeformat_12h: Timeformat_12h
    language: Language
    timezone: Timezone = Field(None, description="e.g. `Europe/Berlin`")
    teams_id: Optional[Union[int, None]]
    initials: Initials
    nonbusiness_groups_id: Optional[Union[int, None]] = Field(None, description="deprecated; use v2/usersNonbusinessGroups instead")
    number: Optional[Union[str, None]] = None
    work_time_regulations_id: Optional[Union[int, None]] = Field(None, description="`0` if the co-worker has no work time regulation\n`null` if the company default is applicable")
    default_work_time_regulation: Optional[Default_work_time_regulation] = Field(None, description="Uses the company's default work time regulation")
    boss: Optional[Union[int, None]] = None
    absence_managers_id: Optional[Absence_managers_id] = None
    email: Optional[Email] = None
    role: Optional[Role] = None
    can_generally_see_absences: Optional[Can_generally_see_absences] = Field(None, description="Only editable for co-workers with the role 'worker'")
    can_generally_manage_absences: Optional[Can_generally_manage_absences] = Field(None, description="Only editable for co-workers with the role 'worker'")
    can_add_customers: Optional[Can_add_customers] = Field(None, description="Only editable for co-workers with the role 'worker'")
    default_holidays_count: Optional[Default_holidays_count] = Field(None, description="Uses the company's default holiday count")
    default_target_hours: Optional[Default_target_hours] = Field(None, description="Uses the company's default target hours")
    future_coworker: Optional[Future_coworker] = Field(None, description="The future co-worker cannot log in yet and the license is free until the start date.", example=True)
    start_date: Optional[Union[str, None]] = Field(None, example='2024-07-15')
    wage_type: Optional[Wage_type] = None
    edit_lock: Optional[Edit_lock] = Field(None, description="Defined editing lock for the co-worker", example='2024-06-15')
    edit_lock_dyn: Optional[Edit_lock_dyn] = Field(None, description="Relative editing lock in days for the co-worker")
    edit_lock_sync: Optional[Union[bool, None]] = None
    work_time_edit_lock_days: Optional[Work_time_edit_lock_days] = Field(None, description="Relative work time editing lock in days for the co-worker")
    budget_notifications: Optional[Budget_notifications] = None
    creator: Optional[Union[int, None]] = None

class UserCannotDeleteThemselvesError(BaseModel):
    type: Optional[Type] = Field(None, example='UserCannotDeleteThemselves')
    message: Optional[Union[str, None]] = Field(None, example='User cannot delete themselves.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

Regular_holidays = float

Sick_self = float

Sick_child = float

Special_leaves = float

School = float

Maternity_protection = float

Home_office = float

Out_of_office = float

Quarantine = float

Military_service = float

class UserReportAbsenceSummaryV1(BaseModel):
    regular_holidays: Regular_holidays
    sick_self: Sick_self
    sick_child: Sick_child
    special_leaves: Special_leaves
    school: School
    maternity_protection: Maternity_protection
    home_office: Home_office
    out_of_office: Out_of_office
    quarantine: Quarantine
    military_service: Military_service

Since = str

Length = float

class UserReportBreakItemV1(BaseModel):
    since: Since
    until: Until
    length: Length

Weekday = int

Diff = float

Breaks = List[UserReportBreakItemV1]

Night = float

Night_increased = float

Nonbusiness_special = float

class UserReportSurchargeSummaryV1(BaseModel):
    saturday: Saturday
    sunday: Sunday
    nonbusiness: Nonbusiness
    nonbusiness_special: Nonbusiness_special
    night: Night
    night_increased: Night_increased

class UserReportDayDetailV1(BaseModel):
    date: Date
    weekday: Weekday
    nonbusiness: Nonbusiness
    count_absence: UserReportAbsenceSummaryV1
    count_reduction_used: Optional[Union[float, None]]
    target: Optional[Union[float, None]]
    target_raw: Optional[Union[float, None]]
    surcharges: UserReportSurchargeSummaryV1
    hours: Optional[Union[float, None]] = None
    hours_without_compensation: Optional[Union[float, None]] = None
    diff: Optional[Diff] = None
    breaks: Optional[Breaks] = None
    work_start: Optional[Union[str, None]] = None
    work_end: Optional[Union[str, None]] = None

Nr = int

Sum_hours = float

Sum_hours_without_compensation = float

Sum_reduction_used = float

Sum_overtime_reduced = float

class UserReportMonthDetailV1(BaseModel):
    nr: Nr
    sum_target: Optional[Union[float, None]]
    sum_hours: Sum_hours
    sum_hours_without_compensation: Sum_hours_without_compensation
    sum_reduction_used: Sum_reduction_used
    sum_overtime_reduced: Sum_overtime_reduced
    diff: Diff
    surcharges: UserReportSurchargeSummaryV1
    week_details: Optional[Union[Any, None]]

UserReportType = int

Users_email = str

Sum_reduction_planned = float

Overtime_carryover = float

Overtime_reduced = float

Holidays_quota = float

Holidays_carry = float

Workdays = float

class UserReportV1(BaseModel):
    users_id: Users_id
    users_name: Users_name
    users_number: Optional[Union[str, None]]
    users_email: Users_email
    sum_target: Optional[Union[float, None]] = Field(None, description="In seconds")
    sum_hours: Sum_hours = Field(None, description="In seconds")
    sum_reduction_used: Sum_reduction_used = Field(None, description="In seconds")
    sum_reduction_planned: Sum_reduction_planned = Field(None, description="In seconds")
    overtime_carryover: Overtime_carryover = Field(None, description="In seconds")
    overtime_reduced: Overtime_reduced = Field(None, description="In seconds")
    diff: Diff = Field(None, description="In seconds")
    holidays_quota: Holidays_quota
    holidays_carry: Holidays_carry
    sum_absence: UserReportAbsenceSummaryV1
    surcharges: UserReportSurchargeSummaryV1
    workdays: Workdays
    month_details: Optional[Union[Any, None]]

class UserReportWeekDetailV1(BaseModel):
    nr: Nr
    sum_target: Optional[Union[float, None]]
    sum_hours: Sum_hours
    sum_reduction_used: Sum_reduction_used
    diff: Diff
    surcharges: UserReportSurchargeSummaryV1
    day_details: Optional[Union[Any, None]]

IdSub = int

class UsersAccessServiceV2(BaseModel):
    add: Add

UserScope = str

Limit = int

class UsersExceedAccessGroupLimit(BaseModel):
    limit: Limit = Field(None, description="The limit of access groups per user", example=30)
    users_ids: Users_ids = Field(None, description="One or more ids of users exceeding the access group limit", example=[99999])

class UsersExceedAccessGroupLimitError(BaseModel):
    type: Optional[Type] = Field(None, example='UsersExceedAccessGroupLimit')
    message: Optional[Union[str, None]] = Field(None, example='Users are exceeding the access group limit.')
    path: Optional[Union[str, None]] = None
    details: Optional[UsersExceedAccessGroupLimit] = None

Days = List[NonbusinessDayV2]

class UsersNonbusinessDayV2(BaseModel):
    users_id: Users_id = Field(None, example=10)
    days: Days = Field(None, description="Nonbusiness days that apply for the user in the queried time span")

class UsersNonbusinessGroupsCollisionError(BaseModel):
    type: Optional[Type] = Field(None, example='UsersNonbusinessGroupsCollision')
    message: Optional[Union[str, None]] = Field(None, example='An error occurred, please try again.')
    path: Optional[Union[str, None]] = None
    details: Optional[Any] = None

class UsersNonbusinessGroupV3(BaseModel):
    id: Id = Field(None, example=10)
    date_since: Date_since = Field(None, example='2025-01-31')
    date_until: Optional[Union[str, None]] = Field(None, example='2025-01-31')
    nonbusiness_groups_id: Optional[Union[int, None]] = Field(None, example=10)
    users_id: Users_id = Field(None, example=10)

Subscription_id = int

Company_id = int

Occurred_at = str

class WebhookEvent_absence_approved_PayloadModel_AbsenceModel(BaseModel):
    id: Id = Field(None, description="The ID of the absence", example=1)

class WebhookEvent_absence_approved_PayloadModel(BaseModel):
    absence: Optional[WebhookEvent_absence_approved_PayloadModel_AbsenceModel] = Field(None, description="The absence entity")

Event_name = str

Token = str

class WebhookEvent_absence_approved(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_absence_approved_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_absence_created_PayloadModel_AbsenceModel(BaseModel):
    id: Id = Field(None, description="The ID of the absence", example=1)

class WebhookEvent_absence_created_PayloadModel(BaseModel):
    absence: Optional[WebhookEvent_absence_created_PayloadModel_AbsenceModel] = Field(None, description="The absence entity")

class WebhookEvent_absence_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_absence_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_absence_deleted_PayloadModel_AbsenceModel(BaseModel):
    id: Id = Field(None, description="The ID of the absence", example=1)

class WebhookEvent_absence_deleted_PayloadModel(BaseModel):
    absence: Optional[WebhookEvent_absence_deleted_PayloadModel_AbsenceModel] = Field(None, description="The absence entity")

class WebhookEvent_absence_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_absence_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_absence_updated_PayloadModel_AbsenceModel(BaseModel):
    id: Id = Field(None, description="The ID of the absence", example=1)

class WebhookEvent_absence_updated_PayloadModel(BaseModel):
    absence: Optional[WebhookEvent_absence_updated_PayloadModel_AbsenceModel] = Field(None, description="The absence entity")

class WebhookEvent_absence_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_absence_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_customer_created_PayloadModel_CustomerModel(BaseModel):
    id: Id = Field(None, description="The ID of the customer", example=1)

class WebhookEvent_customer_created_PayloadModel(BaseModel):
    customer: Optional[WebhookEvent_customer_created_PayloadModel_CustomerModel] = Field(None, description="The customer entity")

class WebhookEvent_customer_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_customer_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_customer_deleted_PayloadModel_CustomerModel(BaseModel):
    id: Id = Field(None, description="The ID of the customer", example=1)

class WebhookEvent_customer_deleted_PayloadModel(BaseModel):
    customer: Optional[WebhookEvent_customer_deleted_PayloadModel_CustomerModel] = Field(None, description="The customer entity")

class WebhookEvent_customer_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_customer_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_customer_updated_PayloadModel_CustomerModel(BaseModel):
    id: Id = Field(None, description="The ID of the customer", example=1)

class WebhookEvent_customer_updated_PayloadModel(BaseModel):
    customer: Optional[WebhookEvent_customer_updated_PayloadModel_CustomerModel] = Field(None, description="The customer entity")

class WebhookEvent_customer_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_customer_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_entry_created_PayloadModel_EntryModel(BaseModel):
    id: Id = Field(None, description="The ID of the entry", example=1)

class WebhookEvent_entry_created_PayloadModel(BaseModel):
    entry: Optional[WebhookEvent_entry_created_PayloadModel_EntryModel] = Field(None, description="The entry entity")

class WebhookEvent_entry_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_entry_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_entry_deleted_PayloadModel_EntryModel(BaseModel):
    id: Id = Field(None, description="The ID of the entry", example=1)

class WebhookEvent_entry_deleted_PayloadModel(BaseModel):
    entry: Optional[WebhookEvent_entry_deleted_PayloadModel_EntryModel] = Field(None, description="The entry entity")

class WebhookEvent_entry_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_entry_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_entry_started_PayloadModel_EntryModel(BaseModel):
    id: Id = Field(None, description="The ID of the entry", example=1)

class WebhookEvent_entry_started_PayloadModel(BaseModel):
    entry: Optional[WebhookEvent_entry_started_PayloadModel_EntryModel] = Field(None, description="The entry entity")

class WebhookEvent_entry_started(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_entry_started_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_entry_stopped_PayloadModel_EntryModel(BaseModel):
    id: Id = Field(None, description="The ID of the entry", example=1)

class WebhookEvent_entry_stopped_PayloadModel(BaseModel):
    entry: Optional[WebhookEvent_entry_stopped_PayloadModel_EntryModel] = Field(None, description="The entry entity")

class WebhookEvent_entry_stopped(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_entry_stopped_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_entry_updated_PayloadModel_EntryModel(BaseModel):
    id: Id = Field(None, description="The ID of the entry", example=1)

class WebhookEvent_entry_updated_PayloadModel(BaseModel):
    entry: Optional[WebhookEvent_entry_updated_PayloadModel_EntryModel] = Field(None, description="The entry entity")

class WebhookEvent_entry_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_entry_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_holidays_carry_created_PayloadModel_Holidays_carryModel(BaseModel):
    id: Id = Field(None, description="The ID of the holidays carry", example=1)

class WebhookEvent_holidays_carry_created_PayloadModel(BaseModel):
    holidays_carry: Optional[WebhookEvent_holidays_carry_created_PayloadModel_Holidays_carryModel] = Field(None, description="The holidays carry entity")

class WebhookEvent_holidays_carry_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_holidays_carry_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_holidays_carry_deleted_PayloadModel_Holidays_carryModel(BaseModel):
    id: Id = Field(None, description="The ID of the holidays carry", example=1)

class WebhookEvent_holidays_carry_deleted_PayloadModel(BaseModel):
    holidays_carry: Optional[WebhookEvent_holidays_carry_deleted_PayloadModel_Holidays_carryModel] = Field(None, description="The holidays carry entity")

class WebhookEvent_holidays_carry_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_holidays_carry_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_holidays_carry_updated_PayloadModel_Holidays_carryModel(BaseModel):
    id: Id = Field(None, description="The ID of the holidays carry", example=1)

class WebhookEvent_holidays_carry_updated_PayloadModel(BaseModel):
    holidays_carry: Optional[WebhookEvent_holidays_carry_updated_PayloadModel_Holidays_carryModel] = Field(None, description="The holidays carry entity")

class WebhookEvent_holidays_carry_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_holidays_carry_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_holidays_quota_created_PayloadModel_Holidays_quotaModel(BaseModel):
    id: Id = Field(None, description="The ID of the holidays quota", example=1)

class WebhookEvent_holidays_quota_created_PayloadModel(BaseModel):
    holidays_quota: Optional[WebhookEvent_holidays_quota_created_PayloadModel_Holidays_quotaModel] = Field(None, description="The holidays quota entity")

class WebhookEvent_holidays_quota_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_holidays_quota_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_holidays_quota_deleted_PayloadModel_Holidays_quotaModel(BaseModel):
    id: Id = Field(None, description="The ID of the holidays quota", example=1)

class WebhookEvent_holidays_quota_deleted_PayloadModel(BaseModel):
    holidays_quota: Optional[WebhookEvent_holidays_quota_deleted_PayloadModel_Holidays_quotaModel] = Field(None, description="The holidays quota entity")

class WebhookEvent_holidays_quota_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_holidays_quota_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_holidays_quota_updated_PayloadModel_Holidays_quotaModel(BaseModel):
    id: Id = Field(None, description="The ID of the holidays quota", example=1)

class WebhookEvent_holidays_quota_updated_PayloadModel(BaseModel):
    holidays_quota: Optional[WebhookEvent_holidays_quota_updated_PayloadModel_Holidays_quotaModel] = Field(None, description="The holidays quota entity")

class WebhookEvent_holidays_quota_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_holidays_quota_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_lump_sum_service_created_PayloadModel_Lump_sum_serviceModel(BaseModel):
    id: Id = Field(None, description="The ID of the lump sum service", example=1)

class WebhookEvent_lump_sum_service_created_PayloadModel(BaseModel):
    lump_sum_service: Optional[WebhookEvent_lump_sum_service_created_PayloadModel_Lump_sum_serviceModel] = Field(None, description="The lump sum service entity")

class WebhookEvent_lump_sum_service_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_lump_sum_service_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_lump_sum_service_deleted_PayloadModel_Lump_sum_serviceModel(BaseModel):
    id: Id = Field(None, description="The ID of the lump sum service", example=1)

class WebhookEvent_lump_sum_service_deleted_PayloadModel(BaseModel):
    lump_sum_service: Optional[WebhookEvent_lump_sum_service_deleted_PayloadModel_Lump_sum_serviceModel] = Field(None, description="The lump sum service entity")

class WebhookEvent_lump_sum_service_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_lump_sum_service_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_lump_sum_service_updated_PayloadModel_Lump_sum_serviceModel(BaseModel):
    id: Id = Field(None, description="The ID of the lump sum service", example=1)

class WebhookEvent_lump_sum_service_updated_PayloadModel(BaseModel):
    lump_sum_service: Optional[WebhookEvent_lump_sum_service_updated_PayloadModel_Lump_sum_serviceModel] = Field(None, description="The lump sum service entity")

class WebhookEvent_lump_sum_service_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_lump_sum_service_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_nonbusiness_group_created_PayloadModel_Nonbusiness_groupModel(BaseModel):
    id: Id = Field(None, description="The ID of the nonbusiness group", example=1)

class WebhookEvent_nonbusiness_group_created_PayloadModel(BaseModel):
    nonbusiness_group: Optional[WebhookEvent_nonbusiness_group_created_PayloadModel_Nonbusiness_groupModel] = Field(None, description="The nonbusiness group entity")

class WebhookEvent_nonbusiness_group_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_nonbusiness_group_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_nonbusiness_group_deleted_PayloadModel_Nonbusiness_groupModel(BaseModel):
    id: Id = Field(None, description="The ID of the nonbusiness group", example=1)

class WebhookEvent_nonbusiness_group_deleted_PayloadModel(BaseModel):
    nonbusiness_group: Optional[WebhookEvent_nonbusiness_group_deleted_PayloadModel_Nonbusiness_groupModel] = Field(None, description="The nonbusiness group entity")

class WebhookEvent_nonbusiness_group_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_nonbusiness_group_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_nonbusiness_group_updated_PayloadModel_Nonbusiness_groupModel(BaseModel):
    id: Id = Field(None, description="The ID of the nonbusiness group", example=1)

class WebhookEvent_nonbusiness_group_updated_PayloadModel(BaseModel):
    nonbusiness_group: Optional[WebhookEvent_nonbusiness_group_updated_PayloadModel_Nonbusiness_groupModel] = Field(None, description="The nonbusiness group entity")

class WebhookEvent_nonbusiness_group_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_nonbusiness_group_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_overtime_carry_created_PayloadModel_Overtime_carryModel(BaseModel):
    id: Id = Field(None, description="The ID of the overtime carry", example=1)

class WebhookEvent_overtime_carry_created_PayloadModel(BaseModel):
    overtime_carry: Optional[WebhookEvent_overtime_carry_created_PayloadModel_Overtime_carryModel] = Field(None, description="The overtime carry entity")

class WebhookEvent_overtime_carry_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_overtime_carry_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_overtime_carry_deleted_PayloadModel_Overtime_carryModel(BaseModel):
    id: Id = Field(None, description="The ID of the overtime carry", example=1)

class WebhookEvent_overtime_carry_deleted_PayloadModel(BaseModel):
    overtime_carry: Optional[WebhookEvent_overtime_carry_deleted_PayloadModel_Overtime_carryModel] = Field(None, description="The overtime carry entity")

class WebhookEvent_overtime_carry_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_overtime_carry_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_overtime_carry_updated_PayloadModel_Overtime_carryModel(BaseModel):
    id: Id = Field(None, description="The ID of the overtime carry", example=1)

class WebhookEvent_overtime_carry_updated_PayloadModel(BaseModel):
    overtime_carry: Optional[WebhookEvent_overtime_carry_updated_PayloadModel_Overtime_carryModel] = Field(None, description="The overtime carry entity")

class WebhookEvent_overtime_carry_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_overtime_carry_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

Threshold = int

class WebhookEvent_project_budget_notification_PayloadModel(BaseModel):
    id: Id = Field(None, description="The ID of the project", example=123)
    type: Type = Field(None, description="The type of budget notification", example='projectBudget')
    threshold: Threshold = Field(None, description="The budget threshold percentage that was exceeded", example=80)

class WebhookEvent_project_budget_notification(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_project_budget_notification_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_project_completed_PayloadModel_ProjectModel(BaseModel):
    id: Id = Field(None, description="The ID of the project", example=1)

class WebhookEvent_project_completed_PayloadModel(BaseModel):
    project: Optional[WebhookEvent_project_completed_PayloadModel_ProjectModel] = Field(None, description="The project entity")

class WebhookEvent_project_completed(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_project_completed_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_project_created_PayloadModel_ProjectModel(BaseModel):
    id: Id = Field(None, description="The ID of the project", example=1)

class WebhookEvent_project_created_PayloadModel(BaseModel):
    project: Optional[WebhookEvent_project_created_PayloadModel_ProjectModel] = Field(None, description="The project entity")

class WebhookEvent_project_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_project_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_project_deleted_PayloadModel_ProjectModel(BaseModel):
    id: Id = Field(None, description="The ID of the project", example=1)

class WebhookEvent_project_deleted_PayloadModel(BaseModel):
    project: Optional[WebhookEvent_project_deleted_PayloadModel_ProjectModel] = Field(None, description="The project entity")

class WebhookEvent_project_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_project_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_project_updated_PayloadModel_ProjectModel(BaseModel):
    id: Id = Field(None, description="The ID of the project", example=1)

class WebhookEvent_project_updated_PayloadModel(BaseModel):
    project: Optional[WebhookEvent_project_updated_PayloadModel_ProjectModel] = Field(None, description="The project entity")

class WebhookEvent_project_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_project_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_service_created_PayloadModel_ServiceModel(BaseModel):
    id: Id = Field(None, description="The ID of the service", example=1)

class WebhookEvent_service_created_PayloadModel(BaseModel):
    service: Optional[WebhookEvent_service_created_PayloadModel_ServiceModel] = Field(None, description="The service entity")

class WebhookEvent_service_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_service_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_service_deleted_PayloadModel_ServiceModel(BaseModel):
    id: Id = Field(None, description="The ID of the service", example=1)

class WebhookEvent_service_deleted_PayloadModel(BaseModel):
    service: Optional[WebhookEvent_service_deleted_PayloadModel_ServiceModel] = Field(None, description="The service entity")

class WebhookEvent_service_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_service_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_service_updated_PayloadModel_ServiceModel(BaseModel):
    id: Id = Field(None, description="The ID of the service", example=1)

class WebhookEvent_service_updated_PayloadModel(BaseModel):
    service: Optional[WebhookEvent_service_updated_PayloadModel_ServiceModel] = Field(None, description="The service entity")

class WebhookEvent_service_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_service_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_subproject_created_PayloadModel_SubprojectModel(BaseModel):
    id: Id = Field(None, description="The ID of the subproject", example=1)

class WebhookEvent_subproject_created_PayloadModel(BaseModel):
    subproject: Optional[WebhookEvent_subproject_created_PayloadModel_SubprojectModel] = Field(None, description="The subproject entity")

class WebhookEvent_subproject_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_subproject_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_subproject_deleted_PayloadModel_SubprojectModel(BaseModel):
    id: Id = Field(None, description="The ID of the subproject", example=1)

class WebhookEvent_subproject_deleted_PayloadModel(BaseModel):
    subproject: Optional[WebhookEvent_subproject_deleted_PayloadModel_SubprojectModel] = Field(None, description="The subproject entity")

class WebhookEvent_subproject_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_subproject_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_subproject_updated_PayloadModel_SubprojectModel(BaseModel):
    id: Id = Field(None, description="The ID of the subproject", example=1)

class WebhookEvent_subproject_updated_PayloadModel(BaseModel):
    subproject: Optional[WebhookEvent_subproject_updated_PayloadModel_SubprojectModel] = Field(None, description="The subproject entity")

class WebhookEvent_subproject_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_subproject_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_team_created_PayloadModel_TeamModel(BaseModel):
    id: Id = Field(None, description="The ID of the team", example=1)

class WebhookEvent_team_created_PayloadModel(BaseModel):
    team: Optional[WebhookEvent_team_created_PayloadModel_TeamModel] = Field(None, description="The team entity")

class WebhookEvent_team_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_team_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_team_deleted_PayloadModel_TeamModel(BaseModel):
    id: Id = Field(None, description="The ID of the team", example=1)

class WebhookEvent_team_deleted_PayloadModel(BaseModel):
    team: Optional[WebhookEvent_team_deleted_PayloadModel_TeamModel] = Field(None, description="The team entity")

class WebhookEvent_team_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_team_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_team_updated_PayloadModel_TeamModel(BaseModel):
    id: Id = Field(None, description="The ID of the team", example=1)

class WebhookEvent_team_updated_PayloadModel(BaseModel):
    team: Optional[WebhookEvent_team_updated_PayloadModel_TeamModel] = Field(None, description="The team entity")

class WebhookEvent_team_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_team_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_user_created_PayloadModel_UserModel(BaseModel):
    id: Id = Field(None, description="The ID of the user", example=1)

class WebhookEvent_user_created_PayloadModel(BaseModel):
    user: Optional[WebhookEvent_user_created_PayloadModel_UserModel] = Field(None, description="The user entity")

class WebhookEvent_user_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_user_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_user_deleted_PayloadModel_UserModel(BaseModel):
    id: Id = Field(None, description="The ID of the user", example=1)

class WebhookEvent_user_deleted_PayloadModel(BaseModel):
    user: Optional[WebhookEvent_user_deleted_PayloadModel_UserModel] = Field(None, description="The user entity")

class WebhookEvent_user_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_user_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_user_updated_PayloadModel_UserModel(BaseModel):
    id: Id = Field(None, description="The ID of the user", example=1)

class WebhookEvent_user_updated_PayloadModel(BaseModel):
    user: Optional[WebhookEvent_user_updated_PayloadModel_UserModel] = Field(None, description="The user entity")

class WebhookEvent_user_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_user_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_work_time_change_request_created_PayloadModel_Work_time_change_requestModel(BaseModel):
    id: Id = Field(None, description="The ID of the work time change request", example=1)

class WebhookEvent_work_time_change_request_created_PayloadModel(BaseModel):
    work_time_change_request: Optional[WebhookEvent_work_time_change_request_created_PayloadModel_Work_time_change_requestModel] = Field(None, description="The work time change request entity")

class WebhookEvent_work_time_change_request_created(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_work_time_change_request_created_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_work_time_change_request_deleted_PayloadModel_Work_time_change_requestModel(BaseModel):
    id: Id = Field(None, description="The ID of the work time change request", example=1)

class WebhookEvent_work_time_change_request_deleted_PayloadModel(BaseModel):
    work_time_change_request: Optional[WebhookEvent_work_time_change_request_deleted_PayloadModel_Work_time_change_requestModel] = Field(None, description="The work time change request entity")

class WebhookEvent_work_time_change_request_deleted(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_work_time_change_request_deleted_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WebhookEvent_work_time_change_request_updated_PayloadModel_Work_time_change_requestModel(BaseModel):
    id: Id = Field(None, description="The ID of the work time change request", example=1)

class WebhookEvent_work_time_change_request_updated_PayloadModel(BaseModel):
    work_time_change_request: Optional[WebhookEvent_work_time_change_request_updated_PayloadModel_Work_time_change_requestModel] = Field(None, description="The work time change request entity")

class WebhookEvent_work_time_change_request_updated(BaseModel):
    subscription_id: Subscription_id = Field(None, description="The ID of the webhook subscription", example=42)
    company_id: Company_id = Field(None, description="The ID of the company", example=1337)
    occurred_at: Occurred_at = Field(None, description="The timestamp when the event occurred (ISO 8601 format)", example='1986-05-10T17:02:00Z')
    payload: WebhookEvent_work_time_change_request_updated_PayloadModel = Field(None, description="The event-specific payload data")
    event_name: Event_name = Field(None, description="The name of the webhook event")
    token: Token = Field(None, description="The webhook verification token", example='My_Sup3r_T0k3n')

class WorkTimeIntervalV2(BaseModel):
    time_since: Time_since
    time_until: Optional[Union[str, None]]

class WorkTimesChangeRequestChangeV2(BaseModel):
    type: ChangeRequestIntervalType
    time_since: Time_since
    time_until: Optional[Union[str, None]]

Created_at = str

Time_until = str

class ChangesItem(BaseModel):
    type: Optional[ChangeRequestIntervalType] = None
    time_since: Optional[Time_since] = Field(None, example='2023-02-28T12:00:00Z')
    time_until: Optional[Time_until] = Field(None, example='2023-02-28T12:00:00Z')

Changes = List[ChangesItem]

class WorkTimesChangeRequestV2(BaseModel):
    id: Id
    date: Date
    users_id: Users_id
    status: ChangeRequestStatus
    created_at: Created_at
    declined_at: Optional[Union[str, None]]
    declined_by: Optional[Union[int, None]]
    changes: Changes

Change_request = Union[WorkTimesChangeRequestV2, Any]

Approved_immediately = bool

class WorkTimesChangeRequestPostV2(BaseModel):
    change_request: Change_request
    approved_immediately: Approved_immediately

class WorkTimesChangeRequestsDeclineChangeV2(BaseModel):
    type: ChangeRequestIntervalType
    time_since: Time_since
    time_until: Optional[Union[str, None]]

class WorkTimesChangeRequestsDeclineV2(BaseModel):
    id: Id
    date: Date
    users_id: Users_id
    status: ChangeRequestStatus
    created_at: Optional[Union[str, None]]
    declined_at: Optional[Union[str, None]]
    declined_by: Optional[Union[int, None]]
    changes: Changes

Offset = int

Intervals = List[WorkTimeIntervalV2]

class WorkTimeV2(BaseModel):
    date: Date
    users_id: Users_id
    offset: Offset = Field(None, description="Only possible for days before 2023-01-01; can be positive or negative.")
    intervals: Intervals

Companies_name = str

class register_post_RequestBodyModel(BaseModel):
    companies_name: Companies_name
    name: Name
    email: Email
    rfs: Optional[Union[str, None]] = Field(None, description="Name of the external application from which the registration is made")
    bs: Optional[Union[str, None]] = Field(None, description="Preselected billing application")
    gtc_agreed: Optional[Union[str, None]] = Field(None, description="Terms of Clockodo were accepted")

class register_post_InputModel(BaseModel):
    requestBody: register_post_RequestBodyModel


targethours_get_users_id_InputModelItem = int

targethours_get_users_id_InputModel = List[targethours_get_users_id_InputModelItem]

class targethours_get_InputModel(BaseModel):
    users_id: targethours_get_users_id_InputModel


Surcharge_models_id = int

class targethours_post_RequestBodyModel(BaseModel):
    users_id: Users_id
    type: TargetHourType
    date_since: Date_since = Field(None, example='2023-02-28')
    date_until: Optional[Union[str, None]] = Field(None, example='2023-02-28')
    monday: Optional[Monday] = None
    tuesday: Optional[Tuesday] = None
    wednesday: Optional[Wednesday] = None
    thursday: Optional[Thursday] = None
    friday: Optional[Friday] = None
    saturday: Optional[Saturday] = None
    sunday: Optional[Sunday] = None
    monthly_target: Optional[Monthly_target] = None
    workday_monday: Optional[Workday_monday] = None
    workday_tuesday: Optional[Workday_tuesday] = None
    workday_wednesday: Optional[Workday_wednesday] = None
    workday_thursday: Optional[Workday_thursday] = None
    workday_friday: Optional[Workday_friday] = None
    workday_saturday: Optional[Workday_saturday] = None
    workday_sunday: Optional[Workday_sunday] = None
    compensation_daily: Optional[Compensation_daily] = Field(None, description="Automatic time compensation per day in minutes")
    compensation_monthly: Compensation_monthly = Field(None, description="Compensation for monthly target hours in minutes")
    holiday_fixed_credit: Optional[Holiday_fixed_credit] = None
    surcharge_models_id: Optional[Surcharge_models_id] = None

class targethours_post_InputModel(BaseModel):
    requestBody: targethours_post_RequestBodyModel


targethours__id__get_id_InputModel = int

class targethours__id__get_InputModel(BaseModel):
    id: targethours__id__get_id_InputModel


targethours__id__put_id_InputModel = int

class targethours__id__put_RequestBodyModel(BaseModel):
    type: TargetHourType
    date_since: Date_since = Field(None, example='2023-02-28')
    date_until: Optional[Union[str, None]] = Field(None, example='2023-02-28')
    monday: Optional[Monday] = None
    tuesday: Optional[Tuesday] = None
    wednesday: Optional[Wednesday] = None
    thursday: Optional[Thursday] = None
    friday: Optional[Friday] = None
    saturday: Optional[Saturday] = None
    sunday: Optional[Sunday] = None
    monthly_target: Optional[Monthly_target] = None
    workday_monday: Optional[Workday_monday] = None
    workday_tuesday: Optional[Workday_tuesday] = None
    workday_wednesday: Optional[Workday_wednesday] = None
    workday_thursday: Optional[Workday_thursday] = None
    workday_friday: Optional[Workday_friday] = None
    workday_saturday: Optional[Workday_saturday] = None
    workday_sunday: Optional[Workday_sunday] = None
    compensation_daily: Optional[Compensation_daily] = Field(None, description="Compensation for daily target hours in minutes")
    compensation_monthly: Optional[Compensation_monthly] = Field(None, description="Compensation for monthly target hours in minutes")
    holiday_fixed_credit: Optional[Holiday_fixed_credit] = None
    surcharge_models_id: Optional[Surcharge_models_id] = None

class targethours__id__put_InputModel(BaseModel):
    id: targethours__id__put_id_InputModel
    requestBody: targethours__id__put_RequestBodyModel


targethours__id__delete_id_InputModel = int

class targethours__id__delete_InputModel(BaseModel):
    id: targethours__id__delete_id_InputModel


userreports_get_year_InputModel = int

class userreports_get_InputModel(BaseModel):
    year: userreports_get_year_InputModel
    type: UserReportType


userreports__id__get_id_InputModel = int

userreports__id__get_year_InputModel = int

class userreports__id__get_InputModel(BaseModel):
    id: userreports__id__get_id_InputModel
    year: userreports__id__get_year_InputModel
    type: UserReportType


class v2_accessGroups_get_InputModel(BaseModel):
    pass


class v2_accessGroups_post_RequestBodyModel(BaseModel):
    name: Name
    users_ids: Optional[Users_ids] = Field(None, description="IDs of the access group members")

class v2_accessGroups_post_InputModel(BaseModel):
    requestBody: v2_accessGroups_post_RequestBodyModel


v2_accessGroups__accessGroupsId__customers_put_accessGroupsId_InputModel = int

class v2_accessGroups__accessGroupsId__customers_put_RequestBodyModel(BaseModel):
    id: Id
    type: AccessType
    value: AccessValue

class v2_accessGroups__accessGroupsId__customers_put_InputModel(BaseModel):
    accessGroupsId: v2_accessGroups__accessGroupsId__customers_put_accessGroupsId_InputModel
    requestBody: v2_accessGroups__accessGroupsId__customers_put_RequestBodyModel


v2_accessGroups__accessGroupsId__customers_general_put_accessGroupsId_InputModel = int

class v2_accessGroups__accessGroupsId__customers_general_put_RequestBodyModel(BaseModel):
    type: AccessType
    value: AccessValue

class v2_accessGroups__accessGroupsId__customers_general_put_InputModel(BaseModel):
    accessGroupsId: v2_accessGroups__accessGroupsId__customers_general_put_accessGroupsId_InputModel
    requestBody: v2_accessGroups__accessGroupsId__customers_general_put_RequestBodyModel


v2_accessGroups__accessGroupsId__customersProjects_get_accessGroupsId_InputModel = int

class v2_accessGroups__accessGroupsId__customersProjects_get_InputModel(BaseModel):
    accessGroupsId: v2_accessGroups__accessGroupsId__customersProjects_get_accessGroupsId_InputModel


v2_accessGroups__accessGroupsId__projects_put_accessGroupsId_InputModel = int

class v2_accessGroups__accessGroupsId__projects_put_RequestBodyModel(BaseModel):
    id: Id
    type: AccessType
    value: ApiAccessGroupsProjectsV2_AccessValueForPut

class v2_accessGroups__accessGroupsId__projects_put_InputModel(BaseModel):
    accessGroupsId: v2_accessGroups__accessGroupsId__projects_put_accessGroupsId_InputModel
    requestBody: v2_accessGroups__accessGroupsId__projects_put_RequestBodyModel


v2_accessGroups__accessGroupsId__services_get_accessGroupsId_InputModel = int

class v2_accessGroups__accessGroupsId__services_get_InputModel(BaseModel):
    accessGroupsId: v2_accessGroups__accessGroupsId__services_get_accessGroupsId_InputModel


v2_accessGroups__accessGroupsId__services_put_accessGroupsId_InputModel = int

class v2_accessGroups__accessGroupsId__services_put_RequestBodyModel(BaseModel):
    id: Id
    type: ApiAccessGroupsServicesV2_AccessTypeForPut
    value: ApiAccessGroupsServicesV2_AccessValueForPut

class v2_accessGroups__accessGroupsId__services_put_InputModel(BaseModel):
    accessGroupsId: v2_accessGroups__accessGroupsId__services_put_accessGroupsId_InputModel
    requestBody: v2_accessGroups__accessGroupsId__services_put_RequestBodyModel


v2_accessGroups__accessGroupsId__services_general_put_accessGroupsId_InputModel = int

class v2_accessGroups__accessGroupsId__services_general_put_RequestBodyModel(BaseModel):
    type: ApiAccessGroupsServicesGeneralV2_AccessTypeForPut
    value: AccessValue

class v2_accessGroups__accessGroupsId__services_general_put_InputModel(BaseModel):
    accessGroupsId: v2_accessGroups__accessGroupsId__services_general_put_accessGroupsId_InputModel
    requestBody: v2_accessGroups__accessGroupsId__services_general_put_RequestBodyModel


v2_accessGroups__id__get_id_InputModel = int

class v2_accessGroups__id__get_InputModel(BaseModel):
    id: v2_accessGroups__id__get_id_InputModel


v2_accessGroups__id__put_id_InputModel = int

class v2_accessGroups__id__put_RequestBodyModel(BaseModel):
    name: Optional[Name] = None
    users_ids: Optional[Users_ids] = Field(None, description="IDs of the access group members")

class v2_accessGroups__id__put_InputModel(BaseModel):
    id: v2_accessGroups__id__put_id_InputModel
    requestBody: v2_accessGroups__id__put_RequestBodyModel


v2_accessGroups__id__delete_id_InputModel = int

class v2_accessGroups__id__delete_InputModel(BaseModel):
    id: v2_accessGroups__id__delete_id_InputModel


class v2_aggregates_users_me_get_InputModel(BaseModel):
    pass


v2_clock_get_users_id_InputModel = int

class v2_clock_get_InputModel(BaseModel):
    users_id: v2_clock_get_users_id_InputModel


Services_idItem = int

Services_id = List[Services_idItem]

class v2_clock_post_RequestBodyModel(BaseModel):
    customers_id: Customers_id
    services_id: Services_id
    billable: Optional[Billable] = None
    duration_transfer: Optional[Union[int, None]] = None
    projects_id: Optional[Union[int, None]] = None
    subprojects_id: Optional[Union[int, None]] = None
    text: Optional[Union[str, None]] = None
    time_since: Optional[Union[str, None]] = Field(None, example='2023-02-28T12:00:00Z')
    users_id: Optional[Union[int, None]] = None

class v2_clock_post_InputModel(BaseModel):
    requestBody: v2_clock_post_RequestBodyModel


v2_clock__id__put_id_InputModel = int

class v2_clock__id__put_RequestBodyModel(BaseModel):
    time_since: Optional[Union[str, None]] = Field(None, example='2023-02-28T12:00:00Z')
    time_since_before: Optional[Union[str, None]] = Field(None, example='2023-02-28T12:00:00Z')
    time_until_before: Optional[Union[str, None]] = Field(None, example='2023-02-28T12:00:00Z')
    duration: Optional[Union[int, None]] = None
    duration_before: Optional[Union[int, None]] = None

class v2_clock__id__put_InputModel(BaseModel):
    id: v2_clock__id__put_id_InputModel
    requestBody: v2_clock__id__put_RequestBodyModel


v2_clock__id__delete_id_InputModel = int

class v2_clock__id__delete_InputModel(BaseModel):
    id: v2_clock__id__delete_id_InputModel
    away: Union[int, None]
    time_until: Union[str, None]
    users_id: Union[int, None]
    start_new: Union[bool, None]


v2_entries_get_time_since_InputModel = str

v2_entries_get_time_until_InputModel = str

Budget_type = Union[BudgetOption, Any]

class v2_entries_get_filter_InputModel(BaseModel):
    users_id: Optional[Union[int, None]] = None
    customers_id: Optional[Union[int, None]] = None
    projects_id: Optional[Union[int, None]] = None
    subprojects_id: Optional[Union[int, None]] = None
    services_id: Optional[Union[int, None]] = None
    lumpsum_services_id: Optional[Union[int, None]] = None
    billable: Optional[Billable] = None
    texts_id: Optional[Union[int, None]] = None
    text: Optional[Union[str, None]] = None
    budget_type: Optional[Budget_type] = None

v2_entries_get_page_InputModel = int

v2_entries_get_items_per_page_InputModel = int

class v2_entries_get_InputModel(BaseModel):
    time_since: v2_entries_get_time_since_InputModel
    time_until: v2_entries_get_time_until_InputModel
    calc_also_revenues_for_projects_with_hard_budget: Union[bool, None]
    enhanced_list: Union[bool, None]
    filter: v2_entries_get_filter_InputModel
    page: v2_entries_get_page_InputModel
    items_per_page: v2_entries_get_items_per_page_InputModel


Lumpsum_services_id = int

Text = str

Time_clocked_since = str

class v2_entries_post_RequestBodyModel(BaseModel):
    time_since: Optional[Time_since] = Field(None, example='2023-02-28T12:00:00Z')
    time_until: Optional[Time_until] = Field(None, example='2023-02-28T12:00:00Z')
    customers_id: Customers_id
    billable: Billable
    projects_id: Optional[Projects_id] = None
    subprojects_id: Optional[Subprojects_id] = None
    services_id: Optional[Services_id] = None
    lumpsum_services_id: Optional[Lumpsum_services_id] = None
    users_id: Optional[Users_id] = None
    clocked_offline: Optional[Clocked_offline] = None
    duration: Optional[Duration] = None
    lumpsum: Optional[Lumpsum] = None
    hourly_rate: Optional[Hourly_rate] = None
    lumpsum_services_amount: Optional[Lumpsum_services_amount] = None
    text: Optional[Text] = None
    time_clocked_since: Optional[Time_clocked_since] = None

class v2_entries_post_InputModel(BaseModel):
    requestBody: v2_entries_post_RequestBodyModel


v2_entries__id__get_id_InputModel = int

class v2_entries__id__get_InputModel(BaseModel):
    id: v2_entries__id__get_id_InputModel


v2_entries__id__put_id_InputModel = int

class v2_entries__id__put_RequestBodyModel(BaseModel):
    time_since: Optional[Time_since] = Field(None, example='2023-02-28T12:00:00Z')
    time_until: Optional[Time_until] = Field(None, example='2023-02-28T12:00:00Z')
    customers_id: Optional[Customers_id] = None
    billable: Optional[Billable] = None
    projects_id: Optional[Projects_id] = None
    subprojects_id: Optional[Subprojects_id] = None
    services_id: Optional[Services_id] = None
    lumpsum_services_id: Optional[Lumpsum_services_id] = None
    users_id: Optional[Users_id] = None
    duration: Optional[Duration] = None
    lumpsum: Optional[Lumpsum] = None
    hourly_rate: Optional[Hourly_rate] = None
    lumpsum_services_amount: Optional[Lumpsum_services_amount] = None
    text: Optional[Text] = None

class v2_entries__id__put_InputModel(BaseModel):
    id: v2_entries__id__put_id_InputModel
    requestBody: v2_entries__id__put_RequestBodyModel


v2_entries__id__delete_id_InputModel = int

class v2_entries__id__delete_InputModel(BaseModel):
    id: v2_entries__id__delete_id_InputModel


v2_entrygroups_get_time_since_InputModel = str

v2_entrygroups_get_time_until_InputModel = str

v2_entrygroups_get_grouping_InputModel = List[Grouping]

class v2_entrygroups_get_filter_InputModel(BaseModel):
    users_id: Optional[Union[int, None]] = None
    teams_id: Optional[Union[int, None]] = None
    customers_id: Optional[Union[int, None]] = None
    projects_id: Optional[Union[int, None]] = None
    subprojects_id: Optional[Union[int, None]] = None
    services_id: Optional[Union[int, None]] = None
    lumpsum_services_id: Optional[Union[int, None]] = None
    billable: Optional[Billable] = None
    texts_id: Optional[Union[int, None]] = None
    text: Optional[Union[str, None]] = None
    budget_type: Optional[Budget_type] = None

class v2_entrygroups_get_InputModel(BaseModel):
    time_since: v2_entrygroups_get_time_since_InputModel
    time_until: v2_entrygroups_get_time_until_InputModel
    grouping: v2_entrygroups_get_grouping_InputModel
    round_to_minutes: Union[int, None]
    prepend_customer_to_project_name: Union[bool, None]
    calc_also_revenues_for_projects_with_hard_budget: Union[bool, None]
    filter: v2_entrygroups_get_filter_InputModel


class Filter(BaseModel):
    users_id: Optional[Union[int, None]] = None
    teams_id: Optional[Union[int, None]] = None
    customers_id: Optional[Union[int, None]] = None
    projects_id: Optional[Union[int, None]] = None
    subprojects_id: Optional[Union[int, None]] = None
    services_id: Optional[Union[int, None]] = None
    lumpsum_services_id: Optional[Union[int, None]] = None
    billable: Optional[Billable] = None
    texts_id: Optional[Union[int, None]] = None
    text: Optional[Union[str, None]] = None
    budget_type: Optional[Budget_type] = None

class v2_entrygroups_put_RequestBodyModel(BaseModel):
    time_since: Time_since = Field(None, example='2023-02-28T12:00:00Z')
    time_until: Time_until = Field(None, example='2023-02-28T12:00:00Z')
    users_id: Optional[Union[int, None]] = None
    customers_id: Optional[Union[int, None]] = None
    projects_id: Optional[Union[int, None]] = None
    subprojects_id: Optional[Union[int, None]] = None
    services_id: Optional[Union[int, None]] = None
    lumpsum_services_id: Optional[Union[int, None]] = None
    billable: Optional[Billable] = None
    text: Optional[Union[str, None]] = None
    hourly_rate: Optional[Union[float, None]] = None
    confirm_key: Optional[Confirm_key] = Field(None, description="For safety, the api will respond with a confirmation key with which you have to request once again in order to confirm your edit action")
    filter: Optional[Filter] = None

class v2_entrygroups_put_InputModel(BaseModel):
    requestBody: v2_entrygroups_put_RequestBodyModel


v2_entrygroups_delete_time_since_InputModel = str

v2_entrygroups_delete_time_until_InputModel = str

v2_entrygroups_delete_confirm_key_InputModel = str

class v2_entrygroups_delete_filter_InputModel(BaseModel):
    users_id: Optional[Union[int, None]] = None
    teams_id: Optional[Union[int, None]] = None
    customers_id: Optional[Union[int, None]] = None
    projects_id: Optional[Union[int, None]] = None
    subprojects_id: Optional[Union[int, None]] = None
    services_id: Optional[Union[int, None]] = None
    lumpsum_services_id: Optional[Union[int, None]] = None
    billable: Optional[Billable] = None
    texts_id: Optional[Union[int, None]] = None
    text: Optional[Union[str, None]] = None
    budget_type: Optional[Budget_type] = None

class v2_entrygroups_delete_InputModel(BaseModel):
    time_since: v2_entrygroups_delete_time_since_InputModel
    time_until: v2_entrygroups_delete_time_until_InputModel
    confirm_key: v2_entrygroups_delete_confirm_key_InputModel
    filter: v2_entrygroups_delete_filter_InputModel


class v2_holidaysQuota_get_filter_InputModel(BaseModel):
    users_id: Optional[Users_id] = None
    year: Optional[Year] = None

v2_holidaysQuota_get_users_id_InputModel = int

v2_holidaysQuota_get_year_InputModel = int

class v2_holidaysQuota_get_InputModel(BaseModel):
    filter: v2_holidaysQuota_get_filter_InputModel
    users_id: v2_holidaysQuota_get_users_id_InputModel
    year: v2_holidaysQuota_get_year_InputModel


class v2_holidaysQuota_post_RequestBodyModel(BaseModel):
    users_id: Users_id
    year_since: Year_since = Field(None, description="Year from which on the holiday quota setting applies.", example='2023')
    year_until: Optional[Union[int, None]] = Field(None, description="Year until the holiday quota setting applies.", example='2023')
    count: Count = Field(None, description="Amount of holidays.")
    note: Optional[Union[str, None]] = None

class v2_holidaysQuota_post_InputModel(BaseModel):
    requestBody: v2_holidaysQuota_post_RequestBodyModel


v2_holidaysQuota__id__get_id_InputModel = int

class v2_holidaysQuota__id__get_InputModel(BaseModel):
    id: v2_holidaysQuota__id__get_id_InputModel


v2_holidaysQuota__id__put_id_InputModel = int

class v2_holidaysQuota__id__put_RequestBodyModel(BaseModel):
    year_since: Optional[Year_since] = Field(None, description="Year from which on the holiday quota setting applies.", example='2023')
    year_until: Optional[Union[int, None]] = Field(None, description="Year until the holiday quota setting applies.", example='2023')
    count: Optional[Count] = Field(None, description="Amount of holidays.")
    note: Optional[Union[str, None]] = None

class v2_holidaysQuota__id__put_InputModel(BaseModel):
    id: v2_holidaysQuota__id__put_id_InputModel
    requestBody: v2_holidaysQuota__id__put_RequestBodyModel


v2_holidaysQuota__id__delete_id_InputModel = int

class v2_holidaysQuota__id__delete_InputModel(BaseModel):
    id: v2_holidaysQuota__id__delete_id_InputModel


v2_individualUserAccess__usersId__clear_post_usersId_InputModel = int

class v2_individualUserAccess__usersId__clear_post_InputModel(BaseModel):
    usersId: v2_individualUserAccess__usersId__clear_post_usersId_InputModel


v2_individualUserAccess__usersId__customers_put_usersId_InputModel = int

class v2_individualUserAccess__usersId__customers_put_RequestBodyModel(BaseModel):
    id: Id
    type: AccessType
    value: AccessValue

class v2_individualUserAccess__usersId__customers_put_InputModel(BaseModel):
    usersId: v2_individualUserAccess__usersId__customers_put_usersId_InputModel
    requestBody: v2_individualUserAccess__usersId__customers_put_RequestBodyModel


v2_individualUserAccess__usersId__customers_general_put_usersId_InputModel = int

class v2_individualUserAccess__usersId__customers_general_put_RequestBodyModel(BaseModel):
    type: AccessType
    value: AccessValue

class v2_individualUserAccess__usersId__customers_general_put_InputModel(BaseModel):
    usersId: v2_individualUserAccess__usersId__customers_general_put_usersId_InputModel
    requestBody: v2_individualUserAccess__usersId__customers_general_put_RequestBodyModel


v2_individualUserAccess__usersId__customersProjects_get_usersId_InputModel = int

class v2_individualUserAccess__usersId__customersProjects_get_InputModel(BaseModel):
    usersId: v2_individualUserAccess__usersId__customersProjects_get_usersId_InputModel


v2_individualUserAccess__usersId__projects_put_usersId_InputModel = int

class v2_individualUserAccess__usersId__projects_put_RequestBodyModel(BaseModel):
    id: Id
    type: AccessType
    value: ApiAccessGroupsProjectsV2_AccessValueForPut

class v2_individualUserAccess__usersId__projects_put_InputModel(BaseModel):
    usersId: v2_individualUserAccess__usersId__projects_put_usersId_InputModel
    requestBody: v2_individualUserAccess__usersId__projects_put_RequestBodyModel


v2_individualUserAccess__usersId__services_get_usersId_InputModel = int

class v2_individualUserAccess__usersId__services_get_InputModel(BaseModel):
    usersId: v2_individualUserAccess__usersId__services_get_usersId_InputModel


v2_individualUserAccess__usersId__services_put_usersId_InputModel = int

class v2_individualUserAccess__usersId__services_put_RequestBodyModel(BaseModel):
    id: Id
    type: ApiAccessGroupsServicesV2_AccessTypeForPut
    value: ApiAccessGroupsServicesV2_AccessValueForPut

class v2_individualUserAccess__usersId__services_put_InputModel(BaseModel):
    usersId: v2_individualUserAccess__usersId__services_put_usersId_InputModel
    requestBody: v2_individualUserAccess__usersId__services_put_RequestBodyModel


v2_individualUserAccess__usersId__services_general_put_usersId_InputModel = int

class v2_individualUserAccess__usersId__services_general_put_RequestBodyModel(BaseModel):
    type: ApiAccessGroupsServicesGeneralV2_AccessTypeForPut
    value: AccessValue

class v2_individualUserAccess__usersId__services_general_put_InputModel(BaseModel):
    usersId: v2_individualUserAccess__usersId__services_general_put_usersId_InputModel
    requestBody: v2_individualUserAccess__usersId__services_general_put_RequestBodyModel


v2_nonbusinessDays_get_year_InputModel = int

v2_nonbusinessDays_get_nonbusiness_group_id_InputModelItem = int

v2_nonbusinessDays_get_nonbusiness_group_id_InputModel = List[v2_nonbusinessDays_get_nonbusiness_group_id_InputModelItem]

class v2_nonbusinessDays_get_InputModel(BaseModel):
    year: v2_nonbusinessDays_get_year_InputModel
    nonbusiness_group_id: v2_nonbusinessDays_get_nonbusiness_group_id_InputModel


class v2_nonbusinessDays_post_RequestBodyModel(BaseModel):
    nonbusiness_group_id: Nonbusiness_group_id = Field(None, description="Default: Company default nonbusiness group")
    type: NonbusinessDayType
    name: Name
    half_day: Optional[Half_day] = None
    surcharge_special: Optional[Surcharge_special] = None
    special_id: Optional[Special_id] = None
    day: Optional[Day] = None
    month: Optional[Month] = None
    year: Optional[Year] = None

class v2_nonbusinessDays_post_InputModel(BaseModel):
    requestBody: v2_nonbusinessDays_post_RequestBodyModel


v2_nonbusinessDays__id__get_id_InputModel = int

v2_nonbusinessDays__id__get_year_InputModel = int

class v2_nonbusinessDays__id__get_InputModel(BaseModel):
    id: v2_nonbusinessDays__id__get_id_InputModel
    year: v2_nonbusinessDays__id__get_year_InputModel


v2_nonbusinessDays__id__put_id_InputModel = int

class v2_nonbusinessDays__id__put_RequestBodyModel(BaseModel):
    type: Optional[NonbusinessDayType] = None
    name: Optional[Name] = None
    half_day: Optional[Half_day] = None
    surcharge_special: Optional[Surcharge_special] = None
    special_id: Optional[Union[int, None]] = None
    day: Optional[Union[int, None]] = None
    month: Optional[Union[int, None]] = None
    year: Optional[Union[int, None]] = None

class v2_nonbusinessDays__id__put_InputModel(BaseModel):
    id: v2_nonbusinessDays__id__put_id_InputModel
    requestBody: v2_nonbusinessDays__id__put_RequestBodyModel


v2_nonbusinessDays__id__delete_id_InputModel = int

class v2_nonbusinessDays__id__delete_InputModel(BaseModel):
    id: v2_nonbusinessDays__id__delete_id_InputModel


class v2_nonbusinessGroups_get_InputModel(BaseModel):
    pass


class v2_nonbusinessGroups_post_RequestBodyModel(BaseModel):
    name: Name
    preset: Optional[Preset] = None

class v2_nonbusinessGroups_post_InputModel(BaseModel):
    requestBody: v2_nonbusinessGroups_post_RequestBodyModel


v2_nonbusinessGroups__id__get_id_InputModel = int

class v2_nonbusinessGroups__id__get_InputModel(BaseModel):
    id: v2_nonbusinessGroups__id__get_id_InputModel


v2_nonbusinessGroups__id__put_id_InputModel = int

class v2_nonbusinessGroups__id__put_RequestBodyModel(BaseModel):
    name: Optional[Name] = None

class v2_nonbusinessGroups__id__put_InputModel(BaseModel):
    id: v2_nonbusinessGroups__id__put_id_InputModel
    requestBody: v2_nonbusinessGroups__id__put_RequestBodyModel


v2_nonbusinessGroups__id__delete_id_InputModel = int

class v2_nonbusinessGroups__id__delete_InputModel(BaseModel):
    id: v2_nonbusinessGroups__id__delete_id_InputModel


v2_users__id__access_customers_projects_get_id_InputModel = int

class v2_users__id__access_customers_projects_get_InputModel(BaseModel):
    id: v2_users__id__access_customers_projects_get_id_InputModel


v2_users__id__access_services_get_id_InputModel = int

class v2_users__id__access_services_get_InputModel(BaseModel):
    id: v2_users__id__access_services_get_id_InputModel


v2_usersNonbusinessDays_get_year_InputModel = int

Users_idItem = int

class v2_usersNonbusinessDays_get_filter_InputModel(BaseModel):
    users_id: Optional[Users_id] = None

v2_usersNonbusinessDays_get_page_InputModel = int

v2_usersNonbusinessDays_get_items_per_page_InputModel = int

class v2_usersNonbusinessDays_get_InputModel(BaseModel):
    year: v2_usersNonbusinessDays_get_year_InputModel
    filter: v2_usersNonbusinessDays_get_filter_InputModel
    page: v2_usersNonbusinessDays_get_page_InputModel
    items_per_page: v2_usersNonbusinessDays_get_items_per_page_InputModel


v2_workTimes_get_date_since_InputModel = str

v2_workTimes_get_date_until_InputModel = str

v2_workTimes_get_users_id_InputModel = int

class v2_workTimes_get_InputModel(BaseModel):
    date_since: v2_workTimes_get_date_since_InputModel
    date_until: v2_workTimes_get_date_until_InputModel
    users_id: v2_workTimes_get_users_id_InputModel


v2_workTimes_changeRequests_get_date_since_InputModel = str

v2_workTimes_changeRequests_get_date_until_InputModel = str

v2_workTimes_changeRequests_get_users_id_InputModel = int

v2_workTimes_changeRequests_get_scope_InputModel = str

v2_workTimes_changeRequests_get_teams_id_InputModel = List[Union[int, None]]

class v2_workTimes_changeRequests_get_InputModel(BaseModel):
    date_since: v2_workTimes_changeRequests_get_date_since_InputModel
    date_until: v2_workTimes_changeRequests_get_date_until_InputModel
    users_id: v2_workTimes_changeRequests_get_users_id_InputModel
    status: ChangeRequestStatus
    scope: v2_workTimes_changeRequests_get_scope_InputModel
    teams_id: v2_workTimes_changeRequests_get_teams_id_InputModel


class v2_workTimes_changeRequests_post_RequestBodyModel(BaseModel):
    date: Date = Field(None, example='2023-02-28')
    users_id: Users_id
    changes: Changes

class v2_workTimes_changeRequests_post_InputModel(BaseModel):
    requestBody: v2_workTimes_changeRequests_post_RequestBodyModel


v2_workTimes_changeRequests__id__delete_id_InputModel = int

class v2_workTimes_changeRequests__id__delete_InputModel(BaseModel):
    id: v2_workTimes_changeRequests__id__delete_id_InputModel


v2_workTimes_changeRequests__id__approve_post_id_InputModel = int

class v2_workTimes_changeRequests__id__approve_post_InputModel(BaseModel):
    id: v2_workTimes_changeRequests__id__approve_post_id_InputModel


v2_workTimes_changeRequests__id__decline_post_id_InputModel = int

class v2_workTimes_changeRequests__id__decline_post_InputModel(BaseModel):
    id: v2_workTimes_changeRequests__id__decline_post_id_InputModel


Fulltext = str

class v3_customers_get_filter_InputModel(BaseModel):
    active: Optional[Active] = None
    fulltext: Optional[Fulltext] = None

v3_customers_get_sort_InputModel = List[SortIdNameActive]

v3_customers_get_page_InputModel = int

v3_customers_get_items_per_page_InputModel = int

class v3_customers_get_InputModel(BaseModel):
    filter: v3_customers_get_filter_InputModel
    sort: v3_customers_get_sort_InputModel
    scope: CustomerProjectScope
    page: v3_customers_get_page_InputModel
    items_per_page: v3_customers_get_items_per_page_InputModel


Color = Union[CustomerColor, Any]

class v3_customers_post_RequestBodyModel(BaseModel):
    name: Name
    number: Optional[Union[str, None]] = Field(None, description="Freely selectable number for the customer")
    active: Optional[Active] = None
    billable_default: Optional[Billable_default] = None
    note: Optional[Union[str, None]] = Field(None, description="Can only be set by owners or workers with elevated access `manage_customers_and_projects`")
    color: Optional[Color] = Field(None, description="Possible values:\n- `1`: BloodOrange\n- `2`: Sunflower\n- `3`: LightGreen\n- `4`: Caribbean\n- `5`: Sky\n- `6`: BrandBlue\n- `7`: BluePurple\n- `8`: Magenta\n- `9`: ChewingGum")
    bill_service_id: Optional[Union[str, None]] = Field(None, description="Can only be set by owners or workers with elevated access `manage_customers_and_projects` and if a billing application with customers support is linked up")

class v3_customers_post_InputModel(BaseModel):
    requestBody: v3_customers_post_RequestBodyModel


v3_customers_countProjects_get_customers_id_InputModelItem = int

v3_customers_countProjects_get_customers_id_InputModel = List[v3_customers_countProjects_get_customers_id_InputModelItem]

class v3_customers_countProjects_get_InputModel(BaseModel):
    customers_id: v3_customers_countProjects_get_customers_id_InputModel
    scope: CustomerProjectScope


v3_customers__id__get_id_InputModel = int

class v3_customers__id__get_InputModel(BaseModel):
    id: v3_customers__id__get_id_InputModel


v3_customers__id__put_id_InputModel = int

class v3_customers__id__put_RequestBodyModel(BaseModel):
    name: Optional[Name] = None
    number: Optional[Union[str, None]] = Field(None, description="Freely selectable number for the customer")
    active: Optional[Active] = None
    billable_default: Optional[Billable_default] = None
    note: Optional[Union[str, None]] = Field(None, description="Can only be set by owners or workers with elevated access `manage_customers_and_projects`")
    color: Optional[CustomerColor] = Field(None, description="Possible values:\n- `1`: BloodOrange\n- `2`: Sunflower\n- `3`: LightGreen\n- `4`: Caribbean\n- `5`: Sky\n- `6`: BrandBlue\n- `7`: BluePurple\n- `8`: Magenta\n- `9`: ChewingGum")
    bill_service_id: Optional[Union[str, None]] = Field(None, description="Can only be set by owners or workers with elevated access `manage_customers_and_projects` and if a billing application with customers support is linked up")

class v3_customers__id__put_InputModel(BaseModel):
    id: v3_customers__id__put_id_InputModel
    requestBody: v3_customers__id__put_RequestBodyModel


v3_customers__id__delete_id_InputModel = int

v3_customers__id__delete_dry_run_InputModel = bool

v3_customers__id__delete_force_InputModel = bool

class v3_customers__id__delete_InputModel(BaseModel):
    id: v3_customers__id__delete_id_InputModel
    dry_run: v3_customers__id__delete_dry_run_InputModel
    force: v3_customers__id__delete_force_InputModel


v3_entriesTexts_get_term_InputModel = str

v3_entriesTexts_get_items_InputModel = int

Projects_idItem = int

class v3_entriesTexts_get_filter_InputModel(BaseModel):
    customers_id: Optional[Customers_id] = None
    projects_id: Optional[Projects_id] = None
    services_id: Optional[Services_id] = None
    users_id: Optional[Users_id] = None
    billable: Optional[Billable] = None
    time_since: Optional[Time_since] = Field(None, example='2023-02-28')
    time_until: Optional[Time_until] = Field(None, example='2023-02-28')
    day: Optional[Day] = Field(None, example='2023-02-28')

class v3_entriesTexts_get_InputModel(BaseModel):
    term: v3_entriesTexts_get_term_InputModel
    mode: EntryTextMode
    items: v3_entriesTexts_get_items_InputModel
    filter: v3_entriesTexts_get_filter_InputModel


v3_holidaysCarry_get_year_InputModel = int

v3_holidaysCarry_get_users_id_InputModel = int

class v3_holidaysCarry_get_InputModel(BaseModel):
    year: v3_holidaysCarry_get_year_InputModel
    users_id: v3_holidaysCarry_get_users_id_InputModel


class v3_holidaysCarry_post_RequestBodyModel(BaseModel):
    year: Year = Field(None, description="Year for which the holiday carryover applies.", example='2023')
    users_id: Users_id
    count: Count = Field(None, description="Only full and half values allowed.")
    note: Optional[Union[str, None]] = None

class v3_holidaysCarry_post_InputModel(BaseModel):
    requestBody: v3_holidaysCarry_post_RequestBodyModel


v3_holidaysCarry__id__get_id_InputModel = int

class v3_holidaysCarry__id__get_InputModel(BaseModel):
    id: v3_holidaysCarry__id__get_id_InputModel


v3_holidaysCarry__id__put_id_InputModel = int

class v3_holidaysCarry__id__put_RequestBodyModel(BaseModel):
    year: Optional[Year] = Field(None, description="Year for which the holiday carryover applies.", example='2023')
    count: Optional[Count] = Field(None, description="Only full and half values allowed.")
    note: Optional[Union[str, None]] = None

class v3_holidaysCarry__id__put_InputModel(BaseModel):
    id: v3_holidaysCarry__id__put_id_InputModel
    requestBody: v3_holidaysCarry__id__put_RequestBodyModel


v3_holidaysCarry__id__delete_id_InputModel = int

class v3_holidaysCarry__id__delete_InputModel(BaseModel):
    id: v3_holidaysCarry__id__delete_id_InputModel


v3_overtimeCarry_get_year_InputModel = int

v3_overtimeCarry_get_users_id_InputModel = int

class v3_overtimeCarry_get_InputModel(BaseModel):
    year: v3_overtimeCarry_get_year_InputModel
    users_id: v3_overtimeCarry_get_users_id_InputModel


class v3_overtimeCarry_post_RequestBodyModel(BaseModel):
    year: Year
    users_id: Users_id
    hours: Hours
    note: Optional[Union[str, None]] = None

class v3_overtimeCarry_post_InputModel(BaseModel):
    requestBody: v3_overtimeCarry_post_RequestBodyModel


v3_overtimeCarry__id__get_id_InputModel = int

class v3_overtimeCarry__id__get_InputModel(BaseModel):
    id: v3_overtimeCarry__id__get_id_InputModel


v3_overtimeCarry__id__put_id_InputModel = int

class v3_overtimeCarry__id__put_RequestBodyModel(BaseModel):
    year: Optional[Year] = None
    hours: Optional[Hours] = None
    note: Optional[Union[str, None]] = None

class v3_overtimeCarry__id__put_InputModel(BaseModel):
    id: v3_overtimeCarry__id__put_id_InputModel
    requestBody: v3_overtimeCarry__id__put_RequestBodyModel


v3_overtimeCarry__id__delete_id_InputModel = int

class v3_overtimeCarry__id__delete_InputModel(BaseModel):
    id: v3_overtimeCarry__id__delete_id_InputModel


v3_overtimeReductions_get_users_id_InputModelItem = int

v3_overtimeReductions_get_users_id_InputModel = List[v3_overtimeReductions_get_users_id_InputModelItem]

class v3_overtimeReductions_get_InputModel(BaseModel):
    users_id: v3_overtimeReductions_get_users_id_InputModel


class v3_overtimeReductions_post_RequestBodyModel(BaseModel):
    users_id: Users_id
    date: Date = Field(None, example='2023-02-28')
    hours: Hours
    note: Optional[Union[str, None]] = None

class v3_overtimeReductions_post_InputModel(BaseModel):
    requestBody: v3_overtimeReductions_post_RequestBodyModel


v3_overtimeReductions__id__get_id_InputModel = int

class v3_overtimeReductions__id__get_InputModel(BaseModel):
    id: v3_overtimeReductions__id__get_id_InputModel


v3_overtimeReductions__id__put_id_InputModel = int

class v3_overtimeReductions__id__put_RequestBodyModel(BaseModel):
    date: Optional[Date] = Field(None, example='2023-02-28')
    hours: Optional[Hours] = None
    note: Optional[Union[str, None]] = None

class v3_overtimeReductions__id__put_InputModel(BaseModel):
    id: v3_overtimeReductions__id__put_id_InputModel
    requestBody: v3_overtimeReductions__id__put_RequestBodyModel


v3_overtimeReductions__id__delete_id_InputModel = int

class v3_overtimeReductions__id__delete_InputModel(BaseModel):
    id: v3_overtimeReductions__id__delete_id_InputModel


v3_projects__id__setBilled_put_id_InputModel = int

class v3_projects__id__setBilled_put_RequestBodyModel(BaseModel):
    billed: Optional[Billed] = None
    billed_money: Optional[Union[float, None]] = None

class v3_projects__id__setBilled_put_InputModel(BaseModel):
    id: v3_projects__id__setBilled_put_id_InputModel
    requestBody: v3_projects__id__setBilled_put_RequestBodyModel


Budget_source = List[BudgetSource]

class v3_projects_reports_get_filter_InputModel(BaseModel):
    active: Optional[Active] = None
    fulltext: Optional[Fulltext] = None
    budget_source: Optional[Budget_source] = None

v3_projects_reports_get_sort_InputModel = List[ApiProjectsReportsV3_SortForIndex]

v3_projects_reports_get_page_InputModel = int

v3_projects_reports_get_items_per_page_InputModel = int

class v3_projects_reports_get_InputModel(BaseModel):
    filter: v3_projects_reports_get_filter_InputModel
    sort: v3_projects_reports_get_sort_InputModel
    page: v3_projects_reports_get_page_InputModel
    items_per_page: v3_projects_reports_get_items_per_page_InputModel


class v3_subprojects_get_filter_InputModel(BaseModel):
    active: Optional[Active] = None
    completed: Optional[Completed] = None
    fulltext: Optional[Fulltext] = None
    projects_id: Optional[Projects_id] = None

v3_subprojects_get_page_InputModel = int

v3_subprojects_get_items_per_page_InputModel = int

class v3_subprojects_get_InputModel(BaseModel):
    filter: v3_subprojects_get_filter_InputModel
    sort: SortIdName
    page: v3_subprojects_get_page_InputModel
    items_per_page: v3_subprojects_get_items_per_page_InputModel


class v3_subprojects_post_RequestBodyModel(BaseModel):
    projects_id: Projects_id
    name: Name
    billable_default: Optional[Billable_default] = None
    budget: Optional[Budget] = None
    number: Optional[Union[str, None]] = None
    note: Optional[Union[str, None]] = None
    start_date: Optional[Union[str, None]] = Field(None, example='2023-02-28')
    deadline: Optional[Union[str, None]] = Field(None, example='2023-02-28')
    bill_service_id: Optional[Union[str, None]] = None

class v3_subprojects_post_InputModel(BaseModel):
    requestBody: v3_subprojects_post_RequestBodyModel


v3_subprojects__id__get_id_InputModel = int

class v3_subprojects__id__get_InputModel(BaseModel):
    id: v3_subprojects__id__get_id_InputModel


v3_subprojects__id__put_id_InputModel = int

class v3_subprojects__id__put_RequestBodyModel(BaseModel):
    name: Optional[Name] = None
    billable_default: Optional[Billable_default] = None
    budget: Optional[Budget] = None
    number: Optional[Union[str, None]] = None
    note: Optional[Union[str, None]] = None
    start_date: Optional[Union[str, None]] = Field(None, example='2023-02-28')
    deadline: Optional[Union[str, None]] = Field(None, example='2023-02-28')
    bill_service_id: Optional[Union[str, None]] = None

class v3_subprojects__id__put_InputModel(BaseModel):
    id: v3_subprojects__id__put_id_InputModel
    requestBody: v3_subprojects__id__put_RequestBodyModel


v3_subprojects__id__delete_id_InputModel = int

v3_subprojects__id__delete_dry_run_InputModel = bool

v3_subprojects__id__delete_force_InputModel = bool

class v3_subprojects__id__delete_InputModel(BaseModel):
    id: v3_subprojects__id__delete_id_InputModel
    dry_run: v3_subprojects__id__delete_dry_run_InputModel
    force: v3_subprojects__id__delete_force_InputModel


v3_subprojects__id__complete_put_id_InputModel = int

class v3_subprojects__id__complete_put_RequestBodyModel(BaseModel):
    completed: Completed

class v3_subprojects__id__complete_put_InputModel(BaseModel):
    id: v3_subprojects__id__complete_put_id_InputModel
    requestBody: v3_subprojects__id__complete_put_RequestBodyModel


class v3_teams_get_filter_InputModel(BaseModel):
    fulltext: Optional[Fulltext] = None

v3_teams_get_sort_InputModel = List[SortIdName]

v3_teams_get_page_InputModel = int

v3_teams_get_items_per_page_InputModel = int

class v3_teams_get_InputModel(BaseModel):
    filter: v3_teams_get_filter_InputModel
    scope: UserScope
    sort: v3_teams_get_sort_InputModel
    page: v3_teams_get_page_InputModel
    items_per_page: v3_teams_get_items_per_page_InputModel


class v3_teams_post_RequestBodyModel(BaseModel):
    name: Name
    leader: Optional[Union[int, None]] = Field(None, description="The user ID of the team leader")

class v3_teams_post_InputModel(BaseModel):
    requestBody: v3_teams_post_RequestBodyModel


v3_teams__id__get_id_InputModel = int

class v3_teams__id__get_InputModel(BaseModel):
    id: v3_teams__id__get_id_InputModel


v3_teams__id__put_id_InputModel = int

class v3_teams__id__put_RequestBodyModel(BaseModel):
    name: Optional[Name] = None
    leader: Optional[Union[int, None]] = Field(None, description="The user ID of the team leader")

class v3_teams__id__put_InputModel(BaseModel):
    id: v3_teams__id__put_id_InputModel
    requestBody: v3_teams__id__put_RequestBodyModel


v3_teams__id__delete_id_InputModel = int

class v3_teams__id__delete_InputModel(BaseModel):
    id: v3_teams__id__delete_id_InputModel


Teams_id = List[Union[int, None]]

class v3_users_get_filter_InputModel(BaseModel):
    active: Optional[Active] = None
    fulltext: Optional[Fulltext] = None
    teams_id: Optional[Teams_id] = None

v3_users_get_sort_InputModel = List[ApiUsersV3_SortForIndex]

v3_users_get_page_InputModel = int

v3_users_get_items_per_page_InputModel = int

class v3_users_get_InputModel(BaseModel):
    filter: v3_users_get_filter_InputModel
    scope: UserScope
    sort: v3_users_get_sort_InputModel
    page: v3_users_get_page_InputModel
    items_per_page: v3_users_get_items_per_page_InputModel


Show_favorites = bool

Mail_to_user = bool

Edit_lock_sync = bool

class v3_users_post_RequestBodyModel(BaseModel):
    email: Email
    name: Name
    role: Role
    active: Optional[Active] = None
    boss: Optional[Union[int, None]] = None
    number: Optional[Union[str, None]] = None
    language: Optional[Language] = None
    teams_id: Optional[Union[int, None]] = None
    timeformat_12h: Optional[Timeformat_12h] = Field(None, description="Use 12h time format?")
    timezone: Optional[Timezone] = None
    wage_type: Optional[WageType] = None
    weekstart_monday: Optional[Weekstart_monday] = Field(None, description="Start week on Monday?")
    weekend_friday: Optional[Weekend_friday] = Field(None, description="End week on Friday?")
    show_favorites: Optional[Show_favorites] = None
    mail_to_user: Optional[Mail_to_user] = Field(None, description="Sent mail to the new co-worker? (default: false)")
    start_date: Optional[Union[str, None]] = Field(None, example='2023-02-28')
    budget_notifications: Optional[Budget_notifications] = None
    edit_lock: Optional[Union[str, None]] = Field(None, description="The date after the co-worker is not allowed to edit his entries anymore. Can only be set by owners or workers with elevated access `manage_users_access`.", example='2023-02-28')
    edit_lock_dyn: Optional[Edit_lock_dyn] = Field(None, description="Dynamic edit lock for this co-worker. Can only be set by owners or workers with elevated access `manage_users_access`.")
    edit_lock_sync: Optional[Edit_lock_sync] = Field(None, description="Can future changes to the company-wide edit lock overwrite the edit lock for this co-worker? Can only be set by owners or workers with elevated access `manage_users_access`.")
    work_time_edit_lock_days: Optional[Work_time_edit_lock_days] = Field(None, description="Relative work time editing lock in days for the co-worker. Can only be set by owners or workers with elevated access `manage_users_access`.")
    default_holidays_count: Optional[Default_holidays_count] = Field(None, description="Uses the company's default holiday count")
    default_target_hours: Optional[Default_target_hours] = Field(None, description="Uses the company's default target hours")
    work_time_regulations_id: Optional[Union[int, None]] = None
    default_work_time_regulation: Optional[Default_work_time_regulation] = Field(None, description="Uses the company's default work time regulation")
    absence_managers_id: Optional[Absence_managers_id] = None
    access_groups_ids: Optional[Access_groups_ids] = None
    bill_service_id: Optional[Union[str, None]] = None

class v3_users_post_InputModel(BaseModel):
    requestBody: v3_users_post_RequestBodyModel


v3_users__id__get_id_InputModel = int

class v3_users__id__get_InputModel(BaseModel):
    id: v3_users__id__get_id_InputModel
    scope: UserScope


v3_users__id__put_id_InputModel = int

Start_date = str

class v3_users__id__put_RequestBodyModel(BaseModel):
    email: Optional[Email] = None
    name: Optional[Name] = None
    role: Optional[Role] = None
    active: Optional[Active] = None
    boss: Optional[Union[int, None]] = None
    number: Optional[Union[str, None]] = None
    language: Optional[Language] = None
    teams_id: Optional[Union[int, None]] = None
    timeformat_12h: Optional[Timeformat_12h] = Field(None, description="Use 12h time format?")
    timezone: Optional[Timezone] = Field(None, description="Can only be changed for the company creator during the trial phase.")
    wage_type: Optional[WageType] = None
    weekstart_monday: Optional[Weekstart_monday] = Field(None, description="Start week on Monday?")
    weekend_friday: Optional[Weekend_friday] = Field(None, description="End week on Friday?")
    show_favorites: Optional[Show_favorites] = None
    edit_lock: Optional[Union[str, None]] = Field(None, description="The date after the co-worker is not allowed to edit his entries anymore. Can only be managed by owners or workers with elevated access `manage_users_access`.", example='2023-02-28')
    edit_lock_dyn: Optional[Edit_lock_dyn] = Field(None, description="Dynamic edit lock for this co-worker. Can only be managed by owners or workers with elevated access `manage_users_access`.")
    edit_lock_sync: Optional[Edit_lock_sync] = Field(None, description="Can future changes to the company-wide edit lock overwrite the edit lock for this co-worker? Can only be managed by owners or workers with elevated access `manage_users_access`.")
    work_time_edit_lock_days: Optional[Work_time_edit_lock_days] = Field(None, description="Relative work time editing lock in days for the co-worker. Can only be managed by owners or workers with elevated access `manage_users_access`.")
    mail_to_user: Optional[Mail_to_user] = None
    start_date: Optional[Start_date] = Field(None, example='2023-02-28')
    budget_notifications: Optional[Budget_notifications] = None
    default_holidays_count: Optional[Default_holidays_count] = Field(None, description="Uses the company's default holiday count")
    default_target_hours: Optional[Default_target_hours] = Field(None, description="Uses the company's default target hours")
    work_time_regulations_id: Optional[Union[int, None]] = None
    default_work_time_regulation: Optional[Default_work_time_regulation] = Field(None, description="Uses the company's default work time regulation")
    absence_managers_id: Optional[Absence_managers_id] = None
    access_groups_ids: Optional[Access_groups_ids] = None
    bill_service_id: Optional[Union[str, None]] = None

class v3_users__id__put_InputModel(BaseModel):
    id: v3_users__id__put_id_InputModel
    requestBody: v3_users__id__put_RequestBodyModel


v3_users__id__delete_id_InputModel = int

class v3_users__id__delete_InputModel(BaseModel):
    id: v3_users__id__delete_id_InputModel


Nonbusiness_groups_idItem = int

Nonbusiness_groups_id = int

class v3_usersNonbusinessGroups_get_filter_InputModel(BaseModel):
    nonbusiness_groups_id: Optional[Nonbusiness_groups_id] = None
    users_id: Optional[Users_id] = None

v3_usersNonbusinessGroups_get_page_InputModel = int

v3_usersNonbusinessGroups_get_items_per_page_InputModel = int

class v3_usersNonbusinessGroups_get_InputModel(BaseModel):
    filter: v3_usersNonbusinessGroups_get_filter_InputModel
    page: v3_usersNonbusinessGroups_get_page_InputModel
    items_per_page: v3_usersNonbusinessGroups_get_items_per_page_InputModel


class v3_usersNonbusinessGroups_post_RequestBodyModel(BaseModel):
    users_id: Users_id
    nonbusiness_groups_id: Nonbusiness_groups_id
    date_since: Date_since = Field(None, example='2023-02-28')
    date_until: Optional[Union[str, None]] = Field(None, example='2023-02-28')

class v3_usersNonbusinessGroups_post_InputModel(BaseModel):
    requestBody: v3_usersNonbusinessGroups_post_RequestBodyModel


v3_usersNonbusinessGroups__id__get_id_InputModel = int

class v3_usersNonbusinessGroups__id__get_InputModel(BaseModel):
    id: v3_usersNonbusinessGroups__id__get_id_InputModel


v3_usersNonbusinessGroups__id__put_id_InputModel = int

class v3_usersNonbusinessGroups__id__put_RequestBodyModel(BaseModel):
    nonbusiness_groups_id: Optional[Nonbusiness_groups_id] = None
    date_since: Optional[Date_since] = Field(None, example='2023-02-28')
    date_until: Optional[Union[str, None]] = Field(None, example='2023-02-28')

class v3_usersNonbusinessGroups__id__put_InputModel(BaseModel):
    id: v3_usersNonbusinessGroups__id__put_id_InputModel
    requestBody: v3_usersNonbusinessGroups__id__put_RequestBodyModel


v3_usersNonbusinessGroups__id__delete_id_InputModel = int

class v3_usersNonbusinessGroups__id__delete_InputModel(BaseModel):
    id: v3_usersNonbusinessGroups__id__delete_id_InputModel


v3_workTimes_changeRequests__id__approve_post_id_InputModel = int

class v3_workTimes_changeRequests__id__approve_post_InputModel(BaseModel):
    id: v3_workTimes_changeRequests__id__approve_post_id_InputModel


Status = List[AbsenceStatus]

Users_active = bool

class v4_absences_get_filter_InputModel(BaseModel):
    year: Optional[Year] = None
    users_id: Optional[Users_id] = None
    teams_id: Optional[Teams_id] = None
    status: Optional[Status] = None
    type: Optional[Type] = None
    users_active: Optional[Users_active] = None

class v4_absences_get_InputModel(BaseModel):
    filter: v4_absences_get_filter_InputModel
    scope: AbsenceScope


Allow_overrideItem = int

Allow_override = List[Allow_overrideItem]

Sick_note = bool

class v4_absences_post_RequestBodyModel(BaseModel):
    date_since: Date_since = Field(None, example='2023-02-28')
    date_until: Optional[Union[str, None]] = Field(None, example='2023-02-28')
    type: AbsenceType
    half_day: Optional[Half_day] = None
    count_hours: Optional[Union[float, None]] = None
    users_id: Optional[Users_id] = None
    allow_override: Optional[Allow_override] = Field(None, description="IDs of absences that may be shortened or deleted to avoid conflicts")
    status: Optional[AbsenceStatus] = None
    sick_note: Optional[Sick_note] = None
    note: Optional[Union[str, None]] = None
    public_note: Optional[Union[str, None]] = None

class v4_absences_post_InputModel(BaseModel):
    requestBody: v4_absences_post_RequestBodyModel


v4_absences__id__get_id_InputModel = int

class v4_absences__id__get_InputModel(BaseModel):
    id: v4_absences__id__get_id_InputModel


v4_absences__id__put_id_InputModel = int

class v4_absences__id__put_RequestBodyModel(BaseModel):
    date_since: Optional[Date_since] = Field(None, example='2023-02-28')
    date_until: Optional[Date_until] = Field(None, example='2023-02-28')
    type: Optional[AbsenceType] = None
    half_day: Optional[Half_day] = None
    count_hours: Optional[Union[float, None]] = None
    allow_override: Optional[Allow_override] = Field(None, description="IDs of absences that may be shortened or deleted to avoid conflicts")
    status: Optional[AbsenceStatus] = None
    sick_note: Optional[Sick_note] = None
    note: Optional[Union[str, None]] = None
    public_note: Optional[Union[str, None]] = None

class v4_absences__id__put_InputModel(BaseModel):
    id: v4_absences__id__put_id_InputModel
    requestBody: v4_absences__id__put_RequestBodyModel


v4_absences__id__delete_id_InputModel = int

class v4_absences__id__delete_InputModel(BaseModel):
    id: v4_absences__id__delete_id_InputModel


class v4_lumpSumServices_get_filter_InputModel(BaseModel):
    active: Optional[Active] = None
    fulltext: Optional[Fulltext] = None

v4_lumpSumServices_get_sort_InputModel = List[SortIdNameActive]

v4_lumpSumServices_get_page_InputModel = int

v4_lumpSumServices_get_items_per_page_InputModel = int

class v4_lumpSumServices_get_InputModel(BaseModel):
    filter: v4_lumpSumServices_get_filter_InputModel
    sort: v4_lumpSumServices_get_sort_InputModel
    page: v4_lumpSumServices_get_page_InputModel
    items_per_page: v4_lumpSumServices_get_items_per_page_InputModel


class v4_lumpSumServices_post_RequestBodyModel(BaseModel):
    name: Name
    price: Price = Field(None, description="Price per unit")
    unit: Optional[Union[str, None]] = None
    active: Optional[Active] = None
    number: Optional[Union[str, None]] = Field(None, description="Lump sum service number")
    note: Optional[Union[str, None]] = Field(None, description="Only visible for owners or workers with elevated access `manage_services`")

class v4_lumpSumServices_post_InputModel(BaseModel):
    requestBody: v4_lumpSumServices_post_RequestBodyModel


v4_lumpSumServices__id__get_id_InputModel = int

class v4_lumpSumServices__id__get_InputModel(BaseModel):
    id: v4_lumpSumServices__id__get_id_InputModel


v4_lumpSumServices__id__put_id_InputModel = int

class v4_lumpSumServices__id__put_RequestBodyModel(BaseModel):
    name: Optional[Name] = None
    price: Optional[Price] = Field(None, description="Price per unit")
    unit: Optional[Union[str, None]] = None
    active: Optional[Active] = None
    number: Optional[Union[str, None]] = Field(None, description="Lump sum service number")
    note: Optional[Union[str, None]] = Field(None, description="Only visible for owners or workers with elevated access `manage_services`")

class v4_lumpSumServices__id__put_InputModel(BaseModel):
    id: v4_lumpSumServices__id__put_id_InputModel
    requestBody: v4_lumpSumServices__id__put_RequestBodyModel


v4_lumpSumServices__id__delete_id_InputModel = int

v4_lumpSumServices__id__delete_dry_run_InputModel = bool

v4_lumpSumServices__id__delete_force_InputModel = bool

class v4_lumpSumServices__id__delete_InputModel(BaseModel):
    id: v4_lumpSumServices__id__delete_id_InputModel
    dry_run: v4_lumpSumServices__id__delete_dry_run_InputModel
    force: v4_lumpSumServices__id__delete_force_InputModel


class v4_projects_get_filter_InputModel(BaseModel):
    active: Optional[Active] = None
    completed: Optional[Completed] = None
    customers_id: Optional[Customers_id] = None
    fulltext: Optional[Fulltext] = None

v4_projects_get_sort_InputModel = List[SortIdNameActive]

v4_projects_get_page_InputModel = int

v4_projects_get_items_per_page_InputModel = int

class v4_projects_get_InputModel(BaseModel):
    filter: v4_projects_get_filter_InputModel
    sort: v4_projects_get_sort_InputModel
    scope: CustomerProjectScope
    page: v4_projects_get_page_InputModel
    items_per_page: v4_projects_get_items_per_page_InputModel


class v4_projects_post_RequestBodyModel(BaseModel):
    name: Name
    customers_id: Customers_id
    active: Optional[Active] = None
    number: Optional[Union[str, None]] = Field(None, description="Freely selectable number for the project")
    billable_default: Optional[Billable_default] = None
    note: Optional[Union[str, None]] = None
    deadline: Optional[Union[str, None]] = Field(None, description="Date when the project will be completed automatically", example='2023-02-28')
    start_date: Optional[Union[str, None]] = Field(None, description="Date when the project becomes available for time tracking", example='2023-02-28')
    budget: Optional[Budget] = None
    bill_service_id: Optional[Union[str, None]] = None

class v4_projects_post_InputModel(BaseModel):
    requestBody: v4_projects_post_RequestBodyModel


v4_projects__id__get_id_InputModel = int

class v4_projects__id__get_InputModel(BaseModel):
    id: v4_projects__id__get_id_InputModel


v4_projects__id__put_id_InputModel = int

class v4_projects__id__put_RequestBodyModel(BaseModel):
    name: Optional[Name] = None
    customers_id: Optional[Customers_id] = None
    active: Optional[Active] = None
    number: Optional[Union[str, None]] = Field(None, description="Freely selectable number for the project")
    billable_default: Optional[Billable_default] = None
    note: Optional[Union[str, None]] = None
    deadline: Optional[Union[str, None]] = Field(None, description="Date when the project will be completed automatically", example='2023-02-28')
    start_date: Optional[Union[str, None]] = Field(None, description="Date when the project becomes available for time tracking", example='2023-02-28')
    budget: Optional[Budget] = None
    bill_service_id: Optional[Union[str, None]] = None

class v4_projects__id__put_InputModel(BaseModel):
    id: v4_projects__id__put_id_InputModel
    requestBody: v4_projects__id__put_RequestBodyModel


v4_projects__id__delete_id_InputModel = int

v4_projects__id__delete_dry_run_InputModel = bool

v4_projects__id__delete_force_InputModel = bool

class v4_projects__id__delete_InputModel(BaseModel):
    id: v4_projects__id__delete_id_InputModel
    dry_run: v4_projects__id__delete_dry_run_InputModel
    force: v4_projects__id__delete_force_InputModel


v4_projects__id__complete_put_id_InputModel = int

class v4_projects__id__complete_put_RequestBodyModel(BaseModel):
    completed: Completed

class v4_projects__id__complete_put_InputModel(BaseModel):
    id: v4_projects__id__complete_put_id_InputModel
    requestBody: v4_projects__id__complete_put_RequestBodyModel


class v4_projects_reports_get_filter_InputModel(BaseModel):
    active: Optional[Active] = None
    fulltext: Optional[Fulltext] = None
    budget_source: Optional[Budget_source] = None

v4_projects_reports_get_sort_InputModel = List[ApiProjectsReportsV4_SortForIndex]

v4_projects_reports_get_page_InputModel = int

v4_projects_reports_get_items_per_page_InputModel = int

class v4_projects_reports_get_InputModel(BaseModel):
    filter: v4_projects_reports_get_filter_InputModel
    sort: v4_projects_reports_get_sort_InputModel
    page: v4_projects_reports_get_page_InputModel
    items_per_page: v4_projects_reports_get_items_per_page_InputModel


class v4_services_get_filter_InputModel(BaseModel):
    active: Optional[Active] = None
    fulltext: Optional[Fulltext] = None

v4_services_get_sort_InputModel = List[SortIdNameActive]

v4_services_get_page_InputModel = int

v4_services_get_items_per_page_InputModel = int

class v4_services_get_InputModel(BaseModel):
    filter: v4_services_get_filter_InputModel
    sort: v4_services_get_sort_InputModel
    scope: ServiceScope
    page: v4_services_get_page_InputModel
    items_per_page: v4_services_get_items_per_page_InputModel


class v4_services_post_RequestBodyModel(BaseModel):
    name: Name
    active: Optional[Active] = None
    number: Optional[Union[str, None]] = Field(None, description="Freely selectable number for the service.")
    note: Optional[Union[str, None]] = Field(None, description="Only visible for owners or workers with elevated access `manage_services`.")
    bill_service_id: Optional[Union[str, None]] = Field(None, description="Can only be set by owners or workers with elevated access `manage_services` and if a billing application with services support is linked up.")

class v4_services_post_InputModel(BaseModel):
    requestBody: v4_services_post_RequestBodyModel


v4_services__id__get_id_InputModel = int

class v4_services__id__get_InputModel(BaseModel):
    id: v4_services__id__get_id_InputModel


v4_services__id__put_id_InputModel = int

class v4_services__id__put_RequestBodyModel(BaseModel):
    name: Optional[Name] = None
    active: Optional[Active] = None
    number: Optional[Union[str, None]] = Field(None, description="Freely selectable number for the service.")
    note: Optional[Union[str, None]] = Field(None, description="Only visible for owners or workers with elevated access `manage_services`.")
    bill_service_id: Optional[Union[str, None]] = Field(None, description="Can only be set by owners or workers with elevated access `manage_services` and if a billing application with services support is linked up.")

class v4_services__id__put_InputModel(BaseModel):
    id: v4_services__id__put_id_InputModel
    requestBody: v4_services__id__put_RequestBodyModel


v4_services__id__delete_id_InputModel = int

v4_services__id__delete_dry_run_InputModel = bool

v4_services__id__delete_force_InputModel = bool

class v4_services__id__delete_InputModel(BaseModel):
    id: v4_services__id__delete_id_InputModel
    dry_run: v4_services__id__delete_dry_run_InputModel
    force: v4_services__id__delete_force_InputModel


