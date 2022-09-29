import ImageProcess2

def euclidian(x1, x2,y1,y2):
    xnew = (x1-x2)**2
    ynew = (y1-y2)**2
    sum_xy = xnew + ynew
    sonuc = (sum_xy)**(1/2)
    return sonuc

value1 = euclidian(ImageProcess2.x,ImageProcess2.y,ImageProcess2.a[0],ImageProcess2.a[1])
value2 = euclidian(ImageProcess2.x,ImageProcess2.y,ImageProcess2.a[2],ImageProcess2.a[3])

print("values of distances: ",value1,value2)
print(min(value1,value2))
minValue = min(value1,value2)