import requests
import threading


class MyThread(threading.Thread):

    def __init__(self, * args, **kwargs):
        threading.Thread.__init__(self)
        self.result = 0

    def run(self):
        print('Start run...')
        self.my_process()
        print('End run...')
        # requests.get('http://localhost:8000/person/')

    def my_process(self):
        print('Sart my_process.')
        for i in range(11):
            print(i)
        self.result = i
        print('End my_process.')
        context = {'result': self.result}
        self.cb(self, **context)

    def cb(self, *args, **kwargs):
        '''
        Callback
        '''
        print('Callback!', 'result:', kwargs['result'])
