code=input('Caesar code\n')
shift_key=int(input('Enter shift key\n'))
l=len(code)
i=0
while i<l:
    a=ord(code[i])
    if a==32:
        pass
    # for small letters
    if a > 95:
            if (a+shift_key)<=122:
                print(chr(a+shift_key),end='')
            else:
                print(chr(a+shift_key-26),end='')
    # for capitals
    elif a <= 90 :
         if (a+shift_key)<=90:
              print(chr(a+shift_key), end='')
         elif (a+shift_key)>90:
              print(chr(a+shift_key-26), end='')
    i=i+1
    # Caesar shift : cipher stage 2 MHILY LZA ZBHL XBPZXBL MVYABUHL HWWPBZ JSHBKPBZ JHLJBZ KPJABT HYJHUBT LZA ULBAYV

    


