#!/usr/bin/env python
# coding: utf-8

# In[1]:


## implementing neural network using tensors in  pytorch 
## Tensor us identical to a numpy array : a Tensor is a n-d array .
import torch 
import math 


# In[2]:


dtype=torch.float 
device = torch.device("cpu")


# In[3]:


x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
y = torch.sin(x)


# In[4]:


##this creates random input values in x and y 

##now randomly initalizing weights 
a = torch.randn((), device=device, dtype=dtype)
b = torch.randn((), device=device, dtype=dtype)
c = torch.randn((), device=device, dtype=dtype)
d = torch.randn((), device=device, dtype=dtype)


# In[5]:


learning_rate = 1e-6


# In[10]:


for t in range(2000):
    ##forward pas :compute predicted y 
    y_pred = a + b * x + c * x ** 2 + d * x ** 3
        
    # compute and print loss
    loss = (y_pred - y).pow(2).sum().item()
    if t % 100 == 99:
        print(t, loss)

    # backprop to compute gradients of a, b, c, d with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # update weights using gradient descent
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d


# In[11]:


print(f'Result: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')


# In[ ]:




