import os


def pl():
    Uname = os.environ.get('MAIL')
    pwd = os.environ.get('PWDfb')

    return Uname, pwd


def nationspages():
    return ['https://nationsguiden.se/nation/?oid=401',
            'https://nationsguiden.se/nation/?oid=406',
            'https://nationsguiden.se/nation/?oid=394',
            'https://nationsguiden.se/nation/?oid=395',
            'https://nationsguiden.se/nation/?oid=396',
            'https://nationsguiden.se/nation/?oid=397',
            'https://nationsguiden.se/nation/?oid=398',
            'https://nationsguiden.se/nation/?oid=399',
            'https://nationsguiden.se/nation/?oid=400',
            'https://nationsguiden.se/nation/?oid=402',
            'https://nationsguiden.se/nation/?oid=403',
            'https://nationsguiden.se/nation/?oid=404',
            'https://nationsguiden.se/nation/?oid=405']


def login():
    return "https://mbasic.facebook.com/login?"


def monthgetter():
    return ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']


def fbPages():
    array = [
        "https://mbasic.facebook.com/smalandsuppsala?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/gotlandsnation?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/stockholmsnation?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/uplandsnation?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/ghnation?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/ostgotanation?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/vastgotanation?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/snerikes?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/VDala?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/goteborgsnation?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/kalmar.nation.uppsala?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/varmlandsnation?v=events&refid=17&ref=page_internal",
        "https://mbasic.facebook.com/norrlandsnation?v=events&refid=17&ref=page_internal",
    ]

    return array


def names():
    return [
        "Smålands Nation",
        "Gotlands Nation",
        "Stockholms Nation",
        "Uplands Nation",
        "Gästrike-Hälsinge Nation",
        "Östgöta Nation",
        "Västgöta Nation",
        "Södermanlands-Nerikes Nation",
        "Västmanlands-Dala Nation",
        "Göteborgs Nation",
        "Kalmar Nation",
        "Värmlands Nation",
        "Norrlands Nation"
    ]


def shortnames():
    return["småland", "gotland", "stockholm", "upland", "gästrike", "östgöta", "västgöta", "södermanland", "västmanland", "göteborg", "kalmar", "värmland", "norrland"]
