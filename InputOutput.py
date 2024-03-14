#!/usr/bin/env python
# coding: utf-8

# Nilai statis dan dinamis

# In[1]:


bil1 = input('isikan bilangan 1:')
bil2 = input('isikan bilangan 2:')
hasil = int(bil1) + int(bil2)
print("Hasil ", bil1, "+", bil2,"=",hasil)


# buatlah luas dan keliling persegi panjang

# In[3]:


panjang = input ("Masukan nilai panjang :")
lebar = input ("Masukan nilai lebar :")

luas = int(panjang) * int(lebar)
keliling = 2 * (int(panjang) * int(lebar))

print("luas", luas)
print("keliling", keliling)


# In[4]:


print("A","B","C","D", sep='@_@') #sep=seperator atau pembatas


# In[5]:


print("A","B","C","D", sep='\n', end="^_^") 


# format index

# In[6]:


num_1 = 8
num_2 = 10

# Hasil dari 8 modulus 10 = 8
#str.format()

print('Hasil dari {} modulus {} = {}'. format(num_1,num_2,num_1%num_2))


# In[9]:


fname = "Sabella"
mname = "Aufa"
lname = "Syahda"

print('Nama anda {0} {1} {2}'.format(fname,mname,lname))


# In[12]:


print('Nama anda {nama}, nilai anda{nilai}'.format(nama='sabella',nilai=85))


# In[13]:


univ = "Universitas Nusa Putra"

print("karakter pertama : ",univ[0])
print("karakter terakhir: ",univ[-1])
#Universitas
print(univ[0:11])
print(univ[-5:])
print(univ[17:])
print(univ[::-1])


# f string

# In[15]:


f_name = 'Rachmatu'
l_name = 'fauzia'

print(f'Nama saya {f_name} {l_name}')

first = 100
second = 30

print(f'Hasil penjumlahan {first} + {second} = {first+second}')


# split pada string

# In[3]:


nama = "Zilah,Rara,Alya"
nama2 = "Zilah,,Rara,Alya"

print(nama2.split())
print(nama.split(','))

print('@'.join(nama.split(',')))

#input tgl lahir-> 01/juni/2003
#input nama -> Sabella Aufa
#output
#Tgl : 01, Bulan:juni, Tahun :2003
#Nama Inisial : SA

tgl = input ("Masukan tanggal : ")
nama = input ("Masukan nama : ")

pemisah = tgl.split("/")
print(f"tgl : {pemisah[0]}, Bulan :{pemisah[1]}, Tahun :{pemisah[2]}")
pemisah2 = nama.split()
nama_pertama = pemisah2[0]
nama_terakhir = pemisah2[1]
print(f"Nama inisial : {nama_pertama[0]+nama_terakhir[0]}")
      


# In[ ]:





# In[ ]:




