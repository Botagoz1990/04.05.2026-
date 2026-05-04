import os
import re

cases = {
    "ktzh": {
        "title": "Қазақстан Темір Жолы (КТЖ)",
        "industry": "Транспорт",
        "product": "АСКОУ – ТОИР",
        "problem": "Высокая зависимость от человеческого фактора при обслуживании систем сигнализации и связи, неэффективность бумажной отчетности.",
        "solution": "Внедрение «АСКОУ – ТОИР». Автоматизация планирования, фотофиксация неисправностей и электронный документооборот для электромехаников.",
        "results": [
            {"icon": "ph-chart-line-up", "text": "Переход на мониторинг<br>в реальном времени"},
            {"icon": "ph-shield-check", "text": "Повышение безопасности<br>движения поездов"},
            {"icon": "ph-x-circle", "text": "Исключение ошибок<br>ручного ввода данных"}
        ]
    },
    "kazaeronavigatsia": {
        "title": "РГП «Казаэронавигация»",
        "industry": "Аэронавигация",
        "product": "АСКОУ – ТОИР",
        "problem": "Сложность контроля инженеров, работающих на удаленных объектах аэронавигации, и задержки в отчетности.",
        "solution": "Внедрение системы «АСКОУ – ТОИР» с функциями онлайн-контроля местоположения персонала и состояния оборудования.",
        "results": [
            {"icon": "ph-calendar-check", "text": "Прозрачное планирование<br>работ"},
            {"icon": "ph-lightning", "text": "Мгновенная фиксация<br>инцидентов"},
            {"icon": "ph-trophy", "text": "Международное признание<br>на RFID Journal Award"}
        ]
    },
    "kmg": {
        "title": "АО «НК «КазМунайГаз» (КМГ)",
        "industry": "Нефтегаз",
        "product": "АСКОУ – ТОИР / Инвентаризация",
        "problem": "Огромный объем территориально распределенных активов. Ручная инвентаризация занимала месяцы и давала низкую точность.",
        "solution": "Комплекс «АСКОУ – Инвентаризация» и «АСКОУ – ТОИР». Оцифровка тысяч единиц оборудования и внедрение регулярного ТО.",
        "results": [
            {"icon": "ph-eye", "text": "Оперативный контроль<br>перемещения активов"},
            {"icon": "ph-wrench", "text": "Сокращение сбоев<br>оборудования"},
            {"icon": "ph-medal", "text": "Награда<br>RFID Journal Award 2022"}
        ]
    },
    "kaztransoil": {
        "title": "АО «КазТрансОйл»",
        "industry": "Нефтегаз",
        "product": "АСКОУ – Инвентаризация",
        "problem": "Неактуальные данные о состоянии и местонахождении основных средств (ОС), отсутствие интеграции с учетными системами.",
        "solution": "Внедрение «АСКОУ – Инвентаризация» с использованием RFID-меток и полной интеграцией с SAP.",
        "results": [
            {"icon": "ph-check-square", "text": "100% идентификация<br>и фотофиксация ОС"},
            {"icon": "ph-warning-circle", "text": "Автовыявление излишков<br>и недостач"},
            {"icon": "ph-file-text", "text": "Упрощение отчетности<br>для МОЛ"}
        ]
    },
    "shatyr": {
        "title": "ТОО «Шатыр»",
        "industry": "Транспорт / Услуги",
        "product": "АСКОУ – Инвентаризация",
        "problem": "Ручной учет 700 000 единиц мягкого инвентаря (белья) приводил к огромным потерям времени и путанице при приеме-передаче.",
        "solution": "Система «АСКОУ – Инвентаризация» с применением RFID-технологий для контроля всей цепочки (стирка – склад – поезд).",
        "results": [
            {"icon": "ph-package", "text": "Мгновенный учет<br>комплектации"},
            {"icon": "ph-shield-check", "text": "Минимизация потерь<br>имущества"},
            {"icon": "ph-thumbs-up", "text": "Проект-финалист<br>RFID Journal Award 2022"}
        ]
    }
}

template_path = r"cases\energy-toir.html"

with open(template_path, "r", encoding="utf-8") as f:
    orig = f.read()

for key, data in cases.items():
    file_path = f"cases\\{key}.html"
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = re.sub(r"<title>.*?</title>", f"<title>Кейс: {data['title']} - ABITECH</title>", content)
    
    body_match = re.search(r"(<!-- Block 1: Hero / Headline -->.*)(<!-- Block 9: CTA -->)", content, re.DOTALL)
    if body_match:
        new_blocks = f"""<!-- Block 1: Hero / Headline -->
    <header class="section"
        style="background: url('../assets/energy-hero.png') no-repeat center center/cover; color: var(--white); padding: 120px 0; text-align: center;">
        <div class="container" style="position: relative; z-index: 2;">
            <h1 style="max-width: 900px; margin: 0 auto; text-shadow: 0 2px 10px rgba(0,0,0,0.5);">{data['title']}</h1>
        </div>
        <div style="position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(14, 25, 27, 0.85); z-index: 1;"></div>
    </header>

    <!-- Block 2: Facts -->
    <section class="section" style="padding: 40px 0; background-color: var(--white);">
        <div class="container">
            <div class="grid-4">
                <div class="card" style="text-align: center; border: 1px solid #eee; box-shadow: none;">
                    <p style="font-size: 14px; text-transform: uppercase; color: var(--text-gray); margin-bottom: 8px;">Отрасль</p>
                    <h3 style="font-size: 18px; margin: 0;">{data['industry']}</h3>
                </div>
                <div class="card" style="text-align: center; border: 1px solid #eee; box-shadow: none;">
                    <p style="font-size: 14px; text-transform: uppercase; color: var(--text-gray); margin-bottom: 8px;">Продукт</p>
                    <h3 style="font-size: 18px; margin: 0;">{data['product']}</h3>
                </div>
                <div class="card" style="text-align: center; border: 1px solid #eee; box-shadow: none;">
                    <p style="font-size: 14px; text-transform: uppercase; color: var(--text-gray); margin-bottom: 8px;">География</p>
                    <h3 style="font-size: 18px; margin: 0;">Казахстан</h3>
                </div>
                <div class="card" style="text-align: center; border: 1px solid #eee; box-shadow: none;">
                    <p style="font-size: 14px; text-transform: uppercase; color: var(--text-gray); margin-bottom: 8px;">Формат проекта</p>
                    <h3 style="font-size: 18px; margin: 0;">Публичный кейс</h3>
                </div>
            </div>
        </div>
    </section>

    <!-- Block 3: Problem/Solution -->
    <section class="section">
        <div class="container" style="max-width: 800px;">
            <div style="margin-bottom: 60px;">
                <h2 class="section-title" style="text-align: left;">Проблематика</h2>
                <p style="font-size: 18px; line-height: 1.6; color: var(--text-dark); border-left: 4px solid #ddd; padding-left: 20px;">
                    {data['problem']}
                </p>
            </div>
            
            <h2 class="section-title" style="text-align: left;">Решение ABITECH</h2>
            <div class="card" style="padding: 32px; background-color: var(--white); border-left: 4px solid var(--primary);">
                <p style="font-size: 18px; line-height: 1.6; margin: 0;">
                    {data['solution']}
                </p>
            </div>
        </div>
    </section>

    <!-- Block 7: Results -->
    <section class="section" style="background-color: var(--bg-light);">
        <div class="container" style="max-width: 900px;">
            <h2 class="section-title">Ключевые результаты</h2>
            <div class="grid-3">
                <div class="card result-card" style="text-align: center; background: white;">
                    <div class="result-kpi" style="font-size: 40px; color: var(--primary); margin-bottom: 10px;"><i class="ph {data['results'][0]['icon']}"></i></div>
                    <p>{data['results'][0]['text']}</p>
                </div>
                <div class="card result-card" style="text-align: center; background: white;">
                    <div class="result-kpi" style="font-size: 40px; color: var(--primary); margin-bottom: 10px;"><i class="ph {data['results'][1]['icon']}"></i></div>
                    <p>{data['results'][1]['text']}</p>
                </div>
                <div class="card result-card" style="text-align: center; background: white;">
                    <div class="result-kpi" style="font-size: 40px; color: var(--primary); margin-bottom: 10px;"><i class="ph {data['results'][2]['icon']}"></i></div>
                    <p>{data['results'][2]['text']}</p>
                </div>
            </div>
        </div>
    </section>

    """
        content = content[:body_match.start()] + new_blocks + content[body_match.end()-19:]
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
print("done")
