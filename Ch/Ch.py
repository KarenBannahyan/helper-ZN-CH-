import datetime
import random
import schedule
import time
from pypinyin import pinyin, Style

# Глобальная переменная для текущего языка
current_language = 'English'

def get_pinyin(chinese_character):
    pinyin_list = pinyin(chinese_character, style=Style.TONE)
    pinyin_str = ''.join([item[0] for item in pinyin_list])
    return pinyin_str


def show_words():
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            if content:
                print("Saved words with translations and transcriptions:")
                print(content)
            else:
                print("File is empty.")
    except FileNotFoundError:
        print("File words.txt not found. Add words before viewing.")

def show_words_RU():
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            if content:
                print("Сохраненные слова с переводом и c транскрипцией:")
                print(content)
            else:
                print("Файл пустой.")
    except FileNotFoundError:
        print("Файл words.txt не найден.")

def show_stats():
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                print("File is empty.")
                return

            now = datetime.datetime.now()
            one_day_ago = now - datetime.timedelta(days=1)
            one_week_ago = now - datetime.timedelta(weeks=1)
            one_month_ago = now - datetime.timedelta(days=30)
            one_year_ago = now - datetime.timedelta(days=365)

            count_day = 0
            count_week = 0
            count_month = 0
            count_year = 0

            for line in lines:
                date_str = line.split(" | ")[1].strip()
                word_date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

                if word_date >= one_day_ago:
                    count_day += 1
                if word_date >= one_week_ago:
                    count_week += 1
                if word_date >= one_month_ago:
                    count_month += 1
                if word_date >= one_year_ago:
                    count_year += 1

            print(f"Statistics of added words:")
            print(f"Today: {count_day}")
            print(f"Last week: {count_week}")
            print(f"Last month: {count_month}")
            print(f"Last year: {count_year}")

    except FileNotFoundError:
        print("File words.txt not found. Add words before viewing.")

def show_stats_RU():
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                print("Файл пустой.")
                return

            now = datetime.datetime.now()
            one_day_ago = now - datetime.timedelta(days=1)
            one_week_ago = now - datetime.timedelta(weeks=1)
            one_month_ago = now - datetime.timedelta(days=30)
            one_year_ago = now - datetime.timedelta(days=365)

            count_day = 0
            count_week = 0
            count_month = 0
            count_year = 0

            for line in lines:
                date_str = line.split(" | ")[1].strip()
                word_date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

                if word_date >= one_day_ago:
                    count_day += 1
                if word_date >= one_week_ago:
                    count_week += 1
                if word_date >= one_month_ago:
                    count_month += 1
                if word_date >= one_year_ago:
                    count_year += 1

            print(f"Статистика добавленных слов:")
            print(f"Сегодня: {count_day}")
            print(f"За неделю: {count_week}")
            print(f"За месяц: {count_month}")
            print(f"За год: {count_year}")

    except FileNotFoundError:
        print("Файл words.txt не найден.")

def exam():
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                print("File is empty. Add words before starting the exam.")
                return

            random.shuffle(lines)
            correct_answers = 0
            total_questions = len(lines)

            for line in lines:
                chinese_character = line.split("] ")[1].split(":")[0].strip()
                correct_translation = line.split(": ")[1].split(" | ")[0].strip()

                user_translation = input(f"Translate the character '{chinese_character}': ")

                if user_translation.lower() == correct_translation.lower():
                    print("Correct!")
                    correct_answers += 1
                else:
                    print(f"Incorrect. Correct translation: {correct_translation}")

            print(f"You answered correctly {correct_answers} out of {total_questions} questions.")
    except FileNotFoundError:
        print("File words.txt not found. Add words before starting the exam.")
def exam_RU():
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                print("Файл пустой.")
                return

            random.shuffle(lines)
            correct_answers = 0
            total_questions = len(lines)

            for line in lines:
                chinese_character = line.split("] ")[1].split(":")[0].strip()
                correct_translation = line.split(": ")[1].split(" | ")[0].strip()

                user_translation = input(f"Переведите иероглиф '{chinese_character}': ")

                if user_translation.lower() == correct_translation.lower():
                    print("Правильно!")
                    correct_answers += 1
                else:
                    print(f"Неправильно. Правельный перевод: {correct_translation}")

            print(f"Правильно ответили на {correct_answers} из {total_questions} вопросов.")
    except FileNotFoundError:
        print("Файл words.txt не найден.")


def copy_words():
    try:
        with open('words.txt', 'r', encoding='utf-8') as source_file:
            with open('words_copy.txt', 'w', encoding='utf-8') as dest_file:
                dest_file.write(source_file.read())
                print(f"Content of words.txt copied to words_copy.txt at {datetime.datetime.now()}")

    except FileNotFoundError:
        print("File words.txt not found. Cannot copy.")
def copy_words_RU():
    try:
        with open('words.txt', 'r', encoding='utf-8') as source_file:
            with open('words_copy.txt', 'w', encoding='utf-8') as dest_file:
                dest_file.write(source_file.read())
                print(f"Контент words.txt копирован в words_copy.txt во {datetime.datetime.now()}")

    except FileNotFoundError:
        print("Файл words.txt не найден.")


def add_word(chinese_character, translation):
    try:
        pinyin_transcription = get_pinyin(chinese_character)
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open('words.txt', 'a', encoding='utf-8') as file:
            file.write(f"[{pinyin_transcription}] {chinese_character}: {translation} | {current_time}\n")

        print(f"Word '{chinese_character}' added to words.txt.")
    except Exception as e:
        print(f"Error adding word: {str(e)}")
def add_word_RU(chinese_character, translation):
    try:
        pinyin_transcription = get_pinyin(chinese_character)
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open('words.txt', 'a', encoding='utf-8') as file:
            file.write(f"[{pinyin_transcription}] {chinese_character}: {translation} | {current_time}\n")

        print(f"Слово '{chinese_character}' добавлен в words.txt.")
    except Exception as e:
        print(f"Ошибка добавления слова: {str(e)}")


def delete_word(chinese_character):
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open('words.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                if chinese_character not in line:
                    file.write(line)

        print(f"Word '{chinese_character}' deleted from words.txt.")
    except FileNotFoundError:
        print("File words.txt not found. Cannot delete word.")

def delete_word_RU(chinese_character):
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open('words.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                if chinese_character not in line:
                    file.write(line)

        print(f"Слово '{chinese_character}' удалено с words.txt.")
    except FileNotFoundError:
        print("Файл words.txt не надйен.")

def get_pinyin(chinese_character):
    try:
        pinyin_list = pinyin(chinese_character, style=Style.TONE)
        pinyin_str = ''.join([item[0] for item in pinyin_list])
        return pinyin_str
    except Exception as e:
        print(f"Error '{chinese_character}': {str(e)}")
        return None
def get_pinyin_RU(chinese_character):
    try:
        pinyin_list = pinyin(chinese_character, style=Style.TONE)
        pinyin_str = ''.join([item[0] for item in pinyin_list])
        return pinyin_str
    except Exception as e:
        print(f"Ошибка при получении пиньиня для '{chinese_character}': {str(e)}")
        return None
def edit_word(chinese_character):
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        edited_lines = []
        for line in lines:
            if chinese_character in line:
                print(f"Current translation for '{chinese_character}': {line.split(': ')[1].split(' | ')[0].strip()}")
                new_translation = input(f"Enter new translation for '{chinese_character}': ")
                line = line.replace(line.split(': ')[1].split(' | ')[0].strip(), new_translation)
            edited_lines.append(line)

        with open('words.txt', 'w', encoding='utf-8') as file:
            file.writelines(edited_lines)

        print(f"Word '{chinese_character}' successfully edited in words.txt.")
    except FileNotFoundError:
        print("File words.txt not found. Cannot edit word.")

def edit_word_RU(chinese_character):
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        edited_lines = []
        for line in lines:
            if chinese_character in line:
                print(f"Текущий перевод для '{chinese_character}': {line.split(': ')[1].split(' | ')[0].strip()}")
                new_translation = input(f"Напишите новый перевод '{chinese_character}': ")
                line = line.replace(line.split(': ')[1].split(' | ')[0].strip(), new_translation)
            edited_lines.append(line)

        with open('words.txt', 'w', encoding='utf-8') as file:
            file.writelines(edited_lines)

        print(f"Слово '{chinese_character}' успешно изменен в words.txt.")
    except FileNotFoundError:
        print("Файл words.txt не найден.")

def show_level():
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_words = len(lines)
            current_level = calculate_hsk_level(total_words)
            print(f"Current language proficiency level according to HSK standard: {current_level}")
    except FileNotFoundError:
        print("File words.txt not found. Add words before checking level.")

def show_level_RU():
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_words = len(lines)
            current_level = calculate_hsk_level(total_words)
            print(f"Текущий уровень владения языком в соответствии со стандартом HSK: {current_level}")
    except FileNotFoundError:
        print("Файл words.txt не найден.")

def calculate_hsk_level(total_words):
    if total_words < 150:
        return "HSK1"
    elif total_words < 300:
        return "HSK2"
    elif total_words < 600:
        return "HSK3"
    elif total_words < 1200:
        return "HSK4"
    elif total_words < 2500:
        return "HSK5"
    else:
        return "HSK6"


def today():
    try:
        today_words = []
        today_date = datetime.datetime.now().strftime('%Y-%m-%d')

        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                date_str = line.split(" | ")[1].strip()
                word_date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                if word_date == today_date:
                    chinese_character = line.split("] ")[1].split(":")[0].strip()
                    today_words.append(chinese_character)

        if today_words:
            print(f"Characters added today ({today_date}):")
            for word in today_words:
                print(word)
        else:
            print(f"No characters added today.")
    except FileNotFoundError:
        print("File words.txt not found. Cannot show today's additions.")

def today_RU():
    try:
        today_words = []
        today_date = datetime.datetime.now().strftime('%Y-%m-%d')

        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                date_str = line.split(" | ")[1].strip()
                word_date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                if word_date == today_date:
                    chinese_character = line.split("] ")[1].split(":")[0].strip()
                    today_words.append(chinese_character)

        if today_words:
            print(f"Слова добавленные сегодня ({today_date}):")
            for word in today_words:
                print(word)
        else:
            print(f"Нету добавленных слов сегодня.")
    except FileNotFoundError:
        print("Файл words.txt не найден.")

def progress():
    try:
        now = datetime.datetime.now()
        one_week_ago = now - datetime.timedelta(weeks=1)
        one_month_ago = now - datetime.timedelta(days=30)
        one_year_ago = now - datetime.timedelta(days=365)

        week_count = 0
        month_count = 0
        year_count = 0

        with open('words.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                date_str = line.split(" | ")[1].strip()
                word_date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

                if word_date >= one_week_ago:
                    week_count += 1
                if word_date >= one_month_ago:
                    month_count += 1
                if word_date >= one_year_ago:
                    year_count += 1

        print(f"Progress over the last week: {week_count} words")
        print(f"Progress over the last month: {month_count} words")
        print(f"Progress over the last year: {year_count} words")

    except FileNotFoundError:
        print("File words.txt not found. Cannot calculate progress.")


def change_language():
    global current_language
    print("Available languages:")
    print("  - English")
    print("  - Russian")
    new_language = input("Enter language (English/Russian): ").strip().lower()

    if new_language == 'english' or new_language == 'russian':
        current_language = new_language.capitalize()
        print(f"Language set to {current_language}.")
    else:
        print("Invalid language. Please enter 'English' or 'Russian'.")

def change_language_RU():
    global current_language
    print("Доступные языки:")
    print("  - English")
    print("  - Russian")
    new_language = input("Напишите язык (English/Russian): ").strip().lower()

    if new_language == 'english' or new_language == 'russian':
        current_language = new_language.capitalize()
        print(f"Язык сменился на {current_language}.")
    else:
        print("Неверный язык. Напишите 'English' или 'Russian'.")
def display_commands():
    print("Available commands:")
    print("  - add: Add a word to words.txt")
    print("  - show: Show all saved words")
    print("  - stats: Show statistics of added words")
    print("  - exam: Start a character exam")
    print("  - delete: Delete a word from words.txt")
    print("  - edit: Edit a word in words.txt")
    print("  - showlevel: Show language proficiency level according to HSK standard")
    print("  - today: Show characters added today")
    print("  - progress: Show progress over the last week, month, and year")
    print("  - settings: Change application settings (language)")
    print("  - help: Show command list")
    print("  - char: Show transmission of the character")
    print("  - creator: Show creators name")

def display_commands_RU():
    print("Добавленные команды:")
    print("  - add: Добавить слово в файл words.txt")
    print("  - show: Показать все сохраненные слова")
    print("  - stats: Показать статистику добавленных слов")
    print("  - exam: Начать экзамен по иероглифам")
    print("  - delete: Удалить слово из файла words.txt")
    print("  - edit: Редактировать слово в файле words.txt")
    print("  - showlevel: Показать уровень владения языком по стандарту HSK")
    print("  - today: Показать иероглифы, добавленные сегодня")
    print("  - progress: Показать прогресс за последнюю неделю, месяц и год")
    print("  - settings: Изменить настройки приложения (язык)")
    print("  - help: Показать список команд")
    print("  - char: Показать трансмиссию иероглифа")
    print("  - creator: Показать имя создателя")

if __name__ == "__main__":
    schedule.every(10).minutes.do(copy_words)

    while True:
        if (current_language == "English"):
            command = input("Enter command ('help' for command list): ")
        elif (current_language == "Russian"):
            command = input("Напишите комманду ('help' для списка команд): ")
        if command.lower() == 'help':
            if (current_language == "English"):
                display_commands()
            elif (current_language == "Russian"):
                display_commands_RU()
        elif command.lower() == 'show':
            if (current_language == "English"):
                show_words()
            elif (current_language == "Russian"):
                show_words_RU()
        elif command.lower() == 'stats':
            if (current_language == "English"):
                show_stats()
            elif (current_language == "Russian"):
                show_stats_RU()
        elif command.lower() == 'exam':
            if (current_language == "English"):
                exam()
            elif (current_language == "Russian"):
                exam_RU()
        elif command.lower() == 'add':
            if (current_language == "English"):
                chinese_character = input("Enter Chinese character: ")
                translation = input("Enter translation of the character: ")
                add_word(chinese_character, translation)
            elif (current_language == 'Russian'):
                chinese_character = input("Напишите китайский иероглиф: ")
                translation = input("Напишите перевод иероглифа: ")
                add_word_RU(chinese_character, translation)
        elif command.lower() == 'delete':
            if (current_language == "English"):
                chinese_character = input("Enter Chinese character to delete: ")
                delete_word(chinese_character)
            elif (current_language == "Russian"):
                chinese_character = input("Напишите китайский иероглиф для удаления: ")
                delete_word_RU(chinese_character)
        elif command.lower() == 'edit':
            if (current_language == "English"):
                chinese_character = input("Enter Chinese character to edit: ")
                edit_word(chinese_character)
            elif (current_language == "Russian"):
                chinese_character = input("Напишите иероглиф для удаления: ")
                edit_word_RU(chinese_character)
        elif command.lower() == 'showlevel':
            if (current_language == "English"):
                show_level()
            elif (current_language == "Russian"):
                show_level_RU()
        elif command.lower() == 'today':
            if (current_language == "English"):
                today()
            elif (current_language == "Russian"):
                today_RU()
        elif command.lower() == 'settings':
            if (current_language == "English"):
                change_language()
            elif (current_language == "Russian"):
                change_language_RU()
        elif command.lower() == 'char':
                if (current_language == "English"):
                    p = input("Enter the character: ")
                    print(f'Answer: {get_pinyin(p)}')
                elif (current_language == "Russian"):
                    p = input("Напишите иероглиф: ")
                    print(f'Ответ: {get_pinyin(p)}')
        elif command.lower() == 'creator':
            print("Karen Bannahyan (This application have c++ version for fast work)")
        else:
            print("Invalid command. Enter 'help' for command list.")

        schedule.run_pending()
        time.sleep(1)
