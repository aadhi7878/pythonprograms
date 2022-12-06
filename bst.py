


class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


def nrinsert(root,data):
    node=Node(data)
    if(root==None):
        root=node
    else:
        p=None
        c=root
        while(c!=None):
            if(c.data>data):
                p=c
                c=c.left
            elif(c.data<data):
                p=c
                c=c.right
        if(p.data>data):
            p.left=node
        else:
            p.right=node
    return root
def rinorder(root):
    if root==None:
        return
    rinorder(root.left)
    print(root.data,end=" ")
    rinorder()
root=None
root=nrinsert(root,5)
root=nrinsert(root,23)
root=nrinsert(root,19)
root=nrinsert(root,7)
root=nrinsert(root,19)
root=nrinsert(root,90)
rinorder(root)
print(root.data)





    
