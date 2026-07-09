# -*- coding: utf-8 -*-
"""
Created 5/19, 2023

Use NVSS Mortality Data + Census Vintage 2020 Extrap + restricted-access US 2020 Vintage Population Data + 2020 LT
Simulate 50K life tables with random uncertainty on qx and ax
Estimate mx for five age groups

@author: ryan masters


"""
#import packages
import random

# importing in the qx and error and ax
male_t = r"/Users/ryan/Documents/Papers/life table technique/simulation/male_2020.txt"
# change as needed for input files

# read in the file
textFile = open(male_t,'r')
text = textFile.readlines()
# split into different age categories
a0=text[1]
a1=text[2]
a5=text[3]
a10=text[4]
a15=text[5]
a20=text[6]
a25=text[7]
a30=text[8]
a35=text[9]
a40=text[10]
a45=text[11]
a50=text[12]
a55=text[13]
a60=text[14]
a65=text[15]
a70=text[16]
a75=text[17]
a80=text[18]
a85=text[19]
a90=text[20]
a95=text[21]
a100=text[22]


a0_sp = a0.split(",")
a1_sp = a1.split(",")
a5_sp = a5.split(",")
a10_sp = a10.split(",")
a15_sp = a15.split(",")
a20_sp = a20.split(",")
a25_sp = a25.split(",")
a30_sp = a30.split(",")
a35_sp = a35.split(",")
a40_sp = a40.split(",")
a45_sp = a45.split(",")
a50_sp = a50.split(",")
a55_sp = a55.split(",")
a60_sp = a60.split(",")
a65_sp = a65.split(",")
a70_sp = a70.split(",")
a75_sp = a75.split(",")
a80_sp = a80.split(",")
a85_sp = a85.split(",")
a90_sp = a90.split(",")
a95_sp = a95.split(",")
a100_sp = a100.split(",")

# qx
a0_qx = float(a0_sp[1])
a1_qx = float(a1_sp[1])
a5_qx = float(a5_sp[1])
a10_qx = float(a10_sp[1])
a15_qx = float(a15_sp[1])
a20_qx = float(a20_sp[1])
a25_qx = float(a25_sp[1])
a30_qx = float(a30_sp[1])
a35_qx = float(a35_sp[1])
a40_qx = float(a40_sp[1])
a45_qx = float(a45_sp[1])
a50_qx = float(a50_sp[1])
a55_qx = float(a55_sp[1])
a60_qx = float(a60_sp[1])
a65_qx = float(a65_sp[1])
a70_qx = float(a70_sp[1])
a75_qx = float(a75_sp[1])
a80_qx = float(a80_sp[1])
a85_qx = float(a85_sp[1])
a90_qx = float(a90_sp[1])
a95_qx = float(a95_sp[1])
a100_qx = float(a100_sp[1])

# qx - lower bound
a0_qxl = float(a0_sp[2])
a1_qxl = float(a1_sp[2])
a5_qxl = float(a5_sp[2])
a10_qxl = float(a10_sp[2])
a15_qxl = float(a15_sp[2])
a20_qxl = float(a20_sp[2])
a25_qxl = float(a25_sp[2])
a30_qxl = float(a30_sp[2])
a35_qxl = float(a35_sp[2])
a40_qxl = float(a40_sp[2])
a45_qxl = float(a45_sp[2])
a50_qxl = float(a50_sp[2])
a55_qxl = float(a55_sp[2])
a60_qxl = float(a60_sp[2])
a65_qxl = float(a65_sp[2])
a70_qxl = float(a70_sp[2])
a75_qxl = float(a75_sp[2])
a80_qxl = float(a80_sp[2])
a85_qxl = float(a85_sp[2])
a90_qxl = float(a90_sp[2])
a95_qxl = float(a95_sp[2])
a100_qxl = float(a100_sp[2])

# qx - Upper bound
a0_qxu = float(a0_sp[3])
a1_qxu = float(a1_sp[3])
a5_qxu = float(a5_sp[3])
a10_qxu = float(a10_sp[3])
a15_qxu = float(a15_sp[3])
a20_qxu = float(a20_sp[3])
a25_qxu = float(a25_sp[3])
a30_qxu = float(a30_sp[3])
a35_qxu = float(a35_sp[3])
a40_qxu = float(a40_sp[3])
a45_qxu = float(a45_sp[3])
a50_qxu = float(a50_sp[3])
a55_qxu = float(a55_sp[3])
a60_qxu = float(a60_sp[3])
a65_qxu = float(a65_sp[3])
a70_qxu = float(a70_sp[3])
a75_qxu = float(a75_sp[3])
a80_qxu = float(a80_sp[3])
a85_qxu = float(a85_sp[3])
a90_qxu = float(a90_sp[3])
a95_qxu = float(a95_sp[3])
a100_qxu = float(a100_sp[3])


# ax
a0_ax = float(a0_sp[4])
a1_ax = float(a1_sp[4])
a5_ax = float(a5_sp[4])
a10_ax = float(a10_sp[4])
a15_ax = float(a15_sp[4])
a20_ax = float(a20_sp[4])
a25_ax = float(a25_sp[4])
a30_ax = float(a30_sp[4])
a35_ax = float(a35_sp[4])
a40_ax = float(a40_sp[4])
a45_ax = float(a45_sp[4])
a50_ax = float(a50_sp[4])
a55_ax = float(a55_sp[4])
a60_ax = float(a60_sp[4])
a65_ax = float(a65_sp[4])
a70_ax = float(a70_sp[4])
a75_ax = float(a75_sp[4])
a80_ax = float(a80_sp[4])
a85_ax = float(a85_sp[4])
a90_ax = float(a90_sp[4])
a95_ax = float(a95_sp[4])
a100_ax = float(a100_sp[4])


# ax - LB
a0_axl = float(a0_sp[5])
a1_axl = float(a1_sp[5])
a5_axl = float(a5_sp[5])
a10_axl = float(a10_sp[5])
a15_axl = float(a15_sp[5])
a20_axl = float(a20_sp[5])
a25_axl = float(a25_sp[5])
a30_axl = float(a30_sp[5])
a35_axl = float(a35_sp[5])
a40_axl = float(a40_sp[5])
a45_axl = float(a45_sp[5])
a50_axl = float(a50_sp[5])
a55_axl = float(a55_sp[5])
a60_axl = float(a60_sp[5])
a65_axl = float(a65_sp[5])
a70_axl = float(a70_sp[5])
a75_axl = float(a75_sp[5])
a80_axl = float(a80_sp[5])
a85_axl = float(a85_sp[5])
a90_axl = float(a90_sp[5])
a95_axl = float(a95_sp[5])
a100_axl = float(a100_sp[5])


# ax - UB
a0_axu = float(a0_sp[6])
a1_axu = float(a1_sp[6])
a5_axu = float(a5_sp[6])
a10_axu = float(a10_sp[6])
a15_axu = float(a15_sp[6])
a20_axu = float(a20_sp[6])
a25_axu = float(a25_sp[6])
a30_axu = float(a30_sp[6])
a35_axu = float(a35_sp[6])
a40_axu = float(a40_sp[6])
a45_axu = float(a45_sp[6])
a50_axu = float(a50_sp[6])
a55_axu = float(a55_sp[6])
a60_axu = float(a60_sp[6])
a65_axu = float(a65_sp[6])
a70_axu = float(a70_sp[6])
a75_axu = float(a75_sp[6])
a80_axu = float(a80_sp[6])
a85_axu = float(a85_sp[6])
a90_axu = float(a90_sp[6])
a95_axu = float(a95_sp[6])
a100_axu = float(a100_sp[6])

# 2019 mx - 2019 LT
a0_m19 = float(a0_sp[7])
a1_m19 = float(a1_sp[7])
a5_m19 = float(a5_sp[7])
a10_m19 = float(a10_sp[7])
a15_m19 = float(a15_sp[7])
a20_m19 = float(a20_sp[7])
a25_m19 = float(a25_sp[7])
a30_m19 = float(a30_sp[7])
a35_m19 = float(a35_sp[7])
a40_m19 = float(a40_sp[7])
a45_m19 = float(a45_sp[7])
a50_m19 = float(a50_sp[7])
a55_m19 = float(a55_sp[7])
a60_m19 = float(a60_sp[7])
a65_m19 = float(a65_sp[7])
a70_m19 = float(a70_sp[7])
a75_m19 = float(a75_sp[7])
a80_m19 = float(a80_sp[7])
a85_m19 = float(a85_sp[7])
a90_m19 = float(a90_sp[7])
a95_m19 = float(a95_sp[7])
a100_m19 = float(a100_sp[7])


count = 0
while count < 50000:   
  
# Random qx by age 

    a0_rand_qx = random.uniform(a0_qxl,a0_qxu)
    a1_rand_qx = random.uniform(a1_qxl,a1_qxu)
    a5_rand_qx = random.uniform(a5_qxl,a5_qxu)
    a10_rand_qx = random.uniform(a10_qxl,a10_qxu)
    a15_rand_qx = random.uniform(a15_qxl,a15_qxu)
    a20_rand_qx = random.uniform(a20_qxl,a20_qxu)
    a25_rand_qx = random.uniform(a25_qxl,a25_qxu)
    a30_rand_qx = random.uniform(a30_qxl,a30_qxu)
    a35_rand_qx = random.uniform(a35_qxl,a35_qxu)
    a40_rand_qx = random.uniform(a40_qxl,a40_qxu)
    a45_rand_qx = random.uniform(a45_qxl,a45_qxu)
    a50_rand_qx = random.uniform(a50_qxl,a50_qxu)
    a55_rand_qx = random.uniform(a55_qxl,a55_qxu)
    a60_rand_qx = random.uniform(a60_qxl,a60_qxu)
    a65_rand_qx = random.uniform(a65_qxl,a65_qxu)
    a70_rand_qx = random.uniform(a70_qxl,a70_qxu)
    a75_rand_qx = random.uniform(a75_qxl,a75_qxu)
    a80_rand_qx = random.uniform(a80_qxl,a80_qxu)
    a85_rand_qx = random.uniform(a85_qxl,a85_qxu)
    a90_rand_qx = random.uniform(a90_qxl,a90_qxu)
    a95_rand_qx = random.uniform(a95_qxl,a95_qxu)
    a100_rand_qx = 1


# Random ax by age 

    a0_rand_ax = random.uniform(a0_axl,a0_axu)
    a1_rand_ax = random.uniform(a1_axl,a1_axu)
    a5_rand_ax = random.uniform(a5_axl,a5_axu)
    a10_rand_ax = random.uniform(a10_axl,a10_axu)
    a15_rand_ax = random.uniform(a15_axl,a15_axu)
    a20_rand_ax = random.uniform(a20_axl,a20_axu)
    a25_rand_ax = random.uniform(a25_axl,a25_axu)
    a30_rand_ax = random.uniform(a30_axl,a30_axu)
    a35_rand_ax = random.uniform(a35_axl,a35_axu)
    a40_rand_ax = random.uniform(a40_axl,a40_axu)
    a45_rand_ax = random.uniform(a45_axl,a45_axu)
    a50_rand_ax = random.uniform(a50_axl,a50_axu)
    a55_rand_ax = random.uniform(a55_axl,a55_axu)
    a60_rand_ax = random.uniform(a60_axl,a60_axu)
    a65_rand_ax = random.uniform(a65_axl,a65_axu)
    a70_rand_ax = random.uniform(a70_axl,a70_axu)
    a75_rand_ax = random.uniform(a75_axl,a75_axu)
    a80_rand_ax = random.uniform(a80_axl,a80_axu)
    a85_rand_ax = random.uniform(a85_axl,a85_axu)
    a90_rand_ax = random.uniform(a90_axl,a90_axu)
    a95_rand_ax = random.uniform(a95_axl,a95_axu)
    a100_rand_ax = random.uniform(a100_axl,a100_axu)
   

### calculate life table variables
    radix = 1000000.0000000
   
    # calculate the number of deaths age0
    a0_dx = a0_rand_qx*radix
    # calculate survivors
    a0_lx=radix
    a0_sx=a0_lx/radix # this is 1?    
    a1_lx=(radix-a0_dx)
    a1_sx = a1_lx/radix
       
    # calculate the number of deaths age1
    a1_dx = a1_rand_qx*a1_lx
    # calculate survivors
    a5_lx=(a1_lx-a1_dx)
    a5_sx = a5_lx/radix

    # calculate the number of deaths age5
    a5_dx = a5_rand_qx*a5_lx
    # calculate survivors
    a10_lx=(a5_lx-a5_dx)
    a10_sx = a10_lx/radix

    # calculate the number of deaths age10
    a10_dx = a10_rand_qx*a10_lx
    # calculate survivors
    a15_lx=(a10_lx-a10_dx)
    a15_sx = a15_lx/radix

    # calculate the number of deaths age15
    a15_dx = a15_rand_qx*a15_lx
    # calculate survivors
    a20_lx=(a15_lx-a15_dx)
    a20_sx = a20_lx/radix

    # calculate the number of deaths age20
    a20_dx = a20_rand_qx*a20_lx
    # calculate survivors
    a25_lx=(a20_lx-a20_dx)
    a25_sx = a25_lx/radix

    # calculate the number of deaths age25
    a25_dx = a25_rand_qx*a25_lx
    # calculate survivors
    a30_lx=(a25_lx-a25_dx)
    a30_sx = a30_lx/radix

    # calculate the number of deaths age30
    a30_dx = a30_rand_qx*a30_lx
    # calculate survivors
    a35_lx=(a30_lx-a30_dx)
    a35_sx = a35_lx/radix

    # calculate the number of deaths age35
    a35_dx = a35_rand_qx*a35_lx
    # calculate survivors
    a40_lx=(a35_lx-a35_dx)
    a40_sx = a40_lx/radix

    # calculate the number of deaths age40
    a40_dx = a40_rand_qx*a40_lx
    # calculate survivors
    a45_lx=(a40_lx-a40_dx)
    a45_sx = a45_lx/radix

    # calculate the number of deaths age45
    a45_dx = a45_rand_qx*a45_lx
    # calculate survivors
    a50_lx=(a45_lx-a45_dx)
    a50_sx = a50_lx/radix

    # calculate the number of deaths age50
    a50_dx = a50_rand_qx*a50_lx
    # calculate survivors
    a55_lx=(a50_lx-a50_dx)
    a55_sx = a55_lx/radix

    # calculate the number of deaths age55
    a55_dx = a55_rand_qx*a55_lx
    # calculate survivors
    a60_lx=(a55_lx-a55_dx)
    a60_sx = a60_lx/radix

    # calculate the number of deaths age60
    a60_dx = a60_rand_qx*a60_lx
    # calculate survivors
    a65_lx=(a60_lx-a60_dx)
    a65_sx = a65_lx/radix

    # calculate the number of deaths age65
    a65_dx = a65_rand_qx*a65_lx
    # calculate survivors
    a70_lx=(a65_lx-a65_dx)
    a70_sx = a70_lx/radix

    # calculate the number of deaths age70
    a70_dx = a70_rand_qx*a70_lx
    # calculate survivors
    a75_lx=(a70_lx-a70_dx)
    a75_sx = a75_lx/radix

    # calculate the number of deaths age75
    a75_dx = a75_rand_qx*a75_lx
    # calculate survivors
    a80_lx=(a75_lx-a75_dx)
    a80_sx = a80_lx/radix

    # calculate the number of deaths age80
    a80_dx = a80_rand_qx*a80_lx
    # calculate survivors
    a85_lx=(a80_lx-a80_dx)
    a85_sx = a85_lx/radix

    # calculate the number of deaths age85
    a85_dx = a85_rand_qx*a85_lx
    # calculate survivors
    a90_lx=(a85_lx-a85_dx)
    a90_sx = a90_lx/radix

    # calculate the number of deaths age90
    a90_dx = a90_rand_qx*a90_lx
    # calculate survivors
    a95_lx=(a90_lx-a90_dx)
    a95_sx = a95_lx/radix

    # calculate the number of deaths age95
    a95_dx = a95_rand_qx*a95_lx
    # calculate survivors
    a100_lx=(a95_lx-a95_dx)
    a100_sx = a100_lx/radix

    # calculate the number of deaths age100
    a100_dx = a100_rand_qx*a100_lx
    # No Survivors - top-coded

    #calculate Lx
    a0_Lx = (a1_lx*1)+(a0_dx*a0_rand_ax)
    a1_Lx = (a5_lx*4)+(a1_dx*a1_rand_ax)
    a5_Lx = (a10_lx*5)+(a5_dx*a5_rand_ax)
    a10_Lx = (a15_lx*5)+(a10_dx*a10_rand_ax)
    a15_Lx = (a20_lx*5)+(a15_dx*a15_rand_ax)
    a20_Lx = (a25_lx*5)+(a20_dx*a20_rand_ax)
    a25_Lx = (a30_lx*5)+(a25_dx*a25_rand_ax)
    a30_Lx = (a35_lx*5)+(a30_dx*a30_rand_ax)
    a35_Lx = (a40_lx*5)+(a35_dx*a35_rand_ax)
    a40_Lx = (a45_lx*5)+(a40_dx*a40_rand_ax)
    a45_Lx = (a50_lx*5)+(a45_dx*a45_rand_ax)
    a50_Lx = (a55_lx*5)+(a50_dx*a50_rand_ax)
    a55_Lx = (a60_lx*5)+(a55_dx*a55_rand_ax)
    a60_Lx = (a65_lx*5)+(a60_dx*a60_rand_ax)
    a65_Lx = (a70_lx*5)+(a65_dx*a65_rand_ax)
    a70_Lx = (a75_lx*5)+(a70_dx*a70_rand_ax)
    a75_Lx = (a80_lx*5)+(a75_dx*a75_rand_ax)
    a80_Lx = (a85_lx*5)+(a80_dx*a80_rand_ax)
    a85_Lx = (a90_lx*5)+(a85_dx*a85_rand_ax)
    a90_Lx = (a95_lx*5)+(a90_dx*a90_rand_ax)
    a95_Lx = (a100_lx*5)+(a95_dx*a95_rand_ax)
    a100_Lx = (a100_dx*a100_rand_ax)

 
    ####
    # calculate Tx
    a0_Tx = a0_Lx+a1_Lx+a5_Lx+a10_Lx+a15_Lx+a20_Lx+a25_Lx+a30_Lx+a35_Lx+a40_Lx+a45_Lx+a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a1_Tx = a1_Lx+a5_Lx+a10_Lx+a15_Lx+a20_Lx+a25_Lx+a30_Lx+a35_Lx+a40_Lx+a45_Lx+a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a5_Tx = a5_Lx+a10_Lx+a15_Lx+a20_Lx+a25_Lx+a30_Lx+a35_Lx+a40_Lx+a45_Lx+a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a10_Tx = a10_Lx+a15_Lx+a20_Lx+a25_Lx+a30_Lx+a35_Lx+a40_Lx+a45_Lx+a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a15_Tx = a15_Lx+a20_Lx+a25_Lx+a30_Lx+a35_Lx+a40_Lx+a45_Lx+a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a20_Tx = a20_Lx+a25_Lx+a30_Lx+a35_Lx+a40_Lx+a45_Lx+a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a25_Tx = a25_Lx+a30_Lx+a35_Lx+a40_Lx+a45_Lx+a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a30_Tx = a30_Lx+a35_Lx+a40_Lx+a45_Lx+a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a35_Tx = a35_Lx+a40_Lx+a45_Lx+a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a40_Tx = a40_Lx+a45_Lx+a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a45_Tx = a45_Lx+a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a50_Tx = a50_Lx+a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a55_Tx = a55_Lx+a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a60_Tx = a60_Lx+a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a65_Tx = a65_Lx+a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a70_Tx = a70_Lx+a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a75_Tx = a75_Lx+a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a80_Tx = a80_Lx+a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a85_Tx = a85_Lx+a90_Lx+a95_Lx+a100_Lx
    a90_Tx = a90_Lx+a95_Lx+a100_Lx
    a95_Tx = a95_Lx+a100_Lx
    a100_Tx = a100_Lx


    #calculate mx
    a0_mx = (a0_dx)/a0_Lx
    a1_mx = (a1_dx)/a1_Lx
    a5_mx = (a5_dx)/a5_Lx
    a10_mx = (a10_dx)/a10_Lx
    a15_mx = (a15_dx)/a15_Lx
    a20_mx = (a20_dx)/a20_Lx
    a25_mx = (a25_dx)/a25_Lx
    a30_mx = (a30_dx)/a30_Lx
    a35_mx = (a35_dx)/a35_Lx
    a40_mx = (a40_dx)/a40_Lx
    a45_mx = (a45_dx)/a45_Lx
    a50_mx = (a50_dx)/a50_Lx
    a55_mx = (a55_dx)/a55_Lx
    a60_mx = (a60_dx)/a60_Lx
    a65_mx = (a65_dx)/a65_Lx
    a70_mx = (a70_dx)/a70_Lx
    a75_mx = (a75_dx)/a75_Lx
    a80_mx = (a80_dx)/a80_Lx
    a85_mx = (a85_dx)/a85_Lx
    a90_mx = (a90_dx)/a90_Lx
    a95_mx = (a95_dx)/a95_Lx
    a100_mx = (a100_dx)/a100_Lx



# simulation of 2020:2019 mx ratio

    a0_rr = a0_mx/a0_m19
    a1_rr = a1_mx/a1_m19
    a5_rr = a5_mx/a5_m19
    a10_rr = a10_mx/a10_m19
    a15_rr = a15_mx/a15_m19
    a20_rr = a20_mx/a20_m19
    a25_rr = a25_mx/a25_m19
    a30_rr = a30_mx/a30_m19
    a35_rr = a35_mx/a35_m19
    a40_rr = a40_mx/a40_m19
    a45_rr = a45_mx/a45_m19
    a50_rr = a50_mx/a50_m19
    a55_rr = a55_mx/a55_m19
    a60_rr = a60_mx/a60_m19
    a65_rr = a65_mx/a65_m19
    a70_rr = a70_mx/a70_m19
    a75_rr = a75_mx/a75_m19
    a80_rr = a80_mx/a80_m19
    a85_rr = a85_mx/a85_m19
    a90_rr = a90_mx/a90_m19
    a95_rr = a95_mx/a95_m19
    a100_rr = a100_mx/a100_m19
 

# output the mortality rate ratios for each simulation    
    rr = r"/Users/ryan/Documents/Papers/life table technique/simulation/male_20_rr.txt"
    opened_file = open(rr, 'a')

    if count==0:
        opened_file.write('{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22}\n'.format("sim_num","a0_rr","a1_rr","a5_rr","a10_rr","a15_rr","a20_rr","a25_rr","a30_rr","a35_rr","a40_rr","a45_rr","a50_rr","a55_rr","a60_rr","a65_rr","a70_rr","a75_rr","a80_rr","a85_rr","a90_rr","a95_rr","a100_rr"))

    else:
        opened_file.write('{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22}\n'.format(count,a0_rr,a1_rr,a5_rr,a10_rr,a15_rr,a20_rr,a25_rr,a30_rr,a35_rr,a40_rr,a45_rr,a50_rr,a55_rr,a60_rr,a65_rr,a70_rr,a75_rr,a80_rr,a85_rr,a90_rr,a95_rr,a100_rr))
 


    ###### estimate life expectancy

    #calculate ex
    a0_ex = a0_Tx/radix
    a1_ex = a1_Tx/a1_lx
    a5_ex = a5_Tx/a5_lx
    a10_ex = a10_Tx/a10_lx
    a15_ex = a15_Tx/a15_lx
    a20_ex = a20_Tx/a20_lx
    a25_ex = a25_Tx/a25_lx
    a30_ex = a30_Tx/a30_lx
    a35_ex = a35_Tx/a35_lx
    a40_ex = a40_Tx/a40_lx
    a45_ex = a45_Tx/a45_lx
    a50_ex = a50_Tx/a50_lx
    a55_ex = a55_Tx/a55_lx
    a60_ex = a60_Tx/a60_lx
    a65_ex = a65_Tx/a65_lx
    a70_ex = a70_Tx/a70_lx
    a75_ex = a75_Tx/a75_lx
    a80_ex = a80_Tx/a80_lx
    a85_ex = a85_Tx/a85_lx
    a90_ex = a90_Tx/a90_lx
    a95_ex = a95_Tx/a95_lx
    a100_ex = a100_Tx/a100_lx

    # save data
    
    tot_file_name = r"/Users/ryan/Documents/Papers/life table technique/simulation/male_20_ex.txt"
    tot_opened_file = open(tot_file_name, 'a')
    #opened_file.write("%r\n" %age45_ex_total)
    if count==0:
        tot_opened_file.write('{0} {1} {2}\n'.format("sim_num","age", "ex"))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"0",a0_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"1",a1_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"5",a5_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"10",a10_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"15",a15_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"20",a20_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"25",a25_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"30",a30_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"35",a35_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"40",a40_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"45",a45_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"50",a50_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"55",a55_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"60",a60_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"65",a65_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"70",a70_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"75",a75_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"80",a80_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"85",a85_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"90",a90_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"95",a95_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"100",a100_ex))


    else:
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"0",a0_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"1",a1_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"5",a5_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"10",a10_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"15",a15_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"20",a20_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"25",a25_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"30",a30_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"35",a35_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"40",a40_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"45",a45_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"50",a50_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"55",a55_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"60",a60_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"65",a65_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"70",a70_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"75",a75_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"80",a80_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"85",a85_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"90",a90_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"95",a95_ex))
        tot_opened_file.write('{0} {1} {2}\n'.format(count,"100",a100_ex))


    print(count)
    count += 1  # This is the same as count = count + 1

tot_opened_file.close()

print("simulation completed")                    




