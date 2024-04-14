**Инструкция по автоматизации [тест-кейсов](https://github.com/y-titova/qa_avito.start/blob/main/TESTCASES.md) на взятие скриншотов эко-счетчиков**

_Предполагается, что установлен PyCharm_

1. Поставить связку pytest-playwright. Ввод в терминале (последовательно):
   
   pip install pytest-playwright

   playwright install
3. Добавить в проект файл [test_cases_eco_impact.py](https://github.com/y-titova/qa_avito.start/blob/main/test_cases_eco_impact.py)
4. Добавить в проект папку [exchanges](https://github.com/y-titova/qa_avito.start/tree/main/exchanges)
5. Запустить тесты в терминале:
   pytest
6. Убедиться, что в проекте появилась папка output, где кол-во скриншотов совпадает с кол-вом прошедших тестов (6).
7. Полученные скриншоты совпадают со скриншотами [в этой папке](https://github.com/y-titova/qa_avito.start/tree/main/output)
