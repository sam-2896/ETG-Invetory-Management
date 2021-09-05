from datetime import date
import json



def updatePerDayCal (dat,dic):
    with  open("date.json","r") as f:
        s =json.loads( f.read())
    
    if dat in s:
        
        for a in dic:
            if a in s[dat]:
                s[dat][a]+=dic[a]
            else:
                s[dat][a]=dic[a]
    else:
        s[dat] = dic
        
    with open ("date.json","w") as f:
        f.write(json.dumps(s))
    print("all updates registered successfully")


def viewDates():
    with  open("date.json","r") as f:
        s =json.loads( f.read())
    for x in s:
        print(f"sale of date {x} ..........")
        for y in s[x]:
            print(f"pid - {y}   quantity sold -  {s[x][y]}")

def viewSalesByDate():
    dat= input("Enter date = ")
    with  open("date.json","r") as f:
        s =json.loads( f.read())
        if dat in s:
        
            for a in s[dat]:
                print(f"pid - {a}   quantity sold -  {s[dat][a]}")
        else:
            print("wrong date")

#############            
def updatePrice():
    
    pid = input("enter following details,  pID -")
    n = input("new PRICE -") 
    

    with  open("pro.json","r") as f:
        s =json.loads( f.read())
    if pid in s:        
        s[str(pid)]["price(INR)"]= int(n)
    

        with open ("pro.json","w") as f:
            f.write(json.dumps(s))
        print("all updates registered successfully")
    else:
        print("invalid pid")


def updateName():
    pid = input("enter following details,  pID -")
    n = input("name -") 
    

    with  open("pro.json","r") as f:
        s =json.loads( f.read())
    s[str(pid)]["name"]= n
    

    with open ("pro.json","w") as f:
        f.write(json.dumps(s))
    print("all updates registered successfully")

def buy():
    d={}
    ll=[]
    t = 0
    with  open("pro.json","r") as f:
        s =json.loads( f.read())
    n = int(input("enter no of different product you buy - "))
    for x in range(n):
        pid = input("enter pid - ")
        q= int(input("enter Quantity - "))
        d[pid]=q
        s[pid]["qunatity"]-=q
        
        

        lll = [pid,s[pid]["name"],s[pid]["price(INR)"],q]
        ll.append(lll)

    with open ("pro.json","w") as f:
        f.write(json.dumps(s))
    print(".......YOUR BILL IS..........")
    for a in ll:
        print(f"   {a[1]}  ->  {a[2]}   X    {a[3]}   =     {int(a[2])*int(a[3])}"   )
        t = t + int(a[2])*int(a[3])
    print(f"............Total amount is   =>   {t}")
    
    dat = date.today()
    today = str((str(dat.day)+"-"+str(dat.month)+"-" + str(dat.year)[2::]))
    updatePerDayCal(today,d)

    with  open("sales.json","r") as f:
        o =json.loads( f.read())
    d2={}
    for x in ll:
        d2[str(x[0])]=x[3]
    
    o[str(len(o)+1)]=d2
    with open ("sales.json","w") as f:
        f.write(json.dumps(o))



def updateAll():
    pid = input("enter following details,  pID -")
    n = input("name -") 
    e = input ("exp date -" )
    q = int(input ("quantity -"))
    c = input ("category -")
    p = int(input("price(INR)"))

    with  open("pro.json","r") as f:
        s =json.loads( f.read())
    s[str(pid)]["name"]= n
    s[str(pid)]["qunatity"]= q
    s[str(pid)]["expdate"]= e
    s[str(pid)]["category"]= c
    s[str(pid)]["price(INR)"]= p

    with open ("pro.json","w") as f:
        f.write(json.dumps(s))
    print("all updates registered successfully")

def addnewInInventary():
    
    n = input("name -") 
    e = input ("exp date -" )
    q = int(input ("quantity -"))
    c = input ("category -")
    pr = int(input ("price -"))

    with  open("pro.json","r") as f:
        s =json.loads( f.read())
    p=1
    for x in s:
        if s[x]["name"] == n and int(pr) == int(s[x]["price(INR)"]):
            print("product already in Inventary")
            p=0
        
    if p ==1:
        l =len(s)
        pid = str(l+1)
        y = {"name": n,"qunatity": q,"price(INR)":pr,"expdate": e,"category": c}
        s[str(pid)] = y

        with open ("pro.json","w") as f:
            f.write(json.dumps(s))
        print(f"...........pid for {n} is {pid}.............")    
        print("all updates registered successfully")        


def updateQunatity():
    pid = input("enter following details,  pID -")
    
    q = int(input ("quantity -"))
    
    print(f"current quntity is {q}")
    print(f"to increse Quantity BY {q} press 1")
    print(f"to set net Quantity TO {q} press 2")
    l =int(input())
    with  open("pro.json","r") as f:
        s =json.loads( f.read())
    if l == 2:
        s[str(pid)]["qunatity"]= q
        print(f"now net Quantity is {q}")
    else:
        (s[str(pid)]["qunatity"])+= q
        y =s[str(pid)]["qunatity"]
        print(f"now net Quantity is {y}")
    with open ("pro.json","w") as f:
        f.write(json.dumps(s))
    print("all updates registered successfully")

def updateCategory():
    pid = input("enter following details,  pID -")
   
    c = input ("category -")

    with  open("pro.json","r") as f:
        s =json.loads( f.read())
    s[str(pid)]["category"]= c

    with open ("pro.json","w") as f:
        f.write(json.dumps(s))
    print("all updates registered successfully")

def showByCategory():
    with  open("pro.json","r") as f:
        s =json.loads( f.read())
    c = input ("category -")
    for k in s:
        if s[k]["category"]==c:
            n= s[k]["name"]
            q= s[k]["qunatity"]
            e =s[k]["expdate"]
            
            print(f"""
            pid - {k}
            name - {n}
            exp date  - {e} (if -1 = no expdate)
            Quantity - {q}""")

def seeAll():
    with  open("pro.json","r") as f:
        s =json.loads( f.read())
    
    for k in s:
            n= s[k]["name"]
            q= s[k]["qunatity"]
            e =s[k]["expdate"]
            c =s[k]["category"]
            p =s[k]["price(INR)"]
            print(f"""
            pid - {k}
            name - {n}
            exp date  - {e} (if -1 = no expdate)
            Quantity - {q}
            price - {p} INR
            category - {c}""")

def seeByPID():
    with  open("pro.json","r") as f:
        s =json.loads( f.read())

    k = str(input("enter pid - "))
    if k in s:
        n= s[k]["name"]
        q= s[k]["qunatity"]
        e =s[k]["expdate"]
        c =s[k]["category"]
        p =s[k]["price(INR)"]
        print(f"""
        pid - {k}
        name - {n}
        exp date  - {e} (if -1 = no expdate)
        Quantity - {q}
        price - {p} INR
        category - {c}""")
    else:
        print("invalid pid")

    
###sales



def viewDetailByBillNo():
    n = input("Enter bill no - ")
    with  open("sales.json","r") as f:
        s =json.loads( f.read())

    with  open("pro.json","r") as f:
        g =json.loads( f.read())

    d = s[n]
    print(f"bill history of bill no - {n}")
    v=1
    for x in d:
        h=g[x]["name"]
        print(f"{v})  -  {h}  ,pid - {x}  ,quantity - {d[x]}  ")
        v=v+1    


viewDetailByBillNo()