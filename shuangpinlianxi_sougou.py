# -*- coding: utf-8 -*-

# @Author  : billy
# @Email   : 84639806@qq.com

# Q秋 W娃丫 E娥 R远观 T月     Y域外 U舒 I驰 O嗅卧 P云昆
# A阿 S勇送， D汪洋 F分       G更 H航 J岸 K靠 L来
# z贼 X卸 C笑 V追             B怄 N您 M眠

import random
keymapStr = \
    '''
iu->q->秋
ia->w->丫
ua->w->娃
e->e->娥
er->r->远观
uan->r->远观
ve->t->月
ue->t->月
v->y->域
uai->y->外
sh->u->舒
ch->i->驰
uo->o->嗅卧
o->o->嗅卧
un->p->云昆
a->a->阿
ong->s->勇送
iong->s->勇送
ing->d->汪洋
uang->d->汪洋
iang->d->汪洋
en->f->分
eng->g->更
ang->h->航
an->j->岸
ao->k->靠
ai->l->来
ei->z->贼
ie->x->卸
iao->c->笑
zh->v->追
ui->v->追
ou->b->怄
in->n->您
ian->m->眠
    '''
noteStr = \
    '''
iu->秋 ,1.秋娃丫娥远观月
ia->丫 ,1.秋娃丫娥远观月
ua->娃 ,1.秋娃丫娥远观月
e->娥 ,1.秋娃丫娥远观月
er->远观 ,1.秋娃丫娥远观月
uan->远观 ,1.秋娃丫娥远观月
ve->月 ,1.秋娃丫娥远观月
ue->月 ,1.秋娃丫娥远观月
v->域 ,2.域外舒驰噢卧云昆
uai->外 ,2.域外舒驰噢卧云昆
sh->舒 ,2.域外舒驰噢卧云昆
ch->驰 ,2.域外舒驰噢卧云昆
uo->嗅卧 ,2.域外舒驰噢卧云昆
o->嗅卧 ,2.域外舒驰噢卧云昆
un->云昆 ,2.域外舒驰噢卧云昆
a->阿 ,3.阿勇送，
ong->勇送 ,3.阿勇送，
iong->勇送 ,3.阿勇送，
uang->汪洋 ,3.汪洋分
iang->汪洋 ,3.汪洋分
en->分 ,3.汪洋分
eng->更 ,4.更航岸靠来
ang->航 ,4.更航岸靠来
an->岸 ,4.更航岸靠来
ao->靠 ,4.更航岸靠来
ai->来 ,4.更航岸靠来
ei->贼 ,5.贼缷邀追
ie->卸 ,5.贼缷邀追
iao->邀 ,5.贼缷邀追
zh->追 ,5.贼缷邀追
ui->追 ,5.贼缷邀追
ou->怄 ,6.怄您眠
in->您 ,6.怄您眠
ian->眠 .6.怄您眠
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
print("秋娃丫娥远观月 域外舒驰噢卧云昆")
print("阿勇送，汪洋分 更航岸靠来")
print("贼缷邀追 怄您眠")

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
