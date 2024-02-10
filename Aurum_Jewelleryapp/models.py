from django.db import models


#Contact Us Backend Start.
class ContactModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,help_text="Enter your Name")
    email=models.EmailField(max_length=100,help_text="Enter Email")
    mobile=models.CharField(max_length=20, help_text="Enter Mobile Number")
    message=models.CharField(max_length=100,help_text="Enter Your Message")
    
    class Meta:
        db_table= "contact_details"
    
    def __str__(self):
        return str(self.user_id) + ' ' + self.username

#Contact Us Backend End.



#User Started Here.

class UserRegistrationModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,help_text="Enter Username")
    email=models.EmailField(max_length=100,help_text="Enter Email")
    mobile=models.CharField(max_length=20, help_text="Enter Mobile Number")
    address=models.TextField(max_length=300,help_text="Enter Address")
    password=models.CharField(max_length=100,help_text="Enter Password")

    
    class Meta:
        db_table= "user_reg_details"
    
    def __str__(self):
        return str(self.user_id) + ' ' + self.username

#User Ended Here.