xm,ym,xr,yr = input().split()
xm = int(xm)
ym = int(ym)
xr = int(xr)
yr = int(yr)

crossings = 0
if (xr >= xm):
    crossings += xr-xm
else:
    crossings += xm-xr

if (yr >= ym):
    crossings += yr-ym
else:
    crossings += ym-yr

print (crossings)