#!/usr/bin/env python3
"""
Auto Specs Generator for Figma
Автоматически генерирует спецификацию для разработчика:
отступы, цвета, шрифты, эффекты из Figma-файла.

Usage:
    python auto_specs.py --file FILE_KEY --token FIGMA_TOKEN
"""

import argparse
import json
import requests
from typing import Dict, Any

FIGMA_API = "https://api.figma.com/v1"


def get_file(file_key: str, token: str) -> Dict[str, Any]:
    """Получает данные файла из Figma API."""
    response = requests.get(
        f"{FIGMA_API}/files/{file_key}",
        headers={"X-Figma-Token": token}
    )
    response.raise_for_status()
    return response.json()


def extract_specs(node: Dict[str, Any]) -> Dict[str, Any]:
    """Извлекает спецификацию из ноды."""
    specs = {
        "name": node.get("name", "Unnamed"),
        "type": node.get("type", "Unknown"),
        "size": {
            "width": node.get("absoluteBoundingBox", {}).get("width", 0),
            "height": node.get("absoluteBoundingBox", {}).get("height", 0),
        },
        "position": {
            "x": node.get("absoluteBoundingBox", {}).get("x", 0),
            "y": node.get("absoluteBoundingBox", {}).get("y", 0),
        }
    }
    
    # Extract colors
    if "fills" in node:
        specs["colors"] = []
        for fill in node["fills"]:
            if fill.get("type") == "SOLID":
                color = fill.get("color", {})
                specs["colors"].append({
                    "r": round(color.get("r", 0) * 255),
                    "g": round(color.get("g", 0) * 255),
                    "b": round(color.get("b", 0) * 255),
                    "a": color.get("a", 1)
                })
    
    # Extract typography
    if "style" in node:
        style = node["style"]
        specs["typography"] = {
            "fontFamily": style.get("fontFamily", "Unknown"),
            "fontSize": style.get("fontSize", 0),
            "fontWeight": style.get("fontWeight", 400),
            "lineHeight": style.get("lineHeightPercent", 0) / 100 if style.get("lineHeightPercent") else None,
        }
    
    return specs


def generate_markdown_specs(specs: Dict[str, Any]) -> str:
    """Генерирует Markdown-спецификацию."""
    md = f"""# Спецификация: {specs['name']}

## Размеры
- **Ширина:** {specs['size']['width']}px
- **Высота:** {specs['size']['height']}px
- **Позиция:** X: {specs['position']['x']}px, Y: {specs['position']['y']}px

"""
    
    if "colors" in specs:
        md += "## Цвета\n"
        for i, color in enumerate(specs["colors"]):
            hex_color = f"#{color['r']:02x}{color['g']:02x}{color['b']:02x}"
            md += f"- **Цвет {i+1}:** `{hex_color}` (alpha: {color['a']})\n"
        md += "\n"
    
    if "typography" in specs:
        typo = specs["typography"]
        md += f"""## Типографика
- **Шрифт:** {typo['fontFamily']}
- **Размер:** {typo['fontSize']}px
- **Вес:** {typo['fontWeight']}
- **Межстрочный:** {typo['lineHeight'] or 'Auto'}

"""
    
    return md


def main():
    parser = argparse.ArgumentParser(description="Auto Specs Generator for Figma")
    parser.add_argument("--file", required=True, help="Figma file key")
    parser.add_argument("--token", required=True, help="Figma API token")
    parser.add_argument("--output", default="specs.md", help="Output file")
    args = parser.parse_args()
    
    print(f"📥 Загрузка файла {args.file}...")
    file_data = get_file(args.file, args.token)
    
    print(f"✅ Файл загружен: {file_data['name']}")
    print(f"📝 Генерация спецификации...")
    
    # Extract specs from first frame
    document = file_data["document"]
    specs_list = []
    
    def traverse(node):
        if node.get("type") in ["FRAME", "COMPONENT", "INSTANCE"]:
            specs = extract_specs(node)
            specs_list.append(specs)
        
        for child in node.get("children", []):
            traverse(child)
    
    traverse(document)
    
    # Generate output
    output = f"# Спецификация: {file_data['name']}\n\n"
    output += f"**Всего элементов:** {len(specs_list)}\n\n"
    output += "---\n\n"
    
    for specs in specs_list[:10]:  # Limit to first 10 for demo
        output += generate_markdown_specs(specs)
        output += "---\n\n"
    
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(output)
    
    print(f"✅ Спецификация сохранена: {args.output}")
    print(f"📊 Обработано элементов: {len(specs_list)}")


if __name__ == "__main__":
    main()
