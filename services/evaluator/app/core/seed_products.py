"""
Seed data generator — 400 products across 20 categories with real placeholder images.
Uses picsum.photos for product images and loremflickr for variety.
"""

from typing import Any

# ---------------------------------------------------------------------------
# Categories (20)
# ---------------------------------------------------------------------------
CATEGORIES: list[dict[str, Any]] = [
    {"name": "Смартфоны", "slug": "smartphones", "sort_order": 1},
    {"name": "Ноутбуки", "slug": "laptops", "sort_order": 2},
    {"name": "Наушники и аудио", "slug": "audio", "sort_order": 3},
    {"name": "Телевизоры", "slug": "tv", "sort_order": 4},
    {"name": "Фото и видео", "slug": "cameras", "sort_order": 5},
    {"name": "Игровые консоли", "slug": "gaming", "sort_order": 6},
    {"name": "Умный дом", "slug": "smart-home", "sort_order": 7},
    {"name": "Мужская одежда", "slug": "mens-clothing", "sort_order": 8},
    {"name": "Женская одежда", "slug": "womens-clothing", "sort_order": 9},
    {"name": "Обувь", "slug": "shoes", "sort_order": 10},
    {"name": "Спорт и фитнес", "slug": "sports", "sort_order": 11},
    {"name": "Красота и здоровье", "slug": "beauty", "sort_order": 12},
    {"name": "Дом и сад", "slug": "home-garden", "sort_order": 13},
    {"name": "Кухня", "slug": "kitchen", "sort_order": 14},
    {"name": "Детские товары", "slug": "kids", "sort_order": 15},
    {"name": "Книги", "slug": "books", "sort_order": 16},
    {"name": "Автотовары", "slug": "auto", "sort_order": 17},
    {"name": "Зоотовары", "slug": "pets", "sort_order": 18},
    {"name": "Канцелярия", "slug": "office", "sort_order": 19},
    {"name": "Продукты питания", "slug": "food", "sort_order": 20},
]

# ---------------------------------------------------------------------------
# Product templates per category (20 products each = 400 total)
# Each product gets a unique picsum image via seed parameter
# ---------------------------------------------------------------------------

def _img(seed: int) -> str:
    """Generate a stable placeholder image URL."""
    return f"https://picsum.photos/seed/{seed}/600/600"


def _products_smartphones() -> list[dict]:
    base = [
        ("Galaxy S25 Ultra", 1199.99, 1399.99, "Флагман с AI-камерой 200 МП и титановым корпусом"),
        ("iPhone 16 Pro Max", 1299.99, None, "Чип A18 Pro, камера 48 МП, титановый дизайн"),
        ("Pixel 9 Pro", 899.99, 999.99, "Лучшая камера на Android с AI-обработкой"),
        ("OnePlus 13", 799.99, None, "Snapdragon 8 Gen 4, зарядка 100W за 20 минут"),
        ("Xiaomi 15 Ultra", 749.99, 899.99, "Камера Leica, AMOLED 2K, 5500 мАч"),
        ("Samsung Galaxy Z Fold 6", 1799.99, None, "Складной экран 7.6 дюймов, S Pen"),
        ("Nothing Phone 3", 599.99, 699.99, "Уникальный дизайн с LED-подсветкой Glyph"),
        ("Realme GT 7 Pro", 549.99, None, "Snapdragon 8 Gen 3, 120 Гц AMOLED"),
        ("ASUS ROG Phone 9", 999.99, 1099.99, "Игровой смартфон с кулером и 165 Гц"),
        ("Sony Xperia 1 VI", 1099.99, None, "4K OLED дисплей, профессиональная камера"),
        ("Motorola Edge 50 Ultra", 699.99, 799.99, "Деревянная задняя панель, 125W зарядка"),
        ("Honor Magic 7 Pro", 649.99, None, "AI-ассистент, камера 50 МП OIS"),
        ("Vivo X200 Pro", 799.99, 899.99, "Zeiss камера, MediaTek Dimensity 9400"),
        ("OPPO Find X8 Pro", 849.99, None, "Hasselblad камера, 5800 мАч"),
        ("Huawei Pura 80 Pro", 999.99, 1199.99, "Спутниковая связь, XMAGE камера"),
        ("iPhone 16", 799.99, None, "Чип A18, Dynamic Island, USB-C"),
        ("Samsung Galaxy A56", 349.99, 399.99, "Лучший среднебюджетник 2026"),
        ("Poco F7 Pro", 449.99, None, "Snapdragon 8s Gen 3, 67W зарядка"),
        ("Google Pixel 9a", 499.99, None, "Чистый Android, 7 лет обновлений"),
        ("Tecno Phantom X3 Pro", 399.99, 499.99, "Камера 108 МП, AMOLED 144 Гц"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_laptops() -> list[dict]:
    base = [
        ("MacBook Pro 16 M4 Max", 3499.99, None, "Чип M4 Max, 48 ГБ RAM, 1 ТБ SSD, Liquid Retina XDR"),
        ("Dell XPS 16 (2026)", 1899.99, 2099.99, "Intel Core Ultra 9, OLED 4K, 32 ГБ RAM"),
        ("ThinkPad X1 Carbon Gen 12", 1699.99, None, "Ультралёгкий бизнес-ноутбук, 2.8K OLED"),
        ("ASUS ROG Strix G18", 2299.99, 2499.99, "RTX 5080, i9-14900HX, 240 Гц QHD+"),
        ("HP Spectre x360 16", 1599.99, None, "Трансформер с OLED 3K, Intel Core Ultra 7"),
        ("Razer Blade 16", 2799.99, None, "RTX 5090, Mini LED 240 Гц, ЧПУ-алюминий"),
        ("MacBook Air 15 M4", 1299.99, 1499.99, "Чип M4, 18 часов батареи, Liquid Retina"),
        ("Lenovo Yoga Pro 9i", 1799.99, None, "Mini LED 3.2K, Harman Kardon, 32 ГБ"),
        ("Acer Predator Helios 18", 1999.99, 2199.99, "RTX 5070 Ti, i7-14700HX, 165 Гц"),
        ("Samsung Galaxy Book 4 Ultra", 2199.99, None, "AMOLED 3K, RTX 4070, Intel Core Ultra 9"),
        ("Microsoft Surface Laptop 7", 1399.99, None, "Snapdragon X Elite, 22 часа батареи"),
        ("Framework Laptop 16", 1299.99, 1399.99, "Модульный ноутбук, апгрейд GPU"),
        ("LG Gram 17 (2026)", 1499.99, None, "1.35 кг, 80 Вт·ч батарея, WQXGA IPS"),
        ("ASUS Zenbook S 16", 1399.99, 1599.99, "Ceraluminum корпус, OLED 3K, 1.1 кг"),
        ("MSI Creator Z17", 2499.99, None, "Mini LED, RTX 5080, калибровка Calman"),
        ("Gigabyte Aero 16", 1899.99, 2099.99, "AMOLED 4K, RTX 4070, Creator-ориентирован"),
        ("HP Omen 18", 1799.99, None, "RTX 5070, QHD 165 Гц, RGB клавиатура"),
        ("Acer Swift X 16", 999.99, 1199.99, "RTX 4060, OLED 3.2K, для креативщиков"),
        ("Huawei MateBook X Pro 2026", 1599.99, None, "OLED 3.1K, 14.2 дюймов, 1 кг"),
        ("Chromebook Plus HP", 449.99, 549.99, "Google AI, 14 дюймов IPS, 12 часов"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_audio() -> list[dict]:
    base = [
        ("AirPods Pro 3", 279.99, None, "Адаптивный ANC, пространственное аудио, USB-C"),
        ("Sony WH-1000XM6", 349.99, 399.99, "Лучший ANC в мире, 40 часов, LDAC"),
        ("Samsung Galaxy Buds 4 Pro", 229.99, None, "ANC, 360 Audio, IPX7"),
        ("Bose QuietComfort Ultra", 429.99, None, "Иммерсивный звук, CustomTune"),
        ("JBL Charge 6", 179.99, 199.99, "Портативная колонка, 24 часа, IP67"),
        ("Sennheiser Momentum 5", 349.99, None, "Аудиофильские наушники, 60 часов"),
        ("Marshall Emberton III", 149.99, 179.99, "Ретро-дизайн, 360° звук, 30 часов"),
        ("Apple HomePod 3", 299.99, None, "Пространственное аудио, Matter, Siri"),
        ("Sony WF-1000XM6", 299.99, None, "TWS с лучшим ANC, Hi-Res Audio"),
        ("Beats Studio Pro 2", 349.99, 399.99, "Персонализированный звук, ANC, USB-C"),
        ("Bang & Olufsen Beoplay H100", 599.99, None, "Премиум материалы, 60 часов"),
        ("Sonos Era 300", 449.99, None, "Dolby Atmos, Wi-Fi 6E, Trueplay"),
        ("JBL Live 770NC", 199.99, 249.99, "Адаптивный ANC, 65 часов батареи"),
        ("Audio-Technica ATH-M50xBT3", 229.99, None, "Студийное качество, Bluetooth 5.4"),
        ("Google Pixel Buds Pro 2", 199.99, None, "Tensor A1, ANC, 12 часов"),
        ("Harman Kardon Aura Studio 4", 299.99, 349.99, "Дизайнерская колонка, 360° звук"),
        ("Jabra Elite 10 Gen 2", 249.99, None, "Dolby Atmos, мультиточка, ANC"),
        ("Anker Soundcore Space Q45", 99.99, 129.99, "Бюджетный ANC, 50 часов"),
        ("Devialet Phantom II", 1199.99, None, "Компактная Hi-Fi система, 98 дБ"),
        ("Skullcandy Crusher ANC 2", 179.99, 199.99, "Тактильный бас, ANC, 50 часов"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_tv() -> list[dict]:
    base = [
        ("Samsung QN900D 85\" 8K", 4999.99, 5499.99, "Neo QLED 8K, AI-апскейлинг, 120 Гц"),
        ("LG OLED G4 77\"", 3299.99, None, "OLED evo, MLA, Dolby Vision, 144 Гц"),
        ("Sony Bravia 9 75\"", 2799.99, 2999.99, "Mini LED, XR Processor, Acoustic Multi-Audio"),
        ("TCL QM891G 85\"", 1799.99, None, "Mini LED, 240 Гц, Google TV"),
        ("Hisense U9N 75\"", 2499.99, 2799.99, "Mini LED, 5000 нит, Hi-View Engine X"),
        ("Samsung The Frame 65\"", 1499.99, None, "Арт-режим, QLED 4K, сменные рамки"),
        ("LG OLED C4 65\"", 1799.99, 1999.99, "OLED evo, α9 Gen7, 144 Гц, HDMI 2.1"),
        ("Philips OLED+909 65\"", 2199.99, None, "Ambilight, Bowers & Wilkins звук"),
        ("Sony Bravia 7 65\"", 1599.99, 1799.99, "Mini LED, XR Processor, BRAVIA XR"),
        ("Samsung S95D 65\" QD-OLED", 2499.99, None, "QD-OLED, антибликовое покрытие, 144 Гц"),
        ("Panasonic MZ2000 65\"", 2299.99, None, "Master OLED, Dolby Vision IQ, Filmmaker"),
        ("TCL C855 75\"", 999.99, 1199.99, "Mini LED, 144 Гц, Google TV"),
        ("Hisense L9H Laser TV 120\"", 3499.99, None, "Лазерный ТВ, 3000 люмен, 4K"),
        ("LG OLED B4 55\"", 1199.99, 1399.99, "OLED, α8 Gen7, webOS 24"),
        ("Samsung QN85D 75\"", 1999.99, None, "Neo QLED 4K, Object Tracking Sound+"),
        ("Xiaomi TV Max 100\"", 1999.99, 2499.99, "100 дюймов 4K, HDMI 2.1, Dolby Vision"),
        ("Vizio MQX 75\"", 899.99, 999.99, "Quantum Color, 120 Гц, SmartCast"),
        ("Sharp AQUOS XLED 65\"", 1699.99, None, "Mini LED, 120 Гц, Android TV"),
        ("Toshiba Z870M 65\"", 1299.99, 1499.99, "Mini LED, Dolby Vision, REGZA Engine"),
        ("Samsung The Serif 55\"", 999.99, None, "Дизайнерский ТВ, QLED 4K, NFC"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_cameras() -> list[dict]:
    base = [
        ("Sony A7R V", 3499.99, None, "61 МП, AI-автофокус, 8K видео"),
        ("Canon EOS R5 Mark II", 4299.99, None, "45 МП, 8K RAW, Dual Pixel CMOS AF II"),
        ("Nikon Z8", 3999.99, 4299.99, "45.7 МП, 8K, встроенный стабилизатор"),
        ("Fujifilm X-T6", 1699.99, None, "40 МП X-Trans, 6.2K видео, ретро-дизайн"),
        ("DJI Mavic 4 Pro", 2199.99, None, "Дрон с камерой Hasselblad, 8K, 46 мин полёта"),
        ("GoPro Hero 13 Black", 449.99, 499.99, "5.3K 60fps, HyperSmooth 7.0, GPS"),
        ("Sony ZV-E10 II", 899.99, None, "Камера для блогеров, 4K 120fps, AI-автофокус"),
        ("Canon EOS R6 Mark III", 2499.99, None, "24 МП, 40fps, 4K 120p, IBIS"),
        ("Panasonic Lumix S5 III", 1999.99, 2199.99, "24 МП, фазовый AF, 6K видео"),
        ("Insta360 X4", 499.99, None, "360° камера, 8K, невидимая селфи-палка"),
        ("Leica Q3", 5999.99, None, "60 МП, Summilux 28mm f/1.7, 8K"),
        ("Nikon Z6 III", 2499.99, None, "24.5 МП, частично стекированная матрица, 6K"),
        ("Olympus OM-5 II", 1199.99, 1399.99, "Компактная система, 50 МП Hi-Res, IP53"),
        ("DJI Osmo Action 5 Pro", 379.99, 429.99, "4K 120fps, водонепроницаемая до 20м"),
        ("Sigma fp L II", 2199.99, None, "61 МП, компактный полный кадр, L-mount"),
        ("Ricoh GR IIIx HDF", 999.99, None, "Компакт с APS-C, 40mm экв., HDF фильтр"),
        ("Hasselblad X2D 100C", 8199.99, None, "100 МП средний формат, 16-бит цвет"),
        ("Canon PowerShot V10 II", 349.99, 399.99, "Влог-камера, 4K, встроенный стабилизатор"),
        ("Sony FX3 II", 3899.99, None, "Кинокамера, 4K 120fps, S-Cinetone"),
        ("Fujifilm Instax Mini 99", 199.99, None, "Моментальная камера, 6 цветовых эффектов"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_gaming() -> list[dict]:
    base = [
        ("PlayStation 5 Pro", 699.99, None, "GPU 67% мощнее, 2 ТБ SSD, 8K"),
        ("Xbox Series X 2TB", 599.99, None, "2 ТБ SSD, Galaxy Black, Game Pass"),
        ("Nintendo Switch 2", 449.99, None, "8\" LCD, Joy-Con 2.0, обратная совместимость"),
        ("Steam Deck OLED 1TB", 549.99, None, "7.4\" OLED, 90 Гц, SteamOS"),
        ("ASUS ROG Ally X", 799.99, None, "Ryzen Z1 Extreme, 7\" FHD 120 Гц"),
        ("PS5 DualSense Edge", 199.99, None, "Про-контроллер, сменные стики, профили"),
        ("Xbox Elite Controller S3", 179.99, None, "Регулируемое натяжение, 40 часов"),
        ("Meta Quest 3S", 299.99, 349.99, "VR/MR гарнитура, Snapdragon XR2 Gen 2"),
        ("Razer Kishi Ultra", 149.99, None, "Мобильный контроллер, USB-C, Mecha-Tactile"),
        ("Nintendo Pro Controller 2", 69.99, None, "HD Rumble, NFC, 80 часов батареи"),
        ("SteelSeries Arctis Nova Pro", 349.99, None, "Игровая гарнитура, ANC, Hi-Res"),
        ("Logitech G Pro X 60", 179.99, 199.99, "60% клавиатура, LIGHTSPEED, Hall Effect"),
        ("Razer DeathAdder V3 Pro", 89.99, None, "Мышь 63г, Focus Pro 36K, 90 часов"),
        ("BenQ Mobiuz EX2710U", 599.99, 699.99, "27\" 4K 144 Гц, IPS, HDRi"),
        ("Samsung Odyssey G9 G95SC", 1299.99, 1499.99, "49\" OLED, 240 Гц, 0.03мс"),
        ("Corsair K100 RGB", 229.99, None, "Оптико-механическая, iCUE, колесо управления"),
        ("HyperX Cloud III Wireless", 149.99, 179.99, "Игровая гарнитура, DTS:X, 120 часов"),
        ("Elgato Stream Deck +", 199.99, None, "Стриминг-контроллер, тач-полоса, 8 кнопок"),
        ("Secretlab Titan Evo 2026", 549.99, None, "Игровое кресло, магнитные подушки, 4D"),
        ("Lian Li O11 Dynamic EVO", 169.99, None, "Корпус ПК, двойная камера, RGB"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_smart_home() -> list[dict]:
    base = [
        ("Apple HomePod mini 2", 99.99, None, "Siri, Thread, UWB, пространственное аудио"),
        ("Amazon Echo Show 15", 249.99, 279.99, "15.6\" дисплей, Alexa, Fire TV встроен"),
        ("Google Nest Hub Max 2", 229.99, None, "10\" дисплей, Gemini AI, камера 6.5 МП"),
        ("Ring Video Doorbell 5 Pro", 249.99, None, "Видеозвонок, 3D-радар, Head-to-Toe HD+"),
        ("Philips Hue Starter Kit", 199.99, 229.99, "4 лампы + Bridge, 16 млн цветов, Zigbee"),
        ("Aqara Smart Lock U200", 229.99, None, "Замок с отпечатком, Apple Home Key, Matter"),
        ("Ecovacs Deebot X5 Omni", 1099.99, 1299.99, "Робот-пылесос, 12800 Па, самоочистка"),
        ("iRobot Roomba j9+", 799.99, None, "Навигация PrecisionVision, самоопустошение"),
        ("Dyson Purifier Big Quiet+", 699.99, None, "Очиститель воздуха, HEPA H13, тихий"),
        ("Nest Learning Thermostat 4", 279.99, None, "AI-обучение, Matter, датчик присутствия"),
        ("Arlo Ultra 2 XL (4 камеры)", 799.99, 899.99, "4K HDR, цветное ночное видение, 12 мес батарея"),
        ("Yale Assure Lock 2 Plus", 279.99, None, "Умный замок, Wi-Fi, Apple/Google/Alexa"),
        ("Nanoleaf Shapes Hexagons 15pk", 299.99, None, "Модульные LED-панели, Thread, ритм музыки"),
        ("Roborock S8 MaxV Ultra", 1399.99, 1599.99, "Робот-пылесос, FlexiArm, 10000 Па"),
        ("TP-Link Deco BE85 (3-pack)", 699.99, None, "Wi-Fi 7 Mesh, 19 Гбит/с, покрытие 750 м²"),
        ("Withings Body Scan", 399.99, None, "Умные весы, ЭКГ, сегментный анализ тела"),
        ("SwitchBot Curtain 3", 89.99, 99.99, "Автоматизация штор, солнечная панель, Matter"),
        ("Eufy Security S380", 549.99, None, "Система безопасности, локальное хранение, 4K"),
        ("Govee RGBIC LED Strip 10m", 49.99, 69.99, "Светодиодная лента, Wi-Fi, сегментный цвет"),
        ("Sonoff NSPanel Pro", 89.99, None, "Панель управления умным домом, Zigbee, Wi-Fi"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_mens_clothing() -> list[dict]:
    base = [
        ("Пуховик North Face Nuptse 700", 299.99, 349.99, "Пух 700 Fill, водоотталкивающий, -30°C"),
        ("Кожаная куртка Zara Premium", 189.99, None, "Натуральная кожа ягнёнка, slim fit"),
        ("Костюм Hugo Boss Slim Fit", 599.99, 699.99, "Шерсть Super 130s, итальянский крой"),
        ("Джинсы Levi's 501 Original", 79.99, None, "Классический прямой крой, 100% хлопок"),
        ("Худи Nike Tech Fleece", 109.99, 129.99, "Двойной флис, молния, slim fit"),
        ("Рубашка Ralph Lauren Oxford", 89.99, None, "Хлопок, button-down, классический крой"),
        ("Пальто Massimo Dutti Wool", 249.99, 299.99, "Шерсть 80%, кашемир 20%, двубортное"),
        ("Футболка Uniqlo Supima", 19.99, None, "Хлопок Supima, базовая, 12 цветов"),
        ("Брюки чинос H&M Regular", 34.99, 44.99, "Хлопок-стрейч, 8 цветов"),
        ("Свитер Zara Merino Wool", 59.99, None, "100% шерсть мериноса, V-образный вырез"),
        ("Бомбер Alpha Industries MA-1", 159.99, None, "Нейлон, реверсивный, оранжевая подкладка"),
        ("Шорты Adidas Essentials", 29.99, 39.99, "Французская махра, 3 полоски"),
        ("Жилет Patagonia Down Sweater", 179.99, None, "Пух 800 Fill, переработанный нейлон"),
        ("Поло Lacoste Classic Fit", 99.99, None, "Пике хлопок, крокодил, 20 цветов"),
        ("Тренч Burberry Kensington", 1990.00, None, "Габардин, Heritage крой, Made in England"),
        ("Спортивный костюм Puma", 79.99, 99.99, "Полиэстер, молния, манжеты"),
        ("Джинсовая куртка Wrangler", 89.99, None, "Деним 12 oz, классический Western крой"),
        ("Термобельё Columbia Omni-Heat", 49.99, 59.99, "Отражающая подкладка, влагоотвод"),
        ("Кардиган COS Merino", 119.99, None, "Шерсть мериноса, оверсайз, минимализм"),
        ("Ветровка The North Face", 129.99, 149.99, "DryVent, упаковывается в карман"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_womens_clothing() -> list[dict]:
    base = [
        ("Платье Zara Midi Satin", 69.99, 89.99, "Атлас, А-силуэт, 6 цветов"),
        ("Пальто Max Mara Teddy Bear", 2990.00, None, "Альпака-шерсть, оверсайз, иконический"),
        ("Джинсы Levi's Ribcage Wide", 89.99, None, "Высокая посадка, широкие, 100% хлопок"),
        ("Блузка Massimo Dutti Silk", 79.99, 99.99, "100% шёлк, свободный крой"),
        ("Куртка Mango Leather Effect", 69.99, None, "Эко-кожа, байкерский стиль, молнии"),
        ("Юбка H&M Pleated Midi", 34.99, 44.99, "Плиссе, эластичный пояс, 5 цветов"),
        ("Свитер COS Cashmere Blend", 149.99, None, "Кашемир 30%, оверсайз, мягкий"),
        ("Тренч Mango Classic", 129.99, 159.99, "Хлопок, двубортный, пояс"),
        ("Топ Zara Crop Knit", 25.99, None, "Трикотаж, укороченный, 10 цветов"),
        ("Брюки Massimo Dutti Tailored", 89.99, None, "Шерсть, прямой крой, стрелки"),
        ("Пуховик Uniqlo Ultra Light", 99.99, 129.99, "Пух 640 Fill, 180г, упаковывается"),
        ("Кардиган & Other Stories", 79.99, None, "Мохер-шерсть, объёмный, пуговицы"),
        ("Комбинезон Zara Denim", 59.99, 79.99, "Деним, широкие штанины, пояс"),
        ("Рубашка Uniqlo Linen", 39.99, None, "100% лён, оверсайз, летняя"),
        ("Платье COS Knit Maxi", 119.99, None, "Трикотаж, макси, минимализм"),
        ("Жакет Mango Tweed", 89.99, 109.99, "Твид, укороченный, золотые пуговицы"),
        ("Леггинсы Lululemon Align", 98.00, None, "Nulu ткань, высокая посадка, 25 дюймов"),
        ("Шуба H&M Faux Fur", 149.99, 199.99, "Эко-мех, оверсайз, тёплая"),
        ("Боди Zara Seamless", 19.99, None, "Бесшовный, стрейч, 8 цветов"),
        ("Костюм Massimo Dutti Linen", 199.99, None, "Лён, жакет + брюки, летний"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_shoes() -> list[dict]:
    base = [
        ("Nike Air Max Dn", 159.99, None, "Dynamic Air, новая амортизация 2026"),
        ("Adidas Ultraboost 24", 189.99, 199.99, "Boost Light, Continental подошва"),
        ("New Balance 990v6", 199.99, None, "Made in USA, ENCAP, замша + сетка"),
        ("Nike Air Jordan 1 Retro High", 179.99, None, "Классика, кожа, 30+ расцветок"),
        ("Converse Chuck 70 Hi", 89.99, None, "Винтажный холст, OrthoLite стелька"),
        ("Dr. Martens 1460 Smooth", 169.99, None, "Кожа, AirWair подошва, 8 люверсов"),
        ("Adidas Samba OG", 99.99, 119.99, "Замша + кожа, gum подошва, ретро"),
        ("Puma Suede Classic", 74.99, None, "Замша, культовая модель с 1968"),
        ("Timberland 6-Inch Premium", 199.99, None, "Нубук, водонепроницаемые, Primaloft"),
        ("Vans Old Skool", 69.99, None, "Холст + замша, вафельная подошва"),
        ("Reebok Club C 85", 79.99, 89.99, "Кожа, винтажный теннисный стиль"),
        ("ASICS Gel-Kayano 31", 159.99, None, "Стабилизация, FF Blast+, 4D Guidance"),
        ("Salomon XT-6", 189.99, None, "Трейл, Advanced Chassis, Contagrip"),
        ("Birkenstock Arizona", 109.99, None, "Пробковая стелька, замша, 2 ремешка"),
        ("Nike Dunk Low", 109.99, 119.99, "Кожа, баскетбольная классика, 50+ цветов"),
        ("UGG Classic Mini II", 149.99, None, "Овчина, Treadlite подошва, зимние"),
        ("On Cloud 5", 139.99, None, "CloudTec, Speedboard, швейцарский дизайн"),
        ("Hoka Clifton 9", 144.99, 159.99, "Максимальная амортизация, 248г"),
        ("Crocs Classic Clog", 49.99, None, "Croslite, вентиляция, Jibbitz-совместимые"),
        ("Chelsea Boots Zara Leather", 99.99, 129.99, "Кожа, эластичные вставки, 4 см каблук"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_sports() -> list[dict]:
    base = [
        ("Беговая дорожка NordicTrack 2450", 1799.99, 1999.99, "22\" HD экран, iFIT, наклон -3% до 15%"),
        ("Велотренажёр Peloton Bike+", 2495.00, None, "24\" поворотный экран, Apple GymKit"),
        ("Гантели Bowflex SelectTech 552", 399.99, 449.99, "Регулируемые 2-24 кг, 15 позиций"),
        ("Коврик для йоги Manduka PRO", 119.99, None, "6 мм, закрытые поры, пожизненная гарантия"),
        ("Фитнес-браслет Fitbit Charge 6", 159.99, None, "GPS, ЧСС, SpO2, Google интеграция"),
        ("Garmin Forerunner 965", 499.99, 549.99, "AMOLED, мультиспорт, карты, 23 дня"),
        ("Apple Watch Ultra 3", 799.99, None, "Титан, 72 часа, дайвинг 40м, L5 GPS"),
        ("Скакалка Tangram Smart Rope", 79.99, None, "LED-дисплей в воздухе, Bluetooth, счётчик"),
        ("Эспандер набор Fit Simplify", 14.99, 19.99, "5 уровней сопротивления, латекс"),
        ("Ролик для пресса Ab Wheel Pro", 29.99, None, "Двойное колесо, коврик для колен"),
        ("Боксёрские перчатки Everlast Pro", 59.99, 69.99, "14 oz, кожа, EverCool вентиляция"),
        ("Мяч баскетбольный Spalding TF", 34.99, None, "Композитная кожа, размер 7, indoor/outdoor"),
        ("Велосипед Giant Defy Advanced", 2499.99, None, "Карбон, Shimano 105, дисковые тормоза"),
        ("Самокат Xiaomi Electric Scooter 4", 499.99, 599.99, "30 км/ч, 35 км запас, 10\" шины"),
        ("Палатка MSR Hubba Hubba NX", 449.99, None, "2-местная, 1.54 кг, 3-сезонная"),
        ("Рюкзак Osprey Atmos AG 65", 269.99, None, "65 л, Anti-Gravity подвеска, вентиляция"),
        ("Лыжи Atomic Redster X9S", 799.99, 899.99, "Карвинг, Servotec, 165-177 см"),
        ("Сноуборд Burton Custom", 549.99, None, "All-mountain, Flying V, 154-162 см"),
        ("Теннисная ракетка Wilson Pro Staff", 249.99, None, "97 sq in, 315г, Countervail"),
        ("Гиря чугунная 16 кг", 49.99, 59.99, "Чугун с покрытием, широкая ручка"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_beauty() -> list[dict]:
    base = [
        ("Dyson Airwrap Complete Long", 599.99, None, "Мультистайлер, эффект Коанда, 6 насадок"),
        ("Dyson Supersonic HD15", 429.99, None, "Фен, 5 насадок, контроль температуры"),
        ("La Mer Moisturizing Cream 60ml", 345.00, None, "Miracle Broth, регенерация, увлажнение"),
        ("SK-II Facial Treatment Essence", 185.00, 229.00, "Pitera, 90% чистый фермент, 230 мл"),
        ("Foreo Luna 4 Plus", 299.99, None, "Щётка для лица, T-Sonic, 16 интенсивностей"),
        ("Estée Lauder Advanced Night Repair", 75.00, None, "Сыворотка, Chronolux, гиалуроновая кислота"),
        ("Charlotte Tilbury Pillow Talk Set", 89.00, 110.00, "Помада + карандаш + блеск, культовый оттенок"),
        ("Olaplex No.3 Hair Perfector", 30.00, None, "Восстановление связей волос, 100 мл"),
        ("Drunk Elephant Protini Cream", 68.00, None, "Пептиды, 9 сигнальных пептидов, без силиконов"),
        ("Tom Ford Black Orchid EDP 100ml", 175.00, None, "Унисекс, чёрная орхидея, трюфель, пачули"),
        ("Chanel No.5 L'Eau EDT 100ml", 135.00, None, "Современная интерпретация классики"),
        ("NuFace Trinity+ Starter Kit", 339.00, 395.00, "Микротоки, лифтинг, тонус, 5 мин/день"),
        ("Paula's Choice 2% BHA Exfoliant", 32.00, None, "Салициловая кислота, поры, 118 мл"),
        ("Tatcha Dewy Skin Cream", 68.00, None, "Японский рис, водоросли, гиалуроновая кислота"),
        ("Dior Sauvage EDP 100ml", 155.00, None, "Бергамот, амброксан, ваниль"),
        ("Augustinus Bader The Cream 50ml", 280.00, None, "TFC8 технология, стволовые клетки"),
        ("Rare Beauty Soft Pinch Blush", 23.00, None, "Жидкие румяна, 8 оттенков, Selena Gomez"),
        ("CeraVe Moisturizing Cream 453g", 16.99, 19.99, "Церамиды, гиалуроновая кислота, MVE"),
        ("Therabody Theragun PRO Plus", 499.99, None, "Перкуссионный массажёр, 6 насадок, Bluetooth"),
        ("Oral-B iO Series 10", 299.99, 349.99, "Электрическая щётка, AI 3D-трекинг, iO Sense"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_home_garden() -> list[dict]:
    base = [
        ("Диван IKEA Kivik 3-местный", 799.99, None, "Ткань, глубокое сиденье, сменные чехлы"),
        ("Матрас Casper Original Queen", 1095.00, 1295.00, "Пена, 3 зоны, 100 ночей тест"),
        ("Робот-газонокосилка Husqvarna 450X", 2999.99, None, "GPS, 5000 м², всепогодная"),
        ("Кресло Herman Miller Aeron", 1395.00, None, "Эргономичное, PostureFit SL, 12 лет гарантия"),
        ("Постельное бельё Brooklinen Luxe", 149.99, 179.99, "Сатин 480 нитей, 100% хлопок"),
        ("Пылесос Dyson V15 Detect", 749.99, None, "Лазерное обнаружение пыли, LCD, 60 мин"),
        ("Стиральная машина LG WashTower", 1999.99, 2299.99, "Стирка + сушка, AI DD, TurboWash 360"),
        ("Кондиционер Daikin Emura 3", 1299.99, None, "Инвертор, Wi-Fi, R-32, 35 м²"),
        ("Набор полотенец Parachute Classic", 109.99, None, "Турецкий хлопок, 6 штук, 700 GSM"),
        ("Настольная лампа Dyson Solarcycle", 649.99, None, "Автояркость, цветовая температура, 60 лет"),
        ("Комод IKEA Malm 6 ящиков", 199.99, None, "Белый, 160x78 см, плавное закрывание"),
        ("Увлажнитель Levoit LV600S", 89.99, 109.99, "6 л, тёплый/холодный туман, Wi-Fi"),
        ("Набор садовых инструментов Fiskars", 79.99, None, "Лопата, грабли, секатор, перчатки"),
        ("Гриль Weber Spirit II E-310", 499.99, 549.99, "Газовый, 3 горелки, GS4, 529 см²"),
        ("Шторы IKEA Majgull Blackout", 49.99, None, "Блэкаут, 145x300 см, 2 шт"),
        ("Ковёр Ruggable Washable 5x7", 199.99, 249.99, "Моющийся, 2 слоя, 150+ дизайнов"),
        ("Зеркало с подсветкой Keonjinn", 129.99, None, "LED, антизапотевание, 60x80 см"),
        ("Комплект кашпо Lechuza Cube", 89.99, None, "Автополив, 3 размера, белый глянец"),
        ("Гамак Vivere Double Cotton", 79.99, 99.99, "Хлопок, 200x150 см, до 200 кг"),
        ("Садовый фонтан Solar Birdbath", 59.99, None, "Солнечная батарея, LED, 3 уровня"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_kitchen() -> list[dict]:
    base = [
        ("KitchenAid Artisan 5KSM185", 449.99, 499.99, "Планетарный миксер, 4.8 л, 10 скоростей"),
        ("Nespresso Vertuo Next", 179.99, None, "Капсульная кофемашина, 5 размеров чашек"),
        ("Instant Pot Duo Plus 6L", 89.99, 109.99, "9-в-1, скороварка, мультиварка, йогуртница"),
        ("Vitamix A3500", 649.99, None, "Блендер, 5 программ, таймер, самоочистка"),
        ("Набор ножей Wüsthof Classic 8шт", 599.99, 699.99, "Кованая сталь, полный хвостовик"),
        ("Сковорода Le Creuset 26 см", 199.99, None, "Чугун, эмаль, пожизненная гарантия"),
        ("Тостер Smeg TSF01", 169.99, None, "Ретро-дизайн, 2 слота, 6 уровней"),
        ("Кофемолка Baratza Encore ESP", 199.99, None, "Жернова 40 мм, 40 настроек помола"),
        ("Набор кастрюль All-Clad D5 10шт", 899.99, 999.99, "5-слойная сталь, индукция, Made in USA"),
        ("Аэрогриль Philips XXL HD9870", 299.99, None, "7.3 л, Fat Removal, Smart Sensing"),
        ("Чайник Stagg EKG Electric", 169.99, None, "Гусиная шея, термометр, 0.9 л"),
        ("Хлебопечка Panasonic SD-YR2550", 249.99, 279.99, "Автодозатор дрожжей, 35 программ"),
        ("Набор контейнеров OXO Good Grips", 49.99, None, "10 шт, герметичные, BPA-free"),
        ("Мясорубка Bosch MFW68660", 179.99, None, "800 Вт, 3 диска, насадка для колбас"),
        ("Вафельница Breville Smart Waffle", 149.99, 179.99, "4 настройки, антипригарное, таймер"),
        ("Термос Stanley Classic 1.9L", 49.99, None, "Нержавеющая сталь, 45 часов тепло"),
        ("Набор бокалов Riedel Vinum 8шт", 199.99, None, "Хрусталь, 4 типа, для вина"),
        ("Доска разделочная Epicurean", 39.99, 49.99, "Древесное волокно, не тупит ножи"),
        ("Соковыжималка Hurom H-AA", 399.99, None, "Шнековая, холодный отжим, 43 об/мин"),
        ("Кухонные весы Etekcity ESN00", 14.99, 19.99, "До 5 кг, точность 1г, тара, LCD"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_kids() -> list[dict]:
    base = [
        ("LEGO Technic Bugatti Chiron", 349.99, 399.99, "3599 деталей, 1:8, коробка передач"),
        ("Коляска Bugaboo Fox 5", 1299.99, None, "Полный привод, реверсивное сиденье"),
        ("Конструктор Magna-Tiles 100шт", 119.99, None, "Магнитный, прозрачный, STEM"),
        ("Детский велосипед Woom 4", 449.99, None, "20 дюймов, 7.7 кг, 6-8 лет"),
        ("Набор Playmobil Пиратский корабль", 79.99, 99.99, "Плавающий, фигурки, пушки"),
        ("Кукла Barbie Dreamhouse", 199.99, None, "3 этажа, бассейн, горка, 75+ аксессуаров"),
        ("Hot Wheels Ultimate Garage", 89.99, 109.99, "Гараж на 100+ машин, лифт, трек"),
        ("Детский планшет Amazon Fire HD 10 Kids", 199.99, None, "10.1\", чехол, 2 года контента"),
        ("Набор Play-Doh Kitchen Creations", 24.99, None, "Духовка, 6 банок, формочки"),
        ("Самокат Micro Maxi Deluxe", 149.99, None, "5-12 лет, LED колёса, до 50 кг"),
        ("Детское автокресло Cybex Sirona", 449.99, 499.99, "0-4 года, ISOFIX, 360° поворот"),
        ("Набор Crayola Inspiration Art Case", 29.99, None, "140 предметов, карандаши, фломастеры"),
        ("Радиоуправляемая машина Traxxas Slash", 269.99, None, "1:10, 4WD, 50+ км/ч, водонепроницаемая"),
        ("Детский батут Springfree 10ft", 1399.99, None, "Безопасный, без пружин, сетка"),
        ("Набор Melissa & Doug Wooden Kitchen", 199.99, 249.99, "Деревянная кухня, аксессуары"),
        ("Детские часы Garmin Bounce", 129.99, None, "GPS, звонки, геозоны, без экрана"),
        ("Конструктор LEGO City Space Station", 59.99, None, "588 деталей, 6 минифигурок"),
        ("Набор для опытов National Geographic", 34.99, 39.99, "15 экспериментов, вулкан, кристаллы"),
        ("Детский рюкзак Deuter Kids", 39.99, None, "12 л, мягкая спинка, светоотражатели"),
        ("Мягкая игрушка Jellycat Bashful Bunny", 24.99, None, "31 см, плюш, 20+ цветов"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_books() -> list[dict]:
    base = [
        ("Atomic Habits — James Clear", 16.99, None, "Маленькие привычки, большие результаты"),
        ("Sapiens — Yuval Noah Harari", 18.99, 22.99, "Краткая история человечества"),
        ("Thinking, Fast and Slow — Kahneman", 17.99, None, "Два режима мышления, Нобелевский лауреат"),
        ("The Pragmatic Programmer", 49.99, None, "20th Anniversary Edition, программирование"),
        ("Dune — Frank Herbert", 14.99, None, "Классика научной фантастики, экранизация"),
        ("1984 — George Orwell", 9.99, 12.99, "Антиутопия, тоталитаризм, классика"),
        ("Clean Code — Robert C. Martin", 39.99, None, "Чистый код, рефакторинг, SOLID"),
        ("The Art of War — Sun Tzu", 7.99, None, "Стратегия, 2500 лет мудрости"),
        ("Educated — Tara Westover", 15.99, None, "Мемуары, самообразование, семья"),
        ("Project Hail Mary — Andy Weir", 16.99, 19.99, "Научная фантастика, от автора Марсианина"),
        ("Designing Data-Intensive Apps", 44.99, None, "Распределённые системы, Martin Kleppmann"),
        ("The Psychology of Money", 18.99, None, "Morgan Housel, финансовое мышление"),
        ("Мастер и Маргарита — Булгаков", 12.99, None, "Классика русской литературы"),
        ("Война и мир — Толстой", 14.99, 17.99, "Эпопея, 4 тома, полное издание"),
        ("System Design Interview Vol.2", 39.99, None, "Alex Xu, подготовка к собеседованиям"),
        ("Meditations — Marcus Aurelius", 8.99, None, "Стоицизм, философия, самосовершенствование"),
        ("The Alchemist — Paulo Coelho", 13.99, None, "Притча, путешествие, мечта"),
        ("Eloquent JavaScript 4th Ed", 34.99, None, "Современный JavaScript, интерактивный"),
        ("Краткая история времени — Хокинг", 15.99, 18.99, "Космология, чёрные дыры, Big Bang"),
        ("Becoming — Michelle Obama", 16.99, None, "Мемуары, первая леди, вдохновение"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_auto() -> list[dict]:
    base = [
        ("Видеорегистратор Viofo A139 Pro 3CH", 299.99, 349.99, "3 камеры, 4K, Starvis 2, GPS, Wi-Fi"),
        ("Автомобильное зарядное Anker 67W", 27.99, None, "USB-C + USB-A, PPS, PowerIQ 3.0"),
        ("Компрессор Xiaomi Portable Air Pump", 49.99, None, "150 PSI, LED, аккумулятор, авто-стоп"),
        ("Навигатор Garmin DriveSmart 76", 299.99, None, "7 дюймов, голосовое управление, трафик"),
        ("Чехлы на сиденья Coverado Premium", 89.99, 109.99, "Экокожа, полный комплект, 5 цветов"),
        ("Автопылесос Dyson Humdinger", 279.99, None, "Ручной, 100 AW, 25 мин, HEPA"),
        ("Набор инструментов Dewalt 205шт", 199.99, None, "Хром-ванадий, кейс, трещотки, биты"),
        ("Шины Michelin Pilot Sport 5 (4шт)", 799.99, 899.99, "225/45 R18, AA рейтинг, 50000 км"),
        ("Автохолодильник Dometic CFX3 35", 699.99, None, "35 л, компрессор, -22°C, Wi-Fi"),
        ("Багажник на крышу Thule WingBar Evo", 349.99, None, "Аэродинамический, до 75 кг, тихий"),
        ("Пусковое устройство NOCO GB40", 99.99, 119.99, "1000A, литий, до 6 л бензин"),
        ("Ароматизатор Diptyque Car Diffuser", 65.00, None, "Сменные капсулы, 3 аромата"),
        ("Коврики WeatherTech FloorLiner", 149.99, None, "Точная подгонка, TPE, 3D-сканирование"),
        ("Антирадар Valentine One Gen2", 499.99, None, "Стрелки направления, Bluetooth, GPS"),
        ("Органайзер в багажник Fortem", 29.99, 39.99, "Складной, 3 секции, нескользящий"),
        ("Щётки стеклоочистителя Bosch Icon 2шт", 39.99, None, "Бескаркасные, ClearMax 365, тихие"),
        ("Автомобильный держатель iOttie Easy One Touch 6", 29.99, None, "Присоска + вент, Qi2 зарядка"),
        ("Масло моторное Mobil 1 5W-30 5L", 34.99, 39.99, "Синтетика, защита 20000 км"),
        ("Камера заднего вида AUTO-VOX Solar4", 149.99, None, "Беспроводная, солнечная батарея, 1080p"),
        ("Аптечка автомобильная First Aid Only", 24.99, None, "312 предметов, FDA, компактная"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_pets() -> list[dict]:
    base = [
        ("Автокормушка PetSafe Smart Feed", 189.99, None, "Wi-Fi, 24 порции, приложение, 5.7 л"),
        ("Лежанка Casper Dog Bed Large", 149.99, 179.99, "Пена с памятью, моющийся чехол"),
        ("Когтеточка SmartCat Ultimate", 49.99, None, "Сизаль, 81 см, устойчивая база"),
        ("Шлейка Ruffwear Front Range", 39.99, None, "Мягкая, 2 точки крепления, светоотражатели"),
        ("Корм Royal Canin Medium Adult 15кг", 69.99, 79.99, "Для средних пород, 12 мес+"),
        ("Автопоилка Catit Pixi Smart", 49.99, None, "Фильтр, Wi-Fi, LED, 2 л"),
        ("Игрушка Kong Classic XL", 14.99, None, "Натуральный каучук, для лакомств"),
        ("GPS-трекер Fi Series 3", 149.99, None, "LTE, 3 мес батарея, геозоны, LED"),
        ("Переноска Sleepypod Air", 89.99, 99.99, "Авиа-одобренная, сетка, 5.4 кг"),
        ("Корм Orijen Cat & Kitten 5.4кг", 49.99, None, "85% мяса, беззерновой, Канада"),
        ("Лоток Litter-Robot 4", 699.99, None, "Автоматический, Wi-Fi, датчик веса"),
        ("Ошейник с GPS Tractive DOG XL", 49.99, 59.99, "Подписка, зоны, история, водонепроницаемый"),
        ("Щётка FURminator deShedding L", 34.99, None, "Для длинношёрстных, уменьшает линьку 90%"),
        ("Домик для кошки Vesper High Base", 99.99, None, "Дерево + ткань, 2 уровня, гамак"),
        ("Поводок-рулетка Flexi Giant L", 29.99, None, "8 м, до 50 кг, тормоз, светоотражатель"),
        ("Корм Hill's Science Diet Adult 12кг", 59.99, 69.99, "Курица, сбалансированный, ветеринарный"),
        ("Игрушка Chuckit! Ultra Ball 3шт", 12.99, None, "Высокий отскок, прочный, яркий"),
        ("Миска с подставкой YETI Boomer 8", 49.99, None, "Нержавеющая сталь, нескользящая, 1.8 л"),
        ("Шампунь Burt's Bees Oatmeal", 9.99, None, "Овсянка + мёд, pH для собак, 473 мл"),
        ("Аквариум Fluval Flex 57L", 129.99, 149.99, "LED, фильтр, изогнутое стекло"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_office() -> list[dict]:
    base = [
        ("Ручка Parker Jotter XL", 24.99, None, "Нержавеющая сталь, стержень Quinkflow"),
        ("Блокнот Moleskine Classic Large", 19.99, None, "Линейка, 240 стр, твёрдая обложка"),
        ("Степлер Swingline Optima 40", 29.99, 34.99, "40 листов, Low Force, jam-free"),
        ("Маркеры Stabilo Boss 15шт", 14.99, None, "Пастельные + яркие, 2-5 мм"),
        ("Органайзер для стола Grovemade", 89.99, None, "Орех, 3 секции, кабель-менеджмент"),
        ("Бумага HP Premium A4 500л", 9.99, None, "80 г/м², ColorLok, для лазерных"),
        ("Калькулятор Casio FX-991CW", 24.99, None, "Научный, 540+ функций, солнечная батарея"),
        ("Ламинатор Fellowes Saturn 3i A4", 79.99, 99.99, "80-125 мкм, 1 мин прогрев"),
        ("Набор карандашей Faber-Castell 36шт", 29.99, None, "Polychromos, профессиональные, жестяная коробка"),
        ("Папка-регистратор Leitz 180° 10шт", 39.99, None, "75 мм, механизм 180°, 5 цветов"),
        ("Клейкие стикеры Post-it Super Sticky", 12.99, None, "12 блоков, 76x76 мм, 6 цветов"),
        ("Ножницы Fiskars Titanium 21 см", 14.99, None, "Титановое покрытие, эргономичные"),
        ("Доска магнитная Quartet 90x60", 49.99, 59.99, "Маркерная, алюминиевая рамка, магниты"),
        ("Скотч 3M Magic Tape 6шт", 9.99, None, "Невидимый, матовый, 19 мм x 33 м"),
        ("Файлы-вкладыши Esselte A4 100шт", 7.99, None, "Прозрачные, 60 мкм, перфорация"),
        ("Печать самонаборная Colop R40", 29.99, None, "Круглая, 2 круга текста, подушка"),
        ("Точилка электрическая X-Acto", 24.99, 29.99, "Автостоп, контейнер, тихая"),
        ("Набор гелевых ручек Pilot G2 12шт", 14.99, None, "0.7 мм, 12 цветов, сменные стержни"),
        ("Корзина для бумаг Umbra Skinny", 12.99, None, "7.5 л, полипропилен, 4 цвета"),
        ("Настольный календарь Leuchtturm1917", 16.99, None, "2026, еженедельник, твёрдая обложка"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


def _products_food() -> list[dict]:
    base = [
        ("Кофе в зёрнах Lavazza Super Crema 1кг", 19.99, None, "Арабика + робуста, средняя обжарка"),
        ("Чай Twinings Earl Grey 100 пакетиков", 8.99, None, "Бергамот, классический английский"),
        ("Шоколад Lindt Excellence 85% 10шт", 29.99, 34.99, "Тёмный, 100г каждый, швейцарский"),
        ("Оливковое масло Frantoi Cutrera 750мл", 24.99, None, "Extra Virgin, Сицилия, DOP"),
        ("Мёд Manuka Health MGO 400+ 500г", 49.99, None, "Новая Зеландия, антибактериальный"),
        ("Паста De Cecco Spaghetti №12 6шт", 14.99, None, "500г каждый, бронзовая матрица"),
        ("Рис Koshihikari 5кг", 29.99, 34.99, "Японский, премиум, для суши"),
        ("Орехи микс Kirkland 1.13кг", 19.99, None, "Кешью, миндаль, фисташки, пекан"),
        ("Протеин Optimum Nutrition Gold 2.27кг", 59.99, 69.99, "Whey, 24г белка, 5г BCAA"),
        ("Матча Ippodo Ummon 40г", 34.99, None, "Церемониальный, Удзи, Киото"),
        ("Варенье Bonne Maman набор 6шт", 24.99, None, "Клубника, абрикос, вишня, малина, черника, апельсин"),
        ("Кокосовое масло Nutiva Organic 1.6л", 19.99, None, "Virgin, холодный отжим, USDA Organic"),
        ("Гранола Bear Naked 1.2кг", 12.99, 14.99, "Мёд, миндаль, без ГМО"),
        ("Соус Sriracha Huy Fong 740мл", 6.99, None, "Оригинальный, острый, чеснок"),
        ("Кофе молотый illy Classico 250г 6шт", 49.99, None, "100% арабика, средняя обжарка"),
        ("Сухофрукты Mariani 1кг", 14.99, None, "Манго, ананас, папайя, без сахара"),
        ("Масло сливочное Kerrygold 454г 4шт", 19.99, 24.99, "Ирландское, травяной откорм"),
        ("Чипсы Torres Truffle 150г 6шт", 29.99, None, "Чёрный трюфель, Испания"),
        ("Вода San Pellegrino 12x750мл", 18.99, None, "Газированная, минеральная, Италия"),
        ("Энергетик Monster Energy 24шт", 34.99, 39.99, "500 мл, Original, кофеин 160 мг"),
    ]
    return [{"name": n, "price": p, "old_price": o, "description": d} for n, p, o, d in base]


# Map category slug -> product generator
_GENERATORS = {
    "smartphones": _products_smartphones,
    "laptops": _products_laptops,
    "audio": _products_audio,
    "tv": _products_tv,
    "cameras": _products_cameras,
    "gaming": _products_gaming,
    "smart-home": _products_smart_home,
    "mens-clothing": _products_mens_clothing,
    "womens-clothing": _products_womens_clothing,
    "shoes": _products_shoes,
    "sports": _products_sports,
    "beauty": _products_beauty,
    "home-garden": _products_home_garden,
    "kitchen": _products_kitchen,
    "kids": _products_kids,
    "books": _products_books,
    "auto": _products_auto,
    "pets": _products_pets,
    "office": _products_office,
    "food": _products_food,
}


def generate_all_products() -> list[dict[str, Any]]:
    """
    Return a flat list of 400 product dicts ready for DB insertion.
    Each dict has: name, slug, description, price, old_price, sku, stock,
    category_slug, image, rating, sales_count, is_active, is_featured.
    """
    import re
    all_products: list[dict[str, Any]] = []
    global_idx = 0

    for cat_slug, gen_fn in _GENERATORS.items():
        items = gen_fn()
        for i, item in enumerate(items):
            global_idx += 1
            # Generate slug from name
            slug = re.sub(r"[^a-z0-9]+", "-", item["name"].lower().strip()).strip("-")
            # Ensure unique slug
            slug = f"{slug}-{global_idx}"
            # Stable image from picsum
            image_url = _img(global_idx + 1000)
            # Rating between 3.5 and 5.0
            rating = round(3.5 + (global_idx % 16) * 0.1, 1)
            if rating > 5.0:
                rating = 5.0
            # Stock between 5 and 200
            stock = 5 + (global_idx * 7) % 196
            # Sales count
            sales_count = (global_idx * 13) % 500
            # Featured: first 2 in each category
            is_featured = i < 2

            all_products.append({
                "name": item["name"],
                "slug": slug,
                "description": item["description"],
                "price": item["price"],
                "old_price": item.get("old_price"),
                "sku": f"SKU-{global_idx:04d}",
                "stock": stock,
                "category_slug": cat_slug,
                "image": image_url,
                "rating": rating,
                "sales_count": sales_count,
                "is_active": True,
                "is_featured": is_featured,
            })

    return all_products
