







import os



from math import ceil




while True:



 print("be cafe yas  khosh amadid:")

 menu_cafe_yas=input("1.esperso      2.cake    3.gheyloon   4.exit:")
 while True:
  match menu_cafe_yas:
   case"1":
     menu_esperso_cafe_yas=input("1.capouchino    400    2.lata   500    3.moca  550    4.exit:")
     match menu_esperso_cafe_yas:
      case"1":
       tedad_capouchino=int(input("tedad capouchino:"))
       mablaghe_capouchino=400*tedad_capouchino*1.1
       print(ceil(mablaghe_capouchino))
       os.system("cls")
       continue
        
      case"2":
       tedad_lata=int(input("tedad lata:"))
       mablaghe_lata=500*tedad_lata*1.1
       print(ceil(mablaghe_lata))

       continue
        
      case"3":
       tedad_moca=int(input("tedad moca:"))
       mablaghe_moca=550*tedad_moca*1.1
       print(ceil(mablaghe_moca))

       continue

      
      case"4":
       break


   case"2":
     menu_cake_cafe_yas=input("1.cake havig   350   2.cake notela   550    3.cake tiramiso  450    4.exit:")
     match menu_cake_cafe_yas:
      case"1":
       tedad_cake_havig =int(input("tedad cake havig:"))
       mablaghe_cake_havig =350*tedad_cake_havig*1.1
       print(ceil(mablaghe_cake_havig))
       continue
        
      case"2":
       tedad_cake_notela=int(input("tedad cake notela:"))
       mablaghe_cake_notela=550*tedad_cake_notela*1.1
       print(ceil(mablaghe_cake_notela))
       continue
        
      case"3":
       tedad_cake_tiramiso=int(input("tedad cake tiramiso:"))
       mablaghe_cake_tiramiso=450*tedad_cake_tiramiso*1.1
       print(ceil(mablaghe_cake_tiramiso))
       continue



      case"4":
       break

           
   case"3":
     menu_gheyloon_cafe_yas=input("1.gheyloon dosib   800    2.gheyloon mosco   850   3.gheyloon English  900    4.exit:")
     match menu_gheyloon_cafe_yas:
       case"1":
         tedad_gheyloon_dosib=int(input("tedad gheyloon dosib:"))
         mablaghe_gheyloon_dosib=800*tedad_gheyloon_dosib*1.1
         print(ceil(mablaghe_gheyloon_dosib))
         continue

       case"2":
         tedad_gheyloon_mosco=int(input("tedad gheyloon mosco:"))
         mablaghe_gheyloon_mosco=850*tedad_gheyloon_mosco*1.1
         print(ceil(mablaghe_gheyloon_mosco))
         continue
        
       case"3":
         tedad_gheyloon_English=int(input("tedad gheyloon English:"))
         mablaghe_gheyloon_English=900*tedad_gheyloon_English*1.1
         print(ceil(mablaghe_gheyloon_English))
         continue

        
       case"4":
        break

        
   case"4":
        print("be omid didar mojadad")
        break
     
 break
       

 
    