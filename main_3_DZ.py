from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Открываем браузер
browser = webdriver.Firefox()
# Спрашиваем у пользователя запрос
query = input("Введите поисковый запрос: ")
# Открываем страницу поиска на Википедии
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
search_box = browser.find_element(By.NAME, "search")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(3)  # Даем время на загрузку страницы
while True:
    print("\nВыберите действие:")
    print("1 - Читать параграфы статьи")
    print("2 - Перейти по внутренней ссылке")
    print("3 - Выйти")
    choice = input("Введите номер действия: ")
    if choice == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for i, p in enumerate(paragraphs[:5], 1):  # Показываем первые 5 абзацев
            print(f"\nПараграф {i}: {p.text[:500]}")
            input("Нажмите Enter для продолжения...")
    elif choice == "2":
        links = browser.find_elements(By.XPATH, '//div[@id="bodyContent"]//a[@href]')
        internal_links = [link for link in links if link.get_attribute("href").startswith("https://ru.wikipedia.org/wiki/")]
        if internal_links:
            print("\nДоступные ссылки:")
            for i, link in enumerate(internal_links[:5], 1):
                print(f"{i}: {link.text} ({link.get_attribute('href')})")
            num = input("Введите номер ссылки для перехода: ")
            if num.isdigit() and 1 <= int(num) <= len(internal_links):
                browser.get(internal_links[int(num) - 1].get_attribute("href"))
                time.sleep(3)  # Даем время на загрузку
            else:
                print("Некорректный выбор.")
        else:
            print("Внутренних ссылок не найдено.")
    elif choice == "3":
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
browser.quit()
