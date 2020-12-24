#!/usr/bin/python
# -*- coding: utf-8 -*-

# 4个bytes 合成一个小段 Dword
def Bytes_to_Dword(byarray):
    a=byarray[3]
    b=byarray[2]
    c=byarray[1]
    d=byarray[0]
    Dw= (a<<24)|(b<<16)|(c<<8)|d
    return Dw
def Bytes_to_word(byarray):
    c=byarray[1]
    d=byarray[0]
    wd= (c<<8)|d
    return wd


def get_file_rva_dword(fp,rva,size=0x4):
    fp.seek(rva,0)
    arg1 = fp.read(0x4)
    arg1_bytes = bytearray(arg1)
    arg1_dword = Bytes_to_Dword(arg1_bytes)  # 转成DWORD
    return  arg1_dword

def get_file_rva_word(fp,rva,size=0x2):
    fp.seek(rva, 0)
    arg1 = fp.read(0x2)
    arg1_bytes = bytearray(arg1)
    arg1_word = Bytes_to_word(arg1_bytes)  # 转成DWORD
    return arg1_word
