from  sample.sample.main.model import Users,Products

class Users_dbops(models.Model):

    def add_user(self,u_Data):

        # adding user to the user table
        # args- u_Data: a dictionary having user details via form
        
        insertUser=Users(u_Data)
        insertUser.save(force_insert=True)



