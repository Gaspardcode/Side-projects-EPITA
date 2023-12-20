def TP(a,b):
    plt.clf()
    plt.figure("TABLEAU")
    plt.title("Distance à la case ({},{})".format(a,b))
    plt.axis("off")
    plt.axis("equal")
    i = 0
    j = 0
    plt.plot([0,0,0,0],[0,160,20,150],'k')
    while i < 9:
        plt.plot([i*20,i*20],[0,160],'k')
        i+=1
    i = 1
    while j < 9:
        plt.plot([0,160],[j*20,j*20],'k')
        j+=1
    
def MovesKing(a,b):
    x = (a-1) * 20 + 10
    y = (b-1) * 20 + 10
    TP(a,b)
    c = 'k'
    plt.plot([x,x+20],[y,y],c)
    plt.plot([x,x+20],[y,y-20],c)
    plt.plot([x,x],[y,y-20],c)
    plt.plot([x,x-20],[y,y-20],c)
    
    plt.plot([x,x-20],[y,y],c)
    plt.plot([x,x-20],[y,y+20],c)
    plt.plot([x,x],[y,y+20],c)
    plt.plot([x,x+20],[y,y+20],c)
    
    plt.show()

MovesKing(4,8)
def courbe(r):
    plt.clf()
    i = 0
    ordo = []
    absc = []
    while i < 103:
        theta = i*2*math.pi/100
        x = r*math.cos(theta)
        y = r*math.sin(theta)
        ordo.append(x)
        absc.append(y)
        i+= 1
    plt.plot(absc,ordo,'b')
    plt.axis('equal')
    plt.show()
    
#courbe(5)
