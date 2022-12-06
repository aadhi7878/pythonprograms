from threading import Thread
class mythread(Thread):
    def fun():
        for i in range(5):
            print("child thread")

            # print("thread is running:",current_thread().getName())   
    # print(current_thread().getName())       
t=mythread()
t.start()
# t.setName('aditya')
# print(t.name)
for i in range(5):
    print("main thread")
    # current_thread().setName('father of aditya')
    # print(current_thread().getName())

