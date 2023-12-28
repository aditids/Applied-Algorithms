#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem 1
def max_cherries(cake) :
    total_count = 0
    count = 0
    st = str(cake)
    c = 0 
    resultH = 0
    resultV = 0
    total_count = st.count('#')
    min = 1000
    for i in range(len(cake)):
        c = c + cake[i].count('#')
        #print("c",c)
        count = total_count - c
        if count<min and count!=0:
            min = count
            resultH = c
    #print("h",resultH)
    c = 0 
    total_count = st.count('#')
    count = 0
    min = 1000
    for i in range(len(cake[0])):
        #c = 0
        for j in range(len(cake)):
            if cake[j][i]=='#':
                c = c + 1
                
                #print("c",c)
                if c<=(total_count/2):
                    count = total_count - c
        
            if count<min and count!=0:
            #print("Count", count)
                min = count
                resultV = c
    
    return max(resultH, resultV)

input1= [['.', '#', '.'], ['#','.','.'], ['#','#','#']]
#input2= [['.','#','#','#','#'], ['.','.','.','.','.']]
print("Output =",max_cherries(input1))


# In[1]:


#Problem 2
def spy_locations ( heights ) :
    answer=[]
    answer.append(0)
    for i in range(1,len(heights)):
        if heights[i]>heights[i-1]:
                   answer.append(i)
    return answer


n = int(input("Enter number of buildings : "))
array = []
for i in range(0,n):
    array.append(int(input()))
result = spy_locations(array)
print("Output =")
for i in result:
    print(i)


# In[2]:


#Problem 3
def whos_the_winner (s,p) :
    k = s.find(p)
    l1 = k
    l2 = len(s)-(len(p)+l1)
    if l1==l2:
        return "Walter"
    return "Veidt"

print("Output =", whos_the_winner("Abcdefghij","cdef"))


# In[3]:


#Problem 4
def return_resultant_string (s,p) :
    k = ''
    if s.find(p):
        k=s.replace(p,'')
    return k

print("Output =",return_resultant_string('aababccbcabc','abc'))


# In[4]:


#Problem 5
def flip_game (s , queries ) :
    result = []
    str_list = list(s)
    for querry in queries:
        if querry=='get':
            result.append(str_list.count('1'))
        if querry=='flip':
            i = 0
            while True:
                if i>=len(str_list):
                    break
                if str_list[i]=='1':
                    str_list[i]='0'
                    break
                else:
                    if s[i]=='0':
                        str_list[i] = '1'
                i=i+1
            
    return result

queries=["get","flip","flip","get","flip","flip","flip","get"]
print(flip_game("0000101011",queries))


# In[5]:


#Problem 6
def calculate_points ( list ) :
    ans = []
    score = 0
    for i in list:
        if i=='D':
            x = ans[len(ans)-1]*2
            #print("in d",x, "i ",i, "f " ,ans[len(ans)-1])
            ans.append(x)
        if i=='I':
            x = ans.pop(len(ans)-1)
        if i=='+':
            x = ans[len(ans)-1] + ans[len(ans)-2]
            ans.append(x)
        if i=='-':
            x = abs(ans[len(ans)-1] - ans[len(ans)-2])
            ans.append(x)
        if i=='*':
            x = ans[len(ans)-1] * ans[len(ans)-2]
            ans.append(x)
        if i=='/':
            x = ans[len(ans)-2] // ans[len(ans)-1]
            ans.append(x)
        if i=='%':
            x = ans[len(ans)-1] % ans[len(ans)-2]
            ans.append(x)
        if i.lstrip('-').isdigit():
            #print(i)
            #print("***")
            ans.append(int(i))
            
        
    for i in ans:
        score = score+i
            
    return score

#list = ["5","2","I","D","+"]
#print("Output =",calculate_points(list))
list = ["5","-2","4","I","D","9","+","/"]
print("Output =",calculate_points(list))


# In[6]:


#Problem 7
class Node :
    def __init__ ( self , num , next = None ) :
        self . num = num
        self . next = next
        
class LinkedList():
    def __init__ (self):
        self.head = None   
        
    def Insert ( self , element , position ) :
        node = Node(element)
        prev = None
        temp = self.head
        if(position==1):
            node.next=self.head
            self.head = node
        else:    
            i = 1
            while(i!=position):
                prev = temp
                temp=temp.next
                i=i+1
            prev.next = node
            node.next = temp
            node.num = element
        
    def merge_linkedlists ( self, l2 ):
        #head = None
        temp = Node(0)
        tail = temp
        temp2 = l2.head
        temp1 = self.head
        while True:
            if temp1 is None:
                tail.next = temp2
                break
            if temp2 is None:
                tail.next = temp1
                break
            
            if temp1.num<=temp2.num:
                tail.next = temp1
                temp1=temp1.next
            else:
                tail.next = temp2
                temp2=temp2.next
            tail=tail.next
            
        return temp.next;
    
    
    def delete ( self , element ):
        temp = self.head
        if temp is not None:
            if temp.num == element:
                self.head = temp.next
                temp=None
                return
            while temp is not None:
                if temp.num == element:
                    break
                    #prev.next = temp.next
                prev = temp
                temp = temp.next
            
            if temp==None:
                return
            prev.next = temp.next
            temp = None
            
        
    
    def Update ( self , search_element , replace_element ) :
        flag = 0
        temp = self.head
        while flag ==0:
            if temp is None:
                flag = 1
            elif temp.num == search_element:
                temp.num = replace_element
                
                flag = 1
            else:
                temp = temp.next
                
    def Search ( self , element ):
        temp = self.head
        flag=0
        while flag ==0:
            if temp is None:
                flag = 1
            elif temp.num==element:
                flag=1
                return True
            else:
                temp=temp.next
        return False
                
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.num)
            temp = temp.next
            

l = LinkedList()
l.Insert(2,1)
l.Insert(3,2)
l.Insert(6,3)
l.Insert(14,4)
l.Insert(15,5)
print("After Insertion in list 1 =")
l.print()

l2 = LinkedList()
l2.Insert(1,1)
l2.Insert(4,2)
l2.Insert(5,3)
l2.Insert(7,4)
l2.Insert(10,5)
print("After Insertion in list 2 =")
l2.print()

print("After Deleting 2 from list 1 =")
l.delete(2)
l.print()

print("After Updating 6 to 11 from list 1 =")
l.Update(6,11)
l.print()

print("Searching for 12 in List 1 =")
print(l.Search(12))
print("Searching for 11 in List 1 =")
print(l.Search(11))

l.head = l.merge_linkedlists(l2)
print("Merge function on List 1 and List 2 =")
l.print()


# In[7]:


#Problem 8
def validate_order ( nums ) :
    nest = []
    tunnel = []
    count = 1
    for i in range(0,len(nums)):
        if nums[i]==count:
            nest.append(nums[i])
            count = count+1
            if tunnel[len(tunnel)-1] == count:
                flag=0
                while(flag == 0):
                    if len(tunnel)==0:
                        flag = 1
                    elif tunnel[len(tunnel)-1] != count:
                        flag = 1
                    else:
                        if tunnel[len(tunnel)-1] == count:
                            temp = tunnel.pop(len(tunnel)-1)
                            nest.append(temp)
                            count = count+1
                    
        else:
            if len(tunnel)==0:
                tunnel.append(nums[i])
            elif tunnel[len(tunnel)-1]<nums[i]:
                return 0
            elif tunnel[len(tunnel)-1]>nums[i]:
                tunnel.append(nums[i])
        
    return 1


#nums =  [4,5,1,3,2]
#print("Output =",validate_order(nums))
nums =  [5,3,2,1,4]
print("Output =",validate_order(nums))


# In[ ]:




