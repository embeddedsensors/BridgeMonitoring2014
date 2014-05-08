'''
GPS Utility functions

Matthew Iannucci for OCE 496 2014
'''
import pyproj

def lat2meter(lat, lon, lat0, lon0):
    '''Convert latitute to x,y coordinates in meters

    @param lat List of latitudes
    @param lon List on longitudes
    @param lat0 Origin of latitudes
    @param lon0 Origin of longitudes

    @return (x,y) coordinates in meters
    '''
    localProj = pyproj.Proj("+proj=tmerc +lon_0=%.9f +lat_0=%.9f +units=m" % (lon0, lat0))
    wgs84 = pyproj.Proj('+init=epsg:4326')
    (x,y) = pyproj.transform(wgs84, localProj, lon, lat)
    return x,y