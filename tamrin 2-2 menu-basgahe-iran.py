







import os




from math import floor




while True:




 print(" be bashgah badansazi iran khosh amadid:")

 menu_Tamrin_barname_bashgahiran=input("1.tamrin egkhtesasi  2.tamrin gorohi     3.tamrin yooga        4.exit:")
 while True:
   match menu_Tamrin_barname_bashgahiran:
    case"1":
     menu_Tamrin_egkhtesasi_basgahiran=input("1.tamrin ba morabi  700   2. tamrin ba emkhnat   950   3.exit:")
    
     match menu_Tamrin_egkhtesasi_basgahiran:
      case"1":
       tedad_tamrinbamorabi=int(input("tedad tamrin ba morabi:"))
       mablaghe_tamrinbamorabi=2500*tedad_tamrinbamorabi*1.1
       print(mablaghe_tamrinbamorabi)
       break


      case"2":
       tedad_tamrinbaemkhnat=int(input("tedad_tamrinbaemkhnat:"))
       mablaghe_tamrinbaemkhnat=3500*tedad_tamrinbaemkhnat*1.1
       print((mablaghe_tamrinbaemkhnat))
       break

     
      case"3":
       break


    case "2":
     menu_Tamrin_gorohi_basgahiran=input("1.tamrinbatredmil   500   2.tamrinbadocharche   400    3.exit:")


     match menu_Tamrin_gorohi_basgahiran:    
       case"1":
        tedad_tamrinbatredmil=int(input("tedad tamrinbatredmil:"))
        mablaghe_tamrinbatredmil=500*tedad_tamrinbatredmil*1.1
        print(mablaghe_tamrinbatredmil)
        break

       case"2":
        teded_tamrinbadocharche=int(input("teded tamrinbadocharche:"))
        mablaghe_tamrinbadocharche=400*teded_tamrinbadocharche*1.1
        print(mablaghe_tamrinbadocharche)
        break


       case"3":
        break

    case"3":
      
     menu_tamrin_yooga_bashgahiran=input("1.tamrin hata  450    2.tamrin yeen  550    3.tamrin power   650  4.exit:")
     match menu_tamrin_yooga_bashgahiran:
      
      case"1":
       tedad_tamrinhata=int(input("tedad tamrinhata:"))
       mablaghe_tamrinhata=450*tedad_tamrinhata*1.1
       print(mablaghe_tamrinhata)
       break


      case"2":
       tedad_tamrinyeen=int(input("tedad tamrinyeen:"))
       mablaghe_tamrinyeen=550*tedad_tamrinyeen*1.1
       print(mablaghe_tamrinyeen)
       break


      case"3":
       tedad_tamrinpower=int(input("teded tamrinpower:"))
       mablaghe_tamrinpower=650*tedad_tamrinpower*1.1
       print(mablaghe_tamrinpower)


      case"4":
       break


  




      
      

     

