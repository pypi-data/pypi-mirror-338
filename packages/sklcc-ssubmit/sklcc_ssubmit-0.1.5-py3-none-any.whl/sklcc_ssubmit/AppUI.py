import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_TEXT, DND_FILES
from sklcc_ssubmit.thread_func import thread_func

class UI(object):
    def __init__(self, window, App):
        self.root=window
        self.App=App
        win_w,win_h=(1280,720)
        # win_w,win_h=(1366,768)
        # window.option_add("*Font", ("Times New Roman", 10))

        screen_w, screen_h=window.maxsize()
        x=int((screen_w-win_w)/2)
        y=int((screen_h-win_h)/2)
        window.title("Slurm作业提交器")
        window.geometry(f"{win_w}x{win_h}+{x}+{y}")
        # window.iconphoto(False,tk.PhotoImage(file='Hust_HPC.png')

        menu=tk.Menu(window)
        window.config(menu=menu)

        menu.add_command(label="导入配置", command=App.open_cfg)
        menu.add_command(label="保存配置", command=App.save_cfg)
        menu.add_command(label="设为默认", command=App.save_cfg_default)

        statusbar_Frame=tk.Frame(window, bd=1, relief=tk.SUNKEN)
        statusbar_Frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.statusbar=tk.Label(statusbar_Frame, text="Starting...")
        self.statusbar.pack(side=tk.LEFT, anchor=tk.W)
        self.serverstatusbar=tk.Label(statusbar_Frame, text="未连接服务器")
        self.serverstatusbar.pack(side=tk.RIGHT)

        self.def_FileFrame()
        self.def_SetFrame()
        self.def_BashFrame()
           
        # self.sshc_transport=self.sshc.client.get_transport()

        
        
    

    def def_FileFrame(self):
        self.File_Frame=tk.Frame(self.root)
        self.File_Frame.pack(padx=(20,10), pady=20, side=tk.LEFT, anchor=tk.W, fill=tk.Y)

        Login_Frame=tk.Frame(self.File_Frame, relief=tk.SUNKEN, bd=1)
        Login_Frame.pack(side=tk.TOP)

        
        LoginLabel_Frame=tk.Frame(Login_Frame)
        LoginEntry_Frame=tk.Frame(Login_Frame)
        LoginButton=tk.Button(Login_Frame, text="登录", width=10, height=3, command=lambda :thread_func(self.App.Login))
        LoginLabel_Frame.pack(side=tk.LEFT, padx=5)
        LoginEntry_Frame.pack(side=tk.LEFT, padx=5)
        LoginButton.pack(side=tk.LEFT, padx=5)


        Server_Label=tk.Label(LoginLabel_Frame, text="服务器")
        Username_Label=tk.Label(LoginLabel_Frame, text="用户名")
        Password_Label=tk.Label(LoginLabel_Frame, text="密码")
        Server_Label.pack(side=tk.TOP, pady=5, anchor=tk.E)
        Username_Label.pack(side=tk.TOP, pady=5, anchor=tk.E)
        Password_Label.pack(side=tk.TOP, pady=5, anchor=tk.E)

        ServerEntry_Frame=tk.Frame(LoginEntry_Frame)
        self.Server_Entry=tk.Entry(ServerEntry_Frame, width=14)
        ServerColon_Label=tk.Label(ServerEntry_Frame, text=":")
        self.ServerPort_Entry=tk.Entry(ServerEntry_Frame, width=5)
        self.Username_Entry=tk.Entry(LoginEntry_Frame, width=21)
        self.Password_Entry=tk.Entry(LoginEntry_Frame, show="·", width=21)
        ServerEntry_Frame.pack(side=tk.TOP, pady=5)
        self.Server_Entry.pack(side=tk.LEFT)
        ServerColon_Label.pack(side=tk.LEFT)
        self.ServerPort_Entry.pack(side=tk.RIGHT, padx=(2,0))
        self.Username_Entry.pack(side=tk.TOP, pady=5)
        self.Password_Entry.pack(side=tk.TOP, pady=5)
        self.Password_Entry.bind("<Return>", self.App.Login)

        FileManager_Frame=tk.Frame(self.File_Frame)
        FileManager_Frame.pack(pady=(5,0), side=tk.TOP, expand=True, fill=tk.BOTH)

        CurrentDir_Frame=tk.Label(FileManager_Frame)
        CurrentDir_Frame.pack(side=tk.TOP, fill=tk.X)

        CurrentDir_Label=tk.Label(CurrentDir_Frame, text="当前目录")
        CurrentDir_Label.pack(side=tk.LEFT, pady=(0,0))
        self.CurrentDir_Path=tk.Entry(CurrentDir_Frame)
        self.CurrentDir_Path.pack(side=tk.LEFT, expand=True, fill=tk.X, anchor=tk.W, padx=(5,0))
        self.CurrentDir_Path.bind("<Return>", lambda *args: self.App.c_cd(self.CurrentDir_Path.get().strip()))

        
        ToDir_But=tk.Button(CurrentDir_Frame, text="转到", command=lambda: self.App.c_cd(self.CurrentDir_Path.get().strip()))
        ToDir_But.pack(side=tk.RIGHT, padx=(5,0))

        FileButton_Frame1=tk.Frame(FileManager_Frame)
        FileButton_Frame1.pack(side=tk.TOP, pady=(5,5), fill=tk.X)
        
        File_Up_Button=tk.Button(FileButton_Frame1, text="上级目录", command=self.App.c_cd_up)
        File_Up_Button.pack(side=tk.LEFT, padx=(5,5))
        File_Up_Button=tk.Button(FileButton_Frame1, text="用户目录", command=self.App.c_cd_u)
        File_Up_Button.pack(side=tk.LEFT, padx=(0,5))
        File_Up_Button=tk.Button(FileButton_Frame1, text="刷新⟳", command=self.App.c_refresh)
        File_Up_Button.pack(side=tk.RIGHT, padx=(5,0))

        self.FileManager_Listbox=tk.Listbox(FileManager_Frame, selectmode=tk.EXTENDED)
        DownloadBut=tk.Button(self.FileManager_Listbox, text="下载⏬", command=lambda :thread_func(self.App.DragDown))
        DownloadBut.pack(side=tk.TOP, anchor=tk.E, padx=(0,3), pady=(5,0))
        self.FileManager_Listbox.config()
        self.FileManager_Listbox.pack(side=tk.TOP,expand=True, fill=tk.BOTH, pady=(0,5))

        self.FileManager_Listbox.bind("<Double-Button-1>", self.App.FM_double_click)
        self.FileManager_Listbox.bind("<Button-3>", self.App.w_popout)



        

    def def_SetFrame(self):
        self.Set_Frame=tk.Frame(self.root)
        self.Set_Frame.pack(padx=10, pady=20, side=tk.LEFT, anchor=tk.W, fill=tk.Y)
        
        # Cluster_Frame=tk.Frame(self.Set_Frame)
        # Cluster_Frame.pack(side=tk.TOP, anchor=tk.W)
        VS_Frame=tk.Frame(self.Set_Frame)
        VS_Frame.pack(side=tk.TOP, anchor=tk.W, pady=(10,0))
        
        Cluster_Label=tk.Label(VS_Frame, text="集群")
        Cluster_Label.pack(side=tk.LEFT, padx=(0,4))
        self.Cluster_Combobox=ttk.Combobox(VS_Frame, values=("hust" ,"sklcc", "cpt"), width=4)
        self.Cluster_Combobox.pack(side=tk.LEFT)

        self.Cluster_Combobox.bind("<<ComboboxSelected>>", self.selectCluster)


        Ver_Label=tk.Label(VS_Frame, text="版本")
        Ver_Label.pack(side=tk.LEFT, padx=(8,4))
        self.Ver_Combobox=ttk.Combobox(VS_Frame, values=("17.2","19.2","20.2.0","22.1","23.1"), width=4)
        self.Ver_Combobox.pack(side=tk.LEFT)
        Solver_Label=tk.Label(VS_Frame, text="求解器")
        Solver_Label.pack(side=tk.LEFT, padx=(8,4))
        self.Solver_Combobox=ttk.Combobox(VS_Frame, values=("2d","2ddp","3d","3ddp"), width=4)
        self.Solver_Combobox.pack(side=tk.LEFT)


        WorkingDirLB_Frame=tk.Frame(self.Set_Frame)
        WorkingDirLB_Frame.pack(side=tk.TOP, fill=tk.X, pady=(10,0))
        WorkingDir_Label=tk.Label(WorkingDirLB_Frame, text="工作文件夹")
        WorkingDir_Label.pack(side=tk.LEFT, anchor=tk.W, padx=(0,5))
        WorkingDirS_Button=tk.Button(WorkingDirLB_Frame, text="选择当前", command=lambda: self.App.C_wd_selcur(self.WorkingDir_Entry))
        WorkingDirS_Button.pack(side=tk.LEFT, padx=(0,5))
        WorkingDirT_Button=tk.Button(WorkingDirLB_Frame, text="跟踪输出", command=lambda: self.App.C_wd_tail(self.WorkingDir_Entry,self.Journal_Entry))
        WorkingDirT_Button.pack(side=tk.RIGHT, padx=(0,5))
        WorkingDir_Frame=tk.Frame(self.Set_Frame)
        WorkingDir_Frame.pack(side=tk.TOP, fill=tk.X, pady=(5,0))
        self.WorkingDir_Entry=tk.Entry(WorkingDir_Frame)
        self.WorkingDir_Entry.pack(side=tk.BOTTOM, anchor=tk.W, fill=tk.X)

        JournalLB_Frame=tk.Frame(self.Set_Frame)
        JournalLB_Frame.pack(side=tk.TOP, fill=tk.X, pady=(10,0))
        Journal_Label=tk.Label(JournalLB_Frame, text="Journal文件")
        Journal_Label.pack(side=tk.LEFT, anchor=tk.W, padx=(0,5))
        Journal_Button=tk.Button(JournalLB_Frame, text="选择", command=lambda: self.App.C_jo_selcur(self.Journal_Entry))
        Journal_Button.pack(side=tk.LEFT)
        Journal_Frame=tk.Frame(self.Set_Frame)
        Journal_Frame.pack(side=tk.TOP, fill=tk.X, pady=(5,0))
        self.Journal_Entry=tk.Entry(Journal_Frame)
        self.Journal_Entry.pack(side=tk.BOTTOM, anchor=tk.W, fill=tk.X)

        PP_Frame=tk.Frame(self.Set_Frame)
        PP_Frame.pack(side=tk.TOP, anchor=tk.W, pady=(10,0), fill=tk.X)
        MPI_Label=tk.Label(PP_Frame, text="MPI")
        MPI_Label.pack(side=tk.LEFT, padx=(0,4))
        self.MPI_Combobox=ttk.Combobox(PP_Frame, values=("intel" ,"openmpi"), width=6)
        self.MPI_Combobox.pack(side=tk.LEFT)
        self.MPI_Combobox.set("intel")
        INC_Label=tk.Label(PP_Frame, text="互联")
        INC_Label.pack(side=tk.LEFT, padx=(8,4))
        self.INC_Combobox=ttk.Combobox(PP_Frame, values=("ethernet","InfiniBand"), width=6)
        self.INC_Combobox.pack(side=tk.LEFT)
        self.INC_Combobox.set("ethernet")

        
        Node_Label=tk.Label(PP_Frame, text="节点")
        self.Node_Spinbox=tk.Spinbox(PP_Frame, width=3, from_=1, to=99)
        self.Node_Spinbox.pack(side=tk.RIGHT)
        Node_Label.pack(side=tk.RIGHT, padx=(10,5))
        self.App.Entry_Text(self.Node_Spinbox,"1")



        mpi_Frame=tk.Frame(self.Set_Frame)
        mpi_Frame.pack(side=tk.TOP, anchor=tk.W, pady=(10,0), fill=tk.X)
        
        Processor_Label=tk.Label(mpi_Frame, text="核心")
        self.Processor_Spinbox=tk.Spinbox(mpi_Frame, width=3, from_=1, to=999)
        self.Processor_Spinbox.pack(side=tk.RIGHT)
        Processor_Label.pack(side=tk.RIGHT, padx=(10,5))
        self.App.Entry_Text(self.Processor_Spinbox,"8")



        Partition_Label=tk.Label(mpi_Frame, text="分区")
        Partition_Label.pack(side=tk.LEFT, padx=(0,4))
        self.Partition_Entry=tk.Entry(mpi_Frame, width=8)
        self.Partition_Entry.pack(side=tk.LEFT, fill=tk.X)
        
        Account_Label=tk.Label(mpi_Frame, text="账户")
        Account_Label.pack(side=tk.LEFT, padx=(8,4))
        self.Account_Entry=tk.Entry(mpi_Frame, width=9)
        self.Account_Entry.pack(side=tk.LEFT)

        Mail_Frame=tk.Frame(self.Set_Frame)
        Mail_Frame.pack(side=tk.TOP, pady=(10,0), fill=tk.X)
        MAILDEST_Label=tk.Label(Mail_Frame, text="邮件提醒")
        MAILDEST_Label.pack(side=tk.LEFT, padx=(0,5))
        
        self.MAILDEST_Entry=tk.Entry(Mail_Frame)
        self.MAILDEST_Entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
   


        Job_Frame=tk.Frame(self.Set_Frame)
        Job_Frame.pack(side=tk.TOP, pady=(10,5), fill=tk.X)
        Submit_Frame=tk.Frame(Job_Frame)
        Submit_Button=tk.Button(Submit_Frame, text="提交作业", command=self.App.S_submit)
        Submit_Button.pack(side=tk.TOP)
        Scancel_Button=tk.Button(Job_Frame, text="中止❌", command=self.App.S_scancel)
        Scancel_Button.pack(side=tk.RIGHT)
        Submit_Frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        Stdout_Frame=tk.Frame(self.Set_Frame)
        Stdout_Frame.pack(side=tk.TOP, pady=(5,5), fill=tk.BOTH, expand=True)
        # StdoutS_Buttoon=tk.Button(Stdout_Frame, text="清除", command=lambda :self.Stdout_Text.delete('1.0',tk.END))
        # StdoutS_Buttoon.pack(side=tk.TOP, anchor=tk.E, pady=(0,5))
        Stdout_Scl=tk.Scrollbar(Stdout_Frame)
        self.Stdout_Text=tk.Text(Stdout_Frame, font=("Consolas",10), width=10, height=5, wrap="none")
        Stdout_Scl.pack(side=tk.RIGHT, fill=tk.Y)
        self.Stdout_Text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.Stdout_Text.config(yscrollcommand=Stdout_Scl.set)
        Stdout_Scl.config(command=self.Stdout_Text.yview)



        # Scancel_Button=tk.Button(Job_Frame, text="中止全部作业", command=self.App.S_scancel_u)
        # Scancel_Button.pack(side=tk.RIGHT, padx=(15,5))


        
    def def_BashFrame(self):
        self.Bash_Frame=tk.Frame(self.root)
        self.Bash_Frame.pack(padx=(10,20), pady=20, side=tk.LEFT, anchor=tk.E, fill=tk.BOTH, expand=True)

        TerCtl_Frame=tk.Frame(self.Bash_Frame)
        TerCtl_Frame.pack(side=tk.TOP, fill=tk.X)

        StopTail_Button=tk.Button(TerCtl_Frame, text="停止输出", command=self.App.S_stoptail)
        StopTail_Button.pack(side=tk.LEFT)
        Sinfo_Button=tk.Button(TerCtl_Frame, text="节点状态", command=self.App.S_sinfo)
        Sinfo_Button.pack(side=tk.LEFT, padx=(10,5))
        Squeue_Button=tk.Button(TerCtl_Frame, text="作业队列", command=self.App.S_squeue)
        Squeue_Button.pack(side=tk.LEFT, padx=(5,10))
        Ssacct_Button=tk.Button(TerCtl_Frame, text="历史作业", command=self.App.S_sacct)
        Ssacct_Button.pack(side=tk.LEFT)


        TerExpand_Button=tk.Button(TerCtl_Frame, text="扩展终端 <<", command=self.App.TC_expand_Bash)
        TerExpand_Button.pack(side=tk.RIGHT)
        Reconnect_Button=tk.Button(TerCtl_Frame, text="重连终端", command=self.App.TC_reconnect)
        Reconnect_Button.pack(side=tk.RIGHT, padx=(0,10))
        Cls_Button=tk.Button(TerCtl_Frame, text="清屏", command=self.App.I_cls)
        Cls_Button.pack(side=tk.RIGHT, padx=(0,10))

        TerCtl_Frame=tk.Frame(self.Bash_Frame)
        TerCtl_Frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(5,0))

        self.Terminal_Text=tk.Text(TerCtl_Frame, font=("Consolas",11), wrap="none")
        TerScl=tk.Scrollbar(TerCtl_Frame)
        TerScl.pack(side=tk.RIGHT, fill=tk.Y)
        TerScl.config(command=self.Terminal_Text.yview)

        TerSclx=tk.Scrollbar(TerCtl_Frame, orient=tk.HORIZONTAL)
        TerSclx.pack(side=tk.BOTTOM, fill=tk.X)
        TerSclx.config(command=self.Terminal_Text.xview)
        self.Terminal_Text.pack(expand=True, fill=tk.BOTH)
        self.Terminal_Text.config(xscrollcommand=TerSclx.set, yscrollcommand=TerScl.set)

        # self.Terminal_Text.bind("<Key>", lambda a: "break")

        Command_Frame=tk.Frame(self.Bash_Frame)
        Command_Frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(10,0))
        
        Command_Button=tk.Button(Command_Frame, text="发送➡️", command=self.App.I_sendcmd)
        Command_Button.pack(side=tk.RIGHT, padx=(10,0))
        self.Command_Entry=tk.Entry(Command_Frame, font=("Consolas",11))
        self.Command_Entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.Command_Entry.bind("<Return>", self.App.I_sendcmd)
    
    def selectCluster(self, event=None):
        cluster=self.Cluster_Combobox.get().strip()
        if cluster=="hust":
            self.MPI_Combobox.configure(state="disabled")
            self.INC_Combobox.configure(state="disabled")
            self.Account_Entry.configure(state="normal")
            self.Partition_Entry.configure(state="normal")
            self.MAILDEST_Entry.configure(state="readonly")
        elif cluster=="sklcc":
            self.MPI_Combobox.configure(state="disabled")
            self.INC_Combobox.configure(state="disabled")
            self.Account_Entry.configure(state="readonly")
            self.Partition_Entry.configure(state="normal")
            self.MAILDEST_Entry.configure(state="readonly")
        elif cluster=="cpt":
            self.MPI_Combobox.configure(state="normal")
            self.INC_Combobox.configure(state="disabled")
            self.Account_Entry.configure(state="readonly")
            self.Partition_Entry.configure(state="readonly")
            self.MAILDEST_Entry.configure(state="normal")
        else:
            self.MPI_Combobox.configure(state="disabled")
            self.INC_Combobox.configure(state="disabled")
            self.Account_Entry.configure(state="readonly")
            self.Partition_Entry.configure(state="readonly")
            self.MAILDEST_Entry.configure(state="readonly")



