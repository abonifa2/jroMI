from pylab import *
import covXYs as covXY

geom=covXY.geom
covs=covXY.covs

dr=5.
h=arange(200)*dr
sf = 0;

fig = figure(figsize = (20,15))
fig = figure(1)
fig.subplots_adjust(hspace=.7,wspace = 0.7)

for ir in range(13):
    
    tx=0.0245*(ir-6);ty=-tx
    print "tx-ty in 1D profile : ", tx, ty
    px,py,uB,Bo,theta,uphi,uthe=geom(tx,ty,dr) 
    Ne=3.0e12*exp(-h/180.-50.*exp(-h/60.))     
    covXX,covXY=covs(px,py,uB,Bo,theta,uphi,uthe,Ne,h)

    ax = fig.add_subplot(13, 1, sf)
    #subplot(13,1,ir)
    ax.plot(h,covXX);  ax.plot(h,covXY,color='r');

    ax.set_xticks((0,500,1000)); 
        
    ax.set_yticks((0.000,0.014,0.007));  
        
    sf +=1
        
    if  ir != 0:
            
        setp(ax.get_xticklabels(), visible=False)
        
    elif ir == 0:

        xlabel('Height (km)');

show()
