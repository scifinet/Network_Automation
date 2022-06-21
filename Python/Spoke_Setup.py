from tkinter import *
from tkinter.ttk import *
import os
import pexpect

def show_entry_fields():
    quit2button.grid_forget()
    confbutton.grid_forget()
    global ipaddr
    global subnet
    global gateway
    global username
    global password
    if static is True:
        ipaddr = ip.get()
        subnet = sub.get()
        gateway = gw.get()
        username = un.get()
        password = pw.get()
        print(ipaddr, subnet, gateway)
    elif dhcp is True:
        username = un.get()
        password = pw.get()
    master.destroy()

def router_connect():
    print("CONNECT")
    global un
    global pw
    global quit2button
    global confbutton
    if static is True:
        quitbutton.grid_forget()
        loginbutton.grid_forget()
        Label(master,
                text="Username").grid(row=0)
        Label(master,
                text="Password").grid(row=1)
        un = Entry(master)
        pw = Entry(master, show="*")
        un.grid(row=0, column=1)
        pw.grid(row=1, column=1)
        quit2button = Button(master,
                text='Quit',
                command=master.quit)
        quit2button.grid(row=2, column=0, sticky=W, pady=4)
        confbutton = Button(master,
                text='Configure', command=show_entry_fields)
        confbutton.grid(row=2, column=1, sticky=W, pady=4)
    elif dhcp is True:
        print("DHCP IS TURE")
        Label(master,
                text="Username").grid(row=0)
        Label(master,
                text="Password").grid(row=1)
        un = Entry(master)
        pw = Entry(master, show="*")
        un.grid(row=0, column=1)
        pw.grid(row=1, column=1)
        quit2button = Button(master,
                text='Quit',
                command=master.quit)
        quit2button.grid(row=2, column=0, sticky=W, pady=4)
        confbutton = Button(master,
                text='Configure', command=show_entry_fields)
        confbutton.grid(row=2, column=1, sticky=W, pady=4)

def dhcpb():
    global dhcp
    dhcp = True
    warning.grid_forget()
    dhcpbutton.grid_forget()
    staticbutton.grid_forget()
    print('DHCP')
    return router_connect()

def static():
    global static
    static = True
    warning.grid_forget()
    dhcpbutton.grid_forget()
    staticbutton.grid_forget()
    print('static')
    Label(master, text="IP Address").grid(row=0)
    Label(master, text="Subnet").grid(row=1)
    Label(master, text="Gateway").grid(row=2)
    global ip
    global sub
    global gw
    ip = Entry(master)
    sub = Entry(master)
    gw = Entry(master)
    ip.grid(row=0, column=1)
    sub.grid(row=1, column=1)
    gw.grid(row=2, column=1)
    global quitbutton
    quitbutton = Button(master, text='Quit', command=master.quit)
    quitbutton.grid(row=3, column=0, sticky=W, pady=4)
    global loginbutton
    loginbutton = Button(master, text='Router Credentials', command=router_connect)
    loginbutton.grid(row=3, column=1, sticky=W, pady=4)

master = Tk()

warning = Label(master, text='Warning: Make sure your computer\'s IP, Subnet, and Gateway are already configured to access the router!')
warning.grid(row=0)
dhcpbutton = Button(master, text='DHCP', command=dhcpb)
dhcpbutton.grid(row=1, column=0, pady=4)
staticbutton = Button (master, text='STATIC', command=static)
staticbutton.grid(row=2, column=0, pady=4)
staic = False
dhcp = False

mainloop()

default = os.popen("netstat -nr | grep default | awk \'NR == 1 { print $2 }\'").read()
host = default.strip('\n')
print(host)

def telnet():
    if static is True:
        child = pexpect.spawn('telnet '+host)
        child.expect('Username: ')
        child.sendline(username)
        child.expect('Password:')
        child.sendline(password)
        child.expect('#')
        child.sendline('conf t')
        child.expect('#')
        child.sendline('int g4')
        child.expect('#')
        child.sendline('no ip address')
        child.expect('#')
        child.sendline('ip address '+ipaddr+ ' '+subnet)
        child.expect('#')
        child.sendline('exit')
        child.expect('#')
        child.sendline('no ip route 72.34.128.163 255.255.255.255')
        child.expect('#')
        child.sendline('no ip route 72.34.128.163 255.255.255.255 dhcp')
        child.expect('#')
        child.sendline('ip route 72.34.128.163 255.255.255.255 '+gateway)
        child.expect('#')
        child.sendline('write memory')
        child.expect('[OK]')
        child.expect('#')
    elif dhcp is True:
        child = pexpect.spawn('telnet '+host)
        child.expect('Username: ')
        child.sendline(username)
        child.expect('Password:')
        child.sendline(password)
        child.expect('#')
        child.sendline('conf t')
        child.expect('#')
        child.sendline('int g4')
        child.expect('#')
        child.sendline('no ip address')
        child.expect('#')
        child.sendline('ip address dhcp')
        child.expect('#')
        child.sendline('exit')
        child.expect('#')
        child.sendline('no ip route 72.34.128.163 255.255.255.255')
        child.expect('#')
        child.sendline('ip route 72.34.128.163 255.255.255.255 dhcp')
        child.expect('#')
        child.sendline('write memory')
        child.expect('[OK]')
        child.expect('#')


telnet()
