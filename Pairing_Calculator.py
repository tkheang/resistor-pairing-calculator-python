cable_array = ["5A", "5B", "7A", "7B", "10A", "10B", "15A", "15B", "20A", "20B", "25A", "25B", "30A", "30B", "35A", "35B", "40A", "40B", "45A", "45B", "45D1", "45D2", "50A", "50B", "55A", "55B", "55D1", "55D2", "60A", "60B", "100", "115"]

Rc1_array = [0.12, 0.13, 0.16, 0.16, 0.22, 0.21, 0.30, 0.30, 0.39, 0.39, 0.47, 0.48, 0.57, 0.57, 0.66, 0.64, 0.74, 0.73, 0.82, 0.82, 0.83, 0.82, 0.92, 0.92, 1.00, 0.99, 1.01, 1.01, 1.11, 1.09, 1.76, 2.11]

Rc2_array = [0.04, 0.05, 0.05, 0.05, 0.06, 0.06, 0.07, 0.07, 0.09, 0.09, 0.10, 0.11, 0.11, 0.12, 0.11, 0.14, 0.12, 0.16, 0.15, 0.17, 0.82, 0.83, 0.16, 0.20, 0.28, 0.21, 1.00, 1.01, 0.18, 0.22, 0.27, 2.09]

def calculateRatio():
  Rp = float(input("Rp (Mohms): "))*1000000
  Rs = float(input("Rs (kohms): "))*1000
  Rin = float(input("Rin: "))
  Req = 1/(1/Rs+1/(Rc1+Rc2+Rin))
  V1 = Vin*(Req/(Rp+Req))
  Vout = V1*((Rin+Rc2)/(Rin+Rc1+Rc2))
  ratio = round(Vin/Vout, 2)
  print("Ratio: " + str(ratio))

def calculateRp():
  Rs = float(input("Enter Rs in kohms: "))*1000
  Req = (1/Rs+1/(Rc1+Rc2+Rin))**-1
  Rp = Vin*(Req/V1)-Req
  Rp = round(Rp/1000000, 2)
  print()
  print("Rp: " + str(Rp) + " Mohms\n")

def calculateRs():
  Rp = float(input("Enter Rp in Mohms: "))*1000000
  Req = V1*(Rp/(Vin-V1))
  Rs = (1/Req-1/(Rc1+Rc2+Rin))**-1
  Rs = round(Rs/1000, 3)
  print()
  print("Rs: " + str(Rs) + " kohms\n")

Vin = float(input("Nominal voltage (kV): "))*1000
cable = input("Cable: ")
print()

for x, y, z in zip(cable_array, Rc1_array, Rc2_array):
  if (x == cable):
    Rc1 = y
    Rc2 = z

print("1: Calculate ratio")
print("2: Calculate Rp")
print("3: Calculate Rs")
print()

select = int(input("Select calculation: "))

print()

while True:
  if select == 1:
    calculateRatio()
    break
  elif select == 2:
    calculateRp()
    break
  elif select == 3:
    calculateRs()
    break
