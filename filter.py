import re

fp=open('cn.m3u','r',encoding='utf-8')
s=fp.read()
fp.close()

s=s.replace('LocalTVHD','地方卫视')
s=s.replace("LocalTV",'地方卫视')
s=s.split('\n')


def get_info(x):
    res=[]
    id_patt=r'tvg-id='
    name_patt=r'tvg-name='
    logo_patt=r'tvg-logo='
    group_patt=r'group-title='
    show_patt=r','
    id_index=re.search(id_patt,x,flags=0).span()[1]
    id=x[id_index:].split(' ')[0][1:len(x[id_index:].split(' ')[0])-1]
    res.append(id)

    name_index=re.search(name_patt,x,flags=0).span()[1]
    name=x[name_index:].split(' ')[0][1:len(x[name_index:].split(' ')[0])-1]
    res.append(name)

    logo_index=re.search(logo_patt,x,flags=0).span()[1]
    logo=x[logo_index:].split(' ')[0][1:len(x[logo_index:].split(' ')[0])-1]
    res.append(logo)

    group_index=re.search(group_patt,x,flags=0).span()[1]
    group=x[group_index:].split(' ')[0][1:len(x[group_index:].split(',')[0])-1]
    res.append(group)

    show_index=re.search(show_patt,x,flags=0).span()[1]
    show=x[show_index:]
    res.append(show)
    return res

def recover_info(x):
    res='#EXTINF:-1 '+'tvg-id="'+x[0]+'" tvg-name="'+x[1]+'" tvg-logo="'+x[2]+'" group-title="'+x[3]+'",'+x[4]
    return res

id=[]
res=[]
for i in range(len(s)):
    if s[i][:7]=='#EXTINF':
        info=get_info(s[i])
        if info[0]!='' and info[0] not in id:
            id.append(info[0])
            inf=recover_info(info)
            res.append([inf,s[i+1]])

s='#EXTM3U\n\n\n'

for i in range(len(res)):
    s+=res[i][0]+'\n'
    s+=res[i][1]+'\n'
    s+='\n'

with codecs.open('test.m3u','w',encoding='utf-8') as f:
    f.write(s)
