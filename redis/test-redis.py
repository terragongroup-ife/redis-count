import redis

def main():
    r = redis.StrictRedis(host='localhost', port='6379', db='0')
    r.set('name', 'Atuma')
    print(r.get('name'))
    print(r.exists('name'))
    print(r.exists('age'))


if __name__ == '__main__':
    main()
