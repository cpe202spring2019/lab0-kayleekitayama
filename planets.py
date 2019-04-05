def weight_on_planets():
   # write your code here
   weight_e = float(input("What do you weigh on earth? "))
   weight_m = (weight_e)*0.38
   weight_j = (weight_e)*2.34
   
   m_text = '\nOn Mars you would weigh'
   j_text = '\nOn Jupiter you would weigh'
   lb = "pounds."

   print(m_text,weight_m,lb + j_text, weight_j,lb)
   
   
if __name__ == '__main__':
   weight_on_planets()
