class Card:
    def __init__(self,imageURL,price,rating,description,delivery,comment,brand):
       self.imageURL=imageURL
       self.price=price
       self.rating=rating
       self.description=description
       self.delivery=delivery
       self.comment=comment
       self.brand=brand

    def printalldetails(self):
      print("IMAGE URL:",self.imageURL)
      print("PRICE:",self.price)
      print("RATING:",self.rating)
      print("DESCRIPTION:",self.description)
      print("DELIVERY:",self.delivery)
      print("COMMENTS:",self.comment)
      print("BRAND:",self.brand)

    def printbasicdetails(self):
        print("BRAND:",self.brand)
        print("PRICE:",self.price)
        print("RATING:",self.rating)
    
    def calculateGST(self):
      print("Calculating GST")
     
    def printInvoice(self,extraprice):
        print("Printing Invoice")

laptop=Card("1-dummy-url1", 50000, 4, "ABD","4days",['good','best'], "DELL")
laptop.printbasicdetails()
laptop.calculateGST()
laptop.printInvoice(1250)

phone=Card("2-dummy-url2",25000, 4.5, "DEF","2days",['better','best'], "samsung")
phone.printbasicdetails()
phone.calculateGST()
phone.printInvoice(1350)

smartwatch=Card("3-dummy-url3", 6000, 4, "FGH","5days",['good','best'], "boat")
smartwatch.printbasicdetails()
smartwatch.calculateGST()
smartwatch.printInvoice(1200)

