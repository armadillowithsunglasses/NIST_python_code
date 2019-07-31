
from nltk.translate.nist_score import sentence_nist
import xlrd

# Give the location of the file
#if sheet.cell_value(i,0)==0:
#   score= str(sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))+ ','+ str(sentence_bleu(reference, candidate, weights=(0, 1, 0, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0, 0, 1, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0, 0, 0, 1)))+','+ str(sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25)))+',Human-generated' '''''' else:
#       score= str(sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))+ ','+ str(sentence_bleu(reference, candidate, weights=(0, 1, 0, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0, 0, 1, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0, 0, 0, 1)))+','+ str(sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))+','+ str(sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25)))+',Machine-generated' '''

loc = ("/Users/ishitagupta/Desktop/kashgari_data.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(2)
i=0
for i in range(1,4):
    textreference = str(sheet.cell_value(i, 0))
    textcandidate = str(sheet.cell_value(i, 1))
    print(textreference.split())
    print(textcandidate.split())
    
    reference = [textreference.split()]
    candidate = textcandidate.split()
    if len(candidate) == 1 :
       score= 1.0
       print(round(100*score))
    else:
       score= str(round(100*sentence_nist(reference, candidate, 2)))
       print(score)






