t = (3, 30, 2019, 9, 25)
dic = {
    'hour': t[0],
    'minute': t[1],
    'year': t[2],
    'month': t[3],
    'day': t[4]
}
print('%02d'%dic["month"], end = '/')
print('%02d'%dic["day"], end = '/')
print('%04d'%dic["year"], end = ' ')
print('%02d'%dic["hour"], end = ':')
print('%02d'%dic["minute"])