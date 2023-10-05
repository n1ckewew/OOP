def reverse(word):#Создается функция reverse с аргументом word
    punctuation_marks='.,?-:;!"'#Создается переменная punctuation_marks со значениями пунктуационных знаков
    word_rev=''#Создается переменная word_rev которые будут использоватся для создания обратного слова
    res='' #переменная res для того же что и word_rev
    for sym in word:
        if sym not in punctuation_marks:#Если символ sym не является пунктуационным знаком то он добавляется к переменной word_rev
            word_rev+=sym
        else:#Если символ sym является пунктуационным знаком то переменная word_rev обращается и добавляется к переменной res вместе с пунктуационным знаком sym.
            word_rev=word_rev[::-1]
            res+=word_rev+sym
            word_rev=''
    word_rev=word_rev[::-1]
    res+=word_rev
    return res
message=input('Сообщение').split()#Вводится сообщение от пользователя и оно разбивается на отдельные слова с помощью метода split()
reverse_mes=''#Создается переменная reverse_mes которая будет содержать обратное написание сообщения
for word in message:
    reverse_mes+=''+reverse(word)#К переменной reverse_mes добавляется обратное написание слова с помощью вызова функции reverse(word)
    print('Новое сообщение:', reverse_mes)#Выводится новое сообщение reverse_mes