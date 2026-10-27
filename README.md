# Programlama Dilleri Ödevleri

Bu proje, Programlama Dilleri dersi kapsamında Python kullanılarak hazırlanan iki ödevden oluşmaktadır.

## Ödev 1: DFA Tabanlı Sözcüksel Analizi

Bu ödevde, Deterministik Sonlu Otomat (DFA) mantığı kullanılarak bir sözcüksel analiz programı geliştirilmiştir.

Program, Java benzeri bir kod içerisindeki anahtar kelimeleri, değişkenleri, sayıları ve operatörleri tespit ederek token türlerini ekrana yazdırır.

**Dosyalar:**
- `lexer.py`: Sözcüksel analiz programı
- `ornek.java`: Örnek kaynak kod
- `DFA_Diyagramlari.md`: DFA açıklamaları
- `README.txt`: Ödev açıklaması

**Çalıştırma:**
```bash
python DFA_Odev1/lexer.py
```

## Ödev 2: BNF Kuralları ile Aritmetik İfadelerin Sözdizimsel Analizi

Bu ödevde, BNF kurallarına uygun aritmetik ifadeleri kontrol eden bir sözdizimsel analiz programı geliştirilmiştir.

Program, Recursive Descent Parsing yöntemiyle ifadeleri analiz eder. İfade geçerliyse ayrıştırma ağacını (Parse Tree) ekrana yazdırır.

**Desteklenen işlemler:**
- Toplama (+)
- Çıkarma (-)
- Çarpma (*)
- Bölme (/)
- Parantezler
- Sayılar ve değişkenler

**Örnek ifade:**
```text
a + 3 * (b - 2)
```

**Çalıştırma:**
```bash
python "pd odev 2/odev2.py"
```

## Kullanılan Teknolojiler

- Python
- Visual Studio Code
- Git ve GitHub

## Ders Bilgisi

**Ders:** Programlama Dilleri