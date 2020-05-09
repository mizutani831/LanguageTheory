import sys, os
import re

def lexical_analysis(content: str) -> list:
    result = list()
    index = 0
    word = ''
    try:
        while index < len(content):
            match = re.match('\n', content[index])
            if match:
                word = "\n"
                break
            match = re.match(r'\d', content[index])
            if match:
                word += content[index]
                while True:
                    index += 1
                    match = re.match(r'\d', content[index])
                    if match is None:
                        break
                    word += content[index]
                result.append(int(word))
                word = ''
                continue
            match = re.match(r'[a-zA-Z]', content[index])
            if match:
                word += content[index]
                while True:
                    index += 1
                    match = re.match(r'[a-zA-Z0-9]', content[index])
                    if match is None:
                        break
                    word += content[index]
                result.append(word)
                word = ''
                continue
            if content[index] == ' ':
                index += 1
                continue
            result.append(content[index])
            index += 1
    except IndexError:
        result.append(word)
    return result

if __name__ == '__main__':
    content = input("text: ")
    result = lexical_analysis(content)
    print(result)
