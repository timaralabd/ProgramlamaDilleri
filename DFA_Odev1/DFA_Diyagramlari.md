# Ödev 1 – DFA Tabanlı Sözcüksel Analizci

**Amaç:** Java kaynak kodundaki lexeme ve token türlerini belirlemek.

## 1. Identifier ve keyword DFA

```text
(q0) --harf, _, $--> ((q1))
                       ^  |
                       |__| harf, rakam, _, $
```

q1 kabul durumudur. Okunan kelime keyword kümesindeyse KEYWORD, değilse IDENTIFIER olarak sınıflandırılır.

## 2. Sayısal sabit DFA

```text
(q0) --rakam--> ((q1)) --.--> (q2) --rakam--> ((q3))
                    ↺ rakam                     ↺ rakam
```

q1 ve q3 kabul durumlarıdır. Noktadan sonra rakam gelmezse hatalı sayı kabul edilir.

## 3. Operatör DFA

```text
(q0) -- = --> ((q1)) -- = --> ((q2))    (=, ==)
(q0) -- ! --> ((q3)) -- = --> ((q4))    (!, !=)
(q0) -- < --> ((q5)) -- = --> ((q6))    (<, <=)
(q0) -- > --> ((q7)) -- = --> ((q8))    (>, >=)
(q0) -- + --> ((q9)) -- + --> ((q10))   (+, ++)
```

Çift parantez kabul durumunu gösterir. Program önce iki karakterli operatörleri kontrol eder.

## 4. Ayırıcı DFA

```text
(q0) -- ( veya ) veya { veya } veya ; veya , --> ((q1))
```

Diğer desteklenen ayırıcılar: `[ ] .`

## 5. Örnek giriş

```java
int sayi = 10;
if (sayi >= 5) {
    sayi++;
}
```

## 6. Örnek çıktı

| Lexeme | Token |
|---|---|
| int | KEYWORD |
| sayi | IDENTIFIER |
| = | OPERATOR |
| 10 | SAYISAL SABIT |
| ; | AYIRICI |
| if | KEYWORD |
| ( | AYIRICI |
| sayi | IDENTIFIER |
| >= | OPERATOR |
| 5 | SAYISAL SABIT |
| ) | AYIRICI |
| { | AYIRICI |
| sayi | IDENTIFIER |
| ++ | OPERATOR |
| ; | AYIRICI |
| } | AYIRICI |

## 7. Sonuç

Bu çalışmada Python kullanılarak temel bir DFA tabanlı sözcüksel analizci geliştirildi. Program karakterleri sırayla kontrol ederek kelime, sayı, operatör ve ayırıcıları belirler. Tanınmayan karakterleri hata olarak gösterir. Java'nın bütün sözdizimi ve tüm token türleri bu örnek kapsamına dahil değildir.
