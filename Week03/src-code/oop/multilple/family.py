from son import son
from daughter import daughter
s1 = son()
d1 = daughter()
print("Grandpa: " + s1.g_fname + " " + s1.g_lname + " is " + str(s1.g_age) + " years old.")
print("Dad: " + s1.d_fname + " " + s1.g_lname + " is " + str(s1.d_age) + " years old.")
print("Mom: " + s1.m_fname + " " + s1.m_lname + " is " + str(s1.m_age) + " years old.")
print("Son: " + s1.s_fname + " " + s1.g_lname + " is " + str(s1.s_age) + " years old.")
print("Daughter: " + d1.dg_fname + " " + d1.m_lname + " is " + str(d1.dg_age) + " years old.")

