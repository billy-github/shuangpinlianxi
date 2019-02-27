# -*- coding: utf-8 -*-

# @Author  : billy
# @Email   : 84639806@qq.com

# Kuai _ing Liang _uang Ruan Cao Zou T _ue_ve Qiu Yun Wei J_an Mian
# 快   迎    两    王    软   草  走  特  约    秋   云   为  见   面
# Xia _ua Song _iong U_shu I_chi V_zhui_v Geng Dai Bin Niao Fen Pie Hang
# 夏   娃 怂    恿    书    痴    追       更   待  滨   鸟  分  撇  航

#快迎两王软草走，特约秋云为见面
#夏娃怂恿书痴追，更待滨鸟分撇航
import random
noteStr = \
    '''
iu->秋 ， 特约秋云为见面
ei->为 ， 特约秋云为见面
uan->软 ， 快迎两王软草走
ue->约 ， 特约秋云为见面
ve->约 ， 特约秋云为见面
un->云 ， 特约秋云为见面
sh->书 ， 夏娃怂恿书痴追
u->书 ， 夏娃怂恿书痴追
ch->痴 ， 夏娃怂恿书痴追
i->痴 ， 夏娃怂恿书痴追
uo->说 ，自己加， 
ie->撇 ， 更待滨鸟分撇航
iong->恿 ， 夏娃怂恿书痴追
ong->恿 ， 夏娃怂恿书痴追
ai->待 ， 更待滨鸟分撇航
en->分 ， 更待滨鸟分撇航
eng->更 ， 更待滨鸟分撇航
ang->航 ， 更待滨鸟分撇航
an->见 ，特约秋云为见面
uai->快 ， 快迎两王软草走
ing->迎 ， 快迎两王软草走
uang->王 ， 快迎两王软草走
iang->两 ， 快迎两王软草走
ou->走 ，  快迎两王软草走
ua->娃 ， 夏娃怂恿书痴追
ia->夏 ， 夏娃怂恿书痴追
ao->草 ， 快迎两王软草走
zh->追 ， 夏娃怂恿书痴追
ui->追 ， 夏娃怂恿书痴追
in->滨 ， 更待滨鸟分撇航
iao->鸟 ， 更待滨鸟分撇航
ian->面 ， 特约秋云为见面
    '''

keymapStr = \
    '''
iu->q->秋
ei->w->为
uan->r->软
ue->t->约
ve->t->约
un->y->云
sh->u->书
u->u->书
ch->i->痴
i->i->痴
uo->o->说，自己加
ie->p->撇
iong->s->恿
ong->s->恿
ai->d->待
en->f->分
eng->g->更
ang->h->航
an->j->干，自己加
uai->k->快
ing->k->迎
uang->l->王
iang->l->两
ou->z->走
ua->x->娃
ia->x->夏
ao->c->草
zh->v->追
ui->v->追
in->b->滨
iao->n->鸟
ian->m->面
    '''


lines = keymapStr.strip().split('\n')
keyMapDict = {}
noteDict = {}
for lines in lines:
    split = lines.split("->")
    key = split[0].lstrip()  # 去掉左边的空格
    value = split[1]
    keyMapDict.update({key: value})

lines = noteStr.strip().split('\n')
noteDict = {}
for lines in lines:
    split = lines.split("->")
    key = split[0].lstrip()  # 去掉左边的空格
    value = split[1]
    noteDict.update({key: value})

print("------开始练习-------")
print("快 迎 两 王 软 草 走，特约 秋 云 为 见 面。")
print("夏 娃 怂 恿 书 痴 追， 更 待 滨 鸟 分 撇 航？ ")

# 提示输入
while True:
    randomKey = random.choice(list(keyMapDict.keys()))
    correctValue = keyMapDict.get(randomKey)
    note = noteDict.get(randomKey)

    print("韵母/声母：{}  {}".format(randomKey, note))
    inputValue = input("输入键位：")

    if inputValue == correctValue:
        print("success !")
        pass
    else:
        print("error !")
    print()
