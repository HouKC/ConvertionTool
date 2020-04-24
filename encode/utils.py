def string2unicode_string(string):
    """
    输入中文，输出unicode编码的字符串，如：你好->\u4f60\u597d，abc->\u0061\u0062\u0063
    :param string:
    :return:
    """
    unicode_string = ''
    for v in string:
        # 转16进制unicode编码，如果不满2个字节则用0补满
        unicode_string += hex(ord(v)).replace('0x', '\\u') if len(hex(ord(v))) != 4 else hex(ord(v)).replace('0x',
                                                                                                             '\\u00')
    return unicode_string


def unicode_string2string(unicode_string):
    """
    输入unicode编码的字符串，输出中文，如：\u4f60\u597d->你好，\u0061\u0062\u0063->abc
    :param unicode_string:
    :return:
    """
    if not unicode_string and '\\u' not in unicode_string:
        return ''
    string = ''
    unicode_string = unicode_string.split('\\u')[1:]
    for u in unicode_string:
        string += chr(int('0x0' + u, base=16))
    return string


# print(unicode_string2string("\\u0061\\u0062\\u0063\\u4f60\\u597d"))

def string2ascii_10_string(unicode_string):
    """
    输入中文，输出ascii编码方式，你好abc->&amp;#20320;&amp;#22909;&amp;#97;&amp;#98;&amp;#99;
    在前端&amp;会被解析成&，所以最终结果是&#20320;&#22909;&#97;&#98;&#99;
    :param unicode_string:
    :return:
    """
    ascii_10_string = ''
    for v in unicode_string:
        # 由于前端解析html时会把&#进行解析，所以这里把&用&amp代替来通过html解析;这里是十进制表示
        ascii_10_string += '&amp;#' + str(ord(v)) + ';'
    return ascii_10_string


# print(string2ascii_10_string("你好abc"))


def string2ascii_16_string(unicode_string):
    """
    输入中文，输出ascii编码方式的十六进制，你好abc->&amp;#x4f60;&amp;#x597d;&amp;#x0061;&amp;#x0062;&amp;#x0063;
    在前端&amp;会被解析成&，所以最终结果是&#x4f60;&#x597d;&#x0061;&#x0062;&#x0063;
    :param unicode_string:
    :return:
    """
    ascii_16_string = ''
    for v in unicode_string:
        # 由于前端解析html时会把&#进行解析，所以这里把&用&amp代替来通过html解析;这里是16进制表示
        # ascii_16_string += '&amp;#x' + hex(ord(v)) + ';'
        ascii_16_string += hex(ord(v)).replace('0x', '&amp;#x') if len(hex(ord(v))) != 4 else hex(ord(v)).replace('0x',
                                                                                                                  '&amp;#x00')
        ascii_16_string += ';'
    return ascii_16_string


# print(string2ascii_16_string("你好abc"))

def ascii_string2string(ascii_string):
    """
    输入ascii编码的字符串(十六进制或十进制)，输出中文，如：&#x0064;&#x0064;&#x0064;&#x4f60;&#x597d;->ddd你好
    :param ascii_string:
    :return:
    """
    if not ascii_string and '&#' not in ascii_string:
        return ''
    string = ''
    ascii_string = ascii_string.lower()
    if 'x' in ascii_string:   # 判断是否为十六进制
        ascii_string = ascii_string.split('&#x')[1:]
        for u in ascii_string:
            string += chr(int('0x0' + u.replace(';', ''), base=16))
    else:
        ascii_string = ascii_string.split('&#')[1:]
        for u in ascii_string:
            string += chr(int(u.replace(';', '')))
    return string


# print(ascii_string2string("&#x0064;&#x0064;&#x0064;&#x4f60;&#x597d;"))

def unicode_string2ascii_10_string(unicode_string):
    """
    输入Unicode编码的字符串，输出ascii编码的十进制，如：\u4f60\u597d->&amp;#20320;&amp;#22909;
    :param unicode_string:
    :return:
    """
    return string2ascii_10_string(unicode_string2string(unicode_string))


def unicode_string2ascii_16_string(unicode_string):
    """
    输入Unicode编码的字符串，输出ascii编码的十六进制，如：\u4f60\u597d->&amp;#x4f60;&amp;#x597d;
    :param unicode_string:
    :return:
    """
    return string2ascii_16_string(unicode_string2string(unicode_string))


def ascii_string2unicode_string(ascii_string):
    """
    输入ascii编码的字符串(十进制或者十六进制)，输出Unicode编码，如：&amp;#x4f60;&amp;#x597d;->\u4f60\u597d
    :param ascii_string:
    :return:
    """
    return string2unicode_string(ascii_string2string(ascii_string))
