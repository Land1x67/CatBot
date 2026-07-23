import telebot
import requests
import random
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8885097596:AAGrUdH4CCjrLtZ-OdSt91LcAiieytJ83hQ"
ADMIN_IDS = [7145243599, 8263833251]

bot = telebot.TeleBot(TOKEN)
users = {}

COOLDOWN_CARD = 7200
COOLDOWN_SHOP = 3600

ALL_CATS = [
    {"name": "Дворовый хулиган", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/1"},
    {"name": "Барсик простой", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/2"},
    {"name": "Мурзик уличный", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/3"},
    {"name": "Васька бродяга", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/4"},
    {"name": "Рыжик заборный", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/5"},
    {"name": "Пушок пушистый", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/6"},
    {"name": "Снежок белый", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/7"},
    {"name": "Черныш ночной", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/8"},
    {"name": "Тиша домосед", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/9"},
    {"name": "Кузя озорник", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/10"},
    {"name": "Федя толстый", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/11"},
    {"name": "Боря ленивый", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/12"},
    {"name": "Леха рыжий", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/13"},
    {"name": "Петя полосатый", "rarity": "Обычный", "emoji": "⚪", "chance": 30, "price": 0, "photo": "https://cataas.com/cat/14"},
    
    {"name": "Сиамский наглец", "rarity": "Необычный", "emoji": "🟢", "chance": 22, "price": 50, "photo": "https://cataas.com/cat/15"},
    {"name": "Бенгалский тигр", "rarity": "Необычный", "emoji": "🟢", "chance": 22, "price": 50, "photo": "https://cataas.com/cat/16"},
    {"name": "Скоттиш фолд", "rarity": "Необычный", "emoji": "🟢", "chance": 22, "price": 50, "photo": "https://cataas.com/cat/17"},
    {"name": "Русский голубой", "rarity": "Необычный", "emoji": "🟢", "chance": 22, "price": 50, "photo": "https://cataas.com/cat/18"},
    {"name": "Ориентал изящный", "rarity": "Необычный", "emoji": "🟢", "chance": 22, "price": 50, "photo": "https://cataas.com/cat/19"},
    {"name": "Норвежский лесной", "rarity": "Необычный", "emoji": "🟢", "chance": 22, "price": 50, "photo": "https://cataas.com/cat/20"},
    {"name": "Мейн-кун рыжий", "rarity": "Необычный", "emoji": "🟢", "chance": 22, "price": 50, "photo": "https://cataas.com/cat/21"},
    {"name": "Сфинкс лысый", "rarity": "Необычный", "emoji": "🟢", "chance": 22, "price": 50, "photo": "https://cataas.com/cat/22"},
    
    {"name": "Мейн-кун бандит", "rarity": "Редкий", "emoji": "🔵", "chance": 15, "price": 150, "photo": "https://cataas.com/cat/23"},
    {"name": "Персидский лев", "rarity": "Редкий", "emoji": "🔵", "chance": 15, "price": 150, "photo": "https://cataas.com/cat/24"},
    {"name": "Рэгдолл игрушка", "rarity": "Редкий", "emoji": "🔵", "chance": 15, "price": 150, "photo": "https://cataas.com/cat/25"},
    {"name": "Корниш-рекс кудрявый", "rarity": "Редкий", "emoji": "🔵", "chance": 15, "price": 150, "photo": "https://cataas.com/cat/26"},
    {"name": "Девон-рекс кудрявый", "rarity": "Редкий", "emoji": "🔵", "chance": 15, "price": 150, "photo": "https://cataas.com/cat/27"},
    {"name": "Кимрик бесхвостый", "rarity": "Редкий", "emoji": "🔵", "chance": 15, "price": 150, "photo": "https://cataas.com/cat/28"},
    {"name": "Бомбейский пантера", "rarity": "Редкий", "emoji": "🔵", "chance": 15, "price": 150, "photo": "https://cataas.com/cat/29"},
    {"name": "Сингапура карликовый", "rarity": "Редкий", "emoji": "🔵", "chance": 15, "price": 150, "photo": "https://cataas.com/cat/30"},
    
    {"name": "Лысый сфинкс", "rarity": "Эпический", "emoji": "🟣", "chance": 9, "price": 350, "photo": "https://cataas.com/cat/31"},
    {"name": "Саванна дикая", "rarity": "Эпический", "emoji": "🟣", "chance": 9, "price": 350, "photo": "https://cataas.com/cat/32"},
    {"name": "Селкирк-рекс кучерявый", "rarity": "Эпический", "emoji": "🟣", "chance": 9, "price": 350, "photo": "https://cataas.com/cat/33"},
    {"name": "Египетская мау пятнистая", "rarity": "Эпический", "emoji": "🟣", "chance": 9, "price": 350, "photo": "https://cataas.com/cat/34"},
    {"name": "Тойгер полосатый", "rarity": "Эпический", "emoji": "🟣", "chance": 9, "price": 350, "photo": "https://cataas.com/cat/35"},
    {"name": "Чаузи камышовый", "rarity": "Эпический", "emoji": "🟣", "chance": 9, "price": 350, "photo": "https://cataas.com/cat/36"},
    {"name": "Оцикет дикий", "rarity": "Эпический", "emoji": "🟣", "chance": 9, "price": 350, "photo": "https://cataas.com/cat/37"},
    
    {"name": "Британский аристократ", "rarity": "Легендарный", "emoji": "🔥", "chance": 5, "price": 700, "photo": "https://cataas.com/cat/38"},
    {"name": "Каракал рысь", "rarity": "Легендарный", "emoji": "🔥", "chance": 5, "price": 700, "photo": "https://cataas.com/cat/39"},
    {"name": "Сервал длинноногий", "rarity": "Легендарный", "emoji": "🔥", "chance": 5, "price": 700, "photo": "https://cataas.com/cat/40"},
    {"name": "Бурма золотая", "rarity": "Легендарный", "emoji": "🔥", "chance": 5, "price": 700, "photo": "https://cataas.com/cat/41"},
    {"name": "Гималайский снежный", "rarity": "Легендарный", "emoji": "🔥", "chance": 5, "price": 700, "photo": "https://cataas.com/cat/42"},
    {"name": "Тонкинез сиамский", "rarity": "Легендарный", "emoji": "🔥", "chance": 5, "price": 700, "photo": "https://cataas.com/cat/43"},
    
    {"name": "Тайский призрак", "rarity": "Мифический", "emoji": "🌟", "chance": 2.5, "price": 1500, "photo": "https://cataas.com/cat/44"},
    {"name": "Лунный кот", "rarity": "Мифический", "emoji": "🌟", "chance": 2.5, "price": 1500, "photo": "https://cataas.com/cat/45"},
    {"name": "Звёздный странник", "rarity": "Мифический", "emoji": "🌟", "chance": 2.5, "price": 1500, "photo": "https://cataas.com/cat/46"},
    {"name": "Кошачий дракон", "rarity": "Мифический", "emoji": "🌟", "chance": 2.5, "price": 1500, "photo": "https://cataas.com/cat/47"},
    {"name": "Астральный лев", "rarity": "Мифический", "emoji": "🌟", "chance": 2.5, "price": 1500, "photo": "https://cataas.com/cat/48"},
    {"name": "Теневой охотник", "rarity": "Мифический", "emoji": "🌟", "chance": 2.5, "price": 1500, "photo": "https://cataas.com/cat/49"},
    
    {"name": "Кот-невидимка", "rarity": "Секретный", "emoji": "👁️", "chance": 1, "price": 3000, "photo": "https://cataas.com/cat/50"},
    {"name": "Некромант пушистый", "rarity": "Секретный", "emoji": "👁️", "chance": 1, "price": 3000, "photo": "https://cataas.com/cat/51"},
    {"name": "Властелин тьмы", "rarity": "Секретный", "emoji": "👁️", "chance": 1, "price": 3000, "photo": "https://cataas.com/cat/52"},
    {"name": "Кот Шрёдингера", "rarity": "Секретный", "emoji": "👁️", "chance": 1, "price": 3000, "photo": "https://cataas.com/cat/53"},
    {"name": "Бессмертный хранитель", "rarity": "Секретный", "emoji": "👁️", "chance": 1, "price": 3000, "photo": "https://cataas.com/cat/54"},
    
    {"name": "OG зимний кот", "rarity": "OG", "emoji": "🎄", "chance": 0.1, "price": 10000, "special": True, "photo": "https://cataas.com/cat/55"}
]

def get_user(user_id):
    if user_id not in users:
        users[user_id] = {"coins": 0, "collection": [], "shop_cards": [], "last_card": 0, "last_shop_refresh": 0}
    return users[user_id]

def can_open_card(user_id):
    user = get_user(user_id)
    now = time.time()
    if now - user["last_card"] < COOLDOWN_CARD:
        return False, int(COOLDOWN_CARD - (now - user["last_card"]))
    return True, 0

def can_refresh_shop(user_id):
    user = get_user(user_id)
    now = time.time()
    if now - user["last_shop_refresh"] < COOLDOWN_SHOP:
        return False, int(COOLDOWN_SHOP - (now - user["last_shop_refresh"]))
    return True, 0

def generate_shop(user_id):
    user = get_user(user_id)
    rarities = ["Обычный", "Необычный", "Редкий", "Эпический", "Легендарный", "Мифический", "Секретный"]
    selected_rarities = random.sample(rarities, 3)
    cards = []
    for rarity in selected_rarities:
        cats_of_rarity = [c for c in ALL_CATS if c["rarity"] == rarity and not c.get("special")]
        if cats_of_rarity:
            cards.append(random.choice(cats_of_rarity))
        else:
            cards.append(random.choice(ALL_CATS))
    user["shop_cards"] = cards
    user["last_shop_refresh"] = time.time()
    return cards

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours}ч {minutes}мин {secs}с"
    elif minutes > 0:
        return f"{minutes}мин {secs}с"
    else:
        return f"{secs}с"

def is_admin(user_id):
    return user_id in ADMIN_IDS

def get_user_id_by_username(username):
    username = username.replace('@', '').lower()
    for uid in users.keys():
        try:
            user_info = bot.get_chat(uid)
            if user_info.username and user_info.username.lower() == username:
                return uid
        except:
            continue
    return None

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    get_user(user_id)
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🎁 Открыть карту", callback_data="open_card"))
    markup.row(InlineKeyboardButton("🛒 Магазин", callback_data="shop"))
    markup.row(InlineKeyboardButton("💰 Монеты", callback_data="coins"))
    markup.row(InlineKeyboardButton("📚 Коллекция", callback_data="collection"))
    if is_admin(user_id):
        markup.row(InlineKeyboardButton("⚙️ Админ панель", callback_data="admin_panel"))
    bot.send_message(
        message.chat.id,
        "🐱 Привет! Напиши /Kotik чтобы получить карточку!\n"
        "⏳ Кулдаун на карты: 2 часа\n"
        "🔄 Кулдаун на обновление магазина: 1 час",
        reply_markup=markup
    )

@bot.message_handler(commands=['Kotik'])
def kotik_command(message):
    user_id = message.from_user.id
    user = get_user(user_id)
    can_open, remaining = can_open_card(user_id)
    if not can_open:
        bot.reply_to(message, f"⏳ Подожди ещё {format_time(remaining)} до следующей карты!")
        return
    selected = random.choices(ALL_CATS, weights=[c["chance"] for c in ALL_CATS])[0]
    coin_reward = selected.get("price", 0)
    user["coins"] += coin_reward
    user["collection"].append(selected)
    user["last_card"] = time.time()
    msg = f"{selected['emoji']} Выпал: {selected['name']}\nРедкость: {selected['rarity']}\n+{coin_reward} 🪙"
    try:
        bot.send_photo(message.chat.id, selected['photo'], caption=msg)
    except:
        bot.reply_to(message, msg + "\n(Фото не загрузилось, но карта твоя!)")
    if selected.get("special"):
        bot.send_message(message.chat.id, "🎄 ОГО! OG-кот! 1 из 1000!")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    user_id = call.from_user.id
    user = get_user(user_id)
    
    if call.data == "open_card":
        can_open, remaining = can_open_card(user_id)
        if not can_open:
            bot.answer_callback_query(call.id, f"⏳ Жди {format_time(remaining)}!", show_alert=True)
            return
        selected = random.choices(ALL_CATS, weights=[c["chance"] for c in ALL_CATS])[0]
        coin_reward = selected.get("price", 0)
        user["coins"] += coin_reward
        user["collection"].append(selected)
        user["last_card"] = time.time()
        msg = f"{selected['emoji']} Выпал: {selected['name']}\nРедкость: {selected['rarity']}\n+{coin_reward} 🪙"
        bot.answer_callback_query(call.id)
        try:
            bot.send_photo(call.message.chat.id, selected['photo'], caption=msg)
        except:
            bot.send_message(call.message.chat.id, msg + "\n(Фото не загрузилось, но карта твоя!)")
        if selected.get("special"):
            bot.send_message(call.message.chat.id, "🎄 ОГО! OG-кот! 1 из 1000!")

    elif call.data == "shop":
        cards = user.get("shop_cards", [])
        can_refresh, remaining = can_refresh_shop(user_id)
        text = "🛒 Магазин\n\n"
        if cards:
            for cat in cards:
                text += f"{cat['emoji']} {cat['name']} ({cat['rarity']}) — {cat['price']} 🪙\n"
        else:
            text += "Магазин пуст. Нажми 'Обновить'.\n"
        text += f"\n⏳ Обновление через: {format_time(remaining) if not can_refresh else 'Доступно!'}"
        markup = InlineKeyboardMarkup()
        if cards:
            for i, cat in enumerate(cards):
                markup.add(InlineKeyboardButton(f"Купить {cat['name']}", callback_data=f"buy_{i}"))
        if can_refresh:
            markup.add(InlineKeyboardButton("🔄 Обновить магазин", callback_data="refresh_shop"))
        else:
            markup.add(InlineKeyboardButton(f"⏳ Обновить ({format_time(remaining)})", callback_data="noop"))
        markup.add(InlineKeyboardButton("⬅️ Назад", callback_data="back"))
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, text, reply_markup=markup)

    elif call.data == "refresh_shop":
        can_refresh, remaining = can_refresh_shop(user_id)
        if not can_refresh:
            bot.answer_callback_query(call.id, f"⏳ Жди {format_time(remaining)}!", show_alert=True)
            return
        cards = generate_shop(user_id)
        text = "🛒 Магазин обновлён!\n\n"
        for cat in cards:
            text += f"{cat['emoji']} {cat['name']} ({cat['rarity']}) — {cat['price']} 🪙\n"
        text += "\n⏳ Обновление через: 1 час"
        markup = InlineKeyboardMarkup()
        for i, cat in enumerate(cards):
            markup.add(InlineKeyboardButton(f"Купить {cat['name']}", callback_data=f"buy_{i}"))
        markup.add(InlineKeyboardButton("⏳ Обновить (1ч)", callback_data="noop"))
        markup.add(InlineKeyboardButton("⬅️ Назад", callback_data="back"))
        bot.answer_callback_query(call.id)
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "noop":
        bot.answer_callback_query(call.id, "⏳ Подожди, кнопка пока не активна!")

    elif call.data.startswith("buy_"):
        idx = int(call.data.split("_")[1])
        if idx >= len(user["shop_cards"]):
            bot.answer_callback_query(call.id, "Карта уже продана, обнови магазин!")
            return
        cat = user["shop_cards"][idx]
        if user["coins"] < cat["price"]:
            bot.answer_callback_query(call.id, f"Недостаточно монет! Нужно {cat['price']} 🪙")
            return
        user["coins"] -= cat["price"]
        user["collection"].append(cat)
        user["shop_cards"].pop(idx)
        bot.answer_callback_query(call.id, f"✅ Ты купил {cat['name']} за {cat['price']} 🪙!")
        bot.send_message(call.message.chat.id, f"✅ {cat['emoji']} {cat['name']} добавлен в коллекцию!\nОсталось монет: {user['coins']} 🪙")

    elif call.data == "coins":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"💰 У тебя {user['coins']} 🪙 Кот-Коинов")

    elif call.data == "collection":
        if not user["collection"]:
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, "📚 У тебя пока нет котов. Открой карту!")
            return
        stats = {}
        for cat in user["collection"]:
            stats[cat["rarity"]] = stats.get(cat["rarity"], 0) + 1
        text = "📚 Твоя коллекция:\n\n"
        for rarity, count in stats.items():
            text += f"{rarity}: {count}\n"
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, text)

    elif call.data == "back":
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton("🎁 Открыть карту", callback_data="open_card"))
        markup.row(InlineKeyboardButton("🛒 Магазин", callback_data="shop"))
        markup.row(InlineKeyboardButton("💰 Монеты", callback_data="coins"))
        markup.row(InlineKeyboardButton("📚 Коллекция", callback_data="collection"))
        if is_admin(user_id):
            markup.row(InlineKeyboardButton("⚙️ Админ панель", callback_data="admin_panel"))
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            "🐱 Привет! Напиши /Kotik чтобы получить карточку!\n"
            "⏳ Кулдаун на карты: 2 часа\n"
            "🔄 Кулдаун на обновление магазина: 1 час",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    elif call.data == "admin_panel":
        if not is_admin(user_id):
            bot.answer_callback_query(call.id, "❌ Ты не админ!", show_alert=True)
            return
        show_admin_panel(call.message.chat.id)
        bot.answer_callback_query(call.id)

    elif call.data == "admin_users":
        if not is_admin(user_id):
            bot.answer_callback_query(call.id, "❌ Ты не админ!", show_alert=True)
            return
        text = get_users_list()
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, text)

    elif call.data == "admin_give_coins":
        if not is_admin(user_id):
            bot.answer_callback_query(call.id, "❌ Ты не админ!", show_alert=True)
            return
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📝 Введи команду:\n`/givecoins @username 100`\nили `/givecoins 123456789 100`", parse_mode="Markdown")

    elif call.data == "admin_broadcast":
        if not is_admin(user_id):
            bot.answer_callback_query(call.id, "❌ Ты не админ!", show_alert=True)
            return
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📝 Введи команду:\n`/broadcast Текст сообщения`", parse_mode="Markdown")

    elif call.data == "admin_reset_all":
        if not is_admin(user_id):
            bot.answer_callback_query(call.id, "❌ Ты не админ!", show_alert=True)
            return
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📝 Команда `/reset_all` — обнулит ВСЕХ пользователей.")

    elif call.data == "admin_reset_user":
        if not is_admin(user_id):
            bot.answer_callback_query(call.id, "❌ Ты не админ!", show_alert=True)
            return
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📝 Формат: `/reset_user @username` или `/reset_user 123456789`")

    elif call.data == "admin_add_shop":
        if not is_admin(user_id):
            bot.answer_callback_query(call.id, "❌ Ты не админ!", show_alert=True)
            return
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📝 Формат: `/add_shop @username Название карты`\nИли: `/add_shop все Название карты`")

    elif call.data == "admin_reset_shop":
        if not is_admin(user_id):
            bot.answer_callback_query(call.id, "❌ Ты не админ!", show_alert=True)
            return
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📝 Формат: `/reset_shop @username` или `/reset_shop все`")

    elif call.data == "admin_reset_coins":
        if not is_admin(user_id):
            bot.answer_callback_query(call.id, "❌ Ты не админ!", show_alert=True)
            return
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📝 Формат: `/reset_coins @username` или `/reset_coins все`")

    elif call.data == "admin_reset_collection":
        if not is_admin(user_id):
            bot.answer_callback_query(call.id, "❌ Ты не админ!", show_alert=True)
            return
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📝 Формат: `/reset_collection @username` или `/reset_collection все`")

def show_admin_panel(chat_id):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("📊 Список пользователей", callback_data="admin_users"))
    markup.row(InlineKeyboardButton("💰 Выдать монеты", callback_data="admin_give_coins"))
    markup.row(InlineKeyboardButton("📢 Рассылка", callback_data="admin_broadcast"))
    markup.row(InlineKeyboardButton("🔄 Обнулить ВСЁ", callback_data="admin_reset_all"))
    markup.row(InlineKeyboardButton("🔄 Обнулить пользователя", callback_data="admin_reset_user"))
    markup.row(InlineKeyboardButton("➕ Добавить в магазин", callback_data="admin_add_shop"))
    markup.row(InlineKeyboardButton("🗑️ Очистить магазин", callback_data="admin_reset_shop"))
    markup.row(InlineKeyboardButton("💰 Обнулить монеты", callback_data="admin_reset_coins"))
    markup.row(InlineKeyboardButton("📚 Обнулить коллекцию", callback_data="admin_reset_collection"))
    markup.row(InlineKeyboardButton("⬅️ Назад", callback_data="back"))
    bot.send_message(chat_id, "⚙️ Админ панель", reply_markup=markup)

def get_users_list():
    if not users:
        return "📊 Пользователей пока нет."
    text = f"📊 Всего пользователей: {len(users)}\n\n"
    for uid, data in users.items():
        try:
            username = bot.get_chat(uid).username or "нет юзернейма"
        except:
            username = "неизвестно"
        text += f"👤 ID: {uid} (@{username})\n"
        text += f"💰 Монет: {data['coins']}\n"
        text += f"📚 Карт: {len(data['collection'])}\n"
        text += f"⏳ Последняя карта: {format_time(int(time.time() - data['last_card']))} назад\n"
        text += "—" * 20 + "\n"
    return text

@bot.message_handler(commands=['admin'])
def admin_command(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        bot.reply_to(message, "❌ Ты не админ, сука!")
        return
    show_admin_panel(message.chat.id)

@bot.message_handler(commands=['givecoins'])
def give_coins_command(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        bot.reply_to(message, "❌ Ты не админ, сука!")
        return
    try:
        parts = message.text.split()
        target = parts[1]
        amount = int(parts[2])
        target_id = None
        if target.startswith('@'):
            target_id = get_user_id_by_username(target)
            if not target_id:
                bot.reply_to(message, f"❌ Пользователь {target} не найден.")
                return
        else:
            target_id = int(target)
            if target_id not in users:
                bot.reply_to(message, f"❌ Пользователь с ID {target_id} не найден.")
                return
        users[target_id]["coins"] += amount
        bot.reply_to(message, f"✅ Пользователю {target} выдано {amount} 🪙")
    except:
        bot.reply_to(message, "❌ Формат: `/givecoins @username 100` или `/givecoins 123456789 100`")

@bot.message_handler(commands=['broadcast'])
def broadcast_command(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        bot.reply_to(message, "❌ Ты не админ, сука!")
        return
    text = message.text.replace('/broadcast', '', 1).strip()
    if not text:
        bot.reply_to(message, "❌ Напиши текст для рассылки!")
        return
    sent = 0
    for uid in users.keys():
        try:
            bot.send_message(uid, f"📢 Админ: {text}")
            sent += 1
            time.sleep(0.05)
        except:
            pass
    bot.reply_to(message, f"✅ Рассылка отправлена {sent} пользователям.")

@bot.message_handler(commands=['reset_all'])
def reset_all_command(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        bot.reply_to(message, "❌ Ты не админ, сука!")
        return
    for uid in users.keys():
        users[uid] = {"coins": 0, "collection": [], "shop_cards": [], "last_card": 0, "last_shop_refresh": 0}
    bot.reply_to(message, "✅ ВСЕ ПОЛЬЗОВАТЕЛИ ОБНУЛЕНЫ!")

@bot.message_handler(commands=['reset_user'])
def reset_user_command(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        bot.reply_to(message, "❌ Ты не админ, сука!")
        return
    try:
        parts = message.text.split()
        target = parts[1]
        target_id = None
        if target.startswith('@'):
            target_id = get_user_id_by_username(target)
            if not target_id:
                bot.reply_to(message, f"❌ Пользователь {target} не найден.")
                return
        else:
            target_id = int(target)
            if target_id not in users:
                bot.reply_to(message, f"❌ Пользователь с ID {target_id} не найден.")
                return
        users[target_id] = {"coins": 0, "collection": [], "shop_cards": [], "last_card": 0, "last_shop_refresh": 0}
        bot.reply_to(message, f"✅ Пользователь {target} обнулён.")
    except:
        bot.reply_to(message, "❌ Формат: `/reset_user @username` или `/reset_user 123456789`")

@bot.message_handler(commands=['reset_coins'])
def reset_coins_command(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        bot.reply_to(message, "❌ Ты не админ, сука!")
        return
    try:
        parts = message.text.split()
        target = parts[1]
        if target.lower() in ['все', 'all']:
            for uid in users.keys():
                users[uid]["coins"] = 0
            bot.reply_to(message, f"✅ Монеты обнулены у {len(users)} пользователей!")
            return
        target_id = None
        if target.startswith('@'):
            target_id = get_user_id_by_username(target)
            if not target_id:
                bot.reply_to(message, f"❌ Пользователь {target} не найден.")
                return
        else:
            target_id = int(target)
            if target_id not in users:
                bot.reply_to(message, f"❌ Пользователь с ID {target_id} не найден.")
                return
        users[target_id]["coins"] = 0
        bot.reply_to(message, f"✅ Монеты для {target} обнулены.")
    except:
        bot.reply_to(message, "❌ Формат: `/reset_coins @username` или `/reset_coins все`")

@bot.message_handler(commands=['reset_collection'])
def reset_collection_command(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        bot.reply_to(message, "❌ Ты не админ, сука!")
        return
    try:
        parts = message.text.split()
        target = parts[1]
        if target.lower() in ['все', 'all']:
            for uid in users.keys():
                users[uid]["collection"] = []
            bot.reply_to(message, f"✅ Коллекции очищены у {len(users)} пользователей!")
            return
        target_id = None
        if target.startswith('@'):
            target_id = get_user_id_by_username(target)
            if not target_id:
                bot.reply_to(message, f"❌ Пользователь {target} не найден.")
                return
        else:
            target_id = int(target)
            if target_id not in users:
                bot.reply_to(message, f"❌ Пользователь с ID {target_id} не найден.")
                return
        users[target_id]["collection"] = []
        bot.reply_to(message, f"✅ Коллекция для {target} очищена.")
    except:
        bot.reply_to(message, "❌ Формат: `/reset_collection @username` или `/reset_collection все`")

@bot.message_handler(commands=['reset_shop'])
def reset_shop_command(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        bot.reply_to(message, "❌ Ты не админ, сука!")
        return
    try:
        parts = message.text.split()
        target = parts[1]
        if target.lower() in ['все', 'all']:
            for uid in users.keys():
                users[uid]["shop_cards"] = []
            bot.reply_to(message, f"✅ Магазины очищены у {len(users)} пользователей!")
            return
        target_id = None
        if target.startswith('@'):
            target_id = get_user_id_by_username(target)
            if not target_id:
                bot.reply_to(message, f"❌ Пользователь {target} не найден.")
                return
        else:
            target_id = int(target)
            if target_id not in users:
                bot.reply_to(message, f"❌ Пользователь с ID {target_id} не найден.")
                return
        users[target_id]["shop_cards"] = []
        bot.reply_to(message, f"✅ Магазин для {target} очищен.")
    except:
        bot.reply_to(message, "❌ Формат: `/reset_shop @username` или `/reset_shop все`")

@bot.message_handler(commands=['add_shop'])
def add_shop_command(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        bot.reply_to(message, "❌ Ты не админ, сука!")
        return
    try:
        parts = message.text.split(maxsplit=2)
        if len(parts) < 3:
            bot.reply_to(message, "❌ Формат: `/add_shop @username Название карты`\nИли: `/add_shop все Название карты`")
            return
        target = parts[1]
        card_name = parts[2].strip()
        found_cat = None
        for cat in ALL_CATS:
            if cat['name'].lower() == card_name.lower():
                found_cat = cat.copy()
                break
        if not found_cat:
            bot.reply_to(message, f"❌ Карта '{card_name}' не найдена.")
            return
        if target.lower() in ['все', 'all']:
            count = 0
            for uid in users.keys():
                if "shop_cards" not in users[uid]:
                    users[uid]["shop_cards"] = []
                users[uid]["shop_cards"].append(found_cat)
                count += 1
            bot.reply_to(message, f"✅ Карта '{found_cat['name']}' добавлена в магазин {count} пользователям!")
            return
        target_id = None
        if target.startswith('@'):
            target_id = get_user_id_by_username(target)
            if not target_id:
                bot.reply_to(message, f"❌ Пользователь {target} не найден.")
                return
        else:
            target_id = int(target)
            if target_id not in users:
                bot.reply_to(message, f"❌ Пользователь с ID {target_id} не найден.")
                return
        if "shop_cards" not in users[target_id]:
            users[target_id]["shop_cards"] = []
        users[target_id]["shop_cards"].append(found_cat)
        bot.reply_to(message, f"✅ Карта '{found_cat['name']}' добавлена в магазин для {target}!")
    except:
        bot.reply_to(message, "❌ Формат: `/add_shop @username Название карты`")

if __name__ == "__main__":
    print("🐱 Бот с админ панелью запущен, сука!")
    print(f"👑 Админы: {ADMIN_IDS}")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"Ошибка: {e}. Перезапуск через 5 секунд...")
            time.sleep(5)
