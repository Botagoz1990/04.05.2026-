$ErrorActionPreference = "Stop"
$baseDir = "c:\Users\Айзада\Desktop\Сайт Абитек"

$map = [ordered]@{
    "Главная" = "home"
    "Продукты" = "products"
    "Мобильный ТОиР" = "mobile_mro"
    "RFID и спецодежда" = "rfid_workwear"
    "ИИ-коннектор" = "ai_connector"
    "WMS" = "wms"
    "BI-решения" = "bi_solutions"
    "Отрасли" = "industries"
    "Нефтегазовый сектор" = "oil_gas_title"
    "Нефтегаз" = "oil_gas_title"
    "Угольная промышленность" = "mining"
    "Металлургия" = "metallurgy"
    "Логистика" = "logistics"
    "Энергетика" = "energy"
    "Кейсы" = "cases"
    "О компании" = "about_us"
    "Контакты" = "contacts"
    "RU" = "lang_ru"
    "KZ" = "lang_kz"
    "EN" = "lang_en"
    "Превращаем хаос в управляемую систему" = "transforming_chaos"
    "Цифровая автоматизация бизнеса и производства" = "digital_automation"
    "Разработка ПО, внедрение WMS и комплексная автоматизация предприятий в Казахстане. Опыт более 20 лет" = "software_development_wms"
    "Начать цифровизацию" = "start_digitalization"
    "Скролл вниз" = "scroll_down"
    "Отрасли / Кому мы помогаем" = "industries_who_we_help"
    "Проблема" = "problem"
    "Решение" = "solution"
    "Потери и отсутствие прозрачного учёта активов на всех этапах добычи и переработки." = "losses_lack_transparent"
    "RFID-маркировка и система цифрового учёта для 100% прозрачности перемещений ТМЦ." = "rfid_tagging_digital"
    "Подробнее об отраслевом решении" = "more_about_industry"
    "Контроль техники и снижение простоев в угольной добыче" = "equipment_control_downtime"
    "Простои карьерной техники и отсутствие точного контроля перемещений на разрезах и в шахтах." = "downtime_career_equipment"
    "Мониторинг техники в реальном времени, RFID-учёт активов и интеллектуальные системы безопасности." = "monitoring_equipment_realtime"
    "Обсудить проект" = "btn_discuss"
    "Контроль производства и снижение потерь в металлургии" = "control_production_losses"
    "Разрозненные производственные данные и отсутствие системы единого контроля эффективности." = "fragmented_production_data"
    "Бесшовная интеграция ИТ-систем и ИИ-аналитика для поиска узких мест и оптимизации процессов." = "seamless_integration_it"
    "Контроль складских операций и снижение потерь" = "control_warehouse_operations"
    "Высокий риск ошибок комплектации, задержки отгрузок и потери на складах." = "high_risk_errors"
    "Внедрение современных WMS-систем и IoT-контроль складских операций в режиме real-time." = "implementation_wms_iot"
    "Снижение простоев оборудования в энергетике" = "reduction_equipment_downtime"
    "Непредсказуемые простои из-за поломок и отсутствие объективных данных о состоянии оборудования." = "unpredictable_downtime"
    "Мобильный ТОиР и предиктивная видеоаналитика для мониторинга износа и планирования ремонтов." = "mobile_mro_predictive"
    "Цифровое управление обслуживанием оборудования" = "digital_management_equipment"
    "Подробнее" = "read_more"
    "Учёт активов, оборудования и спецодежды" = "asset_equipment_ppe"
    "Учёт спецодежды" = "ppe_tracking"
    "Контроль выдачи и сроков эксплуатации СИЗ" = "control_issuance_ppe"
    "Интеграция и обмен данными между системами" = "data_integration_exchange"
    "Автоматизация складских процессов" = "warehouse_automation"
    "Контроль материальных потоков и данных" = "material_flow_control"
    "Кейсы и результаты" = "cases_and_results"
    "Безопасность" = "security"
    "Қазақстан Темір Жолы (КТЖ)" = "ktzh"
    "Задача" = "task"
    "Результат" = "result"
    "Подробнее →" = "read_more_arrow"
    "до 0" = "to_0"
    "Сокращение аварийных ситуаций" = "reduction_emergencies"
    "Благодарственные письма и отзывы" = "letters_of_appreciation"
    "Нам доверяют лидеры промышленности и бизнеса" = "trusted_by_leaders"
    "Почему ABITECH" = "why_abitech"
    "20+ лет опыта" = "20_years_experience"
    "Собственная разработка" = "in_house_development"
    "Глубокая интеграция" = "deep_integration"
    "Экспертиза в промышленности" = "industry_expertise"
    "Международный опыт" = "international_experience"
    "Подробнее о компании" = "more_about_company"
    "Технологии и интеграции" = "technologies_integrations"
    "Интеграции, которые делают процессы прозрачными" = "integrations_transparent"
    "Полезные материалы" = "useful_materials"
    "Чек-лист ТОиР" = "mro_checklist"
    "Проверьте эффективность обслуживания оборудования." = "check_efficiency_equipment"
    "Получить чек-лист" = "get_checklist"
    "Аудит учёта спецодежды" = "ppe_audit"
    "Пройти аудит" = "take_audit"
    "Калькулятор WMS" = "wms_calculator"
    "Рассчитать" = "calculate"
    "Оценка интеграции" = "integration_estimate"
    "Получить оценку" = "get_estimate"
    "Оставьте заявку" = "leave_request"
    "Имя" = "name"
    "Компания" = "company"
    "Телефон" = "phone"
    "Email" = "email"
    "Кратко задача" = "brief_task"
    "Отправить и получить" = "send_and_receive"
    "История компании" = "company_history"
    "Ключевые вехи" = "key_milestones"
    "2003 год" = "year_2003"
    "Основание ТОО «Advanced Business Technologies» (ABiTech). Старт деятельности как системного интегратора в сфере IT." = "foundation_abitech"
    "2010–2015 гг." = "years_2010_2015"
    "Переход к собственной разработке ПО. Запуск системы АСКОУ (Автоматизированная система контроля и оперативного учета). Начало активной работы с крупными промышленными предприятиями Казахстана." = "transition_software"
    "2018–2021 гг." = "years_2018_2021"
    "Масштабирование экспертизы в RFID-технологии и IoT. Разработка уникальных решений для нефтегазового сектора и угольной промышленности." = "scaling_rfid"
    "2022 год" = "year_2022"
    "Международное признание. Проект «АСКОУ – Бутик» становится финалистом престижной премии RFID Journal Award 2022." = "international_recognition"
    "Сегодня" = "today"
    "ABiTech — ведущий разработчик решений для цифрового управления активами, ТОиР и безопасности в промышленности." = "abitech_leading"
    "Миссия и видение" = "mission_vision"
    "Миссия" = "mission"
    "Мы создаем прозрачную цифровую среду для управления промышленными активами, помогая компаниям исключать потери, предотвращать аварии и повышать эффективность персонала." = "we_create_transparent"
    "Видение" = "vision"
    "Стать технологическим стандартом в цифровизации производственных процессов на рынке Центральной Азии и за ее пределами." = "become_standard"
    "Команда" = "team"
    "Рахматуллаев Равшан Джураевич" = "ravshan_rakhmatullaev"
    "Директор ТОО «ABiTech». Идейный вдохновитель и стратег." = "director_abitech"
    "Тимур Исмагилов" = "timur_ismagilov"
    "Директор филиала (г. Астана). Куратор ключевых промышленных внедрений и взаимодействия с государственным сектором." = "branch_director"
    "Назерке [Фамилия]" = "nazerke_surname"
    "Ведущий бизнес-аналитик. Архитектор решений, адаптирующих ПО под специфику заказчика." = "lead_business_analyst"
    "Партнёры и технологические вендоры" = "partners_technology_vendors"
    "Мы интегрируем наши решения с мировыми лидерами:" = "we_integrate_solutions"
    "Награды и признание" = "awards_recognition"
    "Участник международных выставок" = "participant_exhibitions"
    "Нурым Габбас" = "nurym_gabbas"
    "Финансовый директор" = "financial_director"
    "Шамуратов Канат" = "shamuratov_kanat"
    "Начальник отдела менеджеров проектов" = "head_project_managers"
    "Титенко Владимир" = "titenko_vladimir"
    "Начальник отдела разработки" = "head_development"
}

$htmlFiles = Get-ChildItem -Path $baseDir -Filter *.html -Recurse

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $modified = $false

    # SPECIFIC USER REQUESTS: Change h3 to h2 for these titles
    if ($content -match '(<h[1-6][^>]*?data-i18n="oil_gas_title"[^>]*?>).*?(</h[1-6]>)') {
        $content = [Regex]::Replace($content, '(<h[1-6])([^>]*?data-i18n="oil_gas_title"[^>]*?>)(.*?)(</h[1-6]>)', '<h2$2Нефтегазовый сектор</h2>')
        $modified = $true
    }
    if ($content -match '(<h[1-6][^>]*?data-i18n="mining"[^>]*?>).*?(</h[1-6]>)') {
        $content = [Regex]::Replace($content, '(<h[1-6])([^>]*?data-i18n="mining"[^>]*?>)(.*?)(</h[1-6]>)', '<h2$2Угольная промышленность</h2>')
        $modified = $true
    }

    # Standard tagging for other elements
    foreach ($key in $map.Keys) {
        $slug = $map[$key]
        $escapedKey = [Regex]::Escape($key)
        $pattern = "(?s)(<([a-zA-Z0-9]+)(?:(?!\bdata-i18n\b)[^>])*?)(>)(\s*$escapedKey\s*)(</\2>)"
        if ($content -match $pattern) {
            $content = [Regex]::Replace($content, $pattern, "`$1 data-i18n=""$slug""`$3`$4`$5")
            $modified = $true
        }
        $placeholderPattern = "(placeholder\s*=\s*`")$escapedKey(`")"
        if ($content -match $placeholderPattern) {
            $content = [Regex]::Replace($content, $placeholderPattern, "`$1$escapedKey`$2 data-i18n-placeholder=""$slug""")
            $modified = $true
        }
    }

    if ($modified) {
        [IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Updated $($file.FullName)"
    }
}
Write-Host "Done"
