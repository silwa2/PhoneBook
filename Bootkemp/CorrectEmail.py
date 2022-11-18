def CorrectEmail(email):
    if email.count('@') > 1 or email.count('@') == 0:
        return (False, 'Неверное количество знаков @')
    [name,domain] = email.split('@')
    if len(domain) < 3:
        return (False, 'Доменное имя короче 3 символов')
    if len(domain) > 256:
        return (False, 'Доменное имя длиннее 256 символов')
    if domain.count('.') == 0:
        return (False, 'Доменное имя не содержит точки')
    includedomain = domain.split('.')
    # список с кодами корректных сиволов a-z - и _
    correctchrlist = list(range(ord('a'),ord('z')+1))
    correctchrlist.extend([ord('-'), ord('_')])
    for k in includedomain:
        # проверяем нет ли пустых подстрок в домене
        if k == '':
            return (False, 'Доменное имя содержит пустую строку между точками')
        # проверяем нет ли нелегальных символов в подстроках в домене
        for n in k:
            if ord(n) not in correctchrlist:
                errormsg = "Недопустимый символ " + n
                return (False, errormsg)
        if (k[0] == '-') or (k[len(k)-1] == '-'):
            return (False, 'Доменное имя не может начинаться/заканчиваться знаком "-"')
    if len(name) > 128:
        return (False, 'Имя длиннее 128 символов')
    # Добавляем в список корректных символов . ; " ! : ,
    correctchrlist.extend([ord('.'),ord(';'),ord('"')])
    onlyinquoteschrlist = [ord('!'), ord(','), ord(':')]
    correctchrlist.extend(onlyinquoteschrlist)
    # Проверка на парные кавычки
    if name.count('"')%2 != 0:
        return (False, "Непарные кавычки")
    # Переменные для отслеживания точки и открывающихся кавычек
    doubledot = False
    inquotes = False
    for k in name:
        if (k == '"'):
            inquotes = not inquotes
        if (ord(k) in onlyinquoteschrlist) and (inquotes == False):
            return (False, "Недопустимый символ вне кавычек")
        if ord(k) not in correctchrlist:
            errormsg = "Недопустимый символ " + k
            return (False, errormsg)
        # проверка на две точки подряд
        if (k == '.'):
            if doubledot == True:
                return (False, "Две точки в имени")
            else:
                doubledot = True
    return (email)