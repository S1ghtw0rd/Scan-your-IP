# 🛡️ Scan open port for your IP

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Nmap](https://img.shields.io/badge/Nmap-Required-orange.svg)

A simple and fast Python-based port scanner that utilizes Nmap to detect open ports and services on a target IP address. The tool automatically checks if Nmap is installed and provides installation instructions if it's missing.

## 🚀 Features
- Scans open ports and detects service versions using `nmap -sV -T4`.
- Custom timeout settings to control scan duration.
- Cross-platform support (automatically detects OS and provides Nmap installation instructions if missing).
- Clean and readable output.

## 🛠️ Requirements
- **Python 3.8+**
- **Nmap** (must be installed on your system)

## 📦 Installation
1. Clone the repository:
   git clone https://github.com/S1ghtW0rd/Your-Repo-Name.git
   cd Your-Repo-Name

2. Ensure you have Python installed. No additional pip packages are required as the script uses standard libraries.

## 💻 Usage
Run the script from your terminal, providing the target IP and the desired timeout (in milliseconds).

python scan.py --ip <YOUR_IP> --timeout <TIME_IN_MS>

**Example:**
python scan.py --ip 192.168.0.113 --timeout 15000

*(Note: The default timeout is 30000 milliseconds, which is 30 seconds).*

## 📝 How it works
1. The script uses shutil.which to check if Nmap is installed. If not, it prints OS-specific instructions on how to install it.
2. It uses subprocess to run the Nmap scan (nmap -sV -T4 <IP>).
3. It parses the output using re (regular expressions) to extract open ports and service information.
4. The script handles timeouts using Python's time module to ensure it doesn't hang indefinitely.

## ⚠️ Disclaimer
This tool is created for educational purposes only. Scanning networks without permission is illegal. Use it only on your own devices or networks you have explicit permission to test.

---

# 🇷🇺 Сканер открытых портов

Простой и быстрый сканер портов на Python, который использует Nmap для обнаружения открытых портов и сервисов на целевом IP-адресе. Скрипт автоматически проверяет наличие Nmap в системе и выдает инструкцию по установке, если его нет.

## 🚀 Возможности
- Сканирование портов и определение версий сервисов (nmap -sV -T4).
- Настройка таймаута (времени ожидания) для контроля длительности сканирования.
- Кроссплатформенность (автоматическое определение ОС и подсказки по установке Nmap).
- Понятный и чистый вывод.

## 🛠️ Требования
- **Python 3.8+**
- **Nmap** (должен быть установлен в системе).

## 📦 Установка
1. Клонируйте репозиторий:
   git clone https://github.com/S1ghtW0rd/Scan-your-IP.git
   cd Scan-your-IP

2. Дополнительные библиотеки через pip не требуются (используются только встроенные модули Python).

## 💻 Использование
Запустите скрипт в терминале, указав IP-адрес и желаемый таймаут (в миллисекундах).

python scan.py --ip <ВАШ_IP> --timeout <ВРЕМЯ_В_МС>

**Пример:**
python scan.py --ip 192.168.0.113 --timeout 15000

*(Примечание: по умолчанию таймаут составляет 30000 мс, то есть 30 секунд).*

## 📝 Как это работает
1. Скрипт использует shutil.which для проверки наличия Nmap. Если его нет — выводит инструкцию по установке для вашей ОС.
2. Запускает Nmap через subprocess с параметрами nmap -sV -T4 <IP>.
3. Парсит вывод с помощью регулярных выражений (re), чтобы вытащить открытые порты.
4. Использует модуль time для контроля таймаута, чтобы программа не зависала.

## ⚠️ Дисклеймер
Инструмент создан исключительно в образовательных целях. Сканирование чужих сетей без разрешения незаконно. Используйте его только на своих устройствах или сетях, на тестирование которых у вас есть официальное разрешение.

---
*Author: [S1ghtW0rd](https://github.com/S1ghtW0rd)*

---

## 📄 License / Лицензия

MIT License

Copyright (c) 2026 S1ghtW0rd

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.