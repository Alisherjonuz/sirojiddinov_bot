def check_id(z):
    f = open('chat_id.txt','r')
    list = f.read().split(',')
    a=0
    for i in list:
        if z==int(i):
            a+=1
    if a!=0:
        return 1
    else:
        return 0
    f.close()

def id_add(i):
    f = open('chat_id.txt', 'a')
    f.write(','+str(i))
    f.close()
def reklama():
    f =  open('chat_id.txt', 'r')
    list = f.read().split(',')
    # return len(list)
    f.close()
def users():
    f =  open('chat_id.txt', 'r')
    list = f.read().split(',')
    return len(list)
    f.close()