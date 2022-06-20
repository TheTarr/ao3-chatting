f = open("dialogue.txt",'r',encoding='utf-8')
lines = f.readlines()
f.close()

print('<div class="pad">')

for i in range(0,len(lines)):
    if i%2==1:
        print('<p class="left">' + lines[i][:-1] + '</p>')
    else:
        print('<p class="left">' + lines[i][:-1] + '</p>')

print("</div>")