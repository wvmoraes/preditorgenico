import os
#leitura do arquivo do organismo


path = 'Dados/GCF_000005845.2_ASM584v2_genomic.fna'
#path = 'Dados/teste.fna'
genoma  = open(path)
genomaInfo = os.stat(path)
sequencias = genoma.read()

print("------------------Genoma------------------")
print(sequencias)

#Contagem de nucleotídeos
g = sequencias.count("G")
c = sequencias.count("C")
t = sequencias.count("T")
a = sequencias.count("A")

#pares de base e conteúdo GC
bp = a+t+g+c
gc = (g + c) /(bp)

# Contagem de Start Codon ATG e StopCodon TAG
print("\n")
print("------------------Relatório------------------")
print("Tamanho do arquivo: ", genomaInfo.st_size, "bytes")
print("Guanina:",g)
print("Citosina:",c)
print("Timina:",  t)
print("Adenina:", a)

print("BP: ", bp)
print("% GC: ", gc, "\n")

print("------------------ Start Códons------------------")
print("ATG:", sequencias.count('ATG'))

print("\n")
print("------------------ Stop Códons-------------------")
print("TAG: " , sequencias.count('TAG'))
print("UAG: " , sequencias.count('UAG'))
print("TAA: " , sequencias.count('TAA'))
print("UAA: " , sequencias.count('UAA'))
print("TGA: " , sequencias.count('TGA'))


