import base64
import hashlib

coffees = {
    'covfefe': 'rO0ABXNyABJjb2ZmZWUuQ292ZmVmZUJlYW4AAAAAAAAAAQIAAHhyAAtjb2ZmZWUuQmVhbgAAAAAAAAABAgAETAAHaW5oZXJpdHQADUxjb2ZmZWUvQmVhbjtMAARuYW1ldAASTGphdmEvbGFuZy9TdHJpbmc7TAAHcGFyZW50MXEAfgACTAAHcGFyZW50MnEAfgACeHBwdAAHQ292ZmVmZXBw-7ed88df1a47853cf4f9b8b404a10ae50320765a8918ba2fa9960bb17585466f9',
    'mg': 'rO0ABXNyAA1jb2ZmZWUuTUdCZWFuAAAAAAAAAAECAAB4cgALY29mZmVlLkJlYW4AAAAAAAAAAQIABEwAB2luaGVyaXR0AA1MY29mZmVlL0JlYW47TAAEbmFtZXQAEkxqYXZhL2xhbmcvU3RyaW5nO0wAB3BhcmVudDFxAH4AAkwAB3BhcmVudDJxAH4AAnhwcHQAAk1HcHA=-0d5179f2f856f92d555e9a017b098234b111acbc14b72bde4c9a5e94672d807f',
    'raid': 'rO0ABXNyAA9jb2ZmZWUuUmFpZEJlYW4AAAAAAAAAAQIAAHhyAAtjb2ZmZWUuQmVhbgAAAAAAAAABAgAETAAHaW5oZXJpdHQADUxjb2ZmZWUvQmVhbjtMAARuYW1ldAASTGphdmEvbGFuZy9TdHJpbmc7TAAHcGFyZW50MXEAfgACTAAHcGFyZW50MnEAfgACeHBwdAAEUmFpZHBw-88102edd33ce49771e9c3dae53dd70660484ccaedd4271a93dd8c374a93ede99',
    'God': 'rO0ABXNyAAtjb2ZmZWUuQmVhbgAAAAAAAAABAgAETAAHaW5oZXJpdHQADUxjb2ZmZWUvQmVhbjtMAARuYW1ldAASTGphdmEvbGFuZy9TdHJpbmc7TAAHcGFyZW50MXEAfgABTAAHcGFyZW50MnEAfgABeHBzcgAPY29mZmVlLlJhaWRCZWFuAAAAAAAAAAECAAB4cQB+AABwdAAEUmFpZHBwdAADR29kcQB+AAVzcgANY29mZmVlLk1HQmVhbgAAAAAAAAABAgAAeHEAfgAAcHQAAk1HcHA=-1b8a98dbe2b17ac022af92f39fbdb68e1bcd881d846ebc379b59d077e34dbb1d',
}

for key in coffees:
    s = coffees[key]
    with open('%s_serial' % key, 'wb') as f:
        f.write(base64.b64decode(s[:s.index('-')]))
    with open('%s_hash' % key, 'wb') as f:
        f.write(s[s.index('-')+1:].decode('hex'))

FLAG_BEAN = 'rO0ABXNyAA9jb2ZmZWUuRmxhZ0JlYW4AAAAAAAAAAQIAAHhyAAtjb2ZmZWUuQmVhbgAAAAAAAAABAgAETAAHaW5oZXJpdHQADUxjb2ZmZWUvQmVhbjtMAARuYW1ldAASTGphdmEvbGFuZy9TdHJpbmc7TAAHcGFyZW50MXEAfgACTAAHcGFyZW50MnEAfgACeHBwdAAERmxhZ3Bw'
SALT = 'c@ram31m4cchi@o'

print '%s-%s' % (FLAG_BEAN, hashlib.sha256(FLAG_BEAN+SALT).hexdigest())