자리수명 = ['', '만', '억', '조', '경', '해', '양', '구', '간', '정', '재', '극', '기승아', '타유나', '의사가불', '수대량무']

일에서구까지 = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']

def 숫자를문자로(n):
    n = str(n)
    n = n[::-1]
    if n[0] != '0':
        result = 일에서구까지[int(n[0])]
    else:
        result = ''
    for i in range(1, len(n)):
        if n[i] == '0':
            if i%4 == 0:
                result += 자리수명[i//4]
        elif n[i] == '1':
            if i%4 == 0:
                result += f'{자리수명[i//4]}일'
            elif i%4 == 1:
                result += '십'
            elif i%4 == 2:
                result += '백'
            else:
                result += '천'
        else:
            if i%4 == 0:
                result += f'{자리수명[i//4]}{일에서구까지[int(n[i])]}'
            elif i%4 == 1:
                result += f'십{일에서구까지[int(n[i])]}'
            elif i%4 == 2:
                result += f'백{일에서구까지[int(n[i])]}'
            else:
                result += f'천{일에서구까지[int(n[i])]}'
        print(result[::-1])
    result = result[::-1]
    return result

