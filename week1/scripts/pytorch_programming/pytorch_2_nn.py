#!/usr/bin/env python
# coding: utf-8

# In[1]:


## nn module is a higher level abstraction over the more primiive tensor one 


# In[2]:


import torch 
import math 


# In[3]:


# Create Tensors to hold input and outputs.
x = torch.linspace(-math.pi, math.pi, 2000)
y = torch.sin(x)


# In[4]:


p = torch.tensor([1, 2, 3])
xx = x.unsqueeze(-1).pow(p)

## assumming y is  a linear function of (x,x^2 ,x^3)


# In[5]:


# to match the shape of `y`.
model = torch.nn.Sequential(
    torch.nn.Linear(3, 1),
    torch.nn.Flatten(0, 1)
)


# In[6]:


#we will use Mean Squared Error (MSE) as our loss function.
loss_fn = torch.nn.MSELoss(reduction='sum')


# In[9]:


learning_rate = 1e-6
for t in range(2000):
    y_pred=model(xx) ## doing a forward pass 
    # Compute and print loss. We pass Tensors containing the predicted and true
    # values of y, and the loss function returns a Tensor containing the
    # loss.
    loss = loss_fn(y_pred, y)
    if t % 100 == 99:
        print(t, loss.item())
    #zero the gradients before running the backward pass 
    model.zero_grad()
    ##now doing a backward pass 
    loss.backward()
    
    # Update the weights using gradient descent. Each parameter is a Tensor, so
    # we can access its gradients like we did before.
    with torch.no_grad():
        for param in model.parameters():
            param -= learning_rate * param.grad
#the first layer of model is accessed now like a list 
linear_layer=model[0]
# For linear layer, its parameters are stored as `weight` and `bias`.
print(f'Result: y = {linear_layer.bias.item()} + {linear_layer.weight[:, 0].item()} x + {linear_layer.weight[:, 1].item()} x^2 + {linear_layer.weight[:, 2].item()} x^3')


# In[ ]:




