def get_usd():
  while True:
    try:
      usd = float(input("Enter the dollar amount you wish to convert: "))
      if usd < 1:
       print("Entry must be greater than 0 ")
      else:
        break
    except ValueError:
      print("You did not enter a number")
  return usd




def get_currency():
  while True:
      currency = input("Enter the desired currency(GBP for Pounds, EUR for Euro, or CNY for Yuan): ")
      if currency == "GBP":
        return currency
      elif currency == "EUR":
        return currency
      elif currency == "CNY":
        return currency
      else:
        print("You did not enter a valid currency type")




def usd_to_gbp(usd):
  brit = usd * .77
  return brit




def usd_to_eur(usd):
  germ = usd * .92
  return germ




def usd_to_cny(usd):
  chin = usd * 6.98
  return chin




def main():
  my_get_usd = get_usd()
  currency_type = get_currency()
  if currency_type == "GBP":
    my_brit = usd_to_gbp(my_get_usd)
    print (f"${my_get_usd} in {currency_type} is {my_brit}.")
  elif currency_type =="EUR":
    my_germ = usd_to_eur(my_get_usd)
    print (f"${my_get_usd} in {currency_type} is {my_germ}.")
  elif currency_type =="CNY":
    my_chin = usd_to_cny(my_get_usd)
    print (f"${my_get_usd} in {currency_type} is {my_chin}.")






if __name__ == "__main__":
  main()




