#!/usr/bin/env python3
import sys
import re
import os
import pandas as pd


PYTHONIOENCODING="UTF-8"


pathh = sys.argv[1]
phone1 = re.compile(r"\s(?P<phone>\(\d{3}\)\s\d{3}\-\d{4})")
phone2 = re.compile(r"\s(?P<phone>\(\d{3}\)\s\d{7})")
phone3 = re.compile(r"\s(?P<phone>\d{3}\-\d{3}\-\d{4})")
email1 = re.compile(r"Sender\:\s(?P<email_address>\w.+\@\w+\.\w+)\s")
email2 = re.compile(r"\s\<(?P<email_address>\w+\@\w+\.\w+)\s")
email3 = re.compile(r"\n[^Sender](?P<email_address>\w.+\@\w+\.\w+)\s")
cc1 = re.compile(r"\s(?P<cc1>\d{16})")
cc2 = re.compile(r"\s(?P<cc2>\d{4}\s\d{4}\s\d{4}\s\d{4})")
ssn1 = re.compile(r"(?P<SSN>\d{3}\-\d{2}\-\d{4})")
ssn2 = re.compile(r"(?P<SSN>\d{9})")
cardsDF = pd.DataFrame(columns=['File', 'CC_Number'])
phonesDF = pd.DataFrame(columns=['File', 'Phone_Number'])
emailsDF = pd.DataFrame(columns=['File', 'Email_Address'])
ssnDF = pd.DataFrame(columns=['File', 'SSN'])


filly = open('files.txt', 'w+')
fillie = str(os.listdir(pathh))
filer = re.compile(r"(?P<filename>\S+\.eml)")
f1 = filer.findall(str(fillie))
f2 = re.sub('[\[\]\'\"\,]', '', str(f1))
f3 = re.sub('[\s]', '\n', f2)
filly.write(str(f3))
filly.close()


with open('files.txt', 'r') as fileNames:
	for fileName in fileNames:
		fileName = fileName.strip()
		with open(pathh + fileName, 'r') as searchFile:
			searchableData = searchFile.read().replace('\n', ' ')
			cardsDataFormat1 = cc1.findall(searchableData)
			cardsDataFormat2 = cc2.findall(searchableData)
			if cardsDataFormat1:
				print("CardFormatData1:", cardDataFormat1)
				cardsDF = cardsDF.append({'File': fileName, 'CC_Number': cardsDataFormat1}, ignore_index=True, sort=True)
			if cardsDataFormat2:
				cardsDF = cardsDF.append({'File': fileName, 'CC_Number': cardsDataFormat2}, ignore_index=True, sort=True)
			phonesDataFormat1 = phone1.findall(searchableData)
			phonesDataFormat2 = phone2.findall(searchableData)
			phonesDataFormat3 = phone3.findall(searchableData)
			if phonesDataFormat1:
				phonesDF = phonesDF.append({'File': fileName, 'Phone_Number': phonesDataFormat1}, ignore_index=True, sort=True)
			if phonesDataFormat2:
				phonesDF = phonesDF.append({'File': fileName, 'Phone_Number': phonesDataFormat2}, ignore_index=True, sort=True)
			if phonesDataFormat3:
				phonesDF = phonesDF.append({'File': fileName, 'Phone_Number': phonesDataFormat3}, ignore_index=True, sort=True)
			emailsDataFormat1 = email1.findall(searchableData)
			emailsDataFormat2 = email2.findall(searchableData)
			emailsDataFormat3 = email3.findall(searchableData)
			if emailsDataFormat1:
				emailsDF = emailsDF.append({'File': fileName, 'Email_Address': emailsDataFormat1}, ignore_index=True, sort=True)
			if emailsDataFormat2:
				emailsDF = emailsDF.append({'File': fileName, 'Email_Address': emailsDataFormat1}, ignore_index=True, sort=True)
			if emailsDataFormat3:
				emailsDF = emailsDF.append({'File': fileName, 'Email_Address': emailsDataFormat1}, ignore_index=True, sort=True)
			ssnDataFormat1 = ssn1.findall(searchableData)
			ssnDataFormat2 = ssn2.findall(searchableData)
			if ssnDataFormat1:
				ssnDF = ssnDF.append({'File': fileName, 'SSN': ssnDataFormat1}, ignore_index=True, sort=True)
			if ssnDataFormat2:
				ssnDF = ssnDF.append({'File': fileName, 'SSN': ssnDataFormat1}, ignore_index=True, sort=True)


#cardsDF = cardsDF.drop_duplicates(subset=['CC_Number'])
#phonesDF = phonesDF.drop_duplicates(subset=['Phone_Number'])
#emailsDF = emailsDF.drop_duplicates(subset=['Email_Address'])
#ssnDF = ssnDF.drop_duplicates(subset=['CSSN'])

cardsDF.to_csv('cards.csv')
phonesDF.to_csv('phones.csv')
emailsDF.to_csv('emails.csv')
ssnDF.to_csv('SSNs.csv')

