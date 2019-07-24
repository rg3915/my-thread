import requests
import threading


class MyThread(threading.Thread):

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self)
        print('__init__')

    def run(self):
        print('Start run...')
        self.my_process()
        print('End run...')
        # requests.get('http://localhost:8000/person/')
        print('Chamar my_process2...')
        self.my_process2()

    def my_process(self):
        print('Sart my_process.')
        for i in range(11):
            print(i)
        print('End my_process.')

    def my_process2(self):
        print('Start my_process2.')
        for i in range(11):
            print(i * 2)
        print('End my_process2.')
