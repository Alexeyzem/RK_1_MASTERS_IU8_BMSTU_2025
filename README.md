# Данный репозиторий создан для выполнения РК1

--------------------

## Задача: Анализ отдела продаж

### Студент


### Отдел

отдел продаж (ID: 17 из административных)

### Задание 

Проведите анализ эффективности коммерческой деятельности:

#### 1. Анализ продаж

- Рассчитайте общую прибыль от всех проектов отдела продаж
- Определите средний ROI по коммерческим проектам
- Найдите менеджеров с наибольшим количеством завершенных проектов

#### 2. Персональная эффективностья

- Рассчитайте revenue-per-employee для отдела 
- Определите correlation между зарплатой и performance_score
- Найдите самых эффективных менеджеров (прибыль/зарплата)

#### 3. Языковая аналитика

- Проанализируйте распределение языковых навыков в отделе
- Определите потребность в дополнительном языковом обучении
- Найдите сотрудников с знанием английского и немецкого одновременное

#### 4. Клиентская аналитика

- Проанализируйте проекты по приоритетам и рискам
- Определите соотношение high-priority к low-priority проектам
- Найдите проекты с высоким риском и высокой прибыльностью

#### 5. Стратегические рекомендации

- Предложите систему мотивации для менеджеров
- Рассчитайте потенциальный эффект от увеличения ROI на 5%
- Определите целевые показатели на следующий квартал

--------------------

## Структура

```
project/
├── company.json
├── main.py
├── config/
│   ├── __init__.py
│   ├── helper_const.py
│   └── messages.py
├── analyzers/
│   ├── init.py
│   ├── base_analyzer.py
│   ├── client_analyzer.py
│   ├── language_analyzer.py
│   ├── personal_analyzer.py
│   ├── projects_metrics_analyzer.py
│   └── roi_up_analyzer.py
├── utils/
│   ├── init.py
│   └── logger.py
├── README.md
├── gen.py
├── Отчет.docx
└─ .gitignore
```

---

## Технические зависимости

Основные требования

```
Python 3.8+
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

Команда установки

```
pip install pandas numpy matplotlib seaborn
```

--------------------

## Результат работы кода

```
2025-10-18 18:58:11 - ProjectProfit - INFO - Commercial Department System initialization started
2025-10-18 18:58:11 - ProjectProfit - INFO - Starting data loading process from JSON file
2025-10-18 18:58:11 - ProjectProfit - INFO - Data successfully loaded from file: company.json
2025-10-18 18:58:11 - ProjectProfit - INFO - Starting data processing
2025-10-18 18:58:11 - ProjectProfit - INFO - Total project count: 10
2025-10-18 18:58:11 - ProjectProfit - INFO - Total person count: 26
2025-10-18 18:58:11 - PersonalEfficiencyAnalyzer - INFO - Commercial Department System initialization started
2025-10-18 18:58:11 - PersonalEfficiencyAnalyzer - INFO - Starting data loading process from JSON file
2025-10-18 18:58:11 - PersonalEfficiencyAnalyzer - INFO - Data successfully loaded from file: company.json
2025-10-18 18:58:11 - PersonalEfficiencyAnalyzer - INFO - Starting data processing
2025-10-18 18:58:11 - PersonalEfficiencyAnalyzer - INFO - Total project count: 10
2025-10-18 18:58:11 - PersonalEfficiencyAnalyzer - INFO - Total person count: 26
2025-10-18 18:58:11 - LanguageSkillsAnalyzer - INFO - Commercial Department System initialization started
2025-10-18 18:58:11 - LanguageSkillsAnalyzer - INFO - Starting data loading process from JSON file
2025-10-18 18:58:11 - LanguageSkillsAnalyzer - INFO - Data successfully loaded from file: company.json
2025-10-18 18:58:11 - LanguageSkillsAnalyzer - INFO - Starting data processing
2025-10-18 18:58:11 - LanguageSkillsAnalyzer - INFO - Total project count: 10
2025-10-18 18:58:11 - LanguageSkillsAnalyzer - INFO - Total person count: 26
2025-10-18 18:58:11 - ClientAnalyzer - INFO - Commercial Department System initialization started
2025-10-18 18:58:11 - ClientAnalyzer - INFO - Starting data loading process from JSON file
2025-10-18 18:58:11 - ClientAnalyzer - INFO - Data successfully loaded from file: company.json
2025-10-18 18:58:11 - ClientAnalyzer - INFO - Starting data processing
2025-10-18 18:58:11 - ClientAnalyzer - INFO - Total project count: 10
2025-10-18 18:58:11 - ClientAnalyzer - INFO - Total person count: 26
2025-10-18 18:58:11 - ProjectProfit - INFO - Commercial Department System initialization started
2025-10-18 18:58:11 - ProjectProfit - INFO - Starting data loading process from JSON file
2025-10-18 18:58:11 - ProjectProfit - INFO - Data successfully loaded from file: company.json
2025-10-18 18:58:11 - ProjectProfit - INFO - Starting data processing
2025-10-18 18:58:11 - ProjectProfit - INFO - Total project count: 10
2025-10-18 18:58:11 - ProjectProfit - INFO - Total person count: 26
2025-10-18 18:58:11 - ProjectProfit - INFO - Starting projects_profit analysis
2025-10-18 18:58:11 - ProjectProfit - INFO - Calculating average ROI and profit
2025-10-18 18:58:11 - ProjectProfit - INFO - projects_profit analysis completed successfully
2025-10-18 18:58:11 - PersonalEfficiencyAnalyzer - INFO - Starting personal efficiency analysis
2025-10-18 18:58:11 - PersonalEfficiencyAnalyzer - INFO - Calculating revenue per employee
2025-10-18 18:58:11 - PersonalEfficiencyAnalyzer - INFO - Calculating correlation between salary and performance_score
2025-10-18 18:58:11 - PersonalEfficiencyAnalyzer - INFO - personal efficiency analysis completed successfully
2025-10-18 18:58:11 - LanguageSkillsAnalyzer - INFO - Starting language skills analysis
2025-10-18 18:58:11 - LanguageSkillsAnalyzer - INFO - Language complex analysis
2025-10-18 18:58:11 - LanguageSkillsAnalyzer - INFO - language skills analysis completed successfully
2025-10-18 18:58:11 - ClientAnalyzer - INFO - Starting clients analysis
2025-10-18 18:58:11 - ClientAnalyzer - INFO - Client project analysis
2025-10-18 18:58:11 - ClientAnalyzer - INFO - clients analysis completed successfully
2025-10-18 18:58:11 - ProjectProfit - INFO - Starting roi_up_analyzer analysis
2025-10-18 18:58:11 - ProjectProfit - INFO - ROI up analysis
2025-10-18 18:58:11 - ProjectProfit - INFO - roi_up_analyzer analysis completed successfully
INITIATING COMPREHENSIVE COMMERCIAL DEPARTMENT ANALYSIS
======================================================================
INITIATING PROJECT ANALYSIS
======================================================================
PROFIT ANALYSIS
======================================================================
Total project profit: 2982786
Average roi: 9.93
INITIATING PERSONAL ANALYSIS
======================================================================
PERSON ANALYSIS
======================================================================
revenue-per-employee: 114722.53846153847
Correlation between salary and performance_score: 0.25080136755595567
INITIATING LANGUAGE ANALYSIS
======================================================================
LANGUAGE ANALYSIS
======================================================================
language distribution: {'Китайский': 11, 'Английский': 11, 'Французский': 10, 'Русский': 12, 'Немецкий': 10}
Need upgrade skills: ['Михайлов Виталий Николаевич. Need upgrade russian.', 'Павлова Лидия Вадимовна. Need upgrade english. Need upgrade russian.', 'Виноградова Диана Вячеславовна. Need upgrade english.', 'Виноградов Геннадий Валерьевич. Need upgrade english. Need upgrade russian.', 'Петрова Галина Евгеньевна. Need upgrade russian.', 'Федорова Анастасия Павловна. Need upgrade english.', 'Богданова Яна Владимировна. Need upgrade russian.', 'Лебедев Антон Олегович. Need upgrade english. Need upgrade russian.', 'Морозова Варвара Михайловна. Need upgrade english. Need upgrade russian.', 'Морозова Светлана Вячеславовна. Need upgrade russian.', 'Воробьев Никита Павлович. Need upgrade russian.', 'Волков Вадим Владимирович. Need upgrade russian.', 'Соловьева Юлия Максимовна. Need upgrade english.', 'Морозов Тимур Артемович. Need upgrade english.', 'Новикова Варвара Павловна. Need upgrade english. Need upgrade russian.', 'Новиков Ярослав Евгеньевич. Need upgrade english.', 'Беляева Татьяна Борисовна. Need upgrade english. Need upgrade russian.', 'Кузнецова Наталья Борисовна. Need upgrade english.', 'Иванов Игорь Кириллович. Need upgrade russian.', 'Михайлова Ирина Ивановна. Need upgrade english.', 'Козлова Светлана Максимовна. Need upgrade english. Need upgrade russian.', 'Козлов Валерий Геннадьевич. Need upgrade english.']
Persons who know english and germany: ['Семенов Борис Валерьевич', 'Морозова Светлана Вячеславовна', 'Воробьев Никита Павлович', 'Волков Вадим Владимирович', 'Иванов Игорь Кириллович', 'Васильева Валентина Николаевна']
INITIATING CLIENT ANALYSIS
======================================================================
CLIENT ANALYSIS
======================================================================
Priorities-risk for project: {'medium/high': 1, 'medium/medium': 1, 'low/medium': 2, 'low/high': 1, 'critical/high': 2, 'medium/low': 2, 'low/low': 1}
Ratio high/critical to low priority: 0.5
Project with high risk and profit: [{'name': 'Проект Уничтожение 9107', 'priority': 'low', 'risk': 'high', 'profit': 568234}, {'name': 'Проект Подробность 4877', 'priority': 'critical', 'risk': 'high', 'profit': 1475663}]
INITIATING ROI UP ANALYSIS
======================================================================
ROI UP ANALYSIS
======================================================================
Total potential profit: 511441.3524000002

======================================================================
COMPREHENSIVE COMMERCIAL DEPARTMENT ANALYSIS SUMMARY
======================================================================

KEY PERFORMANCE INDICATORS:
Total profit: 2982786
Average ROI: 9.93
Revenue per employee: 114722.53846153847
Correlation: 0.25080136755595567
Language distribution: {'Китайский': 11, 'Английский': 11, 'Французский': 10, 'Русский': 12, 'Немецкий': 10}
Need upgrade: ['Михайлов Виталий Николаевич. Need upgrade russian.', 'Павлова Лидия Вадимовна. Need upgrade english. Need upgrade russian.', 'Виноградова Диана Вячеславовна. Need upgrade english.', 'Виноградов Геннадий Валерьевич. Need upgrade english. Need upgrade russian.', 'Петрова Галина Евгеньевна. Need upgrade russian.', 'Федорова Анастасия Павловна. Need upgrade english.', 'Богданова Яна Владимировна. Need upgrade russian.', 'Лебедев Антон Олегович. Need upgrade english. Need upgrade russian.', 'Морозова Варвара Михайловна. Need upgrade english. Need upgrade russian.', 'Морозова Светлана Вячеславовна. Need upgrade russian.', 'Воробьев Никита Павлович. Need upgrade russian.', 'Волков Вадим Владимирович. Need upgrade russian.', 'Соловьева Юлия Максимовна. Need upgrade english.', 'Морозов Тимур Артемович. Need upgrade english.', 'Новикова Варвара Павловна. Need upgrade english. Need upgrade russian.', 'Новиков Ярослав Евгеньевич. Need upgrade english.', 'Беляева Татьяна Борисовна. Need upgrade english. Need upgrade russian.', 'Кузнецова Наталья Борисовна. Need upgrade english.', 'Иванов Игорь Кириллович. Need upgrade russian.', 'Михайлова Ирина Ивановна. Need upgrade english.', 'Козлова Светлана Максимовна. Need upgrade english. Need upgrade russian.', 'Козлов Валерий Геннадьевич. Need upgrade english.']
Person with two language: ['Семенов Борис Валерьевич', 'Морозова Светлана Вячеславовна', 'Воробьев Никита Павлович', 'Волков Вадим Владимирович', 'Иванов Игорь Кириллович', 'Васильева Валентина Николаевна']
Priority risk: {'medium/high': 1, 'medium/medium': 1, 'low/medium': 2, 'low/high': 1, 'critical/high': 2, 'medium/low': 2, 'low/low': 1}
Ratio high/critical to low priority: 0.5
Projects with high risk and profit: [{'name': 'Проект Уничтожение 9107', 'priority': 'low', 'risk': 'high', 'profit': 568234}, {'name': 'Проект Подробность 4877', 'priority': 'critical', 'risk': 'high', 'profit': 1475663}]
If roi up for 5%, potential profit: 511441.3524000002

ANALYSIS COMPLETED SUCCESSFULLY!
Log files generated in 'logs/' directory

Process finished with exit code 0
```

Выводы:

1. Анализ продаж

- **Общая прибыль от всех проектов, где учавствовал отдел продаж**: 2982786 руб.
- **Средний ROI**: 9.93%
- **Менеджеры с наибольшим количеством завершенных проектов**: не удалось найти, так как не хватает связей проект -> менеджер в json файле

2. Персональная эффективность

- **revenue-per-employee для отдела**: 114722.53 
- **correlation между зарплатой и performance_score**: 0.25
- **Найдите самых эффективных менеджеров (прибыль/зарплата)**: не удалось определить, так как не хватало связей проект -> менеджер


3. Языковая аналитика

- **распределение языковых навыков в отделе**: 11 людей знают китайский, 11 - английский, 10 - французский, 12 - русский, 10 - немецкий.
- **потребность в дополнительном языковом обучении**: 
  - Михайлов Виталий Николаевич. Необходимо изучить русский.
  - Павлова Лидия Вадимовна. Необходимо изучить русский и английский.
  - Виноградова Диана Вячеславовна. Необходимо изучить английский.
  - Виноградов Геннадий Валерьевич. Необходимо изучить русский и английский.
  - Петрова Галина Евгеньевна. Необходимо изучить английский.
  - Федорова Анастасия Павловна. Необходимо изучить английский.
  - Богданова Яна Владимировна. Необходимо изучить русский.
  - Лебедев Антон Олегович. Необходимо изучить русский и английский.
  - Морозова Варвара Михайловна. Необходимо изучить русский и английский.
  - Морозова Светлана Вячеславовна. Необходимо изучить русский.
  - Воробьев Никита Павлович. Необходимо изучить русский.
  - Волков Вадим Владимирович. Необходимо изучить русский.
  - Соловьева Юлия Максимовна. Необходимо изучить английский.
  - Морозов Тимур Артемович. Необходимо изучить английский.
  - Новикова Варвара Павловна. Необходимо изучить русский и английский.
  - Новиков Ярослав Евгеньевич. Необходимо изучить английский.
  - Беляева Татьяна Борисовна. Необходимо изучить русский и английский.
  - Кузнецова Наталья Борисовна. Необходимо изучить английский.
  - Иванов Игорь Кириллович. Необходимо изучить русский.
  - Михайлова Ирина Ивановна. Необходимо изучить английский.
  - Козлова Светлана Максимовна. Необходимо изучить русский и английский.
  - Козлов Валерий Геннадьевич. Необходимо изучить английский.
- **Сотрудники с знанием английского и немецкого одновременно**:
  - Семенов Борис Валерьевич
  - Морозова Светлана Вячеславовна
  - Воробьев Никита Павлович
  - Волков Вадим Владимирович
  - Иванов Игорь Кириллович
  - Васильева Валентина Николаевна

4. Клиентская аналитика

- **Проекты по приоритетам и рискам**: 
  - medium/high: 1
  - medium/medium: 1
  - low/medium: 2
  - low/high: 1
  - critical/high: 2
  - medium/low: 2
  - low/low: 1
- **Соотношение high(critical)-priority к low-priority проектам**: 0.5
- **проекты с высоким риском и высокой прибыльностью**:
  - Проект Уничтожение 9107. Низкий приоритет. Прибыль - 568234
  - Проект Подробность 4877. Критичный приоритет. Прибыль - 1475663
  - 

5. Стратегические рекомендации

- **Потенциальный эффект от увеличения ROI на 5%**: Увеличение прибыли на 511441
- **Система мотивации для менеджеров**: Премия
- **Целевые показатели на следующий квартал**:
  - Увеличение прибыли на 500000
  - Увеличение ROI на 4% минимум
  - Записать на языковые курсы необходимых сотрудников

--------------------