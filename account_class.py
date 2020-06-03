#!/usr/bin/env python
# coding: utf-8

# In[172]:


class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        print(f"Hi {self.owner} your balance is £{self.balance}")
        pass
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print (f"we just added £{amount} to your account and your balance is now £{self.balance}")
    
    def withdraw(self,amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            print(f"Welcome to Lloyd's bank, you have withdrawn £{amount}. Your Current Account balance is now {self.balance}.")
        else:
            self.balance
            print(f"You have tried to withdraw £{amount}. Transaction failed because there was insufficient funds.")
        pass


# In[173]:


account1 = Account('James',100)


# In[197]:


account1.deposit(300)


# In[179]:


account1.withdraw(200)


# In[ ]:





# In[ ]:





# In[ ]:




