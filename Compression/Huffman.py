import heapq
import os
from collections import defaultdict

def frekans_hesapla(metin):
    frekans = defaultdict(int)
    for karakter in metin:
        frekans[karakter] += 1
    return frekans


def heap_olustur(freq):
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    return heap


def agac_olustur(heap):
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]


def Huffman_Kodu(tree):
    huff_kod = {}
    for pair in tree[1:]:
        char = pair[0]
        code = pair[1]
        huff_kod[char] = code
    return huff_kod

metinGirisi = 'MISSISSIPPI RIVER'
frq = frekans_hesapla(metinGirisi)
print('Frekanslar', frq)

hp = heap_olustur(frq)
print('\nHeap:', hp)

agac = agac_olustur(hp)
print('\nAgac:', agac)

huffman = Huffman_Kodu(agac)
print('\nHuffman:', huffman)
