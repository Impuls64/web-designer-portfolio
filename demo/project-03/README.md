# Демо: Автоматизация рабочих процессов через AI

## Скрипты

### 1. Auto Specs Generator (`auto_specs.py`)
Автоматическая генерация спецификаций для разработчика из Figma-файлов.

**Возможности:**
- Извлечение размеров, позиций, цветов
- Анализ типографики (шрифт, размер, вес)
- Экспорт в Markdown

**Запуск:**
```bash
python scripts/auto_specs.py --file YOUR_FILE_KEY --token YOUR_TOKEN --output specs.md
```

### 2. SEO Meta Generator (`seo_generator.py`)
Автоматическая генерация meta-title и meta-description.

**Возможности:**
- Генерация на основе ключевых слов
- Автоматическое ограничение длины (60/160 символов)
- Экспорт в CSV

**Запуск:**
```bash
python scripts/seo_generator.py --input pages.json --output seo.csv
```

## Примеры результатов

### Auto Specs
```markdown
# Спецификация: Hero Section

## Размеры
- **Ширина:** 1920px
- **Высота:** 800px
- **Позиция:** X: 0px, Y: 0px

## Цвета
- **Цвет 1:** `#1A3A5C` (alpha: 1.0)
- **Цвет 2:** `#C9A96E` (alpha: 1.0)

## Типографика
- **Шрифт:** Inter
- **Размер:** 72px
- **Вес:** 700
- **Межстрочный:** 1.1
```

### SEO Meta
| URL | Title | Description |
|-----|-------|-------------|
| / | Внедрение CRM \| DataFlow Consulting | Внедрение CRM — Профессиональное внедрение amoCRM... |
| /services | Услуги по автоматизации \| DataFlow Consulting | Услуги по автоматизации — Полный спектр услуг... |

## Стек
- Python 3.11+
- Figma REST API
- CSV/JSON для экспорта
