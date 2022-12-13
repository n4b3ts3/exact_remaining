# Exact Remaining
Simple math formula to get a number that when substracting a percent value it returns the original number

# Use cases 
The origin of this was thinking how can a seller increase a product price to a total that when substracting a percent from that total the resulting total becomes the wanted total, for example lets say we want to sell a product in 200 $ but for example PayPal will take its 2.9% from that transaction, but we need to sell the product in 200$ because if not we are going to lose money, we want to get an acurrate way of doing so, for that we use the exact remaining formula that give us a number that when substracting a percent amount will going to return us the exact number we want...

with the previous values lets write the math formula:

n = (x*p)/(100-p) where n is number to be added to the total and x is the total and p is the percent someone is going to take from our total
so replacing the previous values in the previous formula we got that

n = ((200*2.9)/(100-2.9))

so n = 5.973223480947477

now if we add n to x we got that

t = n + x 

t = 205.97322348094747

finally when substracting the 2.9 percent of t minus t we got the initial x

x = t - ((t*2.9)/100) this is True as left member is equal to right member

when using a language like python for this please use round as some values may get an infinite value as the division is not always exact
