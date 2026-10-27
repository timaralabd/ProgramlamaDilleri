# DFA tabanli basit Java sozcuksel analizci
# Odev 1

keywords = {'int', 'double', 'float', 'char', 'boolean', 'if', 'else', 'while', 'for', 'return', 'class', 'public', 'static', 'void', 'new', 'true', 'false'}
operators = {'+', '-', '*', '/', '=', '<', '>', '!', '==', '!=', '<=', '>=', '++', '--', '&&', '||', '%'}
separators = {'(', ')', '{', '}', '[', ']', ';', ',', '.'}

def is_letter(ch):
    return ch.isascii() and (ch.isalpha() or ch in '_$')

def is_digit(ch):
    return '0' <= ch <= '9'

def analyze(code):
    result = []
    i = 0
    while i < len(code):
        ch = code[i]
        if ch.isspace():
            i += 1
            continue

        # Identifier DFA: q0 -> q1 (harf), q1 -> q1 (harf/rakam)
        if is_letter(ch):
            start = i
            i += 1
            while i < len(code) and (is_letter(code[i]) or is_digit(code[i])):
                i += 1
            word = code[start:i]
            result.append((word, 'KEYWORD' if word in keywords else 'IDENTIFIER'))
            continue

        # Sayi DFA: q0 -> q1 (rakam), q1 -> q1 (rakam)
        # q1 -> q2 (nokta), q2 -> q3 (rakam), q3 -> q3 (rakam)
        if is_digit(ch):
            start = i
            while i < len(code) and is_digit(code[i]):
                i += 1
            if i < len(code) and code[i] == '.':
                i += 1
                if i >= len(code) or not is_digit(code[i]):
                    result.append((code[start:i], 'HATALI SAYI'))
                    continue
                while i < len(code) and is_digit(code[i]):
                    i += 1
            result.append((code[start:i], 'SAYISAL SABIT'))
            continue

        # Operator DFA: once iki karakterli operator denenir
        if i + 1 < len(code) and code[i:i+2] in operators:
            result.append((code[i:i+2], 'OPERATOR'))
            i += 2
            continue
        if ch in operators:
            result.append((ch, 'OPERATOR'))
            i += 1
            continue
        if ch in separators:
            result.append((ch, 'AYIRICI'))
            i += 1
            continue
        result.append((ch, 'HATA: TANIMSIZ KARAKTER'))
        i += 1
    return result

if __name__ == '__main__':
    print('Java kodunu giriniz (bitirmek icin bos satir):')
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            break
        lines.append(line)
    code = '\n'.join(lines) if lines else 'int sayi = 10; if (sayi >= 5) { sayi++; }'
    print('\n{:<22} {}'.format('LEXEME', 'TOKEN'))
    print('-' * 46)
    for lexeme, token in analyze(code):
        print('{:<22} {}'.format(lexeme, token))
