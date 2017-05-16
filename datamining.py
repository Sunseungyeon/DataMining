# _*_ coding: utf-8 _*_
import sys
import operator
from operator import itemgetter
infile01 = open("HKIB-20000_001.txt", 'r')
infile02 = open("HKIB-20000_002.txt", 'r')
infile03 = open("HKIB-20000_003.txt", 'r')
infile04 = open("HKIB-20000_004.txt", 'r')
infile05 = open("HKIB-20000_005.txt", 'r')

ca0 = []
ca1 = []
ca2 = []
ca3 = []
ca4 = []
ca5 = []
ca6 = []
ca7 = []
doc = []
all = []

dic0 = dict()
dic1 = dict()
dic2 = dict()
dic3 = dict()
dic4 = dict()
dic5 = dict()
dic6 = dict()
dic7 = dict()

testca0 = []
testca1 = []
testca2 = []
testca3 = []
testca4 = []
testca5 = []
testca6 = []
testca7 = []
testdoc = []
testall = []

cnt = []
cnt = [0 for _ in range(8)]

def defsplit(data): #function of document devide by token
    j1 = data.replace('"', ' ').replace('\n', ' ').replace('<', ' ').replace('>', ' ').replace('{', ' ')
    j2 = j1.replace('}', ' ').replace('[', ' ').replace(']', ' ').replace('-', ' ').replace('.', ' ')
    j3 = j2.replace(',', ' ').replace('<KW>', ' ').replace('(', ' ').replace(')', ' ').split(' ')
    j4 = list(set(j3))
    return j4

def splitWord(data): #function of call split func. and features stored each category
    data1 = data.split('@DOCUMENT')
    data1.pop(0)
    for i in data1:
        i = i.split('#')
        if i[2].find('건강과 의학') > 0:
            cnt[0] = cnt[0] + 1
            j = i[5].split(":")
            if j.__len__() > 1:  # TEXT만 존재하는 경우가 발생하여 본문 내용이 있을경우만 저장
                spl = defsplit(j[1])
                doc = []
                for k in spl:
                    if k == '':
                        continue
                    all.append(k)
                    doc.append(k)
                    if k in dic0:
                        dic0[k] = dic0[k] + 1
                    else:
                        dic0[k] = 1
                ca0.append(doc)
        elif i[2].find('경제') > 0:
            cnt[1] = cnt[1] + 1
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                doc = []
                for k in spl:
                    if k == '':
                        continue
                    all.append(k)
                    doc.append(k)
                    if k in dic1:
                        dic1[k] = dic1[k] + 1
                    else:
                        dic1[k] = 1
                ca1.append(doc)
        elif i[2].find('과학') > 0:
            cnt[2] = cnt[2] + 1
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                doc = []
                for k in spl:
                    if k == '':
                        continue
                    all.append(k)
                    doc.append(k)
                    if k in dic2:
                        dic2[k] = dic2[k] + 1
                    else:
                        dic2[k] = 1
                ca2.append(doc)
        elif i[2].find('교육') > 0:
            cnt[3] = cnt[3] + 1
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                doc = []
                for k in spl:
                    if k == '':
                        continue
                    all.append(k)
                    doc.append(k)
                    if k in dic3:
                        dic3[k] = dic3[k] + 1
                    else:
                        dic3[k] = 1
                ca3.append(doc)
        elif i[2].find('문화와 종교') > 0:
            cnt[4] = cnt[4] + 1
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                doc = []
                for k in spl:
                    if k == '':
                        continue
                    all.append(k)
                    doc.append(k)
                    if k in dic4:
                        dic4[k] = dic4[k] + 1
                    else:
                        dic4[k] = 1
                ca4.append(doc)
        elif i[2].find('사회') > 0:
            cnt[5] = cnt[5] + 1
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                doc = []
                for k in spl:
                    if k == '':
                        continue
                    all.append(k)
                    doc.append(k)
                    if k in dic5:
                        dic5[k] = dic5[k] + 1
                    else:
                        dic5[k] = 1
                ca5.append(doc)
        elif i[2].find('산업') > 0:
            cnt[6] = cnt[6] + 1
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                doc = []
                for k in spl:
                    if k == '':
                        continue
                    all.append(k)
                    doc.append(k)
                    if k in dic6:
                        dic6[k] = dic6[k] + 1
                    else:
                        dic6[k] = 1
                ca6.append(doc)
        elif i[2].find('여가생활') > 0:
            cnt[7] = cnt[7] + 1
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                doc = []
                for k in spl:
                    if k == '':
                        continue
                    all.append(k)
                    doc.append(k)
                    if k in dic7:
                        dic7[k] = dic7[k] + 1
                    else:
                        dic7[k] = 1
                ca7.append(doc)

def Testsplit(data): #same function splitWord. Collect only the elements you need when you test.
    data1 = data.split('@DOCUMENT')
    data1.pop(0)
    for i in data1:
        i = i.split('#')
        if i[2].find('건강과 의학') > 0:
            j = i[5].split(":")
            if j.__len__() > 1:  # Only when TEXT exists, it is saved only when there is contents of text
                spl = defsplit(j[1])
                spl.remove('')
                testca0.append(spl)
        elif i[2].find('경제') > 0:
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                spl.remove('')
                testca1.append(spl)
        elif i[2].find('과학') > 0:
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                spl.remove('')
                testca2.append(spl)
        elif i[2].find('교육') > 0:
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                spl.remove('')
                testca3.append(spl)
        elif i[2].find('문화와 종교') > 0:
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                spl.remove('')
                testca4.append(spl)
        elif i[2].find('사회') > 0:
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                spl.remove('')
                testca5.append(spl)
        elif i[2].find('산업') > 0:
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                spl.remove('')
                testca6.append(spl)
        elif i[2].find('여가생활') > 0:
            j = i[5].split(":")
            if j.__len__() > 1:
                spl = defsplit(j[1])
                spl.remove('')
                testca7.append(spl)

#training
splitWord(infile01.read())
splitWord(infile02.read())
splitWord(infile03.read())
splitWord(infile04.read())

a = []
b = []
c = []
d = []
idx = dict()

cntSum = cnt[0] + cnt[1] + cnt[2] + cnt[3] + cnt[4] + cnt[5] + cnt[6] + cnt[7] #Each cnt has been saved by eliminating duplication by category

for i in all: #calculate chi-square values
    max_chi = 0
    a = [0 for _ in range(8)]
    b = [0 for _ in range(8)]
    c = [0 for _ in range(8)]
    d = [0 for _ in range(8)]
    for j in range(0, 8):
        if j == 0:
            if i in dic0:
                a[j] = dic0.get(i)
            if i in dic1:
                c[j] = c[j] + dic1.get(i)
            if i in dic2:
                c[j] = c[j] + dic2.get(i)
            if i in dic3:
                c[j] = c[j] + dic3.get(i)
            if i in dic4:
                c[j] = c[j] + dic4.get(i)
            if i in dic5:
                c[j] = c[j] + dic5.get(i)
            if i in dic6:
                c[j] = c[j] + dic6.get(i)
            if i in dic7:
                c[j] = c[j] + dic7.get(i)
            b[j] = cnt[0] - a[j]
            d[0] = (cnt[1]+cnt[2]+cnt[3]+cnt[4]+cnt[5]+cnt[6]+cnt[7]) - c[0]

            chi = (cntSum * ((a[j]*d[j])-(c[j]*b[j]))*((a[j]*d[j])-(c[j]*b[j])))
            chi = chi / float(((a[j] + c[j]) * (b[j] + d[j]) * (a[j] + b[j]) * (c[j] + d[j])))
        if j == 1:
            if i in dic1:
                a[j] = dic1.get(i)
            if i in dic0:
                c[j] = c[j] + dic0.get(i)
            if i in dic2:
                c[j] = c[j] + dic2.get(i)
            if i in dic3:
                c[j] = c[j] + dic3.get(i)
            if i in dic4:
                c[j] = c[j] + dic4.get(i)
            if i in dic5:
                c[j] = c[j] + dic5.get(i)
            if i in dic6:
                c[j] = c[j] + dic6.get(i)
            if i in dic7:
                c[j] = c[j] + dic7.get(i)
            b[j] = cnt[1] - a[j]
            d[1] = (cnt[0] + cnt[2] + cnt[3] + cnt[4] + cnt[5] + cnt[6] + cnt[7]) - c[1]
            chi = (cntSum * ((a[j] * d[j]) - (c[j] * b[j])) * ((a[j] * d[j]) - (c[j] * b[j])))
            chi = chi / float(((a[j] + c[j]) * (b[j] + d[j]) * (a[j] + b[j]) * (c[j] + d[j])))
        if j == 2:
            if i in dic2:
                a[j] = dic2.get(i)
            if i in dic0:
                c[j] = c[j] + dic0.get(i)
            if i in dic1:
                c[j] = c[j] + dic1.get(i)
            if i in dic3:
                c[j] = c[j] + dic3.get(i)
            if i in dic4:
                c[j] = c[j] + dic4.get(i)
            if i in dic5:
                c[j] = c[j] + dic5.get(i)
            if i in dic6:
                c[j] = c[j] + dic6.get(i)
            if i in dic7:
                c[j] = c[j] + dic7.get(i)
            b[j] = cnt[2] - a[j]
            d[2] = (cnt[0] + cnt[1] + cnt[3] + cnt[4] + cnt[5] + cnt[6] + cnt[7]) - c[2]
            chi = (cntSum * ((a[j] * d[j]) - (c[j] * b[j])) * ((a[j] * d[j]) - (c[j] * b[j])))
            chi = chi / float(((a[j] + c[j]) * (b[j] + d[j]) * (a[j] + b[j]) * (c[j] + d[j])))
        if j == 3:
            if i in dic3:
                a[j] = dic3.get(i)
            if i in dic0:
                c[j] = c[j] + dic0.get(i)
            if i in dic2:
                c[j] = c[j] + dic2.get(i)
            if i in dic1:
                c[j] = c[j] + dic1.get(i)
            if i in dic4:
                c[j] = c[j] + dic4.get(i)
            if i in dic5:
                c[j] = c[j] + dic5.get(i)
            if i in dic6:
                c[j] = c[j] + dic6.get(i)
            if i in dic7:
                c[j] = c[j] + dic7.get(i)
            b[j] = cnt[3] - a[j]
            d[3] = (cnt[0] + cnt[2] + cnt[1] + cnt[4] + cnt[5] + cnt[6] + cnt[7]) - c[3]
            chi = (cntSum * ((a[j] * d[j]) - (c[j] * b[j])) * ((a[j] * d[j]) - (c[j] * b[j])))
            chi = chi / float(((a[j] + c[j]) * (b[j] + d[j]) * (a[j] + b[j]) * (c[j] + d[j])))
        if j == 4:
            if i in dic4:
                a[j] = dic4.get(i)
            if i in dic0:
                c[j] = c[j] + dic0.get(i)
            if i in dic2:
                c[j] = c[j] + dic2.get(i)
            if i in dic3:
                c[j] = c[j] + dic3.get(i)
            if i in dic1:
                c[j] = c[j] + dic1.get(i)
            if i in dic5:
                c[j] = c[j] + dic5.get(i)
            if i in dic6:
                c[j] = c[j] + dic6.get(i)
            if i in dic7:
                c[j] = c[j] + dic7.get(i)
            b[j] = cnt[4] - a[j]
            d[4] = (cnt[0] + cnt[2] + cnt[3] + cnt[1] + cnt[5] + cnt[6] + cnt[7]) - c[4]
            chi = (cntSum * ((a[j] * d[j]) - (c[j] * b[j])) * ((a[j] * d[j]) - (c[j] * b[j])))
            chi = chi / float(((a[j] + c[j]) * (b[j] + d[j]) * (a[j] + b[j]) * (c[j] + d[j])))
        if j == 5:
            if i in dic5:
                a[j] = dic5.get(i)
            if i in dic0:
                c[j] = c[j] + dic0.get(i)
            if i in dic2:
                c[j] = c[j] + dic2.get(i)
            if i in dic3:
                c[j] = c[j] + dic3.get(i)
            if i in dic4:
                c[j] = c[j] + dic4.get(i)
            if i in dic1:
                c[j] = c[j] + dic1.get(i)
            if i in dic6:
                c[j] = c[j] + dic6.get(i)
            if i in dic7:
                c[j] = c[j] + dic7.get(i)
            b[j] = cnt[5] - a[j]
            d[5] = (cnt[0] + cnt[2] + cnt[3] + cnt[4] + cnt[1] + cnt[6] + cnt[7]) - c[5]
            chi = (cntSum * ((a[j] * d[j]) - (c[j] * b[j])) * ((a[j] * d[j]) - (c[j] * b[j])))
            chi = chi / float(((a[j] + c[j]) * (b[j] + d[j]) * (a[j] + b[j]) * (c[j] + d[j])))
        if j == 6:
            if i in dic6:
                a[j] = dic6.get(i)
            if i in dic0:
                c[j] = c[j] + dic0.get(i)
            if i in dic2:
                c[j] = c[j] + dic2.get(i)
            if i in dic3:
                c[j] = c[j] + dic3.get(i)
            if i in dic4:
                c[j] = c[j] + dic4.get(i)
            if i in dic5:
                c[j] = c[j] + dic5.get(i)
            if i in dic1:
                c[j] = c[j] + dic1.get(i)
            if i in dic7:
                c[j] = c[j] + dic7.get(i)
            b[j] = cnt[6] - a[j]
            d[6] = (cnt[0] + cnt[2] + cnt[3] + cnt[4] + cnt[5] + cnt[1] + cnt[7]) - c[6]
            chi = (cntSum * ((a[j] * d[j]) - (c[j] * b[j])) * ((a[j] * d[j]) - (c[j] * b[j])))
            chi = chi / float(((a[j] + c[j]) * (b[j] + d[j]) * (a[j] + b[j]) * (c[j] + d[j])))
        if j == 7:
            if i in dic7:
                a[j] = dic7.get(i)
            if i in dic0:
                c[j] = c[j] + dic0.get(i)
            if i in dic2:
                c[j] = c[j] + dic2.get(i)
            if i in dic3:
                c[j] = c[j] + dic3.get(i)
            if i in dic4:
                c[j] = c[j] + dic4.get(i)
            if i in dic5:
                c[j] = c[j] + dic5.get(i)
            if i in dic6:
                c[j] = c[j] + dic6.get(i)
            if i in dic1:
                c[j] = c[j] + dic1.get(i)
            b[j] = cnt[7] - a[j]
            d[7] = (cnt[0] + cnt[2] + cnt[3] + cnt[4] + cnt[5] + cnt[6] + cnt[1]) - c[7]
            chi = (cntSum * ((a[j] * d[j]) - (c[j] * b[j])) * ((a[j] * d[j]) - (c[j] * b[j])))
            chi = chi / float(((a[j] + c[j])*(b[j] + d[j]) * (a[j] + b[j]) * (c[j] + d[j])))
        if max_chi < chi:
            max_chi = chi
    idx[i] = max_chi

L = dict() #sorting by descending order. Have pairs of feature and the feature's chi-square value
L.update(sorted(idx.items(), key=itemgetter(1), reverse=True))

L_idx = dict()

count = 1
for k, v in L.items(): #stored pairs of feature and the feature's index by chi-square value
    L_idx[k] = count
    count = count + 1

train = open('train.txt', 'wt')

total = []
total.append(ca0)
total.append(ca1)
total.append(ca2)
total.append(ca3)
total.append(ca4)
total.append(ca5)
total.append(ca6)
total.append(ca7)


c = 0
for ca in total: #Save to a text file in a format that fits the form
    c = c + 1
    for li in ca:
        txt = ''
        train_temp = dict()
        train_temp1 = dict()
        for word in li:
            train_temp[L_idx[word]] = L[word]
        train_temp1.update(sorted(train_temp.items(), key=itemgetter(0)))
        txt = str(c) + " "
        for i, j in train_temp1.items():
            txt = txt + str(i) + ":" + str(j) + " "
        txt = txt + "\n"
        train.write(txt)

#testing
test = open('test2.txt', 'wt')

Testsplit(infile05.read()) #call split function

total_test = []
total_test.append(testca0)
total_test.append(testca1)
total_test.append(testca2)
total_test.append(testca3)
total_test.append(testca4)
total_test.append(testca5)
total_test.append(testca6)
total_test.append(testca7)

c = 0
for ca in total_test: #Save to a text file in a format that fits the form
    c = c + 1
    for li in ca:
        txt = ''
        test_temp = dict()
        test_temp1 = dict()
        for word in li:
            if word in L_idx:
                test_temp[L_idx[word]] = L[word]
            else:
                continue
        test_temp1.update(sorted(test_temp.items(), key=itemgetter(0)))
        txt = str(c) + " "
        for i, j in test_temp1.items():
            txt = txt + str(i) + ":" + str(j) + " "
        txt = txt + "\n"
        test.write(txt)

infile01.close()
infile02.close()
infile03.close()
infile04.close()
train.close()
test.close()