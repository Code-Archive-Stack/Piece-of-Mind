import redis
from faker import Faker 
redis_server =  redis.Redis(host='localhost', port=6379,db=0, decode_responses=True)

def dumpster_data():
    # fake = Faker('en_US')
    
    # a=0
    # n = 1
    # while n > 0:
    #     a += 1

    #     payload =redis_server.hset(f'fake-data:',mapping={
    #         'name':fake.name(),
    #         "Surname":fake.last_name(),
    #         "IP":fake.ipv4(),
    #         "number":fake.random_digit_above_two()
    #     })
    #     print(payload)

    redis_server.hset('user-session:1', mapping={
    'name': 'red',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
    })
    redis_server.hset('user-session:2', mapping={
    'name': 'green',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
    })
    redis_server.hset('user-session:3', mapping={
    'name': 'blue',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
    })





def fetch_redis():
     fetch = redis_server.hgetall('user-session:3')
     print(fetch)   

if __name__ == "__main__":
    # dumpster_data()
    fetch_redis()
