from fastkml import kml
import numpy as np
import sys

AREA = 26.82 * 1000000  # Area of Lambeth in m^2

def hav(lat1,lon1,lat2,lon2):
    # lat/lon in degrees
    lat1 = np.deg2rad(lat1)
    lat2 = np.deg2rad(lat2)
    lon1 = np.deg2rad(lon1)
    lon2 = np.deg2rad(lon2)
    R = 6371000  # Radius of earth in metres
    h = (np.sin((lat2-lat1)/2))**2 
    h = h + np.cos(lat1)*np.cos(lat2)*(np.sin((lon2-lon1)/2))**2
    dist = 2*R*np.arcsin(h**0.5)
    return dist

def read(filename):
    with open(filename, 'rb') as kml_file:
        doc = kml_file.read()
    k = kml.KML()
    k.from_string(doc)
    return k

def getlatlon(k, coords, count=0):
    if count > 20:
        raise RuntimeError('Reached 20 recursions of getLatLon')
    if not getattr(k, 'geometry',0):
        for feature in k.features():
            coords = getlatlon(feature, coords, count+1)
    else:
        coords.append([k.geometry.x, k.geometry.y])
    return coords

def Ki(coords1, coords2, h):
    numer = 0
    for j in coords2:
        for i in coords1:
            if hav(i[1],i[0],j[1],j[0]) <= h:
                numer = numer + 1
    denom = len(coords2) * len(coords1) / AREA
    return (numer/denom)

def crossL(coords1,coords2, h):
    # Find cross L function for two sets of points
    # FOR POINTS WITHIN SAME AREA
    Kab = Ki(coords1,coords2,h) # This is K1, which is returned in one way mode
    coef = (Kab/np.pi)**0.5 - h
    return coef


Coords1 = []
Coords2 = []
file1 = sys.argv[1]
file2 = sys.argv[2]
k1 = read(file1)
Coords1 = getlatlon(k1,Coords1)

k2 = read(file2)
Coords2 = getlatlon(k2,Coords2)
  
print(crossL(Coords1, Coords2, 100))


