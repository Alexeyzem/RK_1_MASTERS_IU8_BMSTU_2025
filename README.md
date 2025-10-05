# Данный репозиторий создан для примера выполнения РК

--------------------

## Задача (Пример): Анализ IT инфраструктуры

### Студент

IT-аналитик

### Отдел

IT отдел (ID: 13 из административных)

### Задание 

Проведите анализ IT инфраструктуры компании:

#### 1. Инвентаризация оборудования

Составьте полный перечень IT оборудования по компании
Рассчитайте общую стоимость IT активов
Определите распределение оборудования по отделам

#### 2. Эффективность использования

Рассчитайте средний utilization rate IT оборудования
Определите отделы с наиболее и наименее эффективным использованием
Найдите оборудование с utilization_rate < 50%

#### 3. Затратный анализ

Рассчитайте общие затраты на обслуживание IT оборудования
Определите cost-per-unit для каждого типа оборудования
Проанализируйте соотношение затрат на покупку и обслуживание

#### 4. Планирование замены

Определите оборудование, приближающееся к концу гарантийного срока
Рассчитайте потенциальные затраты на замену устаревшего оборудования
Разработайте приоритетный план модернизации

#### 5. Оптимизация инфраструктуры

Предложите меры по консолидации IT ресурсов
Рассчитайте экономический эффект от оптимизации
Разработайте KPI для оценки эффективности IT инфраструктуры

--------------------

## Структура

```
project/
├── company.json
├── main.py
├── config/
│   ├── __init__.py
│   ├── enums.py
│   └── messages.py
├── analyzers/
│   ├── __init__.py
│   ├── base_analyzer.py
│   ├── inventory_analyzer.py
│   ├── utilization_analyzer.py
│   ├── cost_analyzer.py
│   ├── replacement_analyzer.py
│   └── optimization_analyzer.py
└── utils/
    ├── __init__.py
    └── logger.py
```

--------------------

## Совет для создания комментариев @brief

| Тег         | Описание                                             | Пример использования                                                                 |
|-------------|------------------------------------------------------|-------------------------------------------------------------------------------------|
| @brief    | Краткое описание функции или метода                 | @brief Convert log level to syslog severity                                       |
| @param    | Описание параметров функции                          | @param llev - ste log level.                                                       |
| @return   | Описание возвращаемого значения                      | @return syslog severity if OK and -1 if FAIL.                                     |
| @throws   | Указывает, какие исключения могут быть выброшены    | @throws InvalidLogLevelException if the log level is invalid.                     |
| @note     | Дополнительная информация или примечания             | @note This function is used for converting internal logging levels to syslog standards. |
| @warning  | Указывает на потенциальные проблемы                  | @warning Ensure that the input level is within the defined range to avoid unexpected behavior. |
| @todo     | Указывает на задачи или улучшения                    | @todo Implement error handling for invalid inputs.                                |
| @deprecated| Указывает на устаревшие функции                      | @deprecated Use newLoggingFunction() instead.                                     |
| @see      | Указывает на связанные функции или классы           | @see newLoggingFunction()                                                           |
| @file     | Имя файла, к которому относится данный блок комментариев | @file logging.c                                                                    |
| @class    | Указывает на класс, если документируется класс      | @class Logger                                                                      |

Минимальный комментарий:

```
"""
@brief Execute complete IT infrastructure analysis
Runs all analysis modules and compiles comprehensive results

@return: Dictionary containing all analysis results
"""
```

Важно помнить, что кириллица - не очень хорошо. У кого-то может это превратиться в мусор.

--------------------

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
2025-10-05 23:10:32 - InventoryAnalysis - INFO - IT Infrastructure Analysis System initialization started
2025-10-05 23:10:32 - InventoryAnalysis - INFO - Starting data loading process from JSON file
2025-10-05 23:10:32 - InventoryAnalysis - INFO - Data successfully loaded from file: company.json
2025-10-05 23:10:32 - InventoryAnalysis - INFO - Starting data processing for InventoryAnalysis
2025-10-05 23:10:32 - InventoryAnalysis - INFO - Filtering IT equipment from dataset
2025-10-05 23:10:32 - InventoryAnalysis - INFO - Total IT equipment identified: 87 units
2025-10-05 23:10:32 - UtilizationAnalysis - INFO - IT Infrastructure Analysis System initialization started
2025-10-05 23:10:32 - UtilizationAnalysis - INFO - Starting data loading process from JSON file
2025-10-05 23:10:32 - UtilizationAnalysis - INFO - Data successfully loaded from file: company.json
2025-10-05 23:10:32 - UtilizationAnalysis - INFO - Starting data processing for UtilizationAnalysis
2025-10-05 23:10:32 - UtilizationAnalysis - INFO - Filtering IT equipment from dataset
2025-10-05 23:10:32 - UtilizationAnalysis - INFO - Total IT equipment identified: 87 units
2025-10-05 23:10:32 - CostAnalysis - INFO - IT Infrastructure Analysis System initialization started
2025-10-05 23:10:32 - CostAnalysis - INFO - Starting data loading process from JSON file
2025-10-05 23:10:32 - CostAnalysis - INFO - Data successfully loaded from file: company.json
2025-10-05 23:10:32 - CostAnalysis - INFO - Starting data processing for CostAnalysis
2025-10-05 23:10:32 - CostAnalysis - INFO - Filtering IT equipment from dataset
2025-10-05 23:10:32 - CostAnalysis - INFO - Total IT equipment identified: 87 units
2025-10-05 23:10:32 - ReplacementAnalysis - INFO - IT Infrastructure Analysis System initialization started
2025-10-05 23:10:32 - ReplacementAnalysis - INFO - Starting data loading process from JSON file
2025-10-05 23:10:32 - ReplacementAnalysis - INFO - Data successfully loaded from file: company.json
2025-10-05 23:10:32 - ReplacementAnalysis - INFO - Starting data processing for ReplacementAnalysis
2025-10-05 23:10:32 - ReplacementAnalysis - INFO - Filtering IT equipment from dataset
2025-10-05 23:10:32 - ReplacementAnalysis - INFO - Total IT equipment identified: 87 units
2025-10-05 23:10:32 - OptimizationAnalysis - INFO - IT Infrastructure Analysis System initialization started
2025-10-05 23:10:32 - OptimizationAnalysis - INFO - Starting data loading process from JSON file
2025-10-05 23:10:32 - OptimizationAnalysis - INFO - Data successfully loaded from file: company.json
2025-10-05 23:10:32 - OptimizationAnalysis - INFO - Starting data processing for OptimizationAnalysis
2025-10-05 23:10:32 - OptimizationAnalysis - INFO - Filtering IT equipment from dataset
2025-10-05 23:10:32 - OptimizationAnalysis - INFO - Total IT equipment identified: 87 units
2025-10-05 23:10:32 - InventoryAnalysis - INFO - Starting inventory analysis
2025-10-05 23:10:32 - InventoryAnalysis - INFO - Calculating total equipment costs
2025-10-05 23:10:32 - InventoryAnalysis - INFO - Inventory analysis completed successfully
2025-10-05 23:10:32 - UtilizationAnalysis - INFO - Starting utilization analysis
2025-10-05 23:10:32 - UtilizationAnalysis - INFO - Calculating equipment utilization metrics
2025-10-05 23:10:32 - UtilizationAnalysis - INFO - Utilization analysis completed successfully
INITIATING COMPREHENSIVE IT INFRASTRUCTURE ANALYSIS
======================================================================

EXECUTING EQUIPMENT INVENTORY ANALYSIS...
======================================================================
EQUIPMENT INVENTORY ANALYSIS
======================================================================

Total IT equipment identified: 87 units
Total IT assets value: 22,735,369 RUB

Equipment Type Distribution:
      Equipment Type  Count  Percentage
             Ноутбук     18       20.69
Сетевое оборудование     14       16.09
             Принтер     13       14.94
              Сервер     12       13.79
             Монитор     11       12.64
              Сканер     10       11.49
           Компьютер      9       10.34

Department Distribution (Top 10 by Cost):
              Department Name  Equipment Count  Total Cost  Average Utilization Rate
           Отдел тестирования                7     2041025                     80.71
   Отдел мобильной разработки                7     1957792                     80.86
                 Отдел продаж                6     1694128                     71.00
                 Отдел кадров                5     1612855                     84.00
Отдел аппаратного обеспечения                5     1521134                     70.20
          Отдел UX/UI дизайна                5     1490088                     69.80
          Отдел разработки ПО                6     1206781                     78.50
     Отдел backend разработки                4     1200160                     82.75
  Отдел партнерских отношений                6     1160030                     84.67
      Отдел кибербезопасности                3     1094034                     74.67

EXECUTING UTILIZATION EFFICIENCY ANALYSIS...
======================================================================
EQUIPMENT UTILIZATION ANALYSIS
======================================================================

Average equipment utilization rate: 77.2%
Equipment with low utilization (<50%): 0 units

Utilization Distribution:
Utilization Level  Equipment Count  Percentage
         very_low                0        0.00
              low                0        0.00
           medium               51       58.62
             high               36       41.38

Top 5 Departments by Utilization Efficiency:
                             Average Utilization Rate  Standard Deviation  Equipment Count
department_name                                                                           
Финансовый отдел                                88.50                4.95                2
Отдел партнерских отношений                     84.67               11.64                6
Отдел кадров                                    84.00                9.27                5
Отдел backend разработки                        82.75                6.24                4
Отдел мобильной разработки                      80.86               13.47                7

EXECUTING COST ANALYSIS...
======================================================================
COST ANALYSIS
======================================================================

Annual maintenance costs: 13,309,416 RUB
Maintenance to purchase cost ratio: 58.5%

Cost Per Unit Analysis by Equipment Type:
                type  Equipment Count  Total Purchase Cost  Average Purchase Cost  Total Monthly Maintenance  Average Monthly Maintenance  Annual Maintenance Cost  TCO Percentage
           Компьютер                9              2558102              284233.56                      98810                     10978.89                131746.68           46.35
             Монитор               11              2437162              221560.18                     138571                     12597.36                151168.32           68.23
             Ноутбук               18              3736673              207592.94                     179235                      9957.50                119490.00           57.56
             Принтер               13              3049878              234606.00                     154662                     11897.08                142764.96           60.85
              Сервер               12              4130001              344166.75                     209720                     17476.67                209720.04           60.94
Сетевое оборудование               14              3848345              274881.79                     171707                     12264.79                147177.48           53.54
              Сканер               10              2975208              297520.80                     156413                     15641.30                187695.60           63.09

Total equipment purchase cost: 22,735,369 RUB
Purchase to maintenance ratio: 1 : 0.59
Estimated payback period: 62.3 years

EXECUTING REPLACEMENT PLANNING ANALYSIS...
2025-10-05 23:10:32 - CostAnalysis - INFO - Starting cost analysis
2025-10-05 23:10:32 - CostAnalysis - INFO - Calculating maintenance costs
2025-10-05 23:10:32 - CostAnalysis - INFO - Cost analysis completed successfully
2025-10-05 23:10:32 - ReplacementAnalysis - INFO - Starting replacement analysis
2025-10-05 23:10:32 - ReplacementAnalysis - INFO - Replacement analysis completed successfully
2025-10-05 23:10:32 - OptimizationAnalysis - INFO - Starting optimization analysis
2025-10-05 23:10:32 - OptimizationAnalysis - INFO - Optimization analysis completed successfully
======================================================================
EQUIPMENT REPLACEMENT PLANNING
======================================================================

Equipment with expiring warranty: 65 units
Outdated equipment (> 3 years): 44 units
Total replacement cost estimate: 11,319,343 RUB

Equipment with Expiring Warranty:
equipment_id                     name                     department_name          warranty_end_date  days_until_warranty_expiration   cost
     EQ_0054               Сервер 859       Отдел аппаратного обеспечения 2021-10-06 22:30:00.835050                           -1461 325772
     EQ_0168              Ноутбук 951          Отдел мобильной разработки 2021-12-19 22:30:00.840051                           -1387 330336
     EQ_0052               Сервер 962          Отдел мобильной разработки 2022-02-04 22:30:00.835050                           -1340 350914
     EQ_0097            Компьютер 991                   Юридический отдел 2022-02-11 22:30:00.837050                           -1333 276876
     EQ_0027               Сканер 544         Отдел партнерских отношений 2022-03-15 22:30:00.834050                           -1301 179455
     EQ_0193               Сканер 403         Отдел партнерских отношений 2022-05-16 22:30:00.841051                           -1239 249513
     EQ_0179               Сканер 442           Отдел клиентского сервиса 2022-10-25 22:30:00.840051                           -1077 397143
     EQ_0069 Сетевое оборудование 374                 Отдел разработки ПО 2023-01-15 22:30:00.835050                            -995 274887
     EQ_0184               Сервер 368            Отдел backend разработки 2023-01-24 22:30:00.840051                            -986 148646
     EQ_0117              Ноутбук 679                        Отдел DevOps 2023-05-09 22:30:00.837050                            -881 138691
     EQ_0017              Монитор 528             Отдел кибербезопасности 2023-06-16 22:30:00.833049                            -843 396996
     EQ_0112               Сервер 564                 Отдел UX/UI дизайна 2023-07-09 22:30:00.837050                            -820 296612
     EQ_0103 Сетевое оборудование 863                 Отдел разработки ПО 2023-09-13 22:30:00.837050                            -754  56917
     EQ_0182              Ноутбук 683                    Отдел маркетинга 2023-09-23 22:30:00.840051                            -744 139895
     EQ_0092            Компьютер 812                        Отдел кадров 2023-09-26 22:30:00.836050                            -741 345612
     EQ_0104 Сетевое оборудование 548            Отдел backend разработки 2023-11-19 22:30:00.837050                            -687 312746
     EQ_0128 Сетевое оборудование 305                  Отдел Data Science 2024-02-13 22:30:00.838051                            -601 255143
     EQ_0152              Ноутбук 860          Отдел мобильной разработки 2024-02-14 22:30:00.839051                            -600 332270
     EQ_0026               Сканер 724                        Отдел продаж 2024-03-06 22:30:00.834050                            -579 478967
     EQ_0150 Сетевое оборудование 510       Отдел аппаратного обеспечения 2024-03-19 22:30:00.839051                            -566 354168
     EQ_0125               Сканер 846                        Отдел продаж 2024-03-24 22:30:00.838051                            -561  97891
     EQ_0135              Ноутбук 364            Отдел backend разработки 2024-04-10 22:30:00.838051                            -544 400062
     EQ_0095               Сканер 801                        Отдел продаж 2024-04-25 22:30:00.837050                            -529 296403
     EQ_0093              Принтер 559                        Отдел продаж 2024-07-31 22:30:00.836050                            -432  97750
     EQ_0153              Ноутбук 876         Отдел партнерских отношений 2024-08-30 22:30:00.839051                            -402 174545
     EQ_0140            Компьютер 136                        Отдел кадров 2024-09-07 22:30:00.839051                            -394 279498
     EQ_0174              Ноутбук 332                  Отдел Data Science 2024-09-09 22:30:00.840051                            -392  53740
     EQ_0050              Принтер 841         Отдел партнерских отношений 2024-09-14 22:30:00.835050                            -387 390396
     EQ_0133              Принтер 183                       Отдел закупок 2024-09-17 22:30:00.838051                            -384 165758
     EQ_0079              Ноутбук 679                    Отдел маркетинга 2024-09-22 22:30:00.836050                            -379  64369
     EQ_0034            Компьютер 213 Административно-хозяйственный отдел 2024-09-23 22:30:00.834050                            -378 315571
     EQ_0006               Сервер 315                 Отдел разработки ПО 2024-10-13 22:30:00.833049                            -358 260101
     EQ_0059              Монитор 721             Отдел кибербезопасности 2024-10-14 22:30:00.835050                            -357 206232
     EQ_0142              Ноутбук 523          Отдел мобильной разработки 2024-10-20 22:30:00.839051                            -351 121660
     EQ_0130            Компьютер 478                   Юридический отдел 2024-11-06 22:30:00.838051                            -334 306197
     EQ_0166               Сервер 711                  Отдел тестирования 2024-11-13 22:30:00.840051                            -327 484276
     EQ_0110               Сканер 983           Отдел клиентского сервиса 2024-12-28 22:30:00.837050                            -282 122808
     EQ_0083              Ноутбук 767             Отдел кибербезопасности 2025-04-03 22:30:00.836050                            -186 490806
     EQ_0190              Ноутбук 229          Отдел мобильной разработки 2025-05-18 22:30:00.841051                            -141 291670
     EQ_0088              Принтер 795 Административно-хозяйственный отдел 2025-09-14 22:30:00.836050                             -22 351455
     EQ_0146              Ноутбук 487                  Отдел тестирования 2025-09-17 22:30:00.839051                             -19 218030
     EQ_0010              Принтер 397                   Юридический отдел 2025-10-01 22:30:00.833049                              -5 260054
     EQ_0161              Принтер 548         Отдел партнерских отношений 2025-10-10 22:30:00.839051                               4  51585
     EQ_0041              Монитор 769                  Отдел тестирования 2025-10-12 22:30:00.834050                               6 110703
     EQ_0029            Компьютер 285 Административно-хозяйственный отдел 2025-10-14 22:30:00.834050                               8 100836
     EQ_0098              Принтер 571                        Отдел кадров 2025-10-16 22:30:00.837050                              10 374136
     EQ_0030              Принтер 546                        Отдел кадров 2025-11-03 22:30:00.834050                              28 319616
     EQ_0055              Монитор 343                 Отдел UX/UI дизайна 2025-11-05 22:30:00.835050                              30 352476
     EQ_0076            Компьютер 774                       Отдел закупок 2025-12-06 22:30:00.836050                              61 421427
     EQ_0113               Сканер 713                        Отдел продаж 2026-01-08 22:30:00.837050                              94 344002
     EQ_0176              Ноутбук 172       Отдел аппаратного обеспечения 2026-01-12 22:30:00.840051                              98 303021
     EQ_0058 Сетевое оборудование 414                 Отдел разработки ПО 2026-01-17 22:30:00.835050                             103  53912
     EQ_0087              Монитор 635                  Отдел Data Science 2026-03-19 22:30:00.836050                             164 187031
     EQ_0048               Сканер 230                    Отдел маркетинга 2026-04-10 22:30:00.835050                             186 429911
     EQ_0008 Сетевое оборудование 758                  Отдел тестирования 2026-04-16 22:30:00.833049                             192 147162
     EQ_0081              Монитор 573          Отдел мобильной разработки 2026-05-02 22:30:00.836050                             208  83875
     EQ_0129              Ноутбук 899         Отдел партнерских отношений 2026-05-05 22:30:00.838051                             211 114536
     EQ_0072               Сервер 515                 Отдел разработки ПО 2026-05-19 22:30:00.836050                             225 435104
     EQ_0047               Сервер 409                  Отдел тестирования 2026-05-28 22:30:00.835050                             234 460915
     EQ_0108 Сетевое оборудование 294           Отдел frontend разработки 2026-07-21 22:30:00.837050                             288 418670
     EQ_0124 Сетевое оборудование 694                        Отдел DevOps 2026-08-10 22:30:00.838051                             308 231725
     EQ_0074 Сетевое оборудование 753            Отдел backend разработки 2026-08-16 22:30:00.836050                             314 338706
     EQ_0037              Принтер 739                        Отдел кадров 2026-08-23 22:30:00.834050                             321 293993
     EQ_0137              Монитор 955                  Отдел тестирования 2026-09-15 22:30:00.838051                             344 424401
     EQ_0082              Ноутбук 973                  Отдел Data Science 2026-10-06 22:30:00.836050                             365 116225

Equipment replacement priority list generated
equipment_id          name             department_name  equipment_age_years  efficiency  utilization_rate   cost  priority_score
     EQ_0193    Сканер 403 Отдел партнерских отношений                4.375           0                64 249513           0.729
     EQ_0076 Компьютер 774               Отдел закупок                4.758           0                78 421427           0.723
     EQ_0113    Сканер 713                Отдел продаж                4.668           0                89 344002           0.708
     EQ_0017   Монитор 528     Отдел кибербезопасности                3.291           0                87 396996           0.662
     EQ_0172   Монитор 547         Отдел UX/UI дизайна                2.513           0                66 298283           0.646
     EQ_0006    Сервер 315         Отдел разработки ПО                3.934           0                75 260101           0.622
     EQ_0081   Монитор 573  Отдел мобильной разработки                4.356           0                84  83875           0.620
     EQ_0026    Сканер 724                Отдел продаж                4.539          41                76 478967           0.611
     EQ_0146   Ноутбук 487          Отдел тестирования                3.006           0                85 218030           0.604
     EQ_0059   Монитор 721     Отдел кибербезопасности                2.946           0                65 206232           0.603

Total cost for top 10 replacement candidates: 2,957,426 RUB

EXECUTING OPTIMIZATION ANALYSIS...
======================================================================
INFRASTRUCTURE OPTIMIZATION
======================================================================

Recommended consolidation measures:
• Consolidate server capacities into unified data center
• Implement virtualization system for server optimization
• Standardize workstation models across departments
• Create shared equipment pool (printers, scanners)
• Optimize software licensing through centralized management

Potential annual savings: 1,996,412 RUB
Return on investment period: 2.0 years

KPI Framework for Infrastructure Monitoring:
                           KPI Metric Current Performance Target Performance Measurement Frequency
   Average Equipment Utilization Rate               77.2%                85%               Monthly
           Server Uptime Availability               99.2%              99.9%             Real-time
       Cost of Ownership per Employee          34,977 RUB      Reduce by 15%             Quarterly
               Incident Response Time           2.5 hours             1 hour          Per incident
  Equipment Under Warranty Percentage               49.4%                80%         Semi-annually
Maintenance Cost to Asset Value Ratio               58.5%           Below 8%                Annual
               Equipment Refresh Rate        15% per year       20% per year                Annual

Monitoring Implementation Recommendations:
• Implement automated monitoring system
• Establish regular performance review cycles
• Create dashboard for real-time KPI tracking
• Set up alert system for metric deviations

======================================================================
COMPREHENSIVE IT INFRASTRUCTURE ANALYSIS SUMMARY
======================================================================

KEY PERFORMANCE INDICATORS:
• Total IT Equipment: 87 units
• Total Asset Value: 22,735,369 RUB
• Average Utilization Rate: 77.2%
• Annual Maintenance Cost: 13,309,416 RUB
• Underutilized Equipment: 0 units
• Equipment with Expiring Warranty: 65 units
• Potential Annual Savings: 1,996,412 RUB

ANALYSIS COMPLETED SUCCESSFULLY!
Log files generated in 'logs/' directory
```

Выводы:

1. Анализ инвентаря

- **Всего IT оборудования**: 87 единиц
- **Общая стоимость активов**: 22 735 369 руб.
- **Распределение оборудования**:
  - Ноутбуки: 20.69% (18 ед.)
  - Сетевое оборудование: 16.09% (14 ед.)
  - Принтеры: 14.94% (13 ед.)
  - Серверы: 13.79% (12 ед.)
  - Мониторы: 12.64% (11 ед.)
  - Сканеры: 11.49% (10 ед.)
  - Компьютеры: 10.34% (9 ед.)

2. Анализ использования

- **Средняя утилизация**: 77.2% (Хороший показатель)
- **Оборудование с низкой утилизацией**: 0 ед. (Отличная эффективность)
- **Распределение утилизации**:
  - Средняя (50-80%): 58.62% (51 ед.)
  - Высокая (80-100%): 41.38% (36 ед.)
- **Лучшие отделы по эффективности**:
  1. Финансовый отдел: 88.50%
  2. Отдел партнерских отношений: 84.67%
  3. Отдел кадров: 84.00%

3. Анализ затрат

- **Годовые затраты на обслуживание**: 13 309 416 руб.
- **Отношение обслуживания к стоимости**: 58.5% (Высокий - требует оптимизации)
- **Общая стоимость владения (TCO)**:
  - Серверы: 60.94%
  - Сканеры: 63.09%
  - Принтеры: 60.85%
- **Период окупаемости**: 62.3 года (Тревожный - указывает на высокие затраты на обслуживание)

4. Планирование замены

- **Оборудование с истекающей гарантией**: 65 ед. (74.7% инвентаря)
- **Устаревшее оборудование (>3 лет)**: 44 ед. (50.6% инвентаря)
- **Общая стоимость замены**: 11 319 343 руб.
- **Топ-10 кандидатов на замену**: 2 957 426 руб.

5. Возможности оптимизации

- **Потенциальная годовая экономия**: 1 996 412 руб.
- **Период окупаемости инвестиций**: 2.0 года
- **Ключевые рекомендации**:
  - Консолидация серверов и виртуализация
  - Стандартизация оборудования
  - Общие пулы ресурсов
  - Централизованное управление лицензиями

--------------------

## требование

- Предоставить реализацию в https://github.com/
- Составить подробный отчет
