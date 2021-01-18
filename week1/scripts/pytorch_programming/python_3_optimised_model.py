#!/usr/bin/env python
# coding: utf-8

# In[2]:


## optimise the previous model using the nn module using the RMSprop algorithm 
import torch 
import math 


# In[3]:


# Create Tensors to hold input and outputs.
x = torch.linspace(-math.pi, math.pi, 2000)
y = torch.sin(x)


# Prepare the input tensor (x, x^2, x^3).
p = torch.tensor([1, 2, 3])
xx = x.unsqueeze(-1).pow(p)


# In[4]:


# Use the nn package to define our model and loss function.
model = torch.nn.Sequential(
    torch.nn.Linear(3, 1),
    torch.nn.Flatten(0, 1)
)
loss_fn = torch.nn.MSELoss(reduction='sum')


# In[5]:


#The first argument to the RMSprop constructor tells the
# optimizer which Tensors it should update.
learning_rate = 1e-3
optimizer = torch.optim.RMSprop(model.parameters(), lr=learning_rate)


# In[7]:


for t in range(2000):
    #forward pass : compute the predicted y by passing x to model
    y_pred=model(xx)
    
    #compute and print the loss 
    loss=loss_fn(y_pred,y)
    if t%100==99:
        print(t,loss.item())
    
    #before the backward pass using the optimizer to 0 all of the gradients 
    ## for the varibales it will update weight of the model 
    
    ### This is because by default ,gradients are accumulated in buffers 
    optimizer.zero_grad()
    
    #backward pass :compute gradient of the loss wrt to model parameters
    loss.backward()
    
    ##calling the step function on an otpmizer makes an update to its parameters
    optimizer.step()
    
    


# In[8]:


linear_layer = model[0]
print(f'Result: y = {linear_layer.bias.item()} + {linear_layer.weight[:, 0].item()} x + {linear_layer.weight[:, 1].item()} x^2 + {linear_layer.weight[:, 2].item()} x^3')


# In[ ]:




