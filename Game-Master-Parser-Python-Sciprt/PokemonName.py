import re
ff=open("1208merged.txt","r",encoding="UTF-8")
b=ff.readlines()
fff=open("1208emerged.txt","r",encoding="UTF-8")
c=fff.readlines()
name=""
engname=""
move=""
engmove=""
for i in range(0,len(c)):
    if "pokemon_nickname_error" in b[i]:break
    if "pokemon_name_" in b[i]:
        temp=re.search("[\u4e00-\u9fa5]+",b[i+1])
        if temp:
            name+=temp.group()+'\n'
    if "pokemon_name_" in c[i]:
        position=c[i+1].find("\"")
        if(c[i+1][position+1]=="-"):i+=1;continue
        for x in range(position+1,len(c[i+1])-2):
            engname+=c[i+1][x]
        engname+="\n"
        
for i in range(0,len(c)):
    if "move_reroll_confirm_desc" in b[i]:break
    if "move_name_" in b[i]:
        temp=re.search("[\u4e00-\u9fa5]+",b[i+1])
        if temp:
            move+=temp.group()+'\n'
    if "move_name_" in c[i]:
        position=c[i+1].find("\"")
        for x in range(position+1,len(c[i+1])-2):
            engmove+=c[i+1][x]
        engmove+="\n"
print(move)
aa=open("name/pokemonchiname.txt","w",encoding="UTF-8")
bb=open("name/pokemoningname.txt","w",encoding="UTF-8")
aa.write(name);aa.close()
bb.write(engname);bb.close()
aa=open("name/pokemonchmove.txt","w",encoding="UTF-8")
bb=open("name/pokemoningmove.txt","w",encoding="UTF-8")
aa.write(move);aa.close()
bb.write(engmove);bb.close()
