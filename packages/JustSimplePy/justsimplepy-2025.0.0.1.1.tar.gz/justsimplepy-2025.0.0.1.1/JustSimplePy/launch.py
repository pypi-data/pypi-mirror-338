def make_me_a_bill(uid_custom = False,uidc = "uid-1"):
    listn = []
    listp = []

    def inputp():
        inputna = ""
        inputpr = 0
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        while inputna != "/end":
            inputna = str(input("Enter Product Name :"))
            if inputna == "/end":
                print("Stopping . . . ")
            else:
                inputpr = int(input("Enter Product Price :"))
                print(" ")
                listn.append(inputna)
                listp.append(inputpr)

    def formatbill():
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        valu = sum([number for number in listp])
        tax = float(input("Enter Tax val :"))
        valt = tax / 100 * valu + valu
        valf = int(valt)
        returnlist = [valu, tax, valt, valf]
        return returnlist

    def printout(valu, tax, valt, valf):
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("|  /")
        print("| /")
        print("|/")
        print("| \\")
        print("|  \\ BILL")
        print("-----------------------------")
        print("ITEMS------------------------")
        for items in listn:
            print(items)
        print("-----------------------------")
        print("PRICE------------------------")
        for price in listp:
            print(price)
        print("-----------------------------")
        print("Sub Total : " + str(valu))
        print("-----------------------------")
        print("Tax : " + str(tax))
        print("-----------------------------")
        print("After Tax : " + str(valt))
        print("-----------------------------")
        print("Final value : " + str(valf))
        print("-----------------------------")

    def makebill():
        print("Starting B.P. By Kshiraj Vij")
        print("Boot complete type UID")
        if uid_custom:
            uidi = str(input("UID :"))
            if uidi == uidc:
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                inputp()
                listb = formatbill()
                valu = listb[0]
                tax = listb[1]
                valt = listb[2]
                valf = listb[3]
                printout(valu, tax, valt, valf)
            else:
                raise SystemExit("Error-UID_NOT_IN_SYSTEM")
        else:
            uidi = str(input("UID :"))
            if uidi == "uid-1":
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                inputp()
                listb = formatbill()
                valu = listb[0]
                tax = listb[1]
                valt = listb[2]
                valf = listb[3]
                printout(valu, tax, valt, valf)
            else:
                raise SystemExit("Error-UID_NOT_IN_SYSTEM")
    makebill()
def char_find_ext():
    print('Welcome to char-fin-ext')
    typ = str(input('Choose Process - Find, Extract :'))
    txt = str(input('Enter text :'))
    if typ == 'Find':
        fnd = str(input('Enter Word or Char to find :'))
        out = txt.find(fnd) + 1
        print(out)
    elif typ == 'Extract':
        lent = str(len(txt))
        extract = int(input('Enter Number of char to extract (Out of ' + lent + ') :'))
        EXT = extract - 1
        bol = str(input('Enter Type +(True) -(False) :'))
        if bol == 'True':
            ext1 = int(EXT)
            print(txt[ext1])
        elif bol == 'False':
            ext2 = int(EXT - EXT - EXT)
            print(txt[ext2])
        else:
            print('error (Error - TYP_ERROR-BOOL) error code 2')
            raise SystemExit(2)
    else:
        print('error (Error - TYP_ERROR-FIND-EXTRACT) error code 1')
        raise SystemExit(1)

def txt_to_grid(returnt_f = False):
    grid = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    grid[0][0] = str(input("enter grid's 0:0 :"))
    grid[0][1] = str(input("enter grid's 0:1 :"))
    grid[0][2] = str(input("enter grid's 0:2 :"))
    grid[1][0] = str(input("enter grid's 1:0 :"))
    grid[1][1] = str(input("enter grid's 1:1 :"))
    grid[1][2] = str(input("enter grid's 1:2 :"))
    grid[2][0] = str(input("enter grid's 2:0 :"))
    grid[2][1] = str(input("enter grid's 2:1 :"))
    grid[2][2] = str(input("enter grid's 2:2 :"))
    input("Press enter to see the grid")
    input("See format 1 (Press Enter)")
    print(grid[0][0] + ' ' + grid[0][1] + ' ' + grid[0][2])
    print(grid[1][0] + ' ' + grid[1][1] + ' ' + grid[1][2])
    print(grid[2][0] + ' ' + grid[2][1] + ' ' + grid[2][2])
    input("See format 2 (Press Enter)")
    print(grid[0])
    print(grid[1])
    print(grid[2])
    input("See format 3 (Press Enter)")
    print(grid)
    if returnt_f:
        return grida

def send_this_to_sql(name_db,db_username,db_password,host,port,table_name,val1,val2):
    import psycopg2
    print("Starting transaction")
    db_data = {
        'dbname' : name_db,
        'user' : db_username,
        'password' : db_password,
        'host' : host,
        'port' : port
    }
    data_to_insert = {
        'column1': val1,
        'column2': val2
    }
    try:
        # Establishing the connection
        conn = psycopg2.connect(**db_data)
        cursor = conn.cursor()

        # Insert data into the table
        insert_query = "INSERT INTO " + table_name +" (column1, column2) VALUES (%s, %s)"
        print("Inserting Query : " + insert_query)
        cursor.execute(insert_query, (data_to_insert['column1'], data_to_insert['column2']))

        # Commit the transaction
        conn.commit()

        print("Data inserted successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
