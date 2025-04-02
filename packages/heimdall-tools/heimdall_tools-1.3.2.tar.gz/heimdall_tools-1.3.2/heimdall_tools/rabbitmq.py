import pika
from pika.exceptions import AMQPConnectionError

def publish_message(queue_name, messages, host, username, password):
    """
    Publishes messages to the specified RabbitMQ queue.

    :param queue_name: The name of the queue to publish messages to.
    :param messages: List of messages to send.
    :param host: RabbitMQ server hostname or IP (default: '127.0.0.1').
    :param username: RabbitMQ username (default: 'admin').
    :param password: RabbitMQ password (default: 'admin').
    :return: True if messages were sent successfully, else False.
    """
    try:
        credentials = pika.PlainCredentials(username, password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host, credentials=credentials))
        channel = connection.channel()

        # Ensure the queue exists
        channel.queue_declare(queue=queue_name)

        # Send messages
        for message in messages:
            channel.basic_publish(exchange='', routing_key=queue_name, body=message)
            print(f"Message sent to {queue_name}: {message}")

        connection.close()
        return True

    except AMQPConnectionError:
        print("RabbitMQ connection failed.")
        return False


def consume_messages(queue_name, host, username, password, callback):
    """
    Consumes messages from the specified RabbitMQ queue with a custom callback.

    :param queue_name: The name of the queue to consume messages from.
    :param host: RabbitMQ server hostname or IP.
    :param username: RabbitMQ username.
    :param password: RabbitMQ password.
    :param callback: A function to process the consumed messages.
    :return: True if the consumer started successfully, else False.
    """
    try:
        credentials = pika.PlainCredentials(username, password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host, credentials=credentials))
        channel = connection.channel()

        # Ensure the queue exists
        channel.queue_declare(queue=queue_name)

        # Start consuming with the provided callback
        channel.basic_consume(queue=queue_name, on_message_callback=callback)
        print(f"Listening for messages on {queue_name}... Press CTRL+C to exit.")
        channel.start_consuming()
        return True

    except AMQPConnectionError:
        print("RabbitMQ connection failed.")
        return False
