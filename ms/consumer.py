import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ms.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://nootuozb:5xwi64mxmutYbMpX6e74v1iPEsEJ7jZL@armadillo.rmq.cloudamqp.com/nootuozb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased')

channel.basic_consume(queue='admin',on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()