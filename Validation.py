import Tkinter as TK
import pickle as PI

##fi = open('results.txt', 'r')
##rl = fi.readlines()
##fi.close()

#fi = open('bills0129may103.csv', 'r')
fi = open('bills03_00.csv', 'r')
bi_rl = fi.readlines()
fi.close()

print 'len(bi_rl) = ', len(bi_rl)



################# Data Structures

###     Python dictionnaries
GeDI = {}
NameGe = {}
Summary = {}
LinVolDI = {}
RecDI = {}
LaDI = {}
OutflowDI = {}
CodeFlowDI = {}

NameDI = {} # NameDI[name] = [gestory_code0, gestory_code1 ..] 
############ Python lists
PrimLI = []


#####

sample__array = [
            ['1',8],
            ['2',4],
            ['3',9],
            ['4',10]
         ]
AbsLI = []


def Get__summ():

    
    lindate = '03/06/2014'
#    lindate = '29/05/2014'
    Get__summ__for__the__day(lindate)

    
def Get__summ__for__the__day(lindate):

    
    total = 0
    
#    limit = 100
    limit = len(PrimLI) - 1

    
    for y in range(limit):
        all_data_lines = PrimLI[y]
        header = all_data_lines[0]
        sl = header.split(';')
        lin_date = sl[8]
        shop = sl[6]
        number = sl[3]
        
        if lin_date == lindate:
            sel__lx.insert(TK.END, y)            
            print number
            data_lines = all_data_lines[1:-1]
            for x in range(len(data_lines)):
                line = data_lines[x]
                ss = line.split(';')
                summa = float(ss[5])
                total += summa
##                

            
    
    print 'total: ', total





def Get__shop__id():

    limit = len(PrimLI) - 1
#    clean__lx('data')
    
    for y in range(limit):
        all_data_lines = PrimLI[y]
        header = all_data_lines[0]
        sl = header.split(';')
        lin_date = sl[8]
        shop = sl[6]
        number = sl[3]
        if lin_date[:2] == '18':
            print y, lin_date, shop, number
   

def Get__absent__checks():

    fna__small = 'imported.txt'
    fi = open(fna__small, 'r')
    rl = fi.readlines()
    fi.close()

    for line in rl:
        line = line.strip()
        AbsLI.append(line)
        
    total = 0

    #limit = 100
    limit = len(PrimLI) - 1
    clean__lx('data')
    
    for y in range(limit):
        all_data_lines = PrimLI[y]
        header = all_data_lines[0]
        sl = header.split(';')
        lin_date = sl[8]
        shop = sl[6]
        number = sl[3]
        
        if lin_date[:2] == '18' and shop == '101' and number not in AbsLI:
            sel__lx.insert(TK.END, y)            
            print number
            data_lines = all_data_lines[1:-1]
            for x in range(len(data_lines)):
                line = data_lines[x]
                ss = line.split(';')
##                summa = float(ss[5])
##                total += summa
##                

            
    print 'Get__absent__checks: done'
    print 'total: ', sel__lx.size()
#    print 'total summa:', total
    

    

def Get__relevant__checks():

    total = 0

    #limit = 100
    limit = len(PrimLI) - 1
    clean__lx('data')
    
    for y in range(limit):
        all_data_lines = PrimLI[y]
        header = all_data_lines[0]
        sl = header.split(';')
        lin_date = sl[8]
        shop = sl[6]
        number = sl[3]
        
        if lin_date[:2] == '18' and shop == '101':
            sel__lx.insert(TK.END, y)            
            print number
            data_lines = all_data_lines[1:-1]
            for x in range(len(data_lines)):
                line = data_lines[x]
                ss = line.split(';')
                summa = float(ss[5])
                total += summa
                

            
    print 'Get__relevant__checks: done'
    print 'total: ', sel__lx.size()
    print 'total summa:', total













    

def Evaluate__len__lines():

#    limit = 100
    limit = len(PrimLI) - 1
    
    for y in range(limit):
        all_data_lines = PrimLI[y]
        data_lines = all_data_lines[1:-1]
        for x in range(len(data_lines)):
            line = data_lines[x]
            if '\n' not in line:
                print line
                
##            sl = line.split(';')
##            if len(sl) != 29:
##               print len(sl)
##               print line
##               print '================'







            

def Get__singles():

    limit = 10
    limit = len(PrimLI)
    
    for y in range(limit):
        all_data_lines = PrimLI[y]
        data_lines = all_data_lines[1:-1]
        for x in range(len(data_lines)):
            line = data_lines[x]
            sl = line.split(';')
            price = sl[8]
            ge_id = sl[9]
            name = sl[17]
            
            if name in PrimLI:
                print name
                NameDI[name].append(ge_id)
            else:
                NameDI[name] = []
                NameDI[name].append(ge_id)
    print 'Get__singles: done'                
#            print ge_id, name
        

    

def Load__Summary():

    fi = open('Summary.li', 'rb')
    ld = PI.load(fi)
    fi.close()

    for k,v in ld.items():
        Summary[k] = v       

        
    print 'Load___Summary: done'


def Dump__Summary():

    fi = open('Summary.li', 'wb')
    PI.dump(Summary, fi)
    fi.close()

    print 'Dump__Summary: done'

    


def Print__CodeFlowDI():

    print '======  CodeFlowDI  ======='
    for k, v in CodeFlowDI.items():
        print k, ':', v
    print '=============================='

    
def Fill__CodeFlowDI():

    for k, v in LaDI.items():

        ## 0
        gest_code = k
        data_list = v
        if gest_code in Summary:
            sum_dal = Summary[gest_code]['sum_dal']
     
            ## 1        
            Flow = Subtract(sum_dal, data_list)
            for fl__line in Flow:
                code = fl__line[0]
                volume = fl__line[1]
                if code in CodeFlowDI:
                    CodeFlowDI[code] += volume
                else:
                    CodeFlowDI[code] = volume
                    
        else:
            print 'not found', gest_code
        
    print 'Fill__CodeFlowDI: done'
    

def Print__OutflowDI():

    for k, v in OutflowDI.items():

        print k, v

def Fill__Outflow():

    for k, v in LaDI.items():

        ## 0
        gest_code = k
        data_list = v
        if gest_code in Summary:
            sum_dal = Summary[gest_code]['sum_dal']
     
            ## 1        
            Flow = Subtract(sum_dal, data_list)

            ## 2
            OutflowDI[gest_code] = Flow
        else:
            print 'not found', gest_code
        
    print 'Fill__Outflow: done'
    

def Subtract(flow_amount, array):

    '''flow_amount: amount to subtract'''

    fa = flow_amount

    Flow = []
    
    for data__line in array:
#        print data__line
        ## variables assingment
        name = data__line[0]
        amt = data__line[1] ## current amount
        ## data transformation

        fl_line = [name, amt]

        if fa >= amt:            
            fa -= amt
            Flow.append(fl_line)
        elif  fa < amt:
            fl_line[1] = fa
            Flow.append(fl_line)
            break
    

    return Flow




def Print__LaDI():

    for k, v in LaDI.items():
        print k, v
    print '==============='

    

def Fill__LaDI():


    for k, v in RecDI.items():

        ## variables assignment
        name = k
        datalist = v

        ## Data transformation

        if name in NameGe.keys():
            ge__code = NameGe[name]

        ## DS fill

            LaDI[ge__code] = datalist
            
    print 'len(RecDI) = ', len(RecDI)        
    print 'len(LaDI) = ', len(LaDI)        
    print 'Fill__LaDI: done'
    

def Load__RecDI():

    fi = open('RecDI.li', 'rb')
    loaded = PI.load(fi)
    fi.close()

    for k, v in loaded.items():
        RecDI[k] = v 

    print 'Load__RecDI: done'



def Printout__volume():

    
    OL = []
    for k, v in Summary.items():
        name = v['name']
        lin_volume = v['lin_volume']
        dal = v['dal']
        sum_dal = v['sum_dal']
        amt = v['amt']

        oline = [sum_dal, amt, name]
        OL.append(oline)
        
    OL.sort()
    OL.reverse()

    for oline in OL:
        dal, amount,  name = oline[0], oline[1], oline[2]
        print dal, amount,  name 

        
#        print sum_dal,':', dal, ':', name        


def Evaluate__volume():

    fi = open('expkat.txt', 'r')
    nomrl = fi.readlines()
    fi.close()

    print 'len(rl) = ', len(rl)
    
    for line in nomrl:
        sl = line.split(';')
        code = sl[6]
        lin_volume = sl[21]
        if code in Summary.keys():
            lin_volume = sl[21]
            if lin_volume[0] == '.':
                lin_volume = '0'+lin_volume
                
            Summary[code]['lin_volume'] = lin_volume
            volume = float(lin_volume)
            Summary[code]['volume'] = volume
            dal = volume/10
            Summary[code]['dal'] = dal

            amount = Summary[code]['amt']
            sum_dal = amount * dal
            Summary[code]['sum_dal'] = sum_dal
            
            
                
    print 'Evaluate__volume: done'                    

def Printout__summary():

    OL = []
    for k, v in Summary.items():
        amount = v['amt']
        name = v['name']

        oline = [amount,  name]
        OL.append(oline)
        
    OL.sort()
    OL.reverse()

    for oline in OL:
        amount,  name = oline[0], oline[1]
        print amount,  name 

def Get__summary():

#    limit = 100
    limit = len(PrimLI)
    Al__keys = GeDI.keys()
    for y in range(limit):
        data__list = PrimLI[y]

        ### get positions
        for line in data__list[1:-1]:
            try:
                sl = line.split(';')
                code = sl[9]
                name = sl[17]
                lin__amount = sl[7]
                price = sl[8]

                ### data transformation
##                if lin__amount[0] == '.':
##                    lin__amount = '0'+lin__amount                
##                
##                amount = float(lin__amount)
                amount = int(lin__amount)

                #### Fill DI (Gamma)
                if code in Al__keys:
                    if code not in Summary.keys():
                        Summary[code] = {}
                        Summary[code]['amt'] = amount
                        Summary[code]['name'] = name
                        
                    elif code in Summary.keys():
                        Summary[code]['amt'] += amount
            except:
                pass
                    
                    
                    
##                print name
##                print code, amount, price
            
    print 'Get__summary: done'            
        



def Bills__primary__parsing():

    PrimLI.append([])
    inx = 0

    #limit = 500
    limit = len(bi_rl) - 1 ## last patch is not informative
    
    for y in range(limit):
        line = bi_rl[y]
        if '===>>===' not in line:
            PrimLI[inx].append(line)
        elif '===>>===' in line:
            inx += 1
            PrimLI.append([])
            
    print 'Bills__primary__parsing: done'      
            
        


######## accessories

def format__line__for__TK(line):

    line = line.decode('cp1251').encode('utf-8')

    return line
    

def prepare__array__for__TK(data__list):

    array = []
    
    for line in data__list:
        line = format__line__for__TK(line)
        array.append(line)

    return array










def Fill__GeDI():
    
    for y in range(len(rl)):
        line = rl[y]
        line = line.strip()
        sl = line.split(':')

        code = sl[0]
        code = code.strip()

        name = sl[1]
        name = name.strip()

        GeDI[code] = name
        NameGe[name] = code
    print 'len(NameGe) = ', len(NameGe)
    print 'len(GeDI) = ', len(GeDI)
    print 'Fill__GeDI: done'    

######################  Tkinter 
root = TK.Tk()
root.title('Evaluation of observed singles')

FRA = {}
LX = {}

FRA[0] = TK.Frame(root)
FRA[0].grid(row = 1, column = 1)

FRA[1] = TK.Frame(root)
FRA[1].grid(row = 2, column = 1)

def clean__lx(lx__name):

    ref__lx = LX[lx__name]
    sz = ref__lx.size()
    if sz > 0:
        for y in range(sz):
            ref__lx.delete(0)
            
    
def Fill__lx(lx__name, array):

    clean__lx(lx__name)

    ref__lx = LX[lx__name]
    for line in array:
        ref__lx.insert(TK.END, line)

############ reflections
        
def reflect__inx(event):

    if inx__lx.size() > 0:
        clean__lx('data')

        cs = int(inx__lx.curselection()[0])
        line = inx__lx.get(cs)
        inx = int(line)

        DataList = PrimLI[inx]
        array = prepare__array__for__TK(DataList)
        Fill__lx('data', array)




inx__lx = TK.Listbox(FRA[0])
inx__lx.grid(row = 2, column = 1)
inx__lx['width'] = 5
inx__lx.bind('<KeyRelease>', reflect__inx)
inx__lx.bind('<ButtonRelease>', reflect__inx)
LX['inx'] = inx__lx


data__lx =  TK.Listbox(FRA[0])
data__lx['width'] = 200
data__lx.grid(row = 2, column = 2)
LX['data'] = data__lx

def reflect__sel(event):

    if sel__lx.size() > 0:
        clean__lx('data')

        cs = int(sel__lx.curselection()[0])
        line = sel__lx.get(cs)
        inx = int(line)

        DataList = PrimLI[inx]
        array = prepare__array__for__TK(DataList)
        Fill__lx('data', array)


sel__lx = TK.Listbox(FRA[1]) ## selected subset
sel__lx.grid(row = 2, column = 1)
sel__lx['width'] = 5
sel__lx.bind('<KeyRelease>', reflect__sel)
sel__lx.bind('<ButtonRelease>', reflect__sel)
LX['sel'] = sel__lx


######################  Menu

m__0 = TK.Menu(root)

m__0__0 = TK.Menu(m__0)
m__0__0.add_command(label = 'Get__summary', command = Get__summary)
m__0__0.add_command(label = 'Printout__summary', command = Printout__summary)
m__0__0.add_command(label = 'Dump__Summary', command = Dump__Summary)
m__0__0.add_command(label = 'Load__Summary', command = Load__Summary)
m__0__0.add_separator()
m__0__0.add_command(label = 'Evaluate__volume', command = Evaluate__volume)
m__0__0.add_command(label = 'Printout__volume', command = Printout__volume)
m__0__0.add_command(label = 'Evaluate__len__lines', command = Evaluate__len__lines)
m__0__0.add_separator()
m__0__0.add_command(label = 'Get__relevant__checks', command = Get__relevant__checks)
m__0__0.add_command(label = 'Get__absent__checks', command = Get__absent__checks)
m__0__0.add_command(label = 'Get__shop__id', command = Get__shop__id)




m__0__1 = TK.Menu(m__0)
m__0__1.add_command(label = 'Load__RecDI', command = Load__RecDI)
m__0__1.add_command(label = 'Fill__LaDI', command = Fill__LaDI)
m__0__1.add_command(label = 'Print__LaDI', command = Print__LaDI)
m__0__1.add_command(label = 'Fill__Outflow', command = Fill__Outflow)
m__0__1.add_command(label = 'Print__OutflowDI', command = Print__OutflowDI)
m__0__1.add_command(label = 'Fill__CodeFlowDI', command = Fill__CodeFlowDI)
m__0__1.add_command(label = 'Print__CodeFlowDI', command =Print__CodeFlowDI)
m__0__1.add_separator()
m__0__1.add_command(label = 'Get__singles', command = Get__singles)
m__0__1.add_command(label = 'Get__summ', command = Get__summ)


m__0.add_cascade(label = 'Evaluate', menu = m__0__0)
m__0.add_cascade(label = 'Subtraction', menu = m__0__1)

root.config(menu = m__0)

############################################################################


##################### Start

def Fill__bill__inxx():

    lena = len(PrimLI)
    array = range(lena)
    Fill__lx('inx', array)

def Starting__fills():

    Fill__bill__inxx()    

def Start():

#    Fill__GeDI()
    Bills__primary__parsing()

    Starting__fills()

Start()

    
