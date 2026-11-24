






import os



from math import ceil




while True:



 print("be  resturan nafas khosh amadid:")

 menu_resturan_nafas=input("1.pitzza      2.psta    3.salad   4.exit:")
 while True:
  match menu_resturan_nafas:
   case"1":
     menu_pittza_resturan_nafas=input("1.rostbif    1.200    2.peperoni   950    3.special  1100    4.exit:")
     match menu_pittza_resturan_nafas:
      case"1":
       tedad_rostbif=int(input("tedad rostbif:"))
       mablaghe_rostbif=1200*tedad_rostbif*1.1
       print(ceil(mablaghe_rostbif))

       continue
        
      case"2":
       tedad_peperoni=int(input("tedad peperoni:"))
       mablaghe_peperoni=950*tedad_peperoni*1.1
       print(ceil(mablaghe_peperoni))

       continue
        
      case"3":
       tedad_special=int(input("tedad special:"))
       mablaghe_special=1100*tedad_special*1.1
       print(ceil(mablaghe_special))

       continue

      
      case"4":
       break


   case"2":
     menu_pasta_resturan_nafas=input("1.alfredo    800    2.sabzigat   700    3.morghe  850    4.exit:")
     match menu_pasta_resturan_nafas:
      case"1":
       tedad_alfredo=int(input("tedad alfredo:"))
       mablaghe_alfredo=800*tedad_alfredo*1.1
       print(ceil(mablaghe_alfredo))
       continue
        
      case"2":
       tedad_sabzigat=int(input("tedad sabzigat:"))
       mablaghe_sabzigat=700*tedad_sabzigat*1.1
       print(ceil(mablaghe_sabzigat))
       continue
        
      case"3":
       tedad_morghe=int(input("tedad morghe:"))
       mablaghe_morghe=800*tedad_morghe*1.1
       print(ceil(mablaghe_morghe))
       continue



      case"4":
       break

           
   case"3":
     menu_salad_resturan_nafas=input("1.saladsezar    750    2.saladfasl  550    3.saladmakaroni  600    4.exit:")
     match menu_salad_resturan_nafas:
       case"1":
         tedad_saladsezar=int(input("tedad saladsezar:"))
         mablaghe_saladsezar=750*tedad_saladsezar*1.1
         print(ceil(mablaghe_saladsezar))
         continue

       case"2":
         tedad_saladfasl=int(input("tedad saladfasl:"))
         mablaghe_saladfasl=550*tedad_saladfasl*1.1
         print(ceil(mablaghe_saladfasl))
         continue
        
       case"3":
         tedad_saladmakaroni=int(input("tedad saladmakaroni:"))
         mablaghe_saladmakaroni=600*tedad_saladmakaroni*1.1
         print(ceil(mablaghe_saladmakaroni))
         continue

        
       case"4":
        break

        
   case"4":
        print("az kharid shoma sepasgozarim")
        break
     
 break
       

 
    