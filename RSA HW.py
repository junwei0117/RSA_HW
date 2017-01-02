#!/usr/bin/python
#coding=utf-8

from fractions import gcd
import sys
def wordCount(text):
  count = sum(map(lambda s: len(s.split()), text))
  return count

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def plain_texttonum(plain_text):
    m2 = plain_text
    m22 = m2.upper()
    m3 = list(m22)
    if wordCount(m2)%2!=0:
        m3.append("[")
    m4 = []
    i = 0
    for x in m3:
        spacea = ['[']
        forspace = 0
        o = i+1
        if m3[i]==' ':
            m4.append("26")
            i = i + 1
        if m3[i]!=' ' and m3[o]==' ':
            aaa = ord(m3[i])-65
            bbb = "%02d"%aaa
            i = i + 1
            ccc = str(bbb)+str("26")
            m4.append(ccc)
        if m3[i]!=' ' and m3[o]!=' ':
            a = ord(m3[i])-65
            b = "%02d"%a
            i = i + 1
            if m3[i] == " ":
                aa = ord(m3[i])-6
            else:
                aa = ord(m3[i])-65
            bb = "%02d"%aa
            i = i + 1
            cc = str(b)+str(bb)
            m4.append(cc)

        if i > len(m3)-1:
            break
    return m4



#輸入p,q
print "此程式能支援長整數運算"
p = input('p = ')
q = input('q = ')

#計算n
n = p * q

print "n = " + str(n)

#輸入e
e = int(raw_input('e = '))


# 計算n的歐拉函數 φ(n)
phi = (p - 1) * (q - 1)

#計算d
d = modinv( e, phi )

print "d = " + str(d)

#輸入paln text
plain_text = raw_input('plan text = ')
print " "
M = plain_texttonum(plain_text)

#M(原文)
showm = ' '.join(M)
print "original M =" + str(M)
print "M = " + str(showm)
print " "

#C(加密後的)
C = []
y = 0
for x in M:
    plain = int(M[y])
    Clist = str(pow(plain, e, n ))
    C.append(Clist)
    y = y + 1
    if y > len(M):
        break
showc = ' '.join(C)
print "C = " + str(showc)
print " "

#After coding(解密)
After_coding = []
yy = 0
for x in C:
    cc = int(C[yy])
    After_codinglist = str(pow( cc, d, n))
    After_coding.append(After_codinglist)
    yy = yy + 1
    if yy > len(C):
        break

showAfter_coding = ' '.join(After_coding)
print "After coding: "
print " "
print str(showAfter_coding)
