import re
from playwright.sync_api import Page, Route, expect


def test_eco_impact1(page):
    page.route(
        "**/https://www.avito.ru/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="exchanges/TCEI_1.json")
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    expect(page).to_have_title(re.compile("Покупайте на Авито, чтобы помочь планете"))
    page.locator(".desktop-impact-items-F7T6E").screenshot(path="output/TCEI_1.png")


def test_eco_impact2(page):
    page.route(
        "**/https://www.avito.ru/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="exchanges/TCEI_2.json")
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    expect(page).to_have_title(re.compile("Покупайте на Авито, чтобы помочь планете"))
    page.locator(".desktop-impact-items-F7T6E").screenshot(path="output/TCEI_2.png")


def test_eco_impact3(page):
    page.route(
        "**/https://www.avito.ru/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="exchanges/TCEI_3.json")
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    expect(page).to_have_title(re.compile("Покупайте на Авито, чтобы помочь планете"))
    page.locator(".desktop-impact-items-F7T6E").screenshot(path="output/TCEI_3.png")


def test_eco_impact4(page):
    page.route(
        "**/https://www.avito.ru/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="exchanges/TCEI_4.json")
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    expect(page).to_have_title(re.compile("Покупайте на Авито, чтобы помочь планете"))
    page.locator(".desktop-impact-items-F7T6E").screenshot(path="output/TCEI_4.png")


def test_eco_impact5(page):
    page.route(
        "**/https://www.avito.ru/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="exchanges/TCEI_5.json")
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    expect(page).to_have_title(re.compile("Покупайте на Авито, чтобы помочь планете"))
    page.locator(".desktop-impact-items-F7T6E").screenshot(path="output/TCEI_5.png")


def test_eco_impact6(page):
    page.route(
        "**/https://www.avito.ru/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="exchanges/TCEI_6.json")
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    expect(page).to_have_title(re.compile("Покупайте на Авито, чтобы помочь планете"))
    page.locator(".desktop-impact-items-F7T6E").screenshot(path="output/TCEI_6.png")
