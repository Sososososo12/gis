import win32com.client as win32
import os.path
import os


def xlsToxlsx(address_inputnum):
    rootdir = r"../based/{}Excel".format(str(address_inputnum)) # 需要转换的xls文件存放处
    rootdir_out = r"../based/{}Excel_xlsx".format(str(address_inputnum))  # 转换好的xlsx文件存放处
    files = os.listdir(rootdir)  # 列出xls文件夹下的所有文件
    file_len = len(files)  # 列出所有文件的个数
    for i in range(file_len):  # 按文件个数执行次数
        kname = os.path.splitext(files[i])[1]  # 分离文件名与扩展名，返回(f_name, f_extension)元组
        if kname == '.xls':  # 判定扩展名是否为xls,屏蔽其它文件
            fname = rootdir + '/' + files[i]  # 合成需要转换的路径与文件名
            fname1 = rootdir_out + '/' + files[i]  # 合成准备存放转换好的路径与文件名
            excel = win32.gencache.EnsureDispatch('Excel.Application')  # 调用win32模块
            wb = excel.Workbooks.Open(fname)  # 打开需要转换的文件
            wb.SaveAs(fname1 + "x", FileFormat=51)  # 文件另存为xlsx扩展名的文件
            wb.Close()
            excel.Application.Quit()
        print('已转换完成excel文件: '+files[i])


if __name__ == '__main__':
    xlsToxlsx('04-08')
