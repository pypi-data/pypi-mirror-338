import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD, DND_TEXT
from tkinter import filedialog, messagebox, simpledialog
import os, json, base64, random, tempfile, zipfile, time, re
from sklcc_ssubmit.sshClient import sshClient
from sklcc_ssubmit.thread_func import thread_func
import sklcc_ssubmit.AppUI as AppUI
dir_sepa="------------------------文件夹------------------------"
file_sepa="-------------------------文件-------------------------"

class Application(object):
    para={"Cluster": "","Server": "","Port": "","Username": "","Password": "","Version": "","Solver": "","Partition": "","Core": "","Account": "","WorkingDir": "","Journal": ""}

    def __init__(self):
        window=TkinterDnD.Tk()
        window.drop_target_register(DND_FILES)
        window.dnd_bind('<<Drop>>', self.DropUpload)


        self.UI=AppUI.UI(window, self)

        self.cfg_dir=os.path.expanduser('~')+"/.config/sklcc_ssubmit"
        self.read_cfg(self.cfg_dir+"/default.json")
        self.sshc=sshClient()
        self.Status("Ready")
        self.Connected=False
        self.ShowFS=True

        window.mainloop()
        self.sshc.Close()
    def open_cfg(self):
        file_path=filedialog.askopenfilename(
            title="打开配置文件", 
            initialdir=self.cfg_dir,
            filetypes=[("JSON File", "*.json"), ("Text File", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            self.I_cls()
            self.UI.FileManager_Listbox.delete(0,tk.END)
            self.read_cfg(file_path)
            self.to_stdout(f"Read {file_path}")


    def save_cfg(self):
        file_path=filedialog.asksaveasfilename(
            title="保存配置文件", 
            initialdir=self.cfg_dir,
            initialfile="*.json",
            filetypes=[("JSON File", "*.json")]
        )
        if not file_path:
            return
        if(file_path[-5:] != ".json"):
            file_path=file_path+".json"
        self.get_para()
        data=self.para
        data["Password"]=str(base64.b64encode(data["Password"].encode('utf-8')), 'utf-8')
        with open(file_path, "w") as cfg:
            json.dump(data, cfg, indent=4)
        self.to_stdout(f"Saved {file_path}")

    def save_cfg_default(self):
        file_path=self.cfg_dir+ "/default.json"
        print(file_path)
        self.get_para()
        data=self.para
        data["Password"]=str(base64.b64encode(data["Password"].encode('utf-8')), 'utf-8')
        with open(file_path, "w") as cfg:
            json.dump(data, cfg, indent=4)
        self.to_stdout(f"Saved {file_path}")

    def read_cfg(self, filepath):
        with open(filepath, "r") as cfg:
            self.para=json.load(cfg)
        self.para["Password"]=base64.b64decode(self.para["Password"]).decode("utf-8")
        self.apply_para()
        self.UI.selectCluster()


    def apply_para(self): # 将cfg中的配置写入Entry
        try:
            self.Entry_Text(self.UI.Server_Entry, self.para.get("Server","127.0.0.1"))
            self.Entry_Text(self.UI.ServerPort_Entry, self.para.get("Port",""))
            self.Entry_Text(self.UI.Username_Entry, self.para.get("Username",""))
            self.Entry_Text(self.UI.Password_Entry, self.para.get("Password",""))
            self.Entry_Text(self.UI.Ver_Combobox, self.para.get("Version","22.1"))
            self.Entry_Text(self.UI.Solver_Combobox, self.para.get("Solver","3ddp"))
            self.Entry_Text(self.UI.Partition_Entry, self.para.get("Partition",""))
            self.Entry_Text(self.UI.Node_Spinbox, self.para.get("Node","1"))
            self.Entry_Text(self.UI.Processor_Spinbox, self.para.get("Core","16"))
            self.Entry_Text(self.UI.Account_Entry, self.para.get("Account",""))
            self.Entry_Text(self.UI.WorkingDir_Entry, self.para.get("WorkingDir",""))
            self.Entry_Text(self.UI.Journal_Entry, self.para.get("Journal",""))
            self.Entry_Text(self.UI.Cluster_Combobox, self.para.get("Cluster","cpt"))
            self.Entry_Text(self.UI.MPI_Combobox, self.para.get("MPI","intel"))
            self.Entry_Text(self.UI.INC_Combobox, self.para.get("INC","ethernet"))

        except:
            pass
        
    def get_para(self): # 将Entry写入cfg
        self.para["Cluster"]=self.UI.Cluster_Combobox.get().strip()
        self.para["Server"]=self.UI.Server_Entry.get().strip()
        self.para["Port"]=self.UI.ServerPort_Entry.get().strip()
        self.para["Username"]=self.UI.Username_Entry.get().strip()
        self.para["Password"]=self.UI.Password_Entry.get().strip()
        self.para["Version"]=self.UI.Ver_Combobox.get().strip()
        self.para["Solver"]=self.UI.Solver_Combobox.get().strip()
        self.para["Partition"]=self.UI.Partition_Entry.get().strip()
        self.para["Core"]=self.UI.Processor_Spinbox.get().strip()
        self.para["Node"]=self.UI.Node_Spinbox.get().strip()
        self.para["Account"]=self.UI.Account_Entry.get().strip()
        self.para["WorkingDir"]=self.UI.WorkingDir_Entry.get().strip()
        self.para["Journal"]=self.UI.Journal_Entry.get().strip()
        self.para["MPI"]=self.UI.MPI_Combobox.get().strip()
        self.para["INC"]=self.UI.INC_Combobox.get().strip()

    def Status(self, str):
        self.UI.statusbar["text"]=str
    def Entry_Text(self, Entry, str):
        Entry.delete(0,tk.END)
        Entry.insert(0,str)

    def stdout_cmd(self, s):
        # print(s)
        res=None
        try:
            res=str(self.sshc.client.exec_command(s)[1].read(), encoding='utf-8')
        except:
            messagebox.showerror("SSH错误", f'尝试重新登录服务器可能解决问题\n当前服务器：{self.para["Server"]}:{self.para["Port"]}')
        if not res is None:
            res=res.strip()
        return res

    def c_cd(self, s):
        # print(s)
        if not self.Connected:
            return
        
        self.pwd=self.stdout_cmd(f"cd \"{s}\"; pwd")
        self.Entry_Text(self.UI.CurrentDir_Path, self.pwd)


        self.Current_Dirs=self.stdout_cmd(f"find -L \"{self.pwd}\""+r" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | grep -v '^\.'").split('\n')
        self.Current_Files=self.stdout_cmd(f"find -L \"{self.pwd}\""+r" -mindepth 1 -maxdepth 1 -type f -exec basename {} \; | grep -v '^\.'").split('\n')
        self.Current_Dirs.sort(key=str.lower)
        self.Current_Dirs.insert(0, "..")
        self.Current_Files.sort(key=str.lower)

        self.UI.FileManager_Listbox.delete(0,tk.END)
        self.UI.FileManager_Listbox.insert(tk.END, dir_sepa)
        for dir in self.Current_Dirs:
            self.UI.FileManager_Listbox.insert(tk.END, dir.strip())
        self.UI.FileManager_Listbox.insert(tk.END, file_sepa)
        for file in self.Current_Files:
            self.UI.FileManager_Listbox.insert(tk.END, file.strip())

    def c_cd_u(self):
        self.to_stdout("cd ~")
        self.c_cd("~")

    def c_cd_up(self):
        self.to_stdout("cd ..")
        self.c_cd(self.pwd+"/..")


    def to_stdout(self, str):
        self.UI.Stdout_Text.insert(tk.END, str+"\n")
        self.UI.Stdout_Text.see(tk.END)

        
    def FM_double_click(self, event):
        name=self.UI.FileManager_Listbox.get(self.UI.FileManager_Listbox.curselection())
        if name in self.Current_Dirs:
            self.to_stdout("cd "+self.pwd+"/"+name)
            self.c_cd(self.pwd+"/"+name)
            
        elif name in self.Current_Files:
            
            Preview=tk.Toplevel()
            Preview.geometry("400x600")
            Preview.geometry(f"{500}x{600}+{100}+{100}")

            Preview_Text=tk.Text(Preview, font=("Consolas",11))
            Preview_Scl=tk.Scrollbar(Preview)

            Preview_Scl.config(command=Preview_Text.yview)
            Preview_Text.config(yscrollcommand=Preview_Scl)

            Preview_Scl.pack(side=tk.RIGHT, fill=tk.Y)
            Preview_Text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


            content=self.stdout_cmd(f"cat \"{self.pwd}/{name}\"")
            Preview_Text.insert(tk.END, content)

        
    def c_refresh(self):
        # self.to_stdout("Refresh "+self.pwd)
        self.c_cd(self.pwd)

    def c_rename(self):
        if not self.Connected:
            return
        
        s=self.UI.FileManager_Listbox.curselection()
        if len(s)>1:
            messagebox.showinfo("重命名", "不支持批量重命名！")
            return
        for i in s:
            if not ( self.UI.FileManager_Listbox.get(i) != dir_sepa and self.UI.FileManager_Listbox.get(i) != file_sepa):
                messagebox.showerror("错误", "选择了分割线！")
                return
            file=self.UI.FileManager_Listbox.get(i)
            s=simpledialog.askstring("重命名", f"将{file}重命名为")
            if not s is None:
                self.to_stdout(f"mv \"{self.pwd}/{file}\" \"{self.pwd}/{s.strip()}\"")
                self.to_stdout(self.stdout_cmd(f"mv \"{self.pwd}/{file}\" \"{self.pwd}/{s.strip()}\""))
                self.c_refresh()
            else:
                # messagebox.showinfo("重命名","未输入文件名，取消操作")
                pass
            return

    def c_mkdir(self):
        if not self.Connected:
            return
        
        s=simpledialog.askstring("新建文件夹", "文件夹名称", initialvalue="New Folder_"+str(random.randint(1,99)))
        if not s is None:
            self.to_stdout(f"mkdir \"{self.pwd}/{s.strip()}\"")
            self.to_stdout(self.stdout_cmd(f"mkdir \"{self.pwd}/{s.strip()}\""))
            self.c_refresh()

    def c_rm(self):
        if not self.Connected:
            return
        
        selection=self.UI.FileManager_Listbox.curselection()

        files=""
        for i in selection:
            files=files+"\n"+self.UI.FileManager_Listbox.get(i)
            if not (self.UI.FileManager_Listbox.get(i) != dir_sepa and self.UI.FileManager_Listbox.get(i) != file_sepa):
                messagebox.showerror("错误", "选择了分割线！")
                return
        if len(files.strip())==0:
            return
        if not messagebox.askokcancel("删除", f"确认删除以下文件？删除后无法恢复！{files}"):
            return

        for i in selection:
            file=self.UI.FileManager_Listbox.get(i)
            self.to_stdout(f"rm -rf \"{self.pwd}/{file}\"")
            self.to_stdout(self.stdout_cmd(f"rm -rf \"{self.pwd}/{file}\""))
        self.c_refresh()

    def c_mv(self):
        if not self.Connected:
            return
        selection=self.UI.FileManager_Listbox.curselection()
        files=""
        for i in selection:
            files=files+self.UI.FileManager_Listbox.get(i)+'\n'
            if not (self.UI.FileManager_Listbox.get(i) != dir_sepa and self.UI.FileManager_Listbox.get(i) != file_sepa):
                messagebox.showerror("错误", "选择了分割线！")
                return
        if len(files.strip())==0:
            return
        
        s=simpledialog.askstring("移动", f"{files}将以上文件移动到", initialvalue=self.pwd)

        if not s is None:
            isdir=self.stdout_cmd(f"[ -d \"{s}\" ] && echo 1").strip()
            if not isdir=="1":
                messagebox.showerror("移动", "目标路径非法！")
                return

            newpath=self.stdout_cmd(f"cd \"{s}\"; pwd")
            if newpath==self.pwd:
                messagebox.showerror("移动", "源文件夹与目标文件夹相同！")
            for i in selection:
                file=self.UI.FileManager_Listbox.get(i)
                self.to_stdout(f"mv \"{self.pwd}/{file}\" \"{newpath}/{file}\" -f")
                self.to_stdout(self.stdout_cmd(f"mv \"{self.pwd}/{file}\" \"{newpath}/{file}\" -f"))
        else:
            # messagebox.showinfo("移动","未输入路径，取消操作！")
            pass

        self.c_refresh()
        return
    def c_cp(self):
        if not self.Connected:
            return
        selection=self.UI.FileManager_Listbox.curselection()
        files=""
        for i in selection:
            files=files+self.UI.FileManager_Listbox.get(i)+'\n'
            if not (self.UI.FileManager_Listbox.get(i) != dir_sepa and self.UI.FileManager_Listbox.get(i) != file_sepa):
                messagebox.showerror("错误", "选择了分割线！")
                return
        if len(files.strip())==0:
            return
        
        s=simpledialog.askstring("复制", f"{files}将以上文件复制到文件夹", initialvalue=self.pwd)

        if not s is None:
            s=s.strip()
            isdir=self.stdout_cmd(f"[ -d \"{s}\" ] && echo 1").strip()
            if not isdir=="1":
                messagebox.showerror("复制", "目标路径非法！")
            
            newpath=self.stdout_cmd(f"cd \"{s}\"; pwd")
            if newpath==self.pwd:
                if len(selection)!=1:
                    messagebox.showerror("复制", "源文件夹与目标文件夹相同，只能复制一个对象！")
                    return
                file=file=self.UI.FileManager_Listbox.get(selection[0])
                s=simpledialog.askstring("复制", f"{file}将以上文件命名为", initialvalue=file)
                self.to_stdout(f"cp \"{self.pwd}/{file}\" \"{newpath}/{s}\" -rf")
                self.to_stdout(self.stdout_cmd(f"cp \"{self.pwd}/{file}\" \"{newpath}/{s}\" -rf"))

            for i in selection:
                file=self.UI.FileManager_Listbox.get(i)
                self.to_stdout(f"cp \"{self.pwd}/{file}\" \"{newpath}/{file}\" -rf")
                self.to_stdout(self.stdout_cmd(f"cp \"{self.pwd}/{file}\" \"{newpath}/{file}\" -rf"))
        else:
            # messagebox.showinfo("复制","未输入路径，取消操作！")
            pass

        self.c_refresh()
        return

    def f_upload(self):
        if not self.Connected:
            return
        # sftp=sshClient()
        # sftp.Connect(self.para["Server"], self.para["Port"], self.para["Username"], self.para["Password"])

        # sftp=paramiko.SFTPClient.from_transport(self.sshc_transport)
        
        file_paths=filedialog.askopenfilenames(title="选择文件", initialdir=os.path.expanduser('~'))

        if not file_paths:
            return
        if len(file_paths)==1 and os.path.isfile():
            self.Status("Uploading...")
            self.to_stdout(f"Upload({file_paths[0]},{self.pwd}/{os.path.basename(file_paths[0])})")
            if not self.sshc.Upload(file_paths[0],self.pwd+"/"+os.path.basename(file_paths[0])):
                self.Status("Upload Failed")
                return
            self.c_refresh()
            # messagebox.showinfo("上传文件", "上传完成！")
            self.to_stdout(f"上传完成！")
            return
        
        with tempfile.NamedTemporaryFile(suffix=".zip") as zfile:
            zfile.close()
            self.Status("Uploading...")
            zip=zipfile.ZipFile(zfile.name, 'w', zipfile.ZIP_DEFLATED)
            for f in file_paths:
                self.to_stdout(f"Zip {os.path.basename(f)}")
                zip.write(f,os.path.basename(f))
            zip.close()
            self.to_stdout(f"Upload({zfile.name},{self.pwd}/{os.path.basename(zfile.name)})")
            if not self.sshc.Upload(zfile.name,self.pwd+"/"+os.path.basename(zfile.name)):
                self.Status("Upload Failed")
                return
            self.to_stdout(self.stdout_cmd(f"unzip -O CP936 {self.pwd}/{os.path.basename(zfile.name)} -d {self.pwd}; rm -f {self.pwd}/{os.path.basename(zfile.name)}"))

            os.remove(zfile.name)
            self.Status("Done Upload")
            self.c_refresh()
            # messagebox.showinfo("上传文件", "上传完成！")
            self.to_stdout(f"上传完成！")
            return
        
        messagebox.showerror("上传错误", "文件未上传")
    
    def DUpFile(self,file_paths):
        for file_path in file_paths:
            self.to_stdout(f"正在上传{file_path}")
            if os.path.isfile(file_path):
                self.Status("Uploading...")
                self.to_stdout(f"Upload({file_path},{self.pwd}/{os.path.basename(file_path)})")
                if not self.sshc.Upload(file_path,self.pwd+"/"+os.path.basename(file_path)):
                    self.Status("Upload Failed")
                    continue
                self.c_refresh()
                continue
            elif os.path.isdir(file_path):
                dir_path=file_path
                with tempfile.NamedTemporaryFile(suffix=".zip") as zfile:
                    zfile.close()
                    self.Status("Uploading...")
                    zip=zipfile.ZipFile(zfile.name, 'w', zipfile.ZIP_DEFLATED)

                    for path, dirnames, filenames in os.walk(dir_path):
                        fpath=path.replace(dir_path, "")
                        for filename in filenames:
                            self.to_stdout(f"Zip {os.path.basename(os.path.join(path, filename))}")
                            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
                    zip.close()
                    self.to_stdout(f"Upload({zfile.name},{self.pwd}/{os.path.basename(zfile.name)})")
                    if not self.sshc.Upload(zfile.name,self.pwd+"/"+os.path.basename(zfile.name)):
                        self.Status("Upload Failed")
                        os.remove(zfile.name)
                        continue
                    os.remove(zfile.name)
                    self.to_stdout(self.stdout_cmd(f"mkdir {os.path.basename(dir_path)}; unzip -O CP936 {self.pwd}/{os.path.basename(zfile.name)} -d {self.pwd}/{os.path.basename(dir_path)}; rm -f {self.pwd}/{os.path.basename(zfile.name)}"))
                    self.Status("Done Upload")
                    self.c_refresh()
                    continue
        # messagebox.showinfo(f"上传{len(file_paths)}个文件", "全部上传完成！")
        self.to_stdout(f"上传{len(file_paths)}个文件，全部完成")

    def DropUpload(self, event):
        if not self.Connected:
            return
        file_paths=event.data.split()
        thread_func(lambda: self.DUpFile(file_paths))
        

    def f_upload_dir(self):
        if not self.Connected:
            return
        
        dir_path=filedialog.askdirectory(title="选择文件夹", initialdir=os.path.expanduser('~'))

        if not dir_path:
            return

        with tempfile.NamedTemporaryFile(suffix=".zip") as zfile:
            zfile.close()
            self.Status("Uploading...")
            zip=zipfile.ZipFile(zfile.name, 'w', zipfile.ZIP_DEFLATED)

            for path, dirnames, filenames in os.walk(dir_path):
                fpath=path.replace(dir_path, "")
                for filename in filenames:
                    self.to_stdout(f"Zip {os.path.basename(os.path.join(path, filename))}")
                    zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
            zip.close()
            self.to_stdout(f"Upload({zfile.name},{self.pwd}/{os.path.basename(zfile.name)})")
            if not self.sshc.Upload(zfile.name,self.pwd+"/"+os.path.basename(zfile.name)):
                self.Status("Upload Failed")
                os.remove(zfile.name)
                return
            os.remove(zfile.name)
            self.to_stdout(self.stdout_cmd(f"mkdir {os.path.basename(dir_path)}; unzip -O CP936 {self.pwd}/{os.path.basename(zfile.name)} -d {self.pwd}/{os.path.basename(dir_path)}; rm -f {self.pwd}/{os.path.basename(zfile.name)}"))
            self.Status("Done Upload")
            self.c_refresh()
            # messagebox.showinfo("上传文件", "上传完成！")
            self.to_stdout(f"上传完成！")
            return
        
        messagebox.showerror("上传错误", "文件夹未上传")


    def f_download(self):
        if not self.Connected:
            return
        
        # sftp=sshClient()
        # sftp.Connect(self.para["Server"], self.para["Port"], self.para["Username"], self.para["Password"])
        
        # sftp=paramiko.SFTPClient.from_transport(self.sshc_transport)
        # sftp=self.sshc.client.open_sftp()

        selection=self.UI.FileManager_Listbox.curselection()
        files=""
        for i in selection:
            files=files+"\n"+self.UI.FileManager_Listbox.get(i)
            if not (self.UI.FileManager_Listbox.get(i) != dir_sepa and self.UI.FileManager_Listbox.get(i) != file_sepa):
                messagebox.showerror("错误", "选择了分割线！")
                return
        if len(files.strip())==0:
            return
        # if not messagebox.askokcancel("下载", f"下载以下文件？{files}"):
        #     return

        
        if len(selection)==1 and self.UI.FileManager_Listbox.get(selection[0]) in self.Current_Files:
            source=self.UI.FileManager_Listbox.get(selection[0])
            dest=filedialog.asksaveasfilename(
                title="保存文件名", 
                initialfile=source
            )
            self.Status("Downloading...")
            self.to_stdout(f"Download({self.pwd+'/'+source},{dest})")
            if not self.sshc.Download(self.pwd+"/"+source, dest):
                self.Status("Download Failed")
                return
            self.Status("Done Download")
            # messagebox.showinfo("下载文件", "下载完成！")
            self.to_stdout(f"下载完成！")
            return
        
        dest=filedialog.asksaveasfilename(
            title="保存文件名", 
            initialfile=self.stdout_cmd(f"basename \"{self.pwd}\"")+".zip",
            filetypes=[("Zip File", "*.zip")]
        )

        self.Status("Downloading...")
        # self.stdout_cmd(r"if [ ! -d $HOME/.tmp ];then mkdir $HOME/.tmp; fi")
        # self.stdout_cmd(r"if [ ! -d $HOME/.tmp/Slurm_Submit ];then mkdir $HOME/.tmp/Slurm_Submit; fi")
        tempfile=self.stdout_cmd(r"mktemp XXXXXX.zip -t")
        print(tempfile)
        self.stdout_cmd(f"rm {tempfile}")
        for i in selection:
            source=self.UI.FileManager_Listbox.get(i)
            self.to_stdout(self.stdout_cmd(f"cd \"{self.pwd}\"; zip -r {tempfile} \"{source}\""))

        self.to_stdout(f"Download({tempfile},{dest})")
        if not self.sshc.Download(tempfile, dest):
            self.Status("Download Failed")
            return

        self.stdout_cmd(f"rm {tempfile}")
        self.Status("Done Download")
        # messagebox.showinfo("下载文件", "下载完成！")
        self.to_stdout(f"下载完成！")

                   

    def DragDown(self):
        if not self.UI.FileManager_Listbox.curselection():
            return
        sfiles=[]
        sdirs=[]
        self.to_stdout("下载文件：")
        for i in self.UI.FileManager_Listbox.curselection():
            sfile=self.UI.FileManager_Listbox.get(i)
            if sfile==dir_sepa or sfile==file_sepa or sfile=="..":
                continue
            if sfile in self.Current_Files:
                sfiles.append(sfile)
            elif sfile in self.Current_Dirs:
                sdirs.append(sfile)
            self.to_stdout("- "+sfile)
        self.to_stdout("")
        d1=""
        with tempfile.TemporaryDirectory() as dest:
            d1=dest
            DWindow=tk.Toplevel()
            DWindow.geometry(f"{600}x{400}+{100}+{100}")
            DWindow.title("下载文件")
            Canvas=tk.Canvas(DWindow, bg="white")
            Canvas.pack(fill=tk.BOTH, expand=True)
            Canvas.filenames={}
            Canvas.nextcoords=[60, 20]
            # Canvas.dragging=False
            Canvas.drag_source_register(1, DND_FILES)
            def DragDown_Init(event):
                data=()
                sel=Canvas.select_item()
                if sel:
                    data=(Canvas.filenames[sel],)
                    # Canvas.dragging=True
                    return(('ASK', 'COPY'), (DND_FILES, DND_TEXT), data)
            Canvas.dnd_bind('<<DragInitCmd>>', DragDown_Init)
            # Canvas.dnd_bind('<<DragEndCmd>>', DragDown_End)
            pwd=self.pwd+"/"
            dest=dest+"/"
            ficon=tk.PhotoImage(data=ficondata)
            dicon=tk.PhotoImage(data=dicondata)
            for f in sfiles:
                self.DDown_File(f, pwd+f, dest+f)
                self.DCanvas(Canvas, ficon, f, dest+f)
            for f in sdirs:
                self.DDown_Dir(dest, f, dest+f+".zip")
                self.DCanvas(Canvas, dicon, f, dest+f)
            self.to_stdout("全部下载完成！")
            os.startfile(dest)
            DWindow.destroy()
            self.UI.root.wait_window()

    def DDown_File(self, f, s, d):
        if not self.sshc.Download(s, d):
            self.to_stdout(f"下载{f}失败！")
            return False
        return True


    def DDown_Dir(self, destd, s, dzip):
        tempfile=self.stdout_cmd(r"mktemp XXXXXX.zip -t")
        self.stdout_cmd(f"rm {tempfile}")
        self.to_stdout(self.stdout_cmd(f"cd \"{self.pwd}\"; zip -r {tempfile} \"{s}\""))
        if not self.sshc.Download(tempfile, dzip):
            self.to_stdout(f"下载{s}失败！")
            self.stdout_cmd(f"rm {tempfile}")
            return False
        self.stdout_cmd(f"rm {tempfile}")
        zfile=zipfile.ZipFile(dzip)
        zfile.extractall(destd)
        zfile.close()
        os.remove(dzip)
        return True
        
    
    def DCanvas(self, Canvas, icon, f, d):
        id1=Canvas.create_image(Canvas.nextcoords[0], Canvas.nextcoords[1], image=icon, anchor='n', tags=('file', ))
        id2=Canvas.create_text(Canvas.nextcoords[0], Canvas.nextcoords[1]+30, text=f, anchor='n', justify=tk.CENTER, width=90)
        def select_item(event):
            Canvas.select_from(id2, 0)
            Canvas.select_to(id2, tk.END)
        Canvas.tag_bind(id1, '<ButtonPress-1>', select_item)
        Canvas.tag_bind(id2, '<ButtonPress-1>', select_item)
        Canvas.filenames[id1]=d
        Canvas.filenames[id2]=d
        if Canvas.nextcoords[0] > 450:
            Canvas.nextcoords=[60, Canvas.nextcoords[1]+100]
        else:
            Canvas.nextcoords=[Canvas.nextcoords[0]+120, Canvas.nextcoords[1]]

        

    def Login(self, event=None):
        self.get_para()
        self.Status("Connecting Server")
        self.sshc.Connect(self.para["Server"], self.para["Port"], self.para["Username"], self.para["Password"])
        self.Status("Ready")
        if not self.sshc.Connected:
            return
        self.UI.serverstatusbar["text"]=f'已连接到服务器{self.para["Server"]}:{self.para["Port"]}'
        self.Connected=True
        self.c_cd("~")
        self.I_cls()
        self.homedir=self.stdout_cmd(f"cd ~; pwd")

        # self.channel.set
        self.TC_reconnect()
        thread_func(self.auto_refresh)
        thread_func(self.keep_terminal)

    def C_wd_selcur(self, Ob):
        if not self.Connected:
            return
        self.Entry_Text(Ob, self.pwd)
        self.get_para()

    
    def C_jo_selcur(self, Ob):
        if not self.Connected:
            return
        selection=self.UI.FileManager_Listbox.curselection()
        if not (len(selection)==1 and self.UI.FileManager_Listbox.get(selection[0]) in self.Current_Files):
            messagebox.showinfo("选择Journal", "选且仅选1个Journal文件")
            return
        self.Entry_Text(Ob, self.UI.FileManager_Listbox.get(selection[0]))
        self.get_para()
        if self.para["Journal"][-4:] != ".jou":
            messagebox.showwarning("警告", "选择的Journal文件，后缀名应为*.jou")
            return
    
    def C_wd_tail(self, Ob_E, Ob_J):
        if not self.Connected:
            return
        self.get_para()
        res_d=f"{Ob_E.get().strip()}/Result_{Ob_J.get().strip().rsplit('.', 1)[0]}/stdout_fluent.txt"
        if(self.stdout_cmd(f"[ ! -e \"{res_d}\" ] && echo 1").strip() == "1"):
            messagebox.showerror("文件不存在", f"请检查输入是否正确，且已经运行\n工作文件夹：{Ob_E.get().strip()}\nJournal文件：{Ob_J.get().strip()}")
            return
        self.channel.send(f'tail \"{res_d}\" -f &'+"\n")

    def send_channel(self, str):
        self.channel.send(str+"\n")

    def S_submit(self):
        if not self.Connected:
            return
        
        self.get_para()
        if self.para["Journal"][-4:] != ".jou":
            messagebox.showwarning("错误", "选择的Journal文件，后缀名应为*.jou")
            return
        jou_abspath=self.para["WorkingDir"]+"/"+self.para["Journal"]
        if(self.stdout_cmd(f"[ ! -e \"{jou_abspath}\" ] && echo 1").strip() == "1"):
            messagebox.showerror("错误", "选择的Journal文件不存在\n"+jou_abspath)
            return
        # self.stdout_cmd(f'dos2unix \"{self.para["WorkingDir"]}/{self.para["Journal"]}\"')
        self.stdout_cmd(r"if [ ! -d $HOME/.fluent_resdir ];then mkdir $HOME/.fluent_resdir; fi")
        if self.UI.Cluster_Combobox.get() == "hust":
            load_fluent="module load app/fluent/"+self.para["Version"]
        elif self.UI.Cluster_Combobox.get() == "sklcc":
            if self.para["Version"]=="23.1":
                load_fluent="module load ansys/fluent_v231"
            elif self.para["Version"]=="22.1":
                load_fluent="export PATH=$PATH:~/.software/ansys_inc/v221/fluent/bin"
            else:
                messagebox.showerror("提交错误", "煤燃烧集群暂仅支持2023R1版本")
                return
        elif self.UI.Cluster_Combobox.get() == "cpt":
            if self.para["Version"]=="22.1":
                load_fluent="export PATH=$PATH:~/.software/ansys_inc/v221/fluent/bin"
            else:
                messagebox.showerror("提交错误", "CPT集群暂仅支持2022R1版本")
        else:
            return

        arg_list=[self.para["WorkingDir"],load_fluent,self.para["Solver"],self.para["Journal"],self.para["Partition"],self.para["Core"],self.para["Account"], self.UI.Node_Spinbox.get().strip()]
        print(arg_list)
        
        self.to_stdout("提交作业")
        self.to_stdout(f'- 集群：{self.UI.Cluster_Combobox.get()}')
        self.to_stdout(f'- Fluent版本：{self.para["Version"]}')
        self.to_stdout(f'- 求解器：{arg_list[2]}')
        self.to_stdout(f'- 工作文件夹：{arg_list[0]}')
        self.to_stdout(f'- Journal脚本：{arg_list[3]}')
        self.to_stdout(f'- 计算分区：{arg_list[4]}')
        self.to_stdout(f'- 计费账户：{arg_list[6]}')
        self.to_stdout(f'- MPI：{self.UI.MPI_Combobox.get()}')
        self.to_stdout(f'- 互联：{self.UI.INC_Combobox.get()}')
        self.to_stdout(f'- 节点数量：{arg_list[7]}')
        self.to_stdout(f'- 核心数量：{arg_list[5]}')

        # if not messagebox.askokcancel("提交作业", f'工作文件夹：{arg_list[0]}\nFluent版本：{self.para["Version"]}\n求解器：{arg_list[2]}\nJournal脚本：{arg_list[3]}\n计算分区：{arg_list[4]}\n核心数量：{arg_list[5]}\n计费账户：{arg_list[6]}\n核心数量：{arg_list[7]}\n确认提交？'):
        #     return
        
        sh_path=self.para["WorkingDir"]+"/RunFluent.sh"
        with tempfile.NamedTemporaryFile(suffix=".sh") as shfile:
            shfile.close()
            shfile=open(shfile.name, "w")
            sh=runfluentsh.replace('\r\n', '\n')
            if self.para["Cluster"]=="sklcc":
                sh=sklcc_runfluentsh.replace('\r\n', '\n')
            elif self.para["Cluster"]=="cpt":
                sh=cpt_runfluentsh.replace('\r\n', '\n')
            shfile.write(sh)
            shfile.close()
            self.to_stdout(f"Write {shfile.name} to {sh_path}")
            self.sshc.Upload(shfile.name,sh_path+"1")
            self.stdout_cmd(f"cat {sh_path}1 | python -c \"import sys; sys.stdout.write(sys.stdin.read().replace('\\r\\n', '\\n'))\" > {sh_path}")
            # self.stdout_cmd(f'dos2unix {sh_path}')
            self.stdout_cmd(f"rm {sh_path}1")
            os.remove(shfile.name)

        # args=""
        # for i in arg_list:
        #     args=args+" \""+i+"\""
        self.send_channel("export FLUENT_SOLVER_VER="+arg_list[2])
        self.send_channel("export JOU_FILE="+arg_list[3])
        self.send_channel("export SLURM_PARTITION="+arg_list[4])
        self.send_channel("export SLURM_NTASKS="+arg_list[5])
        self.send_channel("export SLURM_ACCOUNT="+arg_list[6])
        self.send_channel("export SLURM_NODES="+arg_list[7])
        fluent_mpi="intel"
        if self.UI.MPI_Combobox.get().strip()=="openmpi":
            fluent_mpi="openmpi"
        self.send_channel("export FLUENT_MPI="+fluent_mpi)
        self.send_channel(arg_list[1])
        self.send_channel("cd "+arg_list[0])


        # self.channel.send("bash \""+sh_path+'"'+args+"\n")
        self.channel.send("bash \""+sh_path+'"'+"\n")
        # self.channel.send(f"cd {self.pwd}"+"\n")
        resdir=f'{self.para["WorkingDir"]}/Result_{self.para["Journal"]}'.rsplit('.', 1)[0]
        self.to_stdout(f"cd {resdir}")
        self.C_wd_tail(self.UI.WorkingDir_Entry, self.UI.Journal_Entry)
        self.c_cd(resdir)
    
    def getwdjobid(self):
        self.c_refresh() 
        for i in self.Current_Files:
            if re.fullmatch(r'slurm\.[0-9]+\.hosts',i) is not None:
                return re.findall(r'\d+',i)
        return ""

    def S_scancel(self):
        if not self.Connected:
            return
        # jobid=self.UI.Scancel_Entry.get().strip()

        jobid=simpledialog.askstring("取消作业", f"请输入作业ID（中止全部请输入\"All\"）", initialvalue=self.getwdjobid())
        if jobid=="" or (jobid is None):
            return
        if jobid.strip()=="All":
            self.channel.send(r"scancel -u $USER"+"\n")
            messagebox.showinfo("取消作业", "用户全部作业已取消！")
            return
        if not jobid.isalnum():
            messagebox.showerror("取消作业", "作业ID为数字！")
        self.channel.send(f"scancel {jobid}"+"\n")
        messagebox.showinfo("取消作业", f"作业{jobid}已取消！")

    
    def S_stoptail(self):
        if not self.Connected:
            return
        self.channel.send("\x03")
        self.channel.send(r"pkill tail"+"\n")
    
    def S_sinfo(self):
        if not self.Connected:
            return
        self.channel.send("sinfo -Nel"+"\n")

    def S_squeue(self):
        if not self.Connected:
            return
        self.channel.send(r'squeue -o "%.8i %.10P %.18j %.15u %.5t %.12M %.6D %R"'+"\n")
        self.channel.send(r'squeue -o "%.8i %.10P %.18j %.15u %.5t %.12M %.6D %R" -u $USER'+"\n")

    def S_sacct(self):
        if not self.Connected:
            return
        self.channel.send("sacct"+"\n")
    
    def I_sendcmd(self, event=None):
        if not self.Connected:
            return
        cmd=self.UI.Command_Entry.get().strip()
        self.channel.send(cmd+"\n")
        self.Entry_Text(self.UI.Command_Entry,"")

    def I_cls(self):
        self.UI.Terminal_Text.delete('1.0',tk.END)
        
    def TC_reconnect(self):
        try:
            self.channel.close()
        except:
            pass
        self.channel=self.sshc.client.invoke_shell(width=self.UI.Terminal_Text.winfo_width()//8)
    def auto_refresh(self):
        while True:
            if not self.Connected:
                return
            time.sleep(45)
            self.c_refresh()

    def keep_terminal(self):
        rev=None
        while True:
            time.sleep(0.1)
            try:
                rev=self.channel.recv(4096)
                # print(rev)
                rev=re.sub(rb'\x1b(\[.*?[@-~]|\].*?(\x07|\x1b\\))', rb'', rev)
                # rev=rev.decode("utf-8", "ignore")
                if len(rev)==0:
                    continue
                self.UI.Terminal_Text.insert(tk.END,rev.decode("utf-8", "ignore"))
                self.UI.Terminal_Text.see("end")


            except Exception as e:
                print(e)
                pass


    def TC_expand_Bash(self):
        if self.ShowFS:
            self.UI.File_Frame.pack_forget()
            self.UI.Set_Frame.pack_forget()
            self.ShowFS=False
        else:
            self.UI.Bash_Frame.pack_forget()
            self.UI.File_Frame.pack(padx=(20,10), pady=20, side=tk.LEFT, anchor=tk.W, fill=tk.Y)
            self.UI.Set_Frame.pack(padx=10, pady=20, side=tk.LEFT, anchor=tk.W, fill=tk.Y)
            self.UI.Bash_Frame.pack(padx=(10,20), pady=20, side=tk.LEFT, anchor=tk.E, fill=tk.BOTH, expand=True)
            self.ShowFS=True
        
    def w_popout(self, event=None):
        # name=self.UI.FileManager_Listbox.get(self.UI.FileManager_Listbox.curselection())
        menu=tk.Menu(self.UI.FileManager_Listbox, tearoff=0)
        menu.add_cascade(label="复制", command=self.c_cp)
        menu.add_cascade(label="移动", command=self.c_mv)
        menu.add_cascade(label="删除", command=self.c_rm)
        menu.add_cascade(label="重命名", command=self.c_rename)
        menu.add_cascade(label="上传", command=lambda :thread_func(self.f_upload))
        menu.add_cascade(label="下载", command=lambda :thread_func(self.f_download))
        menu.add_cascade(label="新建文件夹", command=self.c_mkdir)

        menu.post(event.x_root, event.y_root)

        

        

        
    
class Slurm_Submit():
    def __init__(self):
        self.init_cfg()
        
        self.UI=Application()


    def init_cfg(self):
        home_path=os.path.expanduser('~')
        cfg_path=home_path+'/.config'
        if os.path.isfile(cfg_path):
            messagebox.showerror("错误", f"无法在 {home_path} 下创建 .config 文件夹。\n存在同名文件！")
            exit(1)
        cfg_path=cfg_path+'/sklcc_ssubmit'
        if not os.path.isdir(cfg_path):
            os.makedirs(cfg_path)
        cfg_path=cfg_path+'/default.json'
        if not os.path.isfile(cfg_path):
            self.write_cfg(cfg_path)

    def write_cfg(self, cfg_path):
        data={
            "Cluster": "",
            "Server": "",
            "Port": "",
            "Username": "",
            "Password": "",
            "Version": "",
            "Solver": "",
            "Partition": "",
            "Node": "",
            "Core": "",
            "Account": "",
            "WorkingDir": "",
            "Journal": "",
            "MPI": "",
            "INC": ""
        }
        with open(cfg_path, "w") as cfg:
            json.dump(data, cfg, indent=4)
        

ficondata='iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAACxAAAAsQAa0jvXUAAAH0SURBVEhL5dZNSxVRAIfxW2a7QKJQcBG1sUxC8BMogcsgECS1lbbIMqx9q1op6KJFgSBE3yFq41Y0MF2IQhJCizZtelchfZ7bjMy999y544yr+sOPcc6dOW9zPDOlfz4nomN1LmIMnfiDfSTjfbt4g3kLiqQNVmRDv/ADPxM8tzE74fkk6nU8U27Ayl6hG124lnAVvfgMr7Njj3ASuTICK7pTPgunBTa4jU044odoONJQr+yxaY6OoZyJvMMQNjAFG01N2jSk9TZeRKdho87GR0wjdaR5590Km/7+Wc4iBrCCp7DR5O+Hydvgb3zBFVzH5ej8GXbwBBMINlodn4lTdq98Fo4dfQwXyx6+R77Ce/UNfahIqAcu/Zt4jSULArHCZXyCDbpat/AB76OyC1jAKlKTZYSN4i5lHcPls0TyPsNGORUda5K1wR7chaMer2KZv3lNnCMNJDSlM7AszSzi2BHLck/pC3iz257HpNuw/Dly5TgWTeERduAW7IxHOSrfLGdRKEd9hv2oTuER+m60A25X9yMPMIo1FEo8QnuZN/6bZB5hXOb2lDfusaam/tBe6gfUINyI3R/Pwe+c1gzOox0uKvfkl/DlnBorf4t6H1FpvNZ7nE7rsK6K1HszX4ILwg+m0GdivVif07iOOThD/1VKpQNENJDZHaUaMgAAAABJRU5ErkJggg=='
dicondata='iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAACxAAAAsQAa0jvXUAAAE0SURBVEhL7ZY9LwRRFIYHhZCs6CQ+YhOJv6CR7VQK8QOUOtlCtdGplBKV2majs7bSEoXQKDRalWgUkqUR63nPzp1cY43gToF5kif3nlOcs+fO10YFv56+eHWMYAWHLHrLNV51t2GYxGPsfOATbuIAfht/wi2s4R5eKOGhiVdxFvdxDe/xy/gND3EJx/FWiRQ6gV1cxDNs4Ge08QjvLErRRB3dlEW9GcQdTB93lpc4g4Y/4QEuYxlvlMhgAUe720zmsYrbuK6EjxrqF01bFIYxVM2WRdAfr3mhSyBe4jX3hu6SaUoj74bvKBoG5381dLdw8swEwNVK3mi9Gj7HawhcraRhsgH3earjuRIBmMMVVO0NJXz0+TlB95YPpWpOoOFPKEqovxjDFv2cRzzFB4sK/gBR9AoWGk7sVBl3DAAAAABJRU5ErkJggg=='

runfluentsh=r"""
echo $JOU_FILE
JOB_NAME=${JOU_FILE%.*}
dos2unix $JOU_FILE
TEMP_D=$(mktemp -d -p $HOME/.fluent_resdir) || exit 1
SOURCE_D=$PWD
RESULT_DNAME="Result_`basename $JOU_FILE .jou`"
if [ -e $RESULT_DNAME ] || [ -L $RESULT_DNAME ]; then
    LAST_RESULT_D="LastRun$RESULT_DNAME"
    if [ -e $LAST_RESULT_D ] || [ -L $LAST_RESULT_D ]; then
        rm -rf $(readlink -f $LAST_RESULT_D)
    fi
    mv -f $RESULT_DNAME "LastRun$RESULT_DNAME"
fi
ln -s $TEMP_D $RESULT_DNAME

cd "$TEMP_D"
for f in $(ls $SOURCE_D)
do
    if [ ! -L $SOURCE_D/$f ] && [ $f != $RESULT_DNAME ] ;then
        ln -s $SOURCE_D/$f
    fi
done
echo "" > stdout_fluent.txt
echo "" > stderr_fluent.txt

cat > $USER-scheduler.slurm <<EEOOFF
#!/bin/bash
#SBATCH -D .
#SBATCH -N $SLURM_NODES
#SBATCH -n $SLURM_NTASKS
#SBATCH -o stdout_fluent.txt
#SBATCH -e stderr_fluent.txt
#SBATCH -p $SLURM_PARTITION
#SBATCH --comment=$SLURM_ACCOUNT
#SBATCH --job-name=$JOB_NAME
export FLUENT_AFFINITY=0
export SLURM_ENABLED=1
FL_SCHEDULER_HOST_FILE=slurm.\${SLURM_JOB_ID}.hosts
/bin/rm -rf \${FL_SCHEDULER_HOST_FILE}
scontrol show hostnames "\$SLURM_JOB_NODELIST" >> \$FL_SCHEDULER_HOST_FILE
export SCHEDULER_TIGHT_COUPLING=1

echo fluent $FLUENT_SOLVER_VER -g -t\$SLURM_NTASKS -i  $JOU_FILE -mpi=intel -pib -cnf=\${FL_SCHEDULER_HOST_FILE}
fluent $FLUENT_SOLVER_VER -g -t\$SLURM_NTASKS -i  $JOU_FILE -mpi=intel -pib -cnf=\${FL_SCHEDULER_HOST_FILE}

EEOOFF

sbatch $USER-scheduler.slurm
"""

cpt_runfluentsh=r"""
echo $JOU_FILE
JOB_NAME=${JOU_FILE%.*}
dos2unix $JOU_FILE
TEMP_D=$(mktemp -d -p $HOME/.fluent_resdir) || exit 1
SOURCE_D=$PWD
RESULT_DNAME="Result_`basename $JOU_FILE .jou`"
if [ -e $RESULT_DNAME ] || [ -L $RESULT_DNAME ]; then
    LAST_RESULT_D="LastRun$RESULT_DNAME"
    if [ -e $LAST_RESULT_D ] || [ -L $LAST_RESULT_D ]; then
        rm -rf $(readlink -f $LAST_RESULT_D)
    fi
    mv -f $RESULT_DNAME "LastRun$RESULT_DNAME"
fi
ln -s $TEMP_D $RESULT_DNAME

cd "$TEMP_D"
for f in $(ls $SOURCE_D)
do
    if [ ! -L $SOURCE_D/$f ] && [ $f != $RESULT_DNAME ] ;then
        ln -s $SOURCE_D/$f
    fi
done
echo "" > stdout_fluent.txt
echo "" > stderr_fluent.txt

cat > $USER-scheduler.slurm <<EEOOFF
#!/bin/bash
#SBATCH -D .
#SBATCH -N $SLURM_NODES
#SBATCH -n $SLURM_NTASKS
#SBATCH -o stdout_fluent.txt
#SBATCH -e stderr_fluent.txt
#SBATCH --job-name=$JOB_NAME
export FLUENT_AFFINITY=0
export SLURM_ENABLED=1
FL_SCHEDULER_HOST_FILE=slurm.\${SLURM_JOB_ID}.hosts
/bin/rm -rf \${FL_SCHEDULER_HOST_FILE}
scontrol show hostnames "\$SLURM_JOB_NODELIST" >> \$FL_SCHEDULER_HOST_FILE
export SCHEDULER_TIGHT_COUPLING=1

echo fluent $FLUENT_SOLVER_VER -g -t\$SLURM_NTASKS -i  $JOU_FILE -mpi=$FLUENT_MPI -cnf=\${FL_SCHEDULER_HOST_FILE}
fluent $FLUENT_SOLVER_VER -g -t\$SLURM_NTASKS -i  $JOU_FILE -mpi=$FLUENT_MPI -cnf=\${FL_SCHEDULER_HOST_FILE}

EEOOFF

sbatch $USER-scheduler.slurm
"""

sklcc_runfluentsh=r"""
echo $JOU_FILE
JOB_NAME=${JOU_FILE%.*}
dos2unix $JOU_FILE
TEMP_D=$(mktemp -d -p $HOME/.fluent_resdir) || exit 1
SOURCE_D=$PWD
RESULT_DNAME="Result_`basename $JOU_FILE .jou`"
if [ -e $RESULT_DNAME ] || [ -L $RESULT_DNAME ]; then
    LAST_RESULT_D="LastRun$RESULT_DNAME"
    if [ -e $LAST_RESULT_D ] || [ -L $LAST_RESULT_D ]; then
        rm -rf $(readlink -f $LAST_RESULT_D)
    fi
    mv -f $RESULT_DNAME "LastRun$RESULT_DNAME"
fi
ln -s $TEMP_D $RESULT_DNAME

cd "$TEMP_D"
for f in $(ls $SOURCE_D)
do
    if [ ! -L $SOURCE_D/$f ] && [ $f != $RESULT_DNAME ] ;then
        ln -s $SOURCE_D/$f
    fi
done
echo "" > stdout_fluent.txt
echo "" > stderr_fluent.txt

cat > $USER-scheduler.slurm <<EEOOFF
#!/bin/bash
#SBATCH -D .
#SBATCH -N $SLURM_NODES
#SBATCH -n $SLURM_NTASKS
#SBATCH -o stdout_fluent.txt
#SBATCH -e stderr_fluent.txt
#SBATCH --job-name=$JOB_NAME
export FLUENT_AFFINITY=0
export SLURM_ENABLED=1
FL_SCHEDULER_HOST_FILE=slurm.\${SLURM_JOB_ID}.hosts
/bin/rm -rf \${FL_SCHEDULER_HOST_FILE}
scontrol show hostnames "\$SLURM_JOB_NODELIST" >> \$FL_SCHEDULER_HOST_FILE
export SCHEDULER_TIGHT_COUPLING=1

echo fluent $FLUENT_SOLVER_VER -g -t\$SLURM_NTASKS -i  $JOU_FILE -mpi=intel -pib -cnf=\${FL_SCHEDULER_HOST_FILE}
fluent $FLUENT_SOLVER_VER -g -t\$SLURM_NTASKS -i  $JOU_FILE -mpi=intel -pib -cnf=\${FL_SCHEDULER_HOST_FILE}

EEOOFF

sbatch $USER-scheduler.slurm
"""




if __name__== '__main__':
    Slurm_Submit()

# To be implemented
# 拖拽上传文件
# 自动刷新
# 下载打开默认地址
# 下载丢到thread去