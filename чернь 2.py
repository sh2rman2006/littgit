s="0123456789abcdefg"
for x in s:
    a=int(f'8{x}38{x}68',27)+int(f'37{x}3163',27)
    if a%26==0:
        print(a/26)
