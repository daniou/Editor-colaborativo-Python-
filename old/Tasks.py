class Tasks:
    taskList = []
    
    def __init__(self, tasks):
        self.taskList=tasks
    
    def __init__(self):
        self.taskList=[]
    
    def addTask(self,task):
        self.taskList.append(task)
    
    def delTask(self,task):
        self.taskList.pop(0)

    def append(self,task):
        self.taskList.append(task)

    def getNumTasks(self):
        return len(self.taskList)

    def getNextTask(self):
        return self.taskList[0]

    def nextTaskCompleted(self):
        self.taskList.pop(0)

class Task:
    # id=''
    path=''
    action =''
    content=''
    #pointer=''

    def __init__(self,id,path,action,content):
        # self.id = id
        self.path=path
        self.action=action
        self.content=content
    
    def __init__(self,args):
        # self.id = id
        self.path=args[0]
        self.action=args[1]
        self.content=args[2]
        # print(f"CONSTRUCTORA TASK {self.id}, {self.path}, {self.action}, {self.content}")
    
    def getFile(self):
        return self.path

    def getAction(self):
        return self.action

    def getContent(self):
        return self.content

    def getID(self):
        return self.id