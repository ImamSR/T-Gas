import pika, json

params = pika.URLParameters('amqps://nootuozb:5xwi64mxmutYbMpX6e74v1iPEsEJ7jZL@armadillo.rmq.cloudamqp.com/nootuozb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)

    channel.basic_publish(exchange='',routing_key='admin',body=json.dumps(body), properties=properties)