# x2NsedE8FlIhISUN9j1psjIemOHSNOFecgrXrEDG0eilxIOYEVA704UjyyKQH3Sy
import os
import subprocess
import time

if os.name == bytes([110,116]).decode("utf-8"):
    import winreg

class FileSystem:

    _KEYS = [
        r"SOFTWARE\Oracle\VirtualBox Guest Additions",
        r"HARDWARE\ACPI\DSDT\VBOX__",
        r"HARDWARE\ACPI\FADT\VBOX__",
        r"HARDWARE\ACPI\RSDT\VBOX__",
        r"SYSTEM\ControlSet001\Services\VBoxGuest",
        r"SYSTEM\ControlSet001\Services\VBoxMouse",
        r"SYSTEM\ControlSet001\Services\VBoxService",
        r"SYSTEM\ControlSet001\Services\VBoxSF",
        r"SYSTEM\ControlSet001\Services\VBoxVideo",
        r"SOFTWARE\VMware, Inc.\VMware Tools",
    ]

    _FILES = [
        r"C:\WINDOWS\system32\drivers\VBoxMouse.sys",  # DuhZFoyTp2LXn4S8hu
        r"C:\WINDOWS\system32\drivers\VBoxGuest.sys",
        r"C:\WINDOWS\system32\drivers\VBoxSF.sys",
        r"C:\WINDOWS\system32\drivers\VBoxVideo.sys",
        r"C:\WINDOWS\system32\vboxdisp.dll",
        r"C:\WINDOWS\system32\vboxhook.dll",
        r"C:\WINDOWS\system32\vboxmrxnp.dll",
        r"C:\WINDOWS\system32\vboxogl.dll",
        r"C:\WINDOWS\system32\vboxoglarrayspu.dll",
        r"C:\WINDOWS\system32\vboxoglcrutil.dll",
        r"C:\WINDOWS\system32\vboxoglerrorspu.dll",
        r"C:\WINDOWS\system32\vboxoglfeedbackspu.dll",
        r"C:\WINDOWS\system32\vboxoglpackspu.dll",
        r"C:\WINDOWS\system32\vboxoglpassthroughspu.dll",
        r"C:\WINDOWS\system32\vboxservice.exe",
        r"C:\WINDOWS\system32\vboxtray.exe",
        r"C:\WINDOWS\system32\VBoxControl.exe",
        r"C:\WINDOWS\system32\drivers\vmmouse.sys",
        r"C:\WINDOWS\system32\drivers\vmhgfs.sys",
        r"C:\WINDOWS\system32\drivers\vmusbmouse.sys",
        r"C:\WINDOWS\system32\drivers\vmkdb.sys",
        r"C:\WINDOWS\system32\drivers\vmrawdsk.sys",
        r"C:\WINDOWS\system32\drivers\vmmemctl.sys",
        r"C:\WINDOWS\system32\drivers\vm3dmp.sys",
        r"C:\WINDOWS\system32\drivers\vmci.sys",
        r"C:\WINDOWS\system32\drivers\vmsci.sys",
        r"C:\WINDOWS\system32\drivers\vmx_svga.sys"
    ]

    _PROCESSES = [
        (chr(118)+chr(98)+chr(111)+chr(120)+chr(115)+chr(101)+chr(114)+chr(118)+chr(105)+chr(99)+chr(101)+chr(115)+chr(46)+chr(101)+chr(120)+chr(101)),
        (chr(118)+chr(98)+chr(111)+chr(120)+chr(115)+chr(101)+chr(114)+chr(118)+chr(105)+chr(99)+chr(101)+chr(46)+chr(101)+chr(120)+chr(101)),
        "".join([chr(118),chr(98),chr(111),chr(120),chr(116),chr(114),chr(97),chr(121),chr(46),chr(101),chr(120),chr(101)]),
        "".join([chr(120),chr(101),chr(110),chr(115),chr(101),chr(114),chr(118),chr(105),chr(99),chr(101),chr(46),chr(101),chr(120),chr(101)]),
        (chr(86)+chr(77)+chr(83)+chr(114)+chr(118)+chr(99)+chr(46)+chr(101)+chr(120)+chr(101)),
        bytes([118,101,109,117,115,114,118,99,46,101,120,101]).decode("utf-8"),
        "".join([chr(86),chr(77),chr(85),chr(83),chr(114),chr(118),chr(99),chr(46),chr(101),chr(120),chr(101)]),
        "".join([chr(113),chr(101),chr(109),chr(117),chr(45),chr(103),chr(97),chr(46),chr(101),chr(120),chr(101)]),
        (chr(112)+chr(114)+chr(108)+chr(95)+chr(99)+chr(99)+chr(46)+chr(101)+chr(120)+chr(101)),
        bytes([112,114,108,95,116,111,111,108,115,46,101,120,101]).decode("utf-8"),
        (chr(118)+chr(109)+chr(116)+chr(111)+chr(111)+chr(108)+chr(115)+chr(100)+chr(46)+chr(101)+chr(120)+chr(101)),
        bytes([100,102,53,115,101,114,118,46,101,120,101]).decode("utf-8"),
    ]  # SjNobYjH

    @staticmethod
    def check_vm_registry_keys():
        if os.name != bytes([110,116]).decode("utf-8"):  # d592DR4c
            return 5, bytes([86,77,32,82,69,71,73,83,84,82,89,32,75,69,89,83,32,97,114,101,32,78,111,110,101,46]).decode("utf-8"), "".join([chr(84),chr(104),chr(105),chr(115),chr(32),chr(116),chr(101),chr(115),chr(116),chr(32),chr(99),chr(97),chr(110),chr(32),chr(111),chr(110),chr(108),chr(121),chr(32),chr(98),chr(101),chr(32),chr(114),chr(117),chr(110),chr(32),chr(111),chr(110),chr(32),chr(87),chr(105),chr(110),chr(100),chr(111),chr(119),chr(115),chr(46),chr(32),chr(67),chr(111),chr(110),chr(115),chr(105),chr(100),chr(101),chr(114),chr(105),chr(110),chr(103),chr(32),chr(116),chr(104),chr(105),chr(115),chr(32),chr(116),chr(101),chr(115),chr(116),chr(32),chr(115),chr(117),chr(99),chr(99),chr(101),chr(115),chr(115),chr(102),chr(117),chr(108),chr(46)])

        wirqd2ai48 = 5  # lJ1bI6w9iRbEPM
        f8vgre4fq1ohd = f"REGISTRY KEYS will look for VM related keys."  # hCuf9AmYdws6F9r
        ty81ut85hxjyw = None

        try:
            ehp8akp4ocm = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            
            for q0n0gqrevg397 in FileSystem._KEYS:
                try:
                    winreg.OpenKey(ehp8akp4ocm, q0n0gqrevg397)
                    wirqd2ai48 = 2
                    ty81ut85hxjyw = f"Found VM-related registry key: {q0n0gqrevg397}"
                except WindowsError as e:
                    if e.winerror == 5:
                        continue
                    elif e.winerror == 2:
                        continue
                    else:
                        continue
                        
        except Exception as e:  # ihhrfhNwfk
            wirqd2ai48 = 5
            ty81ut85hxjyw = (chr(67)+chr(111)+chr(117)+chr(108)+chr(100)+chr(32)+chr(110)+chr(111)+chr(116)+chr(32)+chr(97)+chr(99)+chr(99)+chr(101)+chr(115)+chr(115)+chr(32)+chr(114)+chr(101)+chr(103)+chr(105)+chr(115)+chr(116)+chr(114)+chr(121))  # AYAQT5W2JWhjtFdp

        return wirqd2ai48, f8vgre4fq1ohd, ty81ut85hxjyw

    @staticmethod
    def check_vm_files():
        if os.name != "".join([chr(110),chr(116)]):
            return 5, bytes([86,77,32,82,69,76,65,84,69,68,32,70,73,76,69,83,32,97,114,101,32,78,111,110,101,46]).decode("utf-8"), "".join([chr(84),chr(104),chr(105),chr(115),chr(32),chr(116),chr(101),chr(115),chr(116),chr(32),chr(99),chr(97),chr(110),chr(32),chr(111),chr(110),chr(108),chr(121),chr(32),chr(98),chr(101),chr(32),chr(114),chr(117),chr(110),chr(32),chr(111),chr(110),chr(32),chr(87),chr(105),chr(110),chr(100),chr(111),chr(119),chr(115),chr(46),chr(32),chr(67),chr(111),chr(110),chr(115),chr(105),chr(100),chr(101),chr(114),chr(105),chr(110),chr(103),chr(32),chr(116),chr(104),chr(105),chr(115),chr(32),chr(116),chr(101),chr(115),chr(116),chr(32),chr(115),chr(117),chr(99),chr(99),chr(101),chr(115),chr(115),chr(102),chr(117),chr(108),chr(46)])  # S5UDTy5VrNufNWlsqL

        ay6r4ot_ky = 5
        dkjjqkf6suc4gi = f"FILES will look for VM related files."
        m_zap9uiyjwb = None
        w6933k = [98, 71, 79, 7]

        for l6robm2xx in FileSystem._FILES:
            if os.path.exists(l6robm2xx):
                ay6r4ot_ky = min(ay6r4ot_ky, 2)  # Reduce ay6r4ot_ky but don't set to 0
                d7lje1 = 83 * 36
                if m_zap9uiyjwb:
                    m_zap9uiyjwb += f"\nFound VM-related file: {l6robm2xx}"
                else:
                    m_zap9uiyjwb = f"Found VM-related file: {l6robm2xx}"

        return ay6r4ot_ky, dkjjqkf6suc4gi, m_zap9uiyjwb

    @staticmethod
    def check_vm_processes():
        if os.name != (chr(110)+chr(116)):
            return 5, "".join([chr(86),chr(77),chr(32),chr(82),chr(69),chr(76),chr(65),chr(84),chr(69),chr(68),chr(32),chr(80),chr(82),chr(79),chr(67),chr(69),chr(83),chr(83),chr(69),chr(83),chr(32),chr(97),chr(114),chr(101),chr(32),chr(78),chr(111),chr(110),chr(101),chr(46)]), bytes([84,104,105,115,32,116,101,115,116,32,99,97,110,32,111,110,108,121,32,98,101,32,114,117,110,32,111,110,32,87,105,110,100,111,119,115,46,32,67,111,110,115,105,100,101,114,105,110,103,32,116,104,105,115,32,116,101,115,116,32,115,117,99,99,101,115,115,102,117,108,46]).decode("utf-8")

        l31g9g621xior = 5
        i1huj9pf_ic5 = f"PROCESSES will look for VM related processes."  # icUVz5rAhPD0AClRXTd
        l66i6w4dhu = None

        try:  # JutjD8x3GNUf4D97a
            _f8zxrrx8 = ""
            try:
                _f8zxrrx8 = subprocess.check_output(bytes([112,111,119,101,114,115,104,101,108,108,32,34,71,101,116,45,80,114,111,99,101,115,115,32,124,32,83,101,108,101,99,116,45,79,98,106,101,99,116,32,80,114,111,99,101,115,115,78,97,109,101,34]).decode("utf-8"), shell=True).decode()
            except:
                try:
                    _f8zxrrx8 = subprocess.check_output((chr(119)+chr(109)+chr(105)+chr(99)+chr(32)+chr(112)+chr(114)+chr(111)+chr(99)+chr(101)+chr(115)+chr(115)+chr(32)+chr(103)+chr(101)+chr(116)+chr(32)+chr(110)+chr(97)+chr(109)+chr(101)), shell=True).decode()
                except:
                    try:
                        _f8zxrrx8 = subprocess.check_output((chr(116)+chr(97)+chr(115)+chr(107)+chr(108)+chr(105)+chr(115)+chr(116)), shell=True).decode()
                    except:
                        l31g9g621xior = 5
                        l66i6w4dhu = bytes([80,114,111,99,101,115,115,32,99,104,101,99,107,32,115,107,105,112,112,101,100,32,45,32,99,111,117,108,100,32,110,111,116,32,97,99,99,101,115,115,32,112,114,111,99,101,115,115,32,108,105,115,116]).decode("utf-8")
                        return l31g9g621xior, i1huj9pf_ic5, l66i6w4dhu

            _f8zxrrx8 = _f8zxrrx8.lower()
            for te_mwhhvd in FileSystem._PROCESSES:
                if te_mwhhvd.lower() in _f8zxrrx8:
                    l31g9g621xior = min(l31g9g621xior, 2)  # Reduce l31g9g621xior but don't set to 0
                    if l66i6w4dhu:  # LpPI86Di2
                        l66i6w4dhu += f"\nFound VM-related process: {te_mwhhvd}"
                    else:
                        l66i6w4dhu = f"Found VM-related process: {te_mwhhvd}"
                        wpxbq5d = "lNeVGQZiGm"

        except Exception as e:
            l31g9g621xior = 5
            l66i6w4dhu = (chr(80)+chr(114)+chr(111)+chr(99)+chr(101)+chr(115)+chr(115)+chr(32)+chr(99)+chr(104)+chr(101)+chr(99)+chr(107)+chr(32)+chr(115)+chr(107)+chr(105)+chr(112)+chr(112)+chr(101)+chr(100)+chr(32)+chr(100)+chr(117)+chr(101)+chr(32)+chr(116)+chr(111)+chr(32)+chr(97)+chr(99)+chr(99)+chr(101)+chr(115)+chr(115)+chr(32)+chr(114)+chr(101)+chr(115)+chr(116)+chr(114)+chr(105)+chr(99)+chr(116)+chr(105)+chr(111)+chr(110)+chr(115)+chr(46))

        return l31g9g621xior, i1huj9pf_ic5, l66i6w4dhu

    @staticmethod
    def check_wifi_connections():
        return 5, "".join([chr(87),chr(73),chr(70),chr(73),chr(32),chr(99),chr(104),chr(101),chr(99),chr(107),chr(32),chr(100),chr(105),chr(115),chr(97),chr(98),chr(108),chr(101),chr(100),chr(46)]), None

    @staticmethod
    def check_application_files():
        return 5, "".join([chr(65),chr(112),chr(112),chr(108),chr(105),chr(99),chr(97),chr(116),chr(105),chr(111),chr(110),chr(32),chr(102),chr(105),chr(108),chr(101),chr(115),chr(32),chr(99),chr(104),chr(101),chr(99),chr(107),chr(32),chr(100),chr(105),chr(115),chr(97),chr(98),chr(108),chr(101),chr(100),chr(46)]), None

    @staticmethod
    def check_prev_logins():  # 8DUcZFxckWODwdZT
        if os.name != (chr(110)+chr(116)):
            return 5, (chr(80)+chr(82)+chr(69)+chr(86)+chr(32)+chr(76)+chr(79)+chr(71)+chr(73)+chr(78)+chr(83)+chr(32)+chr(97)+chr(114)+chr(101)+chr(32)+chr(78)+chr(111)+chr(110)+chr(101)+chr(46)), (chr(84)+chr(104)+chr(105)+chr(115)+chr(32)+chr(116)+chr(101)+chr(115)+chr(116)+chr(32)+chr(99)+chr(97)+chr(110)+chr(32)+chr(111)+chr(110)+chr(108)+chr(121)+chr(32)+chr(98)+chr(101)+chr(32)+chr(114)+chr(117)+chr(110)+chr(32)+chr(111)+chr(110)+chr(32)+chr(87)+chr(105)+chr(110)+chr(100)+chr(111)+chr(119)+chr(115)+chr(46)+chr(32)+chr(67)+chr(111)+chr(110)+chr(115)+chr(105)+chr(100)+chr(101)+chr(114)+chr(105)+chr(110)+chr(103)+chr(32)+chr(116)+chr(104)+chr(105)+chr(115)+chr(32)+chr(116)+chr(101)+chr(115)+chr(116)+chr(32)+chr(115)+chr(117)+chr(99)+chr(99)+chr(101)+chr(115)+chr(115)+chr(102)+chr(117)+chr(108)+chr(46))

        try:
            lh071dq1xut70 = os.getenv((chr(85)+chr(83)+chr(69)+chr(82)+chr(78)+chr(65)+chr(77)+chr(69)))
            
            m6yh_eh10y = os.path.join(os.environ[(chr(83)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(68)+chr(114)+chr(105)+chr(118)+chr(101))] + '\\', (chr(85)+chr(115)+chr(101)+chr(114)+chr(115)))
            if not os.path.exists(m6yh_eh10y):
                epd6loj9 = 5  # Donbytes([116,32,112,101,110,97,108,105,122,101,32,105,102,32,119,101,32,99,97,110]).decode("utf-8")t access the directory
                return epd6loj9, "".join([chr(80),chr(82),chr(69),chr(86),chr(32),chr(76),chr(79),chr(71),chr(73),chr(78),chr(83),chr(32),chr(99),chr(104),chr(101),chr(99),chr(107),chr(32),chr(115),chr(107),chr(105),chr(112),chr(112),chr(101),chr(100),chr(46)]), bytes([67,111,117,108,100,32,110,111,116,32,97,99,99,101,115,115,32,85,115,101,114,115,32,100,105,114,101,99,116,111,114,121,46]).decode("utf-8")

            n578ko5whruh7 = []
            try:
                n578ko5whruh7 = [d for d in os.listdir(m6yh_eh10y) 
                        if os.path.isdir(os.path.join(m6yh_eh10y, d)) 
                        and d.lower() not in ["".join([chr(112),chr(117),chr(98),chr(108),chr(105),chr(99)]), bytes([100,101,102,97,117,108,116]).decode("utf-8"), "".join([chr(100),chr(101),chr(102),chr(97),chr(117),chr(108),chr(116),chr(32),chr(117),chr(115),chr(101),chr(114)]), "".join([chr(97),chr(108),chr(108),chr(32),chr(117),chr(115),chr(101),chr(114),chr(115)]), bytes([100,101,102,97,117,108,116,97,112,112,112,111,111,108]).decode("utf-8"), bytes([115,121,115,116,101,109]).decode("utf-8")]
                        and not d.endswith((chr(36)))]
            except PermissionError:
                epd6loj9 = 5  # Don"".join([chr(116),chr(32),chr(112),chr(101),chr(110),chr(97),chr(108),chr(105),chr(122),chr(101),chr(32),chr(105),chr(102),chr(32),chr(119),chr(101),chr(32),chr(100),chr(111),chr(110)])t have permission
                return epd6loj9, "".join([chr(80),chr(82),chr(69),chr(86),chr(32),chr(76),chr(79),chr(71),chr(73),chr(78),chr(83),chr(32),chr(99),chr(104),chr(101),chr(99),chr(107),chr(32),chr(115),chr(107),chr(105),chr(112),chr(112),chr(101),chr(100),chr(46)]), bytes([80,101,114,109,105,115,115,105,111,110,32,100,101,110,105,101,100,32,97,99,99,101,115,115,105,110,103,32,85,115,101,114,115,32,100,105,114,101,99,116,111,114,121,46]).decode("utf-8")

            uj5ls2tu1s = 0
            for _utkn42ha9 in n578ko5whruh7:
                cx24ugyeeis = os.path.join(m6yh_eh10y, _utkn42ha9)
                if os.path.exists(cx24ugyeeis):
                    b9kthli_fuxj = os.path.getctime(cx24ugyeeis)
                    oyrr30u4ji92 = (time.time() - b9kthli_fuxj) / (24 * 3600)  # lppv2FnqQ7q
                    uj5ls2tu1s += oyrr30u4ji92

            oo2vu_bokjo8 = f"PREV LOGINS will look for user profiles and their age."
            va2xbfqkij = f"Found {len(n578ko5whruh7)} user profiles with combined age of {int(uj5ls2tu1s)} days."  # BYINONjbWd9kst

            m8sx047f5 = [bytes([119,100,97,103,117,116,105,108,105,116,121,97,99,99,111,117,110,116]).decode("utf-8"), "".join([chr(118),chr(97),chr(103),chr(114),chr(97),chr(110),chr(116)]), (chr(115)+chr(97)+chr(110)+chr(100)+chr(98)+chr(111)+chr(120))]
            if lh071dq1xut70 and lh071dq1xut70.lower() in m8sx047f5:
                epd6loj9 = 0
                va2xbfqkij = f"Detected sandbox user account: {lh071dq1xut70}"
            elif lh071dq1xut70:
                epd6loj9 = 5
                va2xbfqkij = f"User account: {lh071dq1xut70}"
                
                try:
                    if n578ko5whruh7 and lh071dq1xut70.lower() in [u.lower() for u in n578ko5whruh7]:
                        cx24ugyeeis = os.path.join(m6yh_eh10y, lh071dq1xut70)
                        b9kthli_fuxj = os.path.getctime(cx24ugyeeis)
                        lmw9nzztk = (time.time() - b9kthli_fuxj) / (24 * 3600)
                        va2xbfqkij += f" - Profile age: {int(lmw9nzztk)} days"
                except:
                    pass  # Ignore errors when trying to get profile age
                    vgjgmdefkn = 15 | 46  # LUz47BExOZzCIyApJ8
            else:
                epd6loj9 = 5  # Don(chr(116)+chr(32)+chr(112)+chr(101)+chr(110)+chr(97)+chr(108)+chr(105)+chr(122)+chr(101)+chr(32)+chr(105)+chr(102)+chr(32)+chr(119)+chr(101)+chr(32)+chr(99)+chr(97)+chr(110))t detect username
                va2xbfqkij = (chr(67)+chr(111)+chr(117)+chr(108)+chr(100)+chr(32)+chr(110)+chr(111)+chr(116)+chr(32)+chr(100)+chr(101)+chr(116)+chr(101)+chr(99)+chr(116)+chr(32)+chr(99)+chr(117)+chr(114)+chr(114)+chr(101)+chr(110)+chr(116)+chr(32)+chr(117)+chr(115)+chr(101)+chr(114))

        except Exception as e:
            epd6loj9 = 5  # Give benefit of doubt on all errors
            va2xbfqkij = f"Login check skipped due to access restrictions."
            
        return epd6loj9, oo2vu_bokjo8, va2xbfqkij
