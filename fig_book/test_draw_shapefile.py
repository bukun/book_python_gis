import shapefile as shp
import matplotlib.pyplot as plt

sf = shp.Reader('gdata/world_borders.shp')

plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
# plt.show()
plt.savefig('xx_shp1.png')