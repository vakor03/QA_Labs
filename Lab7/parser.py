import re
"""
Для парсера рекомендую використовувати бібліотеку re. Для свого парсера, я
використовував регулярку, що можна побачити нижче. Таким чином, можна відсіяти всі
непотрібні рядки з виводу
iperf-клієнта, а залишити тільки ті, що стосуються трафіку.
"""
REGEXP = r'\[\s*[0-9]*\]\s*[0-9\.-]*\s*(sec)\s*[0-9\.]*\s*[A-Z]?(Bytes)\s*[0-9\.]*\s*[A-Z]?(bits/sec)\s*[0-9]*\s*[0-9\.]*\s*[A-Z]?(Bytes)'
KEYS = ('Interval', 'Transfer', 'Bitrate', 'Retr', 'Cwnd')
