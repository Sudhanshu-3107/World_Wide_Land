from django.db import models



class Agent(models.Model):
    id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pic = models.FileField(max_length=100, upload_to='Agent_Images/')
    address = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']



class PropertyOwner(models.Model):
    phone = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    type = models.CharField(max_length=10, default='owner')
    pic = models.FileField(max_length=100, upload_to='Owner_Images/')
    address = models.TextField()


class Member(models.Model):
    m_id = models.CharField(max_length=20,  primary_key=True)
    phone = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    pic = models.FileField(max_length=100, upload_to='Member_Images/')
    address = models.TextField()
    


class Property(models.Model):
    owner = models.ForeignKey(PropertyOwner, on_delete=models.DO_NOTHING)
    property_type = models.CharField(max_length=50)
    property_price = models.CharField(max_length=50)
    property_location = models.CharField(max_length=50)
    property_image = models.FileField(max_length=100, upload_to='Property_Images/')
    property_description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']



class PropertyQuery(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    type_of_property = models.CharField(max_length=50)
    price_range = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']


class Feedback(models.Model):
    name = models.CharField(max_length=50, default="User")
    email = models.CharField(max_length=13, default="")
    remark = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']



class PropertySeeker(models.Model):
    phone = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, default='seeker')
    email = models.CharField(max_length=50)
    pic = models.FileField(max_length=100, upload_to='Property_Images/')
    address = models.TextField()



class Inquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    seeker = models.ForeignKey(PropertySeeker, on_delete=models.DO_NOTHING)
    question = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
