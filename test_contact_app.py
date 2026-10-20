



from unittest import TestCase

from contact_app import create_contact, clear_contacts

class TestContactApp(TestCase):


    def test_that_newContact_canBeCreated_andSaved(self): 
        
        clear_contacts()
        
        first_name = "Lionelii"
        last_name = "messiah"    
        phone_number = "09167514283" 
    
        contact = create_contact(first_name,last_name,phone_number)
        
        self.assertEqual(type(contact), list)
        self.assertEqual(len(contact), 3)
        
        self.assertEqual("09167514283", contact[-1])
    
    

    
    def test_that_Duplicate_contacts_cannot_be_created(self):
        
        clear_contacts()
        
        first_name = "Musa"
        last_name = "Lai"    
        phone_number = "09167514283" 
        
        create_contact(first_name,last_name,phone_number)
        
         
        first_name = "Lionel"
        last_name = "messi"   
        phone_number = "09167514283" 
           
        contact = create_contact(first_name,last_name,phone_number)
        
#        self.assertEqual(type(contact), None)
        self.assertIsNone(contact)
        
  















#
#        self.assertEqual(90, 90)
#        self.assertTrue(True)
#        self.assertFalse(False)
#
#    def test_two(self):
#    
#        self.test_samle()
#
#
