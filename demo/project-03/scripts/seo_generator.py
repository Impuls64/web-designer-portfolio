#!/usr/bin/env python3
"""
SEO Meta Generator
Автоматическая генерация meta-title и meta-description 
для страниц сайта на основе контента.

Usage:
    python seo_generator.py --input pages.json --output seo.csv
"""

import argparse
import csv
import json
from typing import List, Dict


class SEOGenerator:
    """Генератор SEO-метатегов."""
    
    def __init__(self):
        self.title_template = "{keyword} | {brand}"
        self.description_template = "{keyword} — {description}. {cta}"
    
    def generate_title(self, page: Dict) -> str:
        """Генерирует title на основе ключевого слова."""
        keyword = page.get("keyword", page.get("title", ""))
        brand = page.get("brand", "DataFlow Consulting")
        
        title = self.title_template.format(keyword=keyword, brand=brand)
        
        # Ограничение до 60 символов
        if len(title) > 60:
            title = title[:57] + "..."
        
        return title
    
    def generate_description(self, page: Dict) -> str:
        """Генерирует description на основе контента."""
        keyword = page.get("keyword", "")
        description = page.get("description", "")
        cta = page.get("cta", "Узнайте подробности на сайте.")
        
        desc = self.description_template.format(
            keyword=keyword,
            description=description,
            cta=cta
        )
        
        # Ограничение до 160 символов
        if len(desc) > 160:
            desc = desc[:157] + "..."
        
        return desc
    
    def process_pages(self, pages: List[Dict]) -> List[Dict]:
        """Обрабатывает список страниц."""
        results = []
        
        for page in pages:
            result = {
                "url": page.get("url", ""),
                "title": self.generate_title(page),
                "description": self.generate_description(page),
                "h1": page.get("title", ""),
                "keywords": page.get("keywords", "")
            }
            results.append(result)
        
        return results
    
    def export_csv(self, results: List[Dict], output_file: str):
        """Экспортирует результаты в CSV."""
        fieldnames = ["url", "title", "description", "h1", "keywords"]
        
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        
        print(f"✅ SEO-метатеги экспортированы: {output_file}")


def load_pages(input_file: str) -> List[Dict]:
    """Загружает страницы из JSON."""
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("pages", [])


def main():
    parser = argparse.ArgumentParser(description="SEO Meta Generator")
    parser.add_argument("--input", default="pages.json", help="Input JSON file")
    parser.add_argument("--output", default="seo.csv", help="Output CSV file")
    args = parser.parse_args()
    
    print("🚀 SEO Generator запущен")
    
    # Demo data if file doesn't exist
    try:
        pages = load_pages(args.input)
        print(f"📥 Загружено страниц: {len(pages)}")
    except FileNotFoundError:
        print("⚠️ Файл не найден, используем демо-данные")
        pages = [
            {
                "url": "/",
                "title": "Главная",
                "keyword": "Внедрение CRM",
                "description": "Профессиональное внедрение amoCRM и Битрикс24 для среднего бизнеса",
                "cta": "Получите бесплатную консультацию.",
                "brand": "DataFlow Consulting",
                "keywords": "crm, amocrm, битрикс24, автоматизация"
            },
            {
                "url": "/services",
                "title": "Услуги",
                "keyword": "Услуги по автоматизации",
                "description": "Полный спектр услуг по внедрению CRM и автоматизации бизнес-процессов",
                "cta": "Подробнее о наших услугах.",
                "brand": "DataFlow Consulting",
                "keywords": "услуги, автоматизация, crm, интеграции"
            },
            {
                "url": "/cases",
                "title": "Кейсы",
                "keyword": "Кейсы внедрения CRM",
                "description": "Реальные кейсы внедрения CRM-систем с измеримыми результатами",
                "cta": "Посмотрите наши проекты.",
                "brand": "DataFlow Consulting",
                "keywords": "кейсы, портфолио, результаты, crm"
            }
        ]
    
    generator = SEOGenerator()
    results = generator.process_pages(pages)
    
    print("\n📊 Результаты:")
    for result in results:
        print(f"\n  URL: {result['url']}")
        print(f"  Title: {result['title']} ({len(result['title'])} chars)")
        print(f"  Description: {result['description']} ({len(result['description'])} chars)")
    
    generator.export_csv(results, args.output)
    print(f"\n✅ Готово! Обработано страниц: {len(results)}")


if __name__ == "__main__":
    main()
